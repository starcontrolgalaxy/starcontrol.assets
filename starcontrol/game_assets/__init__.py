import time

start = time.time()


import json
import starcontrol.game_assets.TextCompiler as txtc

import starcontrol.game_assets.ImageCompiler as ic
import starcontrol.game_assets.LoreParser as dp
import starcontrol.game_assets.MineralCompiler as mc
import starcontrol.game_assets.TemplateCompiler as tc
import starcontrol.game_assets.CritterCompiler as cc
import starcontrol.game_assets.MarkerCompiler as mkc
import starcontrol.game_assets.GalaxyCompiler as gc

#TODO: remove duplicated in endpoints
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


def export_static_templates(obj, path:str):
    f = open(path, 'w')
    f.write(json.dumps(obj, cls=CustomJSONEncoder))
    f.close()


export_static_templates(tc.planet_templates, './starcontrol/reactui/src/static_data/planet_templates.json')
export_static_templates(gc.assets_by_guid, './starcontrol/reactui/src/static_data/assets_by_guid.json')
export_static_templates(gc.solar_guids, './starcontrol/reactui/src/static_data/solar_list.json')
export_static_templates(cc.critters, './starcontrol/reactui/src/static_data/critters.json')
export_static_templates(mc.mineral_groups, './starcontrol/reactui/src/static_data/mineral_groups.json')
export_static_templates(mkc.system_markers, './starcontrol/reactui/src/static_data/system_markers.json')
export_static_templates(dp.lore_actions, './starcontrol/reactui/src/static_data/lore_actions.json')



#TODO: these are just for the flask API
def solar_list():
    return gc.solar_guids

def template_list():
    return tc.planet_templates

def assets():
    return gc.assets_by_guid



print(f'COMPLETED IN {round(time.time() - start, 2)} SECONDS')