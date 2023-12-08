import markers from './static_data/system_markers.json'

function MarkerIcons({guid}) {

    console.log('MarkerIcons return');
    if (markers[guid]) {
    return (
        <div>
            {markers[guid].map((m, i) => 
                <div key={i} style={{'float':'left'}}>
                    <img 
                        src={require(`./static_data/images/${m}-small.png`)} 
                        title={m}></img>
                </div>
            )}  
        </div>
    )}
    else {
        return ( <div></div> )
    }

}

export default MarkerIcons;