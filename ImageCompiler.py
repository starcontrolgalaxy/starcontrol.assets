import subprocess
import AssetSources as assets
import FileReader as fr

magick = assets.build_file('magickexe')
uisd = assets.folder_paths['ui_static_data'] #This one starts at c:\, not intended for contantenation, thus not accessing via method

completed_images = {}
 
critter_paths = {}

for line in fr.readCsvByKey('CrittersImageData'):
    parts = line.split(',')
    critter_paths[parts[0]] = parts

def createLoreImage(key):
    source_image = f'{assets.asset_folder("lore_images")}/{key}.dds'
    dest_path = f'{uisd}\images\{key}-small.png'
    smallImage(source_image, dest_path)

def consolidateCritterImage(critter_id, critter_name):
    if critter_name in completed_images:
        return

    dest_path = f'{uisd}\images\{critter_name}-small.png'
    ca = assets.asset_folder('critter_art2')

    # image_path = [match for match in critter_image_paths if critter_id in match]
    # parts = image_path[0].split(',')
    parts = critter_paths[critter_id]
    
    if 'Critter' in  parts[1]:
        p = parts[1]
        if 'Base' in p:
            p = critter_id
        source_path = f'{ca}\{p} icon.dds'
    else: source_path = f'{assets.asset_path}\{parts[37]}'

    full_command = f'{magick} "{source_path}" -geometry 35x35 "{dest_path}"'
    result = subprocess.run(full_command, capture_output=True)
    
    if result.returncode > 0: #create default "not found" plageholder image
        # These planetoids have critters without images:
        # Alpha Repeculae IVa
        # Beta Lynx I
        # Beta Lynx III
        # Yusasa (Gamma Acroix A)
        print (f'MISSING CRITTER SOURCE IMAGE: {critter_id}')
        missing_image_command = f'{magick} -size 35x35 xc:#990000 {dest_path}'
        result = subprocess.run(missing_image_command, capture_output=True)
    
    completed_images[critter_name] = 0

def createMarkerImage(marker):
    if marker in completed_images:
        return

    dest_path_sm = f'{uisd}\images\{marker}-small.png'
    # dest_path_md = f'{uisd}\images\{marker}-medium.png'
    # ca = assets.asset_folder('critter_art2')
    source_path = assets.asset_file2(marker)

    smallImage(source_path, dest_path_sm)
    # mediumImage(source_path, dest_path_md)

    completed_images[marker] = 0

def smallImage(source_path, dest_path):
    geometry = '-geometry 35x35'
    runMagick(source_path, dest_path, geometry)

def mediumImage(source_path, dest_path):
    geometry = '-geometry 75x75'
    runMagick(source_path, dest_path, geometry)

def runMagick(source_path, dest_path, geometry):
    full_command = f'{magick} "{source_path}" {geometry} "{dest_path}"'
    result = subprocess.run(full_command, capture_output=True)
    
    if result.returncode > 0: #create default "not found" placeholder image
        # These planetoids have critters without images:
        # Alpha Repeculae IVa
        # Beta Lynx I
        # Beta Lynx III
        # Yusasa (Gamma Acroix A)
        print(result.stderr)
        print (f'MISSING SOURCE IMAGE: {source_path}')
        missing_image_command = f'"{magick}" -size 35x35 xc:#990000 "{dest_path}"'
        result = subprocess.run(missing_image_command, capture_output=True)
        r = ''

def createHazardImages():
    for l in ['Heat','Wind','Toxic']:        
        dest_path = f'{uisd}\images\{l}.png'
        runMagick(assets.asset_file2(l), dest_path,'')
        
createHazardImages()

