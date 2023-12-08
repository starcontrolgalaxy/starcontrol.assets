from xml.dom.minidom import Element


class GalaxyObject:
    'Base class for common attributes of things found on the galaxy map'
    def __init__(self, element:Element):
        #self.element = element
        
        self.guid = element.attrib['guid']
        self.name = element.attrib['name']