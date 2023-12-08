import {useContext} from 'react'
import { PlanetoidGuid } from './App';

import markers from './static_data/system_markers.json'

function Markers() {
    const {selected_planetoid_guid} = useContext(PlanetoidGuid);

    console.log('Markers return');
    if (markers[selected_planetoid_guid]) { //.length > 0) {
        return (
            <div>
                <hr />
                <h3>MARKERS</h3>
                {markers[selected_planetoid_guid].map((m,i) => 
                    <div key={i}>
                        {m}<br />
                        <img src={require(`./static_data/images/${m}-small.png`)} title={m}></img>
                        <br />
                    </div>
                )}
            </div>
        )
    }
    else {
        return (<div></div>)
    }
}

export default Markers;