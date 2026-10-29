Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
using System.Text;

public class CredManager {
    [DllImport("advapi32.dll", SetLastError = true, CharSet = CharSet.Unicode)]
    public static extern bool CredRead(string target, int type, int reservedFlag, out IntPtr credentialPtr);

    [DllImport("advapi32.dll", SetLastError = true)]
    public static extern void CredFree(IntPtr credentialPtr);

    [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Unicode)]
    public struct CREDENTIAL {
        public int Flags;
        public int Type;
        public string TargetName;
        public string Comment;
        public long LastWritten;
        public int CredentialBlobSize;
        public IntPtr CredentialBlob;
        public int Persist;
        public int AttributeCount;
        public IntPtr Attributes;
        public string TargetAlias;
        public string UserName;
    }

    public static string GetPassword(string target) {
        IntPtr credPtr;
        if (CredRead(target, 1, 0, out credPtr)) {
            CREDENTIAL cred = (CREDENTIAL)Marshal.PtrToStructure(credPtr, typeof(CREDENTIAL));
            byte[] blob = new byte[cred.CredentialBlobSize];
            Marshal.Copy(cred.CredentialBlob, blob, 0, cred.CredentialBlobSize);
            CredFree(credPtr);
            string s = Encoding.UTF8.GetString(blob);
            if (s.Length > 0 && s[0] != '\0') return s;
            return Encoding.Unicode.GetString(blob);
        }
        return null;
    }
}
"@

$token = [CredManager]::GetPassword("GitHub - https://api.github.com/heigilin")
if (-not $token) {
    $token = [CredManager]::GetPassword("LegacyGeneric:target=GitHub - https://api.github.com/heigilin")
}

$authUrl = "https://heigilin:$token@github.com/heigilin/ntuh-ic-line-bot.git"

& git push $authUrl main:main --no-verify

if ($LASTEXITCODE -eq 0) {
    Write-Output "PUSH TO ORIGIN SUCCESSFUL!"
} else {
    Write-Error "Push failed: $LASTEXITCODE"
}
