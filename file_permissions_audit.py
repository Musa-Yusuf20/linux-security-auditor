import os
import stat

def get_file_info(path):
    return os.stat(path)

def check_file_permissions():
    findings = []
    file_path = "/etc/passwd"
    file_info = get_file_info(file_path)
    for finding in findings:
        print(finding)

    permissions = file_info.st_mode
    findings.append(f"[INFO] /etc/passwd file permissions: {oct(stat.S_IMODE(permissions))}")

    if permissions & stat.S_IWGRP:
        findings.append("[WARNING] Group has write permissions")
    if permissions & stat.S_IWOTH:
        findings.append("[WARNING] Others have write permissions")
    return findings