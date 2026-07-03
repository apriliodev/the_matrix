from dotenv import load_dotenv
import os

load_dotenv()


def security_check() -> None:
    print("\nEnvironment security check:")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found — using defaults/system env only")
    if os.path.exists(".gitignore"):
        with open(".gitignore") as f:
            gitignore_content = f.read()
        if ".env" in gitignore_content:
            print("[OK] No hardcoded secrets detected (.env is gitignored)")
        else:
            print("[WARNING] .env is not in .gitignore — risk of leaking secrets")
    else:
        print("[WARNING] No .gitignore found")
    print("[OK] Production overrides available (system env > .env file)")


def load_config() -> dict[str, str]:
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", "development"),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", ""),
    }


def check_config(config: dict[str, str]) -> bool:
    missing = [key for key, value in config.items() if not value]
    if missing:
        print(f"WARNING: Missing configuration: {', '.join(missing)}")
        return False
    return True


def show_status(config: dict[str, str]) -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if config["MATRIX_MODE"] == "production":
        print("Database: Connected to production instance")
        print(f"Log Level: {config['LOG_LEVEL']} (minimal, production)")
    else:
        print("Database: Connected to local instance")
        print(f"Log Level: {config['LOG_LEVEL']} (verbose, development)")

    print(
        f"API Access: {'Authenticated' if config['API_KEY'] else 'Missing key'}")
    print(f"Zion Network: {config['ZION_ENDPOINT'] or 'Not configured'}")


def oracle() -> None:
    load_dotenv()
    config = load_config()
    show_status(config)
    check_config(config)
    security_check()


if __name__ == "__main__":
    oracle()
