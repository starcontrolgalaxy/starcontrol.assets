import React, { useContext } from "react";

import './SolarDetails.css';

import data from './static_data/assets_by_guid.json'
import markers from './static_data/system_markers.json'

import { SystemGuid } from "./App";
import MarkerIcons from "./MarkerIcons";

function SolarDetails() {
    const {selected_system_guid} = useContext(SystemGuid);
    console.log('SolarDetails return')
    return (
        <div className="SolarDetails">
            <div style={{'display':'float', 'float':'left', 'width':'50%'}}>
                <h2>{data[selected_system_guid].name}</h2>
                {/* [{data[selected_system_guid].guid}] */}
                [{data[selected_system_guid].pos_x}]
                [{data[selected_system_guid].pos_y}]  
                [{data[selected_system_guid].faction_template}]
            </div>
            <div className="DetailsLeft">
                {/* <MarkerIcons guid={selected_system_guid} /> */}
                
                {markers[selected_system_guid] ? 
                    <MarkerIcons guid={selected_system_guid} />
                    : '' }
                
                {data[selected_system_guid].planetoid_guids.map((pg, i) => 
                    <div key={i}>
                        {markers[pg] ? 
                            <MarkerIcons guid={pg} />
                        : '' }
                    </div>
                )} 
            </div>
        </div>
    );
}

export default SolarDetails;