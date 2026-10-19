import warnings

def check_uid0():
    findings = []
    with open("/etc/passwd", "r") as file:
        for line in file:
            fields = line.strip().split(":")
            uid = fields[2]
            if uid == "0":
                findings.append(f"[WARNING] Account '{fields[0]}' has UID 0")
    return findings
            
