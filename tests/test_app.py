from src.app import add, divide, run_command
import pytest


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Tidak boleh bagi nol"


def test_run_command_normal():
    assert run_command("echo halo").strip() == "halo"


def test_run_command_tidak_bisa_injection():
    # Tanpa shell, ';' dianggap argumen biasa, bukan pemisah perintah kedua.
    output = run_command("echo aman; echo BERBAHAYA")
    assert output.strip() == "aman; echo BERBAHAYA"
