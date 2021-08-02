"""Formatiert die Ausgabe einer Evaluation mit NiCad-6.2 für die Arbeit mit dem
MutationInjectionFramework und gibt sie an einen gestarteten Toolrunner zurück. 
"""


import argparse
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

logging.basicConfig(filename="mif_formatter.log", level=logging.INFO,
    format='%(asctime)s: %(levelname)s: %(message)s', datefmt = "%x - %H:%M")

# Hier muss der Pfad für NiCad angepasst werden
NICAD_PATH = Path.home()/"opt"/"NiCad-6.2"
NICAD_SYSTEMS_PATH = NICAD_PATH / "systems"


def mif_format(system_dir):
    """
    Kopiert ein System von `system_dir` im NiCad `systems` Ordner
    und baut die die richte Formatierung für das MIF auf.
    """
    
    system_path = Path(system_dir)
    system_name = system_path.parts[-1]
    logging.debug(system_path, system_name)

    # Von NiCad und dem jeweiligen Eingaben abhängig
    # TODO: Das müss in Zukunft noch allgemeiner gemacht werden! 
    # <AH 2021-08-02>
    experiment_name = f"{system_path}_functions-blind-clones"
    experiment_path = Path(NICAD_SYSTEMS_PATH, experiment_name)
    logging.debug(experiment_name, experiment_path)

    xml_file = experiment_path / f"{experiment_name}-0.30.xml"
    clone_list = get_clones_from_xml(xml_file, system_path, experiment_path)

    dest_file = experiment_path / f"{experiment_name}-0.30.txt"
    with open(dest_file, "w") as txt_f:
        txt_f.write('\n'.join(clone_list))

    logging.info(f"Datei {dest_file} wurde erstellt")
    return dest_file

def get_clones_from_xml(xml_file, system_path):
  
    logging.debug("searching for clones!")
    # create element tree object
    tree = ET.parse(xml_file)
  
    # get root element
    root = tree.getroot()
  
    # create empty list for news items
    clone_list = []
  
    # iterate news items
    for item in root.findall('./clone'):
        clones = item.findall("./source")
        clone_pair_1, clone_pair_2 = tuple(clones)
        clone_pair_1_attribute_list = clone_pair_1.attrib
        clone_pair_2_attribute_list = clone_pair_2.attrib
        
        # Es werden die absoluten Pfade abhängig vom Ausgangssystem des 
        # MIF-Projekts erstellt und angegeben.

        # `parts[2:]`: wir schneiden `systems/mutantbase_functions-blind-clones` ab
        # und stecken die Pfade zu den einzelnen Dateien an den MIF System Pfad
        # mit ran.
        cp1_suffix_list = Path(clone_pair_1_attribute_list["file"]).parts[2:]
        cp1_file_path = Path(system_path) / Path("/".join(cp1_suffix_list))
        cp1 = {
            # Der Pfad in clone_pair_1 wir relativ zum NiCad-Ordner angegeben.
            # also der Form system/experiment-name/...
            # wir brauchen jedoch den Pfad zur Ausgangsdatei
            "file_path" : cp1_file_path,
            "startline": clone_pair_1_attribute_list["startline"],
            "endline": clone_pair_1_attribute_list["endline"]
        }
        cp2_suffix_list = Path(clone_pair_2_attribute_list["file"]).parts[2:]
        cp2_file_path = Path(system_path) / Path("/".join(cp2_suffix_list))
        cp2 = {
            "file_path" :cp2_file_path,
            "startline": clone_pair_2_attribute_list["startline"],
            "endline": clone_pair_2_attribute_list["endline"]
        }

        cp1_str = f"{cp1['file_path']},{cp1['startline']},{cp1['endline']}"
        cp2_str = f"{cp2['file_path']},{cp2['startline']},{cp2['endline']}"
        clone_list.append(f"{cp1_str},{cp2_str}")
    
    return clone_list



if __name__ =="__main__":
    logging.info("Konvertierung wurde gestartet")
    parser = argparse.ArgumentParser(description='Formatting for NiCad')
    parser.add_argument('systemdir')
    args = parser.parse_args()

    dest = mif_format(args.systemdir)
    # Durch diesen Print-Befehl wird die Datei an MIF im ToolRunner Script
    # wieder übergeben! (Ersatz für `echo` im ToolRunner)
    print(dest)