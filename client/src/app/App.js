import React, { Component } from 'react';
import Frameworks from './frameworks/Frameworks.js'
import Nav from './nav/Nav.js'
import './App.css';

class App extends Component {
    constructor() {
        super();

        this.state = {frameworks:
		      [{
			  name:'Dockerfile',
			  details: null,
			  img: "https://cdn.worldvectorlogo.com/logos/docker.svg",
			  image: null
		      }]
		     };
        this.click = this.click.bind(this);
    }
    
    click(f) {
        //RETURN THE SELECTION TO SERVER 
        console.log(f)
    }
    
    render() {
        return (
              <div className="GPU-CLUSTER-FRONTEND">
                  <Nav/> 
                  <Frameworks frameworks={this.state.frameworks} handler={this.click}/>
              </div>
        );
    }
}

export default App;
