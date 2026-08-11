import sys
from services.add_finanse import add_finanse
import subprocess


def main():
    subprocess.Popen([
        sys.executable,
        "src/ai/train.py",
    ])

    add_finanse()
            
       



if __name__ == "__main__":
    main()
    
