import time

start = time.time()

import json
import TextCompiler as txtc

import ImageCompiler as ic
import LoreParser as dp
import MineralCompiler as mc
import TemplateCompiler as tc
import CritterCompiler as cc
import MarkerCompiler as mkc
import GalaxyCompiler as gc

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


def export_static_templates(obj, path:str):
    f = open(path, 'w')
    f.write(json.dumps(obj, cls=CustomJSONEncoder))
    f.close()


export_static_templates(tc.planet_templates, './web_static/planet_templates.json')
export_static_templates(gc.assets_by_guid, './web_static/assets_by_guid.json')
export_static_templates(gc.solar_guids, './web_static/solar_list.json')
export_static_templates(cc.critters, './web_static/critters.json')
export_static_templates(mc.mineral_groups, './web_static/mineral_groups.json')
export_static_templates(mkc.system_markers, './web_static/system_markers.json')
export_static_templates(dp.lore_actions, './web_static/lore_actions.json')


print(f'COMPLETED IN {round(time.time() - start, 2)} SECONDS')