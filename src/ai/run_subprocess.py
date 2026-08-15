import sys
import subprocess
from pathlib import Path

def run_forecast(on_line=None) -> str:

    proc = subprocess.Popen(
        [sys.executable, "-m", "ai.train"],
        cwd=Path(__file__).resolve().parent.parent,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    output_lines = []
    if proc.stdout is not None:
        for line in proc.stdout:
            output_lines.append(line)
            if on_line:
                try:
                    on_line(line)
                except Exception:
                    # ensure streaming doesn't break the training process
                    pass

    proc.wait()
    stdout = "".join(output_lines)

    if proc.returncode != 0:
        return 'Failed to create forecast. Check if you have at least 3 days of expenses.'

    marker = 'Expense forecast'
    if marker in stdout:
        return stdout[stdout.index(marker):].strip()

    return 'Failed to create forecast. Check if you have at least 3 days of expenses.'
