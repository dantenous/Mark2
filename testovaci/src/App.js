import React from "react";
import "./App.css";
//import Car from "./dalsi/Rpi";

function App() {
  return <MyComponent />;
}

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: []
    };
  }
  componentDidMount() {
    fetch("http://89.176.128.27:44444/api/serial/data/?format=json")
      .then(response => response.json())
      .then(data => this.setState({ isLoaded: true, items: data[0] }));
    /* componentDidMount() {
    fetch("https://hn.algolia.com/api/v1/search?query=redux")
      .then(res => res.json())
      .then(
        result => {
          console.log("errror");
          this.setState({
            isLoaded: true,
            items: result.items
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        error => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      );*/
  }

  render() {
    const { error, isLoaded } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
          <h2>Data z RPI</h2>
          <h4>
            <span class="badge badge-secondary">CAS: </span>
            {this.state.items.cas}
          </h4>
          <h4>
            <span class="badge badge-secondary">TEPLOTA: </span>
            {this.state.items.teplota} &#8451;
          </h4>
          <h4>
            <span class="badge badge-secondary">TLAK: </span>
            {this.state.items.tlak} hPa
          </h4>
          <h4>
            <span class="badge badge-secondary">VLHKOST: </span>
            {this.state.items.vlhkost} %
          </h4>
          <h4>
            <span class="badge badge-secondary">CO2: </span>
            {this.state.items.co2} ppm
          </h4>
        </div>
      );
    }
  }
}

export default App;
