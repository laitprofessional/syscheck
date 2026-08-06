from syscheck.diskcheck import check_disk_usage

def test_disk_usage_returns_percent():
    result = check_disk_usage("/")
    assert 0 <= result["percent_used"] <= 100

def test_disk_usage_flags_when_over_threshold():
    result = check_disk_usage("/", threshold=0)
    assert result["alert"] is True
