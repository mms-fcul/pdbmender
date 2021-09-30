# PDBmender

Mend and add hydrogens to PDB files

## Installation

```bash
apt install python2 gawk
python3 -m pip install pdbmender
```

## Usage

PDBmender is a python module and not a CLI tool (yet). You may find an example in /examples

```
from pdbmender import mend_pdb, add_tautomers

mend_pdb(<original_pdb>, <cleaned_pdb>, <input_ff>, <output_ff>)
```
