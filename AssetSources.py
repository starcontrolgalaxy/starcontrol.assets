import os

script_dir = os.path.dirname(__file__)
# Original game assets:
asset_path = 'C:\Program Files (x86)\Steam\steamapps\common\Star Control - Origins\Assets'

file_paths = { #use for individual files, filename as key TODO: stop using filename as key
    'magickexe':'imagemagick/magick.exe',
    'GalaxyMarkersxml':'Characters/GalaxyMarkers.xml',
    'StarControlGalaxyxml':'Galaxies/StarControlGalaxy.xml',
    'CritterText':'Localization/English/UIText/CritterText.csv',
    'MineralElements':'Tables/MineralElements.csv',    
    'CrittersImageData':'Tables/Critters.csv',
    'LocalText':'Localization/English/UIText/Text.csv',

    #keys match notable_markers
    'RandomCrashedShip':'Ships/Misc/GenericShip_Medium04.png',
    # 'HomeworldLoc':'UI/Art/StarControlStyle/PlanetIcons/TerrestrialPlanet.dds',
    'MuKayIceWorld':'UI/Art/StarControlStyle/IceDangerIcon.dds',
    
    'MelnormeTrading':'UI/Art/StarControlStyle/Portraits/Melnorme_04.dds',
    'HumanHomeworldLoc':'UI/Art/StarControlStyle/Portraits/Earthling1_100.dds',
    'MeasuredHomeworldLoc':'UI/Art/StarControlStyle/Portraits/Measured1_128.dds',
    'MenkmackHomeworldLoc':'UI/Art/StarControlStyle/Portraits/Menkmack.dds',
    'MowlingHomeworldLoc':'UI/Art/StarControlStyle/Portraits/Mowling1_100.dds',
    'MuKayHomeworldLoc':'UI/Art/StarControlStyle/Portraits/Mukay.dds',
    'PinthiHomeworldLoc':'UI/Art/StarControlStyle/Portraits/Pinthi.dds',
    'ScryveHomeworldLoc':'UI/Art/StarControlStyle/Portraits/Scryve100.dds',
    'TywomHomeworldLoc':'UI/Art/StarControlStyle/Portraits/Tywom.dds',
    'PhamyshtHomeworldLoc':'UI/Art/StarControlStyle/SuperMelee/PilotImages/PhamyshtPilot.dds',

    'HumanColony':'Ships/Buildings/ColonyBeacon.png',
    'MeasuredColony':'Ships/Buildings/ColonyBeacon.png',
    'MenkmackColony':'Ships/Buildings/ColonyBeacon.png',
    'MowlingColony':'Ships/Buildings/ColonyBeacon.png',
    'MuKayColony':'Ships/Buildings/ColonyBeacon.png',
    'PinthiColony':'Ships/Buildings/ColonyBeacon.png',
    'ScryveColony':'Ships/Buildings/ColonyBeacon.png',
    'TywomColony':'Ships/Buildings/ColonyBeacon.png',
    'PhamyshtColony':'Ships/Buildings/ColonyBeacon.png',

    # Art/StarControlStyle/ToxicDangerIcon.dds
    'Toxic':'UI/Art/StarControlStyle/PlanetScan/Warning_Toxicity_Icon.dds',
    'Heat':'UI/Art/StarControlStyle/PlanetScan/Warning_Heat_Icon.dds',
    'Wind':'UI/Art/StarControlStyle/PlanetScan/Warning_Wind_Icon.dds',

    'popup_text':'Localization/English/Origins/PopupText.csv',
    'component_descriptions':'Localization/English/Origins/ShipComponentDescriptions.csv',
    'component_names':'Localization/English/Origins/ShipComponentNames.csv',
    # TODO: can find the random crashed ship names in here, lookup in ShipNames
    'characters':'Chracters/StarControlCharacters.xml',
    'ship_names':'Localization/English/Origins/ShipNames.csv',


    # UI\Art\StarControlStyle\QuestIcons/QuestIcons, landers, and more!
}

folder_paths = {
    'planet_templates':'PlanetTemplate',
    'ui_static_data':'./web_static',
    'critter_art2':'UI/Art/StarControlStyle/CritterIcons',
    'lore_scripts':'Dialog',
    'lore_images':'UI/Art/StarControlStyle/ShipyardComponents'
}


def asset_folder(key):
    return os.path.join(asset_path, folder_paths[key])

def asset_file2(key):
    return os.path.join(asset_path, file_paths[key])

def build_file(key):
    return os.path.join(script_dir, file_paths[key])

def build_path(path_key, file):
    return os.path.join(asset_path, folder_paths[path_key], file)