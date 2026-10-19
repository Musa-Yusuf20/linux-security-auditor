with open("test_sshd_config", "r") as file:
    for line in file:
        parts = line.strip().split()
        setting = parts[0]
        value = parts[1]
        if setting == "PasswordAuthentication" and value == "yes":
            print("[WARNING] Password authentication is enabled")
        if setting == "PermitRootLogin" and value == "yes":   
            print("[WARNING] Direct SSH root login is enabled")