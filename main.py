"""
ST4015CMD — Foundations of Computer Science
Krish Adhikari (250487)

Entry point: runs all three tasks in sequence.
"""

from src.encoding import run_demo as encoding_demo
from src.seating  import run_demo as seating_demo
from src.database import run_demo as database_demo


if __name__ == "__main__":
    encoding_demo()
    seating_demo()
    database_demo()
