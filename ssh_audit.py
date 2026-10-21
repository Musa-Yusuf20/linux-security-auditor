def check_ssh_config(config_path="test_sshd_config"):
    findings = []
    with open(config_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            setting = parts[0]
            value = parts[1]
            if setting == "PasswordAuthentication" and value == "yes":
                findings.append("[WARNING] Password authentication is enabled")
            if setting == "PermitRootLogin" and value == "yes":   
                findings.append("[WARNING] Direct SSH root login is enabled")
    return findings