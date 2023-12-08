from xml.dom.minidom import Element

from .GalaxyObject import GalaxyObject

import starcontrol.game_assets.TemplateCompiler as tc
import starcontrol.game_assets.MarkerCompiler as mc

class SolarSystem(GalaxyObject):
#<SolarSystem 
# guid="3-100002468" 
# name="Arcturus" 
# posX="189.399994" 
# posY="412.500000" 
# starTemplate="red" 
# radius="55.000000" 

# internalID="Origins_Arcturus" 
# isArena="false" 
# enabledForSMB="false" 
# canBeWanderedIn="true" 
# background="GreenNebula" 
# starMeleeGravityRadius="10.000000" 
# starMeleeGravityMagnitude="8.500000" 
# factionTemplate="scryve" group="">
	
    def __init__(self, element:Element):
        super().__init__(element)

        self.pos_x = round(float(element.attrib['posX']), 2)
        self.pos_y = round(float(element.attrib['posY']), 2)
        self.radius = round(float(element.attrib['radius']), 2)
        self.star_template = 'yellow' if element.attrib['starTemplate'] == 'sun' else element.attrib['starTemplate']
        self.faction_template = element.attrib['factionTemplate']

        self.total_ru = 0
        self.total_critters = 0

        mc.buildMarker(self.guid)
        self.planetoid_guids = []
        self.rainbow_world = False

        self.storeGuids(element)
        
        # Hacked in for Gamma Jutinim A having 0 planetoids
        # if not any(self.planetoid_guids):
        #     self.planetoid_guids.append('default')

    def storeGuids(self, element):
        ''' Stores a reference to nested planetoid guid and 
            Scrapes nested Planetoids for summary to raise up to SolarSystem level'''
        for planetoid in element:
            if (planetoid.tag == 'Planetoid'):
                planet_template = planetoid.attrib['planetTemplate']                
                template = tc.getTemplate(planet_template)
                self.total_ru += template.ru
                self.total_critters += template.critter_count_consolidated
                
                if planet_template == 'Rainbow':
                    self.rainbow_world = True 
                self.planetoid_guids.append(planetoid.attrib['guid'])
                self.storeGuids(planetoid) 

#<AsteroidBelt internalID="Origins_The Asteroid Belt" 
# guid="89-a44d94944" 
# name="The Asteroid Belt" 
# orbitRadius="60.000000" radius="3.500000" 
# asteroidBeltTemplate="default"/>

#<AsteroidBelt internalID="Origins_The Kuiper Belt" 
# guid="89-a44d94945" 
# name="The Kuiper Belt" 
# orbitRadius="152.000000" radius="3.500000" 
# asteroidBeltTemplate="default"/>

#<AsteroidBelt internalID="Origins_Proxima Centauri Asteroid Belt" 
# guid="3-a00000206" 
# name="Proxima Centauri Asteroid Belt" 
# orbitRadius="21.000000" radius="5.500000" 
# asteroidBeltTemplate="default"/>
	