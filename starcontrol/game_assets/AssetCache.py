

# Planet templates need to "walk up" the inheritance
# hierarchy for some properties and xml elements
# Before AssetCache: PlanetTemplates were created 
# the TemplateCompiler creates a new instance of PlanetTemplate
# which in turn would need to lookup another template
# from the TemplateCompiler...  creating a circular reference?
#....
# Well the "circlar reference" works.
#....
# That said.. some Compilers will read through raw data 
# on every call to get something, so maybe converting all those
# things into ready-to-use obects on a first pass would help?
# If anythingi t'd help the processing time, which... 
# Static file generation time before this class was implemented:
# COMPLETED IN 8.93 SECONDS
# (giv or take a few ms)

