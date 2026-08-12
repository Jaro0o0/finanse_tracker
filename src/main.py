import sys
from services.add_finanse import add_finanse
import subprocess


def main():
    process = subprocess.Popen([
        sys.executable,
        "src/ai/train.py",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    add_finanse()
            
       



if __name__ == "__main__":
    main()
    
