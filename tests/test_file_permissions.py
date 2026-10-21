import file_permissions_audit

def test_check_file_permissions(monkeypatch):
    class FakeFileInfo:
        st_mode = 0o666
    
    monkeypatch.setattr(file_permissions_audit, "get_file_info", lambda path: FakeFileInfo())
    findings = file_permissions_audit.check_file_permissions()
    assert any("[WARNING]" in finding for finding in findings), "no warnings found in file permissions audit"


def test_check_file_permissions(monkeypatch):
    class FakeFileInfo:
        st_mode = 0o644
    
    monkeypatch.setattr(file_permissions_audit, "get_file_info", lambda path: FakeFileInfo())
    findings = file_permissions_audit.check_file_permissions()
    assert not any("[WARNING]" in finding for finding in findings), "Unexpected warnings found in file permissions audit"