def check_ssh_config(config_path="/etc/ssh/sshd_config"):
    findings = []
    try:
         with open(config_path, "r") as file:
              for line in file:
                parts = line.strip().split()
                if len(parts) < 2 or parts[0].startswith("#"):
                    continue
                setting = parts[0]
                value = parts[1]
                if setting == "PasswordAuthentication" and value == "yes":
                    findings.append("[WARNING] Password authentication is enabled")
                if setting == "PermitRootLogin" and value == "yes":   
                    findings.append("[WARNING] Direct SSH root login is enabled")
    except FileNotFoundError:
        findings.append("[INFO] SSH server configuration file not found")
    return findings