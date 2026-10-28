import security_auditor
import subprocess

def test_security_auditor():
    result = subprocess.run(
    ["python3", "security_auditor.py"],
    capture_output=True,
    text=True
)
    assert result.returncode == 0
    assert "[INFO]" in result.stdout
