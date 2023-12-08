import sys
import starcontrol.game_assets.FileReader as fr
from .GalaxyObject import GalaxyObject
from .Planetoid import Planetoid
from .Starbase import Starbase
from .SolarSystem import SolarSystem

galaxy_elements = fr.getXmlTreeByAssetKey('StarControlGalaxyxml')

assets_by_guid = {} #FLATTENED ASSETS KEYED BY GUID

# Hacked in for Gamma Jutinim A having 0 planetoids
# # for whatever reason, was having problems getting js code to find legth
# assets_by_guid['default'] = {
#         "guid": "default",
#         "name": "default",
#         "nest_level": 0,
#         "radius": 0,
#         "orbit_radius": 0,
#         "rotation_speed": 0,
#         "planet_template": "default"}

solar_guids = [] #used by the search list; needs a small subset of SolarSystem data

def recurseChildren(xml, layer):
    for child_node in xml:
        if (child_node.tag != 'AsteroidBelt'):
            element = elementDto(child_node, layer)
            registerSolarGuid(element, child_node.tag)
            assets_by_guid[element.guid] = element
            recurseChildren(child_node, layer+1)

def registerSolarGuid(object_element:SolarSystem, tag:str):
     if (tag == 'SolarSystem'):
        solar_guids.append({
            'guid' : object_element.guid, 
            'name' : object_element.name
        })

def elementDto(xml, layer):
        ElementClass = getattr(sys.modules[__name__], f'{xml.tag}') #xml tag matches class name
        if (xml.tag == 'Planetoid'):
            object_element = ElementClass(xml, layer) #instantiate class for xml tag
        else:
             object_element = ElementClass(xml)
        return object_element
    
recurseChildren(galaxy_elements.getroot(), -1)
