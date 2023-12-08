import { useContext } from  'react';
import { PlanetoidGuid } from "./App";

import data from './static_data/assets_by_guid.json'
import templates from './static_data/planet_templates.json'

function Hazards() {
    const {selected_planetoid_guid} = useContext(PlanetoidGuid);
    
    console.log('Hazards return');
    return (
        <div>
            <hr />
            <h3>HAZARDS</h3>
            <img src={require('./static_data/images/Wind.png')} /> [{templates[data[selected_planetoid_guid].planet_template].weather_factor}] 
            <img src={require('./static_data/images/Toxic.png')} /> [{templates[data[selected_planetoid_guid].planet_template].toxicity_factor}] 
            <img src={require('./static_data/images/Heat.png')} /> [{templates[data[selected_planetoid_guid].planet_template].temperature_factor}]
            {templates[data[selected_planetoid_guid].planet_template].hazards.length > 0 ?
                <div>
                    {templates[data[selected_planetoid_guid].planet_template].hazards.map((h,i) => 
                        <span key={i} style={{'display':'block'}}>
                            {h.hazard} [{h.count}]
                        </span>
                    )}
                </div>
                : ''
            }
        </div>
    )
}
export default Hazards