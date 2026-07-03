from importlib.metadata import version, PackageNotFoundError

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import numpy as np
except ImportError:
    np = None

try:
    import matplotlib
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib = None
    plt = None


def get_version(package_name: str) -> str:
    try:
        return version(package_name)
    except PackageNotFoundError:
        return "unknown"


def check_dependencies() -> bool:
    all_ok = True

    if pd is not None:
        print(
            f"[OK] pandas ({get_version('pandas')}) - Data manipulation ready")
    else:
        print("[MISSING] pandas - run: pip install pandas")
        all_ok = False

    if np is not None:
        print(
            f"[OK] numpy ({get_version('numpy')}) - Numerical computation ready")
    else:
        print("[MISSING] numpy - run: pip install numpy")
        all_ok = False

    if matplotlib is not None:
        print(
            f"[OK] matplotlib ({get_version('matplotlib')}) - Visualization ready")
    else:
        print("[MISSING] matplotlib - run: pip install matplotlib")
        all_ok = False

    return all_ok


def generate_matrix_data() -> "np.ndarray":
    return np.random.normal(loc=50, scale=15, size=1000)


def analyze_data(data: "np.darray") -> "pd.DataFrame":
    df = pd.DataFrame(data, columns=["value"])
    print(f"Processing {len(df)} data points...")
    return df


def visualize(df: "pd.DataFrame") -> None:
    print("Generating visualization...")
    plt.hist(df["value"], bins=30)
    plt.title("Matrix Data Analysis")
    plt.savefig("matrix_analysis.png")
    print("Results saved to: matrix_analysis.png")


def loading() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    if not check_dependencies():
        print("\nInstall missing dependencies with:")
        print("  pip install -r requirements.txt")
        print("  poetry install")
        return

    print("\nAnalyzing Matrix data...")
    data = generate_matrix_data()
    df = analyze_data(data)
    visualize(df)


if __name__ == "__main__":
    loading()
