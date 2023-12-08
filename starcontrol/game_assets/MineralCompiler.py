import starcontrol.game_assets.FileReader as fr

mineral_lines = fr.readCsvByKey('MineralElements')
mineral_map = {}
mineral_groups = {}
mg_ordered_keys = []

def getMineralGroup(mineral):
    #some data is misspelled
    if mineral == 'Flourine':
        mineral = 'Fluorine'
    
    if 'Common' in mineral:
        mineral = 'Common'

    if mineral in mineral_map:
        return mineral_map[mineral]
    
    lines =  [match for match in mineral_lines if mineral in match]

    for line in lines:
        parts = line.split(',')

        group = parts[3]
        if 'Common' in group:
            group = 'Common'

        
        # some templates have no element but do have a group
        # add a group reference to itself
        if group not in mineral_map:
            mineral_map[group] = group
                    
        if (mineral in parts[0] and parts[0] != mineral):
            # Carbon vs Carbon Compounds; Silicon vs SiliconCompounds
            continue

        if mineral not in mineral_map:
            mineral_map[mineral] = group
        
        if group not in mineral_groups:
            colors = parts[2].split(' ')
            ru = int(parts[5])
            # mydict[k] = v
            mineral_groups[group] = {
                # 'group': group,
                'color_red': round(float(colors[0])*255, 2),
                'color_green': round(float(colors[1])*255, 2),
                'color_blue': round(float(colors[2])*255, 2),
                'rarity': parts[4],
                'ru': ru
            }
            
            #sort by ru; store in separate list of just group names
            sorted_groups = sorted(mineral_groups.items(), key=lambda v: v[1]['ru'],reverse=True)            
            mg_ordered_keys.clear()            
            for item in sorted_groups:
                mg_ordered_keys.append(item[0])

    return mineral_map[mineral]

