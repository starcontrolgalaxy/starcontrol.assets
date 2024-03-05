from xml.dom.minidom import Element

from GalaxyObject import GalaxyObject
import MarkerCompiler as mc

class Planetoid(GalaxyObject):
#<Planetoid internalID="Origins_Arcturus I" 
# guid="3-100002469" 
# name="Arcturus I" 
# orbitRadius="225.799988" 
# radius="2.600000" 
# rotationSpeed="1.300000" 
# planetTemplate="Green"

# orbitYaw="-279.621582" 
# axisTilt="0.000000"  
# meleeOrbitSpeed="0.028877" 
# meleeGravityRadius="10.000000" 
# meleeGravityMagnitude="7.250000">

    def __init__(self, element:Element, layer:int):
        super().__init__(element)

        self.nest_level = layer
        
        self.radius = round(float(element.attrib['radius']), 2)
        self.orbit_radius = round(float(element.attrib['orbitRadius']), 2)
        self.rotation_speed = round(float(element.attrib['rotationSpeed']), 2)
        mc.buildMarker(self.guid)
        self.planet_template = element.attrib['planetTemplate']