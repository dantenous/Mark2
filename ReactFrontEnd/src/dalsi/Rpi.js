import React from "react";
import ReactDOM from "react-dom";

class Car extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      brand: "Ford",
      items: []
    };
  }

  render() {
    return (
      <div>
        <h2>Data z RPI</h2>
        <h4>
          <span class="badge badge-secondary">CAS: </span>
        </h4>
        <h4>
          <span class="badge badge-secondary">TEPLOTA: </span>
          &#8451;
        </h4>
        <h4>
          <span class="badge badge-secondary">TLAK: </span>
          hPa
        </h4>
        <h4>
          <span class="badge badge-secondary">VLHKOST: </span>%
        </h4>
        <h4>
          <span class="badge badge-secondary">CO2: </span>
          ppm
        </h4>
      </div>
    );
  }
}

ReactDOM.render(<Car />, document.getElementById("muj"));
