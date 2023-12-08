import React, { useState, useContext } from "react";

import './SolarList.css'

import data from './static_data/assets_by_guid.json'
import solar_list from './static_data/solar_list.json'
import markers from './static_data/system_markers.json'

import { SystemGuid } from "./App";
import MarkerIcons from "./MarkerIcons";

function SolarList() {
    const {selected_system_guid, systemClicked} = useContext(SystemGuid);

    const [search_term, setSearchTerm] = useState('');
    const searchTermChanged = (e) => {
      setSearchTerm(e.target.value.toLowerCase());
    }

    const [markers_filter, setMarkersFilter] = useState(true);
    const markersFilterChanged = (e) => {
      console.log('MARKER FILTERS CHANGED', e.target.checked);
      setMarkersFilter(e.target.checkrf);
    }
    
    console.log('SolarList return');
    return (
      <div className="SolarList">
        <h2>Solar Systems</h2>
        <input type="text"
          onChange={searchTermChanged} />  
        {/* <input type="checkbox" onChange={markersFilterChanged} /> */}
        <div className="SolarList">
          { solar_list
              .filter(ss => ss.name
                .toLowerCase()
                .includes(search_term.toLowerCase()))
              .map((sg) => 
                <div key={data[sg.guid].guid} 
                    className={['SolarSearchItem', 
                    sg.guid === selected_system_guid ? 'SelectedSystem' : ''
                  ].join(' ')}
                  onClick={() => systemClicked(sg)}>
                  <div className="SearchItemHeader">
                    <div className="HeaderLeft">
                      <svg className="planetSvg">
                          <circle cx='7' cy='7' r='6' fill={data[sg.guid].star_template} />
                      </svg>
                      <strong>{data[sg.guid].name}</strong> 
                    </div>
                    <div className={["HeaderRight",
                        data[sg.guid].rainbow_world ? 'rainbow-box': ''
                        ].join(' ')}
                    >
                      RU [{data[sg.guid].total_ru}]
                    </div>
                  </div>
                  <div className="SearchItemDetails">
                    <div className="DetailsLeft">
                      {markers[sg.guid] ? 
                          <MarkerIcons guid={sg.guid} />
                          : '' }
                      {data[sg.guid].planetoid_guids.map((pg, pgi) =>
                        <div key={pgi}>
                          {markers[pg] ? 
                              <MarkerIcons guid={pg} />
                              : '' }
                        </div>
                      )}
                    </div>
                    <div className="DetailsRight">
                      CR [{data[sg.guid].total_critters}]
                    </div>
                  </div>
                </div>
              )}
          </div>
        </div>
    )
}

export default SolarList;