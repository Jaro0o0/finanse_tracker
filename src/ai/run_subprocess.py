import sys
import subprocess
from pathlib import Path

def run_forecast() -> str:
    """Run the forecast script and return only a user-facing message."""
    result = subprocess.run(
        [sys.executable, "-m", "ai.train"],
        cwd=Path(__file__).resolve().parent.parent,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return 'Nie udało się utworzyć prognozy. Sprawdź, czy masz co najmniej 3 dni wydatków.'

    marker = 'Prognoza wydatków:'
    if marker in result.stdout:
        return result.stdout[result.stdout.index(marker):].strip()

    return 'Nie udało się utworzyć prognozy.'
