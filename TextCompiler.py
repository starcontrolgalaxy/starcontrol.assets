# This compiler should be initialized (?) before any others
import FileReader as fr

planetscan_types = {}
local_text = fr.readCsvByKey('LocalText')
planetscan_lines = [i for i in local_text if 'UI_PlanetScan_PlanetType_' in i]
for line in planetscan_lines:
    s = line.split(',')
    planetscan_types[s[0]] = s[1]


popup_text = {}
for line in fr.readCsvByKey('popup_text'):
    s = line.split(',')
    popup_text[s[0]] = s[1]


component_descriptions = {} # {'key':{'name', 'description'}}
# Key,Translated String
# ShipComponent_CrewQuarters_Description,"Your crew will die on occasion. This is regrettable, but such is life. Here's where you keep spares."
for line in fr.readCsvByKey('component_descriptions'):
    s = line.split(',')
    # The full key does not appear anywhere else, but the actual component name does
    scd_key = s[0].replace('ShipComponent_','').replace('_Description', '')
    component_descriptions[scd_key] = s[1]


component_names = {}
# Key,Translated String
# ShipComponent_CrewQuarters,Crew Quarters
for line in fr.readCsvByKey('component_names'):
    s = line.split(',')
    # The full key does not appear anywhere else, but the actual component name does
    scd_key = s[0].replace('ShipComponent_','')
    component_names[scd_key] = s[1]


ship_names = {}
# Key,Translated String
# ShipName_GenericShip_Medium01,Jebyoux Patroller
for line in fr.readCsvByKey('ship_names'):
    s = line.split(',')
    # The full key does not appear anywhere else, but the actual component name does
    scd_key = s[0].replace('ShipName','')
    ship_names[scd_key] = s[1]


# StarControlCharacters.xml
# NoteThe following lines does not exist for all instances of RandomCrashShip
# <Character guid="95-000000001" internalID="RandomCrashedShip001" displayName="UI_PlanetScan_UnknownObject" avatarShipID="Ship404Placeholder" avatarGroundUnitID="GenericShip_Medium01" fleetID="MeleeTestFleet" dialogTreeName="RandomCrashedShipGenericMedium1" spawnMarker="RandomCrashedShipLoc001" dialogPortrait="FirstOfficer100.dds" planetRep="false" canBeAttacked="false" canBeIgnored="false" spawnOnStartup="true" />
# another form that appears to have all Lore_(001,258)
# <Character guid="1-000020001" internalID="Lore_001_CrashedDanNath01" displayName="UI_PlanetScan_UnknownObject" avatarShipID="Ship404Placeholder" avatarGroundUnitID="CrashedShip_Xraki01" fleetID="MeleeTestFleet" dialogTreeName="Lore_001_CrashedDanNath01" spawnMarker="Lore_1" dialogPortrait="FirstOfficer100.dds" planetRep="false" canBeAttacked="false" canBeIgnored="false" spawnOnStartup="true" />
  
