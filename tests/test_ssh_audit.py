import ssh_audit

def test_check_ssh_config(monkeypatch):
    findings = ssh_audit.check_ssh_config()
    assert any("[WARNING] Direct SSH root login is enabled" in finding for finding in findings)
    assert any("[WARNING] Password authentication is enabled" in finding for finding in findings)


def test_secure_ssh_config(monkeypatch):
    findings = ssh_audit.check_ssh_config("test_sshd_config_secure")
    assert not any("[WARNING] Direct SSH root login is enabled" in finding for finding in findings)
    assert not any("[WARNING] Password authentication is enabled" in finding for finding in findings)

