import uid0_audit
import file_permissions_audit
import ssh_audit
from datetime import datetime

def check_uid0():
    return uid0_audit.check_uid0()

def check_file_permissions():
    return file_permissions_audit.check_file_permissions()

def check_ssh_config():
    return ssh_audit.check_ssh_config()

if __name__ == "__main__":

    print("LINUX SECURITY AUDIT REPORT")
    print(f"Audit Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 35)

    uid_findings = check_uid0()
    file_findings = check_file_permissions()
    ssh_findings = check_ssh_config()

    with open("security_report.txt", "w") as file:
        file.write("LINUX SECURITY AUDIT REPORT\n")
        file.write(f"Audit Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for finding in uid_findings:
            print(finding)
            file.write(finding + "\n")

        for finding in file_findings:
            print(finding)
            file.write(finding + "\n")

        for finding in ssh_findings:
            print(finding)
            file.write(finding + "\n")
