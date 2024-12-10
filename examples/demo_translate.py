import os
import sys

from prefscltl2pdfa import *
from loguru import logger
from pathlib import Path

logger.remove()
logger.add(sys.stdout, level="INFO")

# Define paths
CUR_DIR = Path(__file__).resolve().parent
SPECS_DIR = CUR_DIR / "specs"
OUT_DIR = CUR_DIR / "out"
SPECS = os.listdir(SPECS_DIR)


def main():
    # Simple specification
    f0 = PrefScLTL.from_file(SPECS_DIR / "spec0.spec", auto_complete="minimal")
    aut = f0.translate(show_progress=True)
    print("============== spec0.spec, minimal ================")
    print(aut)

    # Simple specification
    f0 = PrefScLTL.from_file(SPECS_DIR / "spec0.spec", auto_complete="incomparable")
    aut = f0.translate(show_progress=True)
    print("============== spec0.spec, incomparable ================")
    print(aut)

    # Simple specification (uses all preference operators)
    f1 = PrefScLTL.from_file(SPECS_DIR / "spec1.spec")
    aut = f1.translate(show_progress=True)
    print("============== spec1.spec, minimal ================")
    print(aut)

    # Corner case:  trivial specification (only `true`)
    f2 = PrefScLTL.from_file(SPECS_DIR / "erroneous" / "spec2.spec")
    try:
        aut = f2.translate(show_progress=True)
    except AssertionError as err:
        logger.success(f"Translation successfully raised AssertionError.\n{err}")

    f3 = PrefScLTL.from_file(SPECS_DIR / "erroneous" / "spec3.spec", auto_complete="minimal")
    try:
        aut = f3.translate(show_progress=True)
    except AssertionError as err:
        logger.success(f"Translation successfully raised AssertionError.\n{err}")


if __name__ == '__main__':
    main()
