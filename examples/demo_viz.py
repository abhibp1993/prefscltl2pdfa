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
    f0 = PrefScLTL.from_file(SPECS_DIR / "spec0.spec")
    aut0 = f0.translate(show_progress=True)

    # See documentation for option description.
    sa, pg = paut2dot(aut0, show_sa_state=True, show_class=True, show_color=True, show_pg_state=True)
    paut2png(sa, pg, fpath=OUT_DIR, fname="aut")
    paut2svg(sa, pg, fpath=OUT_DIR, fname="aut")

    # Simple specification
    f0 = PrefScLTL.from_file(SPECS_DIR / "spec0.spec", auto_complete="minimal")
    aut = f0.translate(show_progress=True)
    sa, pg = paut2dot(aut, show_sa_state=True, show_class=True, show_color=True, show_pg_state=True)
    paut2png(sa, pg, fpath=OUT_DIR, fname="aut0_min")
    paut2svg(sa, pg, fpath=OUT_DIR, fname="aut0_min")

    # Simple specification
    f0 = PrefScLTL.from_file(SPECS_DIR / "spec0.spec", auto_complete="incomparable")
    aut = f0.translate(show_progress=True)
    sa, pg = paut2dot(aut, show_sa_state=True, show_class=True, show_color=True, show_pg_state=True)
    paut2png(sa, pg, fpath=OUT_DIR, fname="aut0_inc")
    paut2svg(sa, pg, fpath=OUT_DIR, fname="aut0_inc")

    # Simple specification (uses all preference operators)
    f1 = PrefScLTL.from_file(SPECS_DIR / "spec1.spec")
    aut = f1.translate(show_progress=True)
    sa, pg = paut2dot(aut, show_sa_state=True, show_class=True, show_color=True, show_pg_state=True)
    paut2png(sa, pg, fpath=OUT_DIR, fname="aut1")
    paut2svg(sa, pg, fpath=OUT_DIR, fname="aut1")


if __name__ == '__main__':
    main()
