from syscheck.servicecheck import check_service

def test_check_service_returns_status():
    result = check_service("sshd")
    assert "active" in result
