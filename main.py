# Main Molecular dynamics simulation loop
import os
import md
import ase.io
from read_mp_project import read_mp_properties

def main_loop():
    mp_properties = read_mp_properties('testing_data_materials.json')
    txt_str = mp_properties["cif"][0]
    f = open("tmp_cif.cif", "w+")
    f.write(txt_str)
    f.close()
    atoms = ase.io.read("tmp_cif.cif", None)
    md.run_md(atoms)
    os.remove("tmp_cif.cif")

if __name__ == "__main__":
    main_loop()
