import starcontrol.game_assets.FileReader as fr
import starcontrol.game_assets.ImageCompiler as ic

critter_data = fr.readCsvByKey('CritterText')
critters_by_id = {} # {'Critter16a':'Therapod'}, cache map of IDs to Names
critters = {} # {'Therapod':'Description'}


def consolidateCritters(critter_id):
    '''Returns the critter_name for use as "ID" outside of this function'''
    if critter_id in critters_by_id:
        return critters_by_id[critter_id]
    
    critter_name, description = getStuff(critter_id)
    critters_by_id[critter_id] = critter_name
    critters[critter_name] = description

    ic.consolidateCritterImage(critter_id, critter_name)
    return critters_by_id[critter_id]


def getStuff(critter_id):
    match_name = f'Critter_{critter_id}_Name'
    match_desc = f'Critter_{critter_id}_Desc'

    name_data = [match for match in critter_data if match_name in match]
    desc_data = [match for match in critter_data if match_desc in match]

    name_parts = name_data[0].split(',')
    desc_parts = desc_data[0].split(',') 

    #Descriptions with commas will split into many pieces:
    #Critter_Critter4a_Desc,"A large, subterranean worm. Does it secrete a number of powerful drugs? Yes, probably several."
    desc_parts.pop(0) # remove the identifier
    
    return condenseName(name_parts[1], ','.join(desc_parts))

def condenseName(critter_name, critter_desc):
    if 'Drone' in critter_name or 'Galamide' in critter_name:
        return 'Drone', 'Drones to perform a variety of tasks.'
    return critter_name, critter_desc