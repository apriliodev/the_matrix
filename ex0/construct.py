import sys
import os
import site


def check_venv() -> bool:
    if sys.prefix != sys.base_prefix:
        return True # on est dans un venv
    return False

def show_interpret() -> None:
    if check_venv():
        venv_name = os.path.basename(sys.prefix)
        print("\nMATRIX STATUS: Welcome to the construct")
        print(f"\nCurrent Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}")
        print(
            "\nSUCCESS: You’re in an isolated environment!"
            "\nSafe to install packages without affecting"
            "\nthe global system."
        )
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])
    else:
        print("\nMATRIX STATUS: You’re still plugged in")
        print(f"\nCurrent Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print(
            "\nWARNING: You’re in the global environment!"
            "\nThe machines can see everything you install."
        )
        print(
            "\nTo enter the construct, run"
            "\npython -m venv matrix_env"
            "\nsource matrix_env/bin/activate # On Unix"
        )
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")

show_interpret()
        
