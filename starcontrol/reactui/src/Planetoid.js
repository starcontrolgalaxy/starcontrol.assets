import React, { useContext } from "react";

import "./Planetoid.css"

import templates from './static_data/planet_templates.json'
import critters_consolidated from './static_data/critters.json'
import data from './static_data/assets_by_guid.json';
import mineral_groups from './static_data/mineral_groups.json'
import markers from './static_data/system_markers.json'

import { PlanetoidGuid } from "./App";
import MarkerIcons from "./MarkerIcons";

function Planetoid({ guid }) {
    const {selected_planetoid_guid, setPlanetoidGuid} = useContext(PlanetoidGuid);

    console.log('Planetoid return');
    return (
        <div className={['Planetoid', 
                guid === selected_planetoid_guid ? 'SelectedPlanetoid' : '',
                data[guid].planet_template == "Rainbow" ? 'rainbow-box' : ''
            ].join(' ')}
            style={{
                'paddingLeft': 10+15*data[guid].nest_level}}
                onClick={() => setPlanetoidGuid(guid)}
            >
            <div className="PlanetoidHeader">
                <div className="HeaderLeft">
                    {data[guid].name}
                </div>
                <div className="HeaderRight">
                    [{templates[data[guid].planet_template].ru}]
                </div>
            </div>
            <div className="PlanetoidDetails">
                <div className="DetailsLeft">
                    {markers[guid] ? 
                        <MarkerIcons guid={guid} />
                        : 
                        ''
                    }
                    {templates[data[guid].planet_template].critters_consolidated.map((c, i) => 
                        <span key={i} title={critters_consolidated[c.critter_name]} >
                            <img title={critters_consolidated[c.critter_name]}
                                src={require(`./static_data/images/${c.critter_name}-small.png`)}></img>
                        </span>)}
                </div>
                <div className="DetailsRight">
                    {templates[data[guid].planet_template].mineral_groups.slice(0).reverse().map((mg, i) => 
                        <svg key={i} className="mineralSvg" >
                            <title id={i}>{mg} [{mineral_groups[mg].ru}]</title>
                            <circle cx='7' cy='7' r='6' fill={`rgba(${mineral_groups[mg].color_red},${mineral_groups[mg].color_green},${mineral_groups[mg].color_blue},1)`} />
                        </svg>
                    )}
                </div>
            </div>
        </div>
    )
}

export default Planetoid;