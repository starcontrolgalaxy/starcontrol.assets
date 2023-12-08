import { useContext } from  'react';
import { PlanetoidGuid } from "./App";

import templates from './static_data/planet_templates.json'
import critters_consolidated from './static_data/critters.json'
import data from './static_data/assets_by_guid.json'

function Critters() {
    const {selected_planetoid_guid} = useContext(PlanetoidGuid);
    
    console.log('Critters return');
    if (templates[data[selected_planetoid_guid].planet_template].critter_count_consolidated > 0) {
        return (
            <div>
                <hr />
                <h3>CRITTERS</h3>
                {templates[data[selected_planetoid_guid].planet_template].critters_consolidated.map((c, i) => 
                    <span key={i} title={critters_consolidated[c.critter_name]} style={{'display':'block'}}>
                        {c.critter_name} [{c.count}]
                         <img src={require(`./static_data/images/${c.critter_name}-small.png`)}></img><br />
                    </span>
                )}
            </div>
        )
    }
    else {
        return (<div></div>)
    }

}
export default Critters;