import xml.etree.ElementTree as ET # lxml.etree?  "vastly superior to defualt installation of ElementTree"
import os

import AssetSources as assets

script_dir = os.path.dirname(__file__)


def getXmlTreeByAssetKey(key):
    abs_path = assets.asset_file2(key)
    tree = ET.parse(abs_path)
    return tree


def getXmlTreeByPath(abs_path):
    tree = ET.parse(abs_path)
    return tree


def readPlanetTemplates():
    ret = {}
    template_path = assets.asset_folder('planet_templates')
    
    for file in os.listdir(template_path):
        xmltree = getXmlTreeByPath(f'{template_path}\{file}')
        element = xmltree.getroot()
        name = element.attrib['internalID']
        ret[name] = xmltree

    return ret


def readCsvByKey(key):
    lines = []
    path = assets.asset_file2(key)
    
    with open(path) as text:
        for line in text:
            ls = line.strip()
            if (ls != ''):
                # print(line)
                lines.append(ls.strip())
    return lines

def filesInPath(path_key):
    return os.listdir(assets.asset_folder(path_key))

def getFileLines(path_key, file_name):
    lines = []
    path = assets.build_path(path_key, file_name)
    
    with open(path) as text:
        for line in text:
            ls = line.strip()
            if (ls != ''):
                # print(line)
                lines.append(ls.strip())
    return lines


