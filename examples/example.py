import sys

sys.path.insert(0, "../")

from pdbmender import mend_pdb, add_tautomers, prepare_for_addHtaut

mend_pdb("4lzt.pdb", "4lzt_cleaned.pqr", "GROMOS", "GROMOS")
prepare_for_addHtaut(
    "4lzt_cleaned.pqr", "4lzt_prep.pdb", {"A": [7]}, {"A": [1, 129]}, []
)
add_tautomers(
    "4lzt_prep.pdb", "1--LYS--A,7--GLU--A,129--CTR--A", "GROMOS", "4lzt_wHs.pdb"
)
