import subprocess

def check_service(name):
    result = subprocess.run(
        ["systemctl", "is-active", name],
        capture_output=True, text=True
    )
    return {"name": name, "active": result.stdout.strip() == "active"}
