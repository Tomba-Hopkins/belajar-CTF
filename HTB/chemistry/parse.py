from pymatgen.io.cif import CifParser
parser = CifParser("exp2.cif")
structure = parser.parse_structures()
