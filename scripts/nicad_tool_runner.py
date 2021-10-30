""" Dieses Skript wird von einem ToolRunnerfür ein MutationInjectionFramework
-Durchlauf ausgeführt und übernimmt die Hauptaufgabe
mittels return (oder print?) muss dann der Pfad zu den Ergebnissen zurück gegeben werden
"""

import sys
from pathlib import Path
import time
import os
import subprocess
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime
import logging

# Logging einstellen
logging.basicConfig(filename="mif_formatter.log", level=logging.DEBUG,
    format='%(asctime)s: %(levelname)s: %(message)s', datefmt = "%x - %H:%M")

# Ort, an dem die Evaluation durchgefürt wird
# NiCad empfiehlt den eigenen `systems`-Ordner
NICAD_BASE_DIR = Path("/media/MIF/NicadDirs")

def nicad_run(system_dir, tool_dir, language, fragment_type, nicad_format):

    base_name = time.time_ns()
    # 'mutantbase', da das system_dir im MIF immer 'mutantbase' heißt
    nicad_system_dir = NICAD_BASE_DIR /str(base_name)
    # os.makedirs(nicad_system_dir)dd

    shutil.copytree(system_dir, nicad_system_dir)
    nicad_call = f"./nicad6 {fragment_type} {language} {nicad_system_dir} {nicad_format} > /dev/null 2> /dev/null"
    subprocess.run(nicad_call,cwd=tool_dir, shell=True)

    return nicad_system_dir

def format_nicad_to_mif(nicad_system_dir, mif_system_dir, fragment_type, nicad_format):

    nicad_system_path = Path(nicad_system_dir)
    nicad_system_name = nicad_system_path.parts[-1]
    if nicad_format == "default-report":
        experiment_name = f"{nicad_system_name}_{fragment_type}-blind-clones"
    else:
         raise TypeError("Keine ordentliche Nicad-Config!")
    experiment_path = nicad_system_path.parent / experiment_name
    xml_file = experiment_path / f"{experiment_name}-0.30.xml"
    clone_list = get_clones_from_nicad_xml(xml_file, mif_system_dir)
    # Versuch die Druchführung des MIF besser nachzuvollziehen
    #dest_file = experiment_path/f"{experiment_name}-{datetime.utcnow()}"
    dest_file = experiment_path / f"{experiment_name}-0.30.txt"
    with open(dest_file, "w") as txt_f:
        txt_f.write('\n'.join(clone_list))

    # logging.info(f"Datei {dest_file} wurde erstellt")
    return dest_file


def get_clones_from_nicad_xml(xml_file, system_path):
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

        # 
        # `parts[X:]`: wir schneiden das oben definierte `NICAD_BASE_DIR` ab
        #  und stecken die Pfade zu den einzelnen Dateien an den MIF System Pfad
        # mit ran.
        cp1_suffix_list = Path(clone_pair_1_attribute_list["file"]).parts[5:]
        cp1_file_path = Path(system_path) / Path("/".join(cp1_suffix_list))
        cp1 = {
            # Der Pfad in clone_pair_1 wir relativ zum NiCad-Ordner angegeben.
            # also der Form system/experiment-name/...
            # wir brauchen jedoch den Pfad zur Ausgangsdatei
            "file_path" : cp1_file_path,
            "startline": clone_pair_1_attribute_list["startline"],
            "endline": clone_pair_1_attribute_list["endline"]
        }
        cp2_suffix_list = Path(clone_pair_2_attribute_list["file"]).parts[5:]
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


if __name__ == '__main__':

    
    # Werte zum testen #
    # ================ #

    # Diese vier Sachen werden benötigt.
    # system_dir = Path("/media/MIF/Reprod_2019/ipscan_functions_default_3750/mutantbase")
    # tool_dir = Path("/home/alexanderhoerig/opt/NiCad-6.2")
    # language = "java"
    # fragment_type = "function"
    # sys.argv = ['nicad_tool_runner.py', system_dir, language, tool_dir, fragment_type]
    logging.debug(str(sys.argv))
    
    nicad_format = "default-report"

    mif_system_dir = Path(sys.argv[1])
    language = sys.argv[2]
    tool_dir = Path(sys.argv[3])
    mif_fragment_type = sys.argv[4]
    if mif_fragment_type == 'function':
        fragment_type = "functions"
    elif mif_fragment_type == 'block':
        fragment_type = "block"
    else:
        raise TypeError("Falscher Fragment-Type (weder function noch bock)")
    
    
    
    nicad_system_dir = nicad_run(mif_system_dir, tool_dir, language, fragment_type, nicad_format)

    mif_style_clone_file = format_nicad_to_mif(nicad_system_dir, mif_system_dir, fragment_type, nicad_format)
    
    # Gibt die Datei der gefundenen Clones an MIF zurück
    print(mif_style_clone_file)
