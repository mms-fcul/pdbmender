import sys

sys.path.insert(0, "../")

from pdbmender import (
    mend_pdb,
    add_tautomers,
    identify_tit_sites,
    rm_cys_bridges,
    identify_cter,
)
from pdbmender.formats import get_chains_from_file

fname = "1CET.pdb"
ff = "GROMOS"
sysname = fname.split(".pdb")[0]

pdb_cleaned = f"{sysname}_cleaned.pdb"
logfile_mend = "LOG_pdb2pqr"
mend_pdb(fname, pdb_cleaned, ff, ff, logfile=logfile_mend)

chains = get_chains_from_file(fname)
chains_res = identify_tit_sites(fname, chains, add_ser_thr=True)

chains_res, cys_bridges = rm_cys_bridges(chains_res, logfile_mend)

old_ctrs = {
    chain: resnumb
    for chain, residues in chains_res.items()
    for resnumb, resname in residues.items()
    if resname == "CTR"
}
new_ctrs = identify_cter(pdb_cleaned, old_ctrs)
for chain, resnumb in new_ctrs.items():
    chains_res[chain][str(resnumb)] = "CTR"

output_pdb = f"{sysname}_final.pdb"
add_tautomers(pdb_cleaned, chains_res, ff, output_pdb)
