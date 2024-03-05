import FileReader as fr
import ImageCompiler as ic
import AssetSources as assets


marker_xml = fr.getXmlTreeByAssetKey('GalaxyMarkersxml')

system_markers = {} # <str,list<str>>
marker_details = {}

#add an AssetSource key matching any notable_markers
notable_markers = [
    'MelnormeTrading',

    'HumanHomeworldLoc',
    'MeasuredHomeworldLoc',
    'MenkmackHomeworldLoc',
    'MowlingHomeworldLoc',
    'MuKayHomeworldLoc',
    'PinthiHomeworldLoc',
    'ScryveHomeworldLoc',
    'TywomHomeworldLoc',
    'PhamyshtHomeworldLoc',

    'HumanColony',
    # 'MeasuredColony',
    'MenkmackColony',
    'MowlingColony',
    'MuKayColony',
    'PinthiColony',
    # 'ScryveColony',
    'TywomColony',
    # 'PhamyshtColony',
    

    'MuKayIceWorld',

    'RandomCrashedShip',
    # 'Colony',
    # 'Lore',
    # 'Fleet / Guard : indicates random fleets for race in system',
    # 'Fleet',
    # 'Guard',
    # 'MeasuredRecordCache',
    # 'Lexite',
    # 'KzantiPirate'
    # 'CrashedTywomScout'
    # 'PinthiCryptWorld'
    # 'MenkmackStorage'
    # 'CrashedScryve'
]

def buildMarker(guid) -> None:
    if guid in system_markers:
        return
    
    markers = marker_xml.findall(f'Marker[@locationID="{guid.upper()}"]')

    for element in markers:
        marker_id = element.attrib['internalID']
        keep_markers = [n for n in notable_markers if n in marker_id]
        
        if len(keep_markers) > 0:
            if guid not in system_markers:
                system_markers[guid] = []
        
            for m in keep_markers:
                # if 'Lore' in m:
                #     if marker_id in lore_markers:
                #         markers[guid].append(lore_markers[marker_id])
                # else:
                system_markers[guid].append(m)
                ic.createMarkerImage(m)



def getRandomCrashedShipName(key):    
    # GalayMarkers.xml : internalID
    # <Marker internalID="RandomCrashedShipLoc217" locationID="3-100001567" />

    # StarControlCharactes.xml : avatarGroundUnitID
    # (abbreviated attributes to just what's probably useful)
    # <Character internalID="RandomCrashedShip217" 
    #   spawnMarker="RandomCrashedShipLoc217" 
    #   avatarGroundUnitID="GenericShip_Medium01" 
    #   dialogTreeName="RandomCrashedShipGenericMedium1" 
    #   spawnOnStartup="true" />
    
    # ShipNames.csv : "ShipName_{avatarGroundUnitId}"
    # ShipName_GenericShip_Medium01,Jebyoux Patroller
    ''