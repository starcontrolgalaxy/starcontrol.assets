import TextCompiler as tc

class LoreActions(): 
    def __init__(self, dialog_script):
        self.id = ''

        self.player_inventory_add_component = []
        self.popup_text_inventory = []
        self.player_change_ru = []
        self.fleet_add_ship = []
        # self.player_install_component = []
        # self.player_refill_fuel = []
        # self.player_inventory_has_item = []
        # self.player_emable_ship_compont_temp = []

        for line in dialog_script:
            if 'Player.InventoryAddComponent' in line:
                # <script>Player.InventoryAddComponent("EnhancedThruster")</script>
                parts = line.split('"')
                self.player_inventory_add_component.append(parts[1])
            elif 'PopupText.Inventory' in line:
                # <script>PopupText.Inventory("./UI/Art/StarControlStyle/QuestIcons/QuestIcon_NewQuestObjective.dds","Popup_Inventory_Thruster2")</script>
                # Lore_226 has non-component PopupText.Inventory
                # <script>PopupText.Inventory("./UI/Art/StarControlStyle/QuestIcons/QuestIcon_NewQuestObjective.dds","Popup_Quest_TrandelMiniQuestDone")</script>                
                parts = line.split('"')
                if 'Popup_Inventory' in parts[3]:
                    self.popup_text_inventory.append(tc.popup_text[parts[3]].replace('Received: ',''))
            elif 'Player.ChangeRU' in line:           
                # Free RU
                # <script>Player.ChangeRU(3000)</script>
                parts = line.split('(')
                self.player_change_ru.append(parts[1].replace(')</script>',''))
            elif 'Fleet.AddShip' in line:
                # <script>Fleet.AddShip(player,ShipDannath)</script>
                # this tag also in the *RandomCrashedShip* xml ...  
                # use same to get those ship names too?
                parts = line.split(',')
                self.fleet_add_ship.append(parts[1].replace(')</script>',''))

            # these do not exist in dialog files, but not in Lore dialogs:
                # The other ship officers
                # <script>Player.InstallComponent("ScienceOfficer1",32,true)</script>
            
                # Free fuel
                # <script>Player.RefillFuel()</script>

                # required mins for various quests
                # Player.InventoryHasItem(Polonium)
                
                # In Starbase and Melnorm files - use in "coponent browser" feature where to find gear
                # <script>Player.EnableShipComponentTemp("HyperDrive2",true)</script>


# ShipNames.csv has the "correct" names
# ShipName_Dannath,Xraki Devourer 
# ShipName_Drenkend,Drenkend Carrier
# ShipName_Measured,The Measured Response
# ShipName_Phamysht,Phamysht Consumer
# ShipName_Scryve,Scryve Battlecruiser
# 


# which Lores have multiple string keys?
    # "Lore_4": {
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "\"Dan'Nath Ship\"",  ###### Xraki Devourer
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #    "player_change_ru": [],
    #    "fleet_add_ship": [
    #        "ShipDannath"
    #    ]
    # },
    # "Lore_6": {
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "Drenkend Ship",  ###### Drenkend Carrier
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #     "player_change_ru": [],
    #    "fleet_add_ship": [
    #        "ShipDrenkend"
    #    ]
    # },
    # "Lore_8": {
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "Drenkend Ship",  ###### Drenkend Carrier
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #    "player_change_ru": [],
    #    "fleet_add_ship": [
    #        "ShipDrenkend"
    #    ]
    # },
    # "Lore_19": {
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "Measured Ship",  ###### The Measured Response
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #    "player_change_ru": [],
    #    "fleet_add_ship": [
    #        "ShipMeasured"
    #    ]
    # },
    # "Lore_43": {
    #     "id": "",
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "Phamysht Ship",  ###### Phamysht Consumer
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #     "player_change_ru": [],
    #    "fleet_add_ship": [
    #        "ShipPhamysht"
    #    ]
    # },
    # "Lore_63": {
    #     "id": "",
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "Scryve Battlecruiser",  ###### Scryve Battlecruiser
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #     "player_change_ru": [],
    #    "fleet_add_ship": [
    #        "ShipScryve"
    #    ]
    # },
    # "Lore_71": {
    #     "id": "",
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "Scryve Battlecruiser",  ###### Scryve Battlecruiser
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #     "player_change_ru": [],
    #    "fleet_add_ship": [
    #        "ShipScryve"
    #    ]
    # },
    # "Lore_89": {
    #     "id": "",
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "Tywom Defender",
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #     "player_change_ru": []
    # },
    # "Lore_92": {
    #     "id": "",
    #     "player_inventory_add_component": [],
    #     "popup_text_inventory": [
    #         "Tywom Defender",  ###### Tywom Defender
    #         "Fleet docking points all occupied. This ship will wait for us at the nearest starbase."
    #     ],
    #     "player_change_ru": [],
    #    "fleet_add_ship": [
    #        "ShipTywom"
    #    ]
    # },