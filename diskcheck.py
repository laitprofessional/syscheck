import shutil

def check_disk_usage(path="/", threshold=90):
    usage = shutil.disk_usage(path)
    percent_used = round((usage.used /usage.total) * 100, 1)
    return {
        "path": path,
        "percent_used": percent_used,
        "alert": percent_used >= threshold,
    }
