import os
import stat

file_path = "/etc/passwd"
file_info = os.stat(file_path)

permissions = file_info.st_mode
print(oct(stat.S_IMODE(permissions)))

if permissions & stat.S_IWGRP:
    print("[WARNING] Group has write permissions")
if permissions & stat.S_IWOTH:
    print("[WARNING] Others have write permissions")