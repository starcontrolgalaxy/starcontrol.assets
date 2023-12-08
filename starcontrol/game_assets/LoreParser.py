from .LoreActions import LoreActions

# import starcontrol.game_assets.ImageCompiler as ic
import starcontrol.game_assets.FileReader as fr
# import starcontrol.game_assets.TextCompiler as tc


# Test case: CrewQuarters exists in Lore_(179,086,076,077)
# ship_components = {}
lore_actions = {} 



def init():
    file_names = [f for f in fr.filesInPath('lore_scripts') if 'Lore_' in f]

    for dialog in file_names:
        lore_id = makeLoreKey(dialog)
        dialog_lines = fr.getFileLines('lore_scripts', dialog)
        lore_actions[lore_id] = LoreActions(dialog_lines)
        #TODO: how does this compare: 
        # list comprehension for key strings 
        # would iterate the whole file multiple times?
        # vs iterate the file once parsing for 



def makeLoreKey(filename):    
    # GalaxyMarkers.xml has no leading zeroes
    # e.g. Lore_1, Lore_99
    # The actual Lore script files do have leading zeroes
    # e.g. Lore_001, Lore_099
    # strip the leading zeros
    parts = filename.split('_')
    return f'{parts[0]}_{int(parts[1])}'



init()




# def buildLoreMarkers():
#     '''
#     Upgrade parts for the ship are found at Lore markers
#     and specific which upgrade part is within associated script xml.
#      search all files file the specific text adding ship components
#      '''

#     # choosing "manual" line reading because we're looking for 2 things
#     # not sure if list comprehension or some other "built in" way 
#     # can search for 2 things...   maybe research for later?
#     path, files = fr.filesInPath('lore_scripts')
#     for file in files:
#         # if 'Lore' in file:
#         lines = fr.readCsvInPath(f'{path}/{file}')

        
#         component_key = ''
#         component_name = ''
#         for line in lines:
#             if 'Player.InventoryAddComponent' in line:
#                 # <script>Player.InventoryAddComponent("EnhancedThruster")</script>
#                 parts = line.split('"')
#                 component_key = parts[1]
#             if 'PopupText.Inventory' in line:
#                 # <script>PopupText.Inventory("./UI/Art/StarControlStyle/QuestIcons/QuestIcon_NewQuestObjective.dds","Popup_Inventory_Thruster2")</script>
#                 parts = line.split('"')
#                 component_name = tc.popup_text[parts[3]].replace('Received: ','')

#                 # The other ship officers
#                 # Player.InstallComponent("ScienceOfficer1",32,true)</script>
            
#                 # Free RU
#                 # Player.ChangeRU

#                 # Free fuel
#                 # Player.RefillFuel()

#                 # required mins for various quests
#                 # Player.InventoryHasItem(Polonium)
                
#                 # Melnorme trading - in feature where to find gear
#                 # Player.EnableShipComponentTemp

#         if component_key != '' and component_name != '':
#             # GalaxyMarkers.xml has no leading zeroes
#             # e.g. Lore_1, Lore_99
#             # The actual Lore script files do have leading zeroes
#             # e.g. Lore_001, Lore_099
#             parts = file.split('_')
#             lore_key = f'{parts[0]}_{int(parts[1])}'
#             # if lore_key not in lore_markers:
#             #     lore_markers[lore_key] = []
#             ship_components[lore_key] = component_key
#             ic.createLoreImage(component_key)
#     # Beta Eleventum I: "Received: Flame Turret"

# buildLoreMarkers()