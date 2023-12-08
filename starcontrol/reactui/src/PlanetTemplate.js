import { useContext } from  'react';
import { PlanetoidGuid } from "./App";

import Resources from './Resources'
import Hazards from './Hazards';
import Critters from './Critters';
import Markers from './Markers';

import './PlanetTemplate.css';

import data from './static_data/assets_by_guid.json'
import templates from './static_data/planet_templates.json'


function PlanetoidDetails() {
    const {selected_planetoid_guid} = useContext(PlanetoidGuid);

    console.log('PlanetoidDetails return');
    return (
        <div className="PlanetTemplate">
            <h3>{data[selected_planetoid_guid].name}</h3>
            [{templates[data[selected_planetoid_guid].planet_template].type ?
                <span>
                    {templates[data[selected_planetoid_guid].planet_template].type}
                </span>                
                : 
                <span>
                    {data[selected_planetoid_guid].name}
                </span>
            }]<br />
            {/* [{data[selected_planetoid_guid].guid}]<br /> */}
            {/* Billboard [{templates[data[selected_planetoid_guid].planet_template].billboard}]<br /> */}
            {/* Most Inh. [{templates[data[selected_planetoid_guid].planet_template].most_inherited}]<br />
            Hier. [{templates[data[selected_planetoid_guid].planet_template].template_hierarchy_str}]<br /> */}
            {/* [{templates[data[selected_planetoid_guid].planet_template].template_hierarchy_str}]<br /> */}<br />
            {/* orbit: {data[selected_planetoid_guid].orbit_radius}<br />
            radius: {data[selected_planetoid_guid].radius}<br />
            rotation: {data[selected_planetoid_guid].rotation_speed} */}
            {/* [CanLand] {templates[data[selected_planetoid_guid].planet_template].can_land}<br /> */}
            {/* [{templates[data[selected_planetoid_guid].planet_template].template_hierarchy_str}]<br /> */}
            <Hazards />
            <Resources />
            <Critters />
            <Markers />
        </div>
    )   
}

export default PlanetoidDetails;