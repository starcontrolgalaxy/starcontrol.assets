import FileReader as fr

from PlanetTemplate import PlanetTemplate

template_xml_dict = fr.readPlanetTemplates()
planet_templates = {}

def getTemplate(template_id):
    if template_id in planet_templates:
        return planet_templates[template_id]
    
    t = template_xml_dict[template_id]
    
    converted = PlanetTemplate(t, template_xml_dict)
    
    planet_templates[converted.name] = converted

    return planet_templates[template_id]
