#!/usr/bin/env python3
"""Run DeliveryOS directly from a clone; no installation required."""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).resolve().parent / "skills/project-delivery/scripts/project.py"), run_name="__main__")
