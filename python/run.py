import os
import platform
import subprocess

APP = os.environ.get("APP", "genFakeData")
WORKERS = 10 + 1
IS_WINDOWS = platform.system() == "Windows"


def setup():
    if IS_WINDOWS:
        subprocess.run(["cmd", "/c", "scripts\\setup.bat"], check=True)
    else:
        subprocess.run(["bash", "scripts/setup.sh"], check=True)


def run():
    gunicorn = "venv\\Scripts\\gunicorn" if IS_WINDOWS else "venv/bin/gunicorn"
    subprocess.run([
        gunicorn,
        f"{APP}.asgi:application",
        "-k", "uvicorn.workers.UvicornWorker",
        "--workers", str(WORKERS),
    ], check=True)


if __name__ == "__main__":
    if not os.path.exists("venv"):
        setup()
    run()
