from xml.etree.ElementTree import Element, ElementTree

import CritterCompiler as cc
import MineralCompiler as mc
import TemplateCompiler as tc
import TextCompiler as txtc

class PlanetTemplate():
    def __init__(self, tree:ElementTree, template_xml):
        element = tree.getroot()
        self.name = element.attrib['internalID']
        self.inherits_from = element.attrib['inheritsFrom']

        template_type = self.walkInheritsForAttribute(element, 'type')
        self.type = txtc.planetscan_types[template_type] if template_type in txtc.planetscan_types else template_type
        
        mineral_record = tree.find('mineralRecord')
        if (mineral_record is not None):
            self.ru = int(mineral_record.attrib['totalRu'])
        else: self.ru = 0

        mineral_records = tree.findall('mineralRecord/elementWeights/MineralElementWeightRecord')
        if (mineral_records is not None):
            mineral_groups = {} #used to distinct keys coming in..  better way?

            for mineral in mineral_records:
                elm = ''
                if 'element' in mineral.attrib and mineral.attrib['element'] != '':
                    elm = mineral.attrib['element']
                else : elm = mineral.attrib['group'] 

                group = mc.getMineralGroup(elm)
                mineral_groups[group]=0
            
            #sort the mineral groups by the already ru-sorted compiler's mineral groups
            d = {v:i for i, v in enumerate(mc.mg_ordered_keys)}
            self.mineral_groups = sorted(mineral_groups.keys(), key=lambda v: d[v]) 


        # TODO: Hazards need to walk-up the inherits_from tree
        # e.g. Io in UI doesn't show hazards because its base planet templates has none
        # but it inherits from does have all the volcanoes
        self.hazards = self.parseHazards(tree.findall('hazardRecord/hazardCounts/HazardCountRecord'))
        
        critters = tree.findall('critterRecord/critterCounts/CritterCountRecord')
        self.critters_consolidated = []
        self.critter_count_consolidated = 0
        
        if (len(critters) > 0):
            critter_counts = {}
            for critter in critters:
                critter_name = cc.consolidateCritters(critter.attrib['critter'])
                if critter_name not in critter_counts:
                    critter_counts[critter_name] = 0
                
                critter_counts[critter_name] += int(critter.attrib['count'])

            for k,v in critter_counts.items():
                self.critter_count_consolidated += v
                self.critters_consolidated.append({
                    'critter_name':k,
                    'count':v
                })

        hazard_levels = { #from the game UI
            'Karn':{'weather': 2,'toxic':8, 'heat':0},
            'Kafs':{'weather': 0,'toxic':0, 'heat':0},
            'Mercury':{'weather': 2.0,'toxic': 8.0, 'heat': 5.0},
            'Ganymede':{'weather': 4.0,'toxic': 0.0, 'heat': 2.5},
        }

        #     'Emerald':{'weather': 2(),'toxic':8,'heat':3},
        #     'Halogen':{'weather': 2(),'toxic':7,'heat':3},
        #     'Halide':{'weather': 4(3.4),'toxic':0,'heat':0},
        #     'Iodine':{'weather': 2(2.0),'toxic':78(7.7),'heat':0}
        # }
        self.weather_factor = round(10*float(element.attrib['weatherFactor']),1) if 'weatherFactor' in element.attrib else 0
        self.toxicity_factor = round(10*float(element.attrib['toxicityFactor']),1) if 'toxicityFactor' in element.attrib else 0
        self.temperature_factor = round(10*float(element.attrib['temperatureFactor']),1) if 'temperatureFactor' in element.attrib else 0

        # self.gravity_factor = element.attrib['gravityFactor']
        # self.biology_factor = element.attrib['biologyFactor']
        
        # templates can inherit some properties from other templates
        # so set such properties walking the inheritance tree as necessary
        self.templateHierarchy(self.name, template_xml, [])
        # self.template_hierarchy_str = ''# '>'.join(self.template_hierarchy)

        # self.can_land = self.canLand(self.name, template_xml)
        # print(self.template_hierarchy)

    def walkInheritsForAttribute(self, element:Element, attr_name):
        if attr_name in element.attrib:            
            return element.attrib[attr_name]
        else:
            parent_template = tc.template_xml_dict[element.attrib['inheritsFrom']].getroot()
            if parent_template.attrib['internalID'] != 'default':
                return self.walkInheritsForAttribute(parent_template, attr_name)
            else:
                return f''

    def parseHazards(self, hazard_elements):
            hazards = []
            if (hazard_elements is not None):
                for hazard in hazard_elements:
                    hazards.append({
                        "hazard": hazard.attrib['hazard'],
                        "count": hazard.attrib['count']
                    })
            return hazards
    
    def templateHierarchy(self, template, templates, template_names:list):
        if template != 'default':
            self.most_inherited = template
            template_names.append(template)

        # self.template_hierarchy.append(template)
        t = templates[template]
        e = t.getroot()        

        if 'inheritsFrom' in e.attrib and e.attrib['inheritsFrom'] != '': # default template a  top inherits from empty string
            self.templateHierarchy(e.attrib['inheritsFrom'], templates, template_names)
        else : self.template_hierarchy_str = '>'.join(template_names)

        

    # def canLand(self, template, templates):
    #     # print(template)
    #     # self.template_hierarchy += f'{template}>'
    #     t = templates[template]
    #     e = t.getroot()

    #     if 'canLand' in e.attrib and e.attrib['canLand'] != '':
    #         return int(e.attrib['canLand'])
    #     else: 
    #         if 'inheritsFrom' in e.attrib and e.attrib['inheritsFrom'] != '':
    #             inh = e.attrib['inheritsFrom']
    #         else : inh = 'default'
            
    #         return self.canLand(inh, templates)


