from xml.dom.minidom import Element

from .GalaxyObject import GalaxyObject


class Starbase(GalaxyObject):
#<Starbase internalID="Origins_Inner Source Starbase" 
# guid="1121-c14738e88" 
# name="Inner Source Starbase" 
# shipDesignName="Precursor_Starbase" 
# shipDesignScale="0.010000" 
# posX="304.899994" posY="187.600006" group=""/>
	
    def __init__(self, element:Element):
        super().__init__(element)

        self.pos_x = element.attrib['posX']
        self.pos_y = element.attrib['posY']
        self.ship_design_name = element.attrib['shipDesignName']
    
    def print_details(self):
            print(self.name.upper())
    
    # def ui_object(self):
    #      obj = super().ui_object()
    #      obj['ship_design_name'] = self.ship_design_name
    #      return obj
