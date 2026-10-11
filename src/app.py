import shlex
import subprocess


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b


def run_command(cmd):
    # Perbaikan: pecah perintah menjadi list argumen dan JANGAN pakai shell=True,
    # sehingga karakter seperti ';', '&&', atau '|' tidak diinterpretasikan shell.
    args = shlex.split(cmd)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
