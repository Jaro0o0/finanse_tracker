import sys
import subprocess

def run_forecast() -> str:
    """Run the forecast script and return its terminal output."""
    result = subprocess.run(
        [sys.executable, "-m", "ai.train"],
        cwd=__file__.rsplit("/", 1)[0],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return f"Nie udało się utworzyć prognozy:\n{result.stderr.strip()}"

    return result.stdout.strip()