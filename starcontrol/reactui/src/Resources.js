import { useContext } from "react";
import { PlanetoidGuid } from "./App";

import data from './static_data/assets_by_guid.json'
import templates from './static_data/planet_templates.json'
import mineral_groups from './static_data/mineral_groups.json'

function Resources() {
    const {selected_planetoid_guid} = useContext(PlanetoidGuid);

    console.log('Ru return')
    if (templates[data[selected_planetoid_guid].planet_template].ru !== 0) {
        return (
            <div>
                <hr />
                <h3>RESOURCES</h3>
                {templates[data[selected_planetoid_guid].planet_template].mineral_groups.map((w, i) => 
                    <span key={i} style={{'display':'block'}} title={mineral_groups[w].rarity}>
                        {w} [{mineral_groups[w].ru}] 
                        <svg className="planetSvg" >
                            <circle cx='7' cy='7' r='6' fill={`rgba(${mineral_groups[w].color_red},${mineral_groups[w].color_green},${mineral_groups[w].color_blue},1)`} />
                        </svg>
                        
                    </span>)}
            </div>
        )}
    else {
        return(
            <div></div>            
        )}

}

export default Resources;