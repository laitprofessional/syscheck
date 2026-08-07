from unittest.mock import patch, MagicMock
from syscheck.servicecheck import check_service


@patch("syscheck.servicecheck.subprocess.run")
def test_check_service_returns_active_true(mock_run):
    mock_run.return_value = MagicMock(stdout="active\n")
    result = check_service("sshd")
    assert result["active"] is True
    assert result["name"] == "sshd"


@patch("syscheck.servicecheck.subprocess.run")
def test_check_service_returns_active_false(mock_run):
    mock_run.return_value = MagicMock(stdout="inactive\n")
    result = check_service("crond")
    assert result["active"] is False
