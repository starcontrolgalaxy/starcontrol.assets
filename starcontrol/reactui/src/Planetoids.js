import React, { useContext } from "react";

import data from './static_data/assets_by_guid.json'

import Planetoid from './Planetoid';
import { SystemGuid } from "./App";

function Planetoids() {
    const {selected_system_guid} = useContext(SystemGuid);
    console.log('Planetoids return');
    return (
        <div className="SolarPlanetoids">
            {/* [{data[selected_system_guid].planetoid_guids}] */}
        { data[selected_system_guid].planetoid_guids.map((p) =>
            <Planetoid key={p} guid={p} />
        )}
      </div>
    )
}

export default Planetoids;