import React, { useState, createContext } from "react";

import './App.css';
import './SolarDetails.css';
import './SolarBrowser.css';

import data from './static_data/assets_by_guid';

import SolarList from './SolarList';
import SolarDetails from './SolarDetails';
import Planetoids from './Planetoids';
import PlanetTemplate from "./PlanetTemplate";
import ShipComponents from "./ShipComponents";

export const SystemGuid = createContext();
export const PlanetoidGuid = createContext();

function App() {  
  const [selected_planetoid_guid, setPlanetoidGuid] = useState ('88-a44d947a5');

  const [selected_system_guid, setSystemGuid] = useState ('168-2291ec185');
  const systemClicked = (childData) => {
    setSystemGuid(childData.guid);
    setPlanetoidGuid(data[childData.guid].planetoid_guids[0]);
    
    // let pguid = data[childData.guid].planetoid_guids[0];
    // console.log(pguid, pguid ? pguid : '168-2291ec185');
    // setPlanetoidGuid(pguid ? pguid : '168-2291ec185');
  }

  return (
      <SystemGuid.Provider value={{selected_system_guid, systemClicked}}>
        <PlanetoidGuid.Provider value={{selected_planetoid_guid, setPlanetoidGuid}}>
          <div className="App">
            <SolarList  />
            <div className='SolarDetailsContainer'>
              <SolarDetails />
              { data[selected_system_guid].planetoid_guids.length > 0 ?
                <div>
                  <Planetoids />                
                  <PlanetTemplate />
                </div>
                  : 'NO PLANETOIDS IN SYSTEM'
              }
            </div>
            <div>
              <ShipComponents />
            </div>
          </div>
        </PlanetoidGuid.Provider>
      </SystemGuid.Provider>
  );
}

export default App;
