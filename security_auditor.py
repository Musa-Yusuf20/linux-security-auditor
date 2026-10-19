import uid0_audit
import file_permissions_audit
import ssh_audit
from datetime import datetime

def check_uid0():
    uid0_audit.check_uid0()

def check_file_permissions():
    file_permissions_audit.check_file_permissions()

def check_ssh_config():
    ssh_audit.check_ssh_config()


print("LINUX SECURITY AUDIT REPORT")
print(f"Audit Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 35)
check_uid0()
check_file_permissions()
check_ssh_config()

with open("security_report.txt", "w") as file:
    file.write("LINUX SECURITY AUDIT REPORT\n")
    file.write(f"Audit Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    for finding in uid0_audit.check_uid0():
        file.write(finding + "\n")

    for finding in file_permissions_audit.check_file_permissions():
        file.write(finding + "\n")

    for finding in ssh_audit.check_ssh_config():
        file.write(finding + "\n")
