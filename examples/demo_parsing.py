import pprint
import os
import sys

from pathlib import Path
from prefscltl2pdfa import *
from loguru import logger

logger.remove()
# logger.add(sys.stdout, level="DEBUG")
logger.add(sys.stdout, level="INFO")

# Define paths
CUR_DIR = Path(__file__).resolve().parent
SPECS_DIR = CUR_DIR / "specs"
OUT_DIR = CUR_DIR / "out"
SPECS = os.listdir(SPECS_DIR)


def main():
    # Simple specification
    f0 = PrefScLTL.from_file(SPECS_DIR / "spec0.spec")
    print(f0)

    # Simple specification (uses all preference operators)
    f1 = PrefScLTL.from_file(SPECS_DIR / "spec1.spec")
    print(f1)

    # Corner case:  trivial specification (only `true`)
    f2 = PrefScLTL.from_file(SPECS_DIR / "spec2.spec")
    print(f2)

    # Corner case (only `F(a)`).
    #   This needs auto-completion.
    try:
        f3 = PrefScLTL.from_file(SPECS_DIR / "spec3.spec")
    except ValueError:
        f3 = PrefScLTL.from_file(SPECS_DIR / "spec3.spec", auto_complete="minimal")
    print(f3)

    # Auto-completion check of `incomparable` option
    f3 = PrefScLTL.from_file(SPECS_DIR / "spec3.spec", auto_complete="incomparable")
    print(f3)

    # Inconsistent specification
    try:
        f4 = PrefScLTL.from_file(SPECS_DIR / "erroneous" / "spec4.spec", auto_complete="minimal")
    except ValueError as err:
        logger.success(err)

    # LTLf parsing error
    try:
        f5 = PrefScLTL.from_file(SPECS_DIR / "erroneous" / "spec5.spec", auto_complete="minimal")
    except SyntaxError as err:
        logger.success(f"Specification successfully raised SyntaxError.\n{err}")

    # LTLf parsing error
    try:
        f6 = PrefScLTL.from_file(SPECS_DIR / "erroneous" / "spec6.spec", auto_complete="minimal")
    except TypeError as err:
        logger.success(f"Specification successfully raised TypeError.\n{err}")



if __name__ == '__main__':
    main()

    # spec = ("""
#     # test
#     spec 4
#
#
#     F a
#     G b
#     !(F(a) | G(b))
#     true U a
#
#     # SPec
#     >, 0, 1
#     >, 0, 2
#     >=, 1, 2
#     """)
#
#
# if __name__ == '__main__':
#     formula = spec(spec)
#
#     print("====================================")
#     print("formula = ")
#     pprint(formula.serialize())
#
#     print()
#     print("====================================")
#     print("aut = ")
#     aut = formula.translate(semantics=semantics_mp_forall_exists)
#     pprint(aut.serialize())
#
#     sa, pg = paut2dot(aut, show_sa_state=True, show_class=True, show_color=True, show_pg_state=True)
#     paut2png(sa, pg, fname="aut")
#     paut2svg(sa, pg, fname="aut")
