import sys
from syscheck.diskcheck import check_disk_usage
from syscheck.servicecheck import check_service

def main():
    disk = check_disk_usage("/")
    print(f"Disk / : {disk['percent_used']}% used", "ALERT" if disk["alert"] else "OK")

    for svc in ["sshd", "cron"]:
        status = check_service(svc)
        print(f"{svc}: {'running' if status['active'] else 'DOWN'}")

if __name__ == "__main__":
    main()
