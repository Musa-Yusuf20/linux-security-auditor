import uid0_audit

def test_check_uid0():
    findings = uid0_audit.check_uid0()
    assert any("[WARNING] Account" in finding for finding in findings), "No UID 0 accounts found"