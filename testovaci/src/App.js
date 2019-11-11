import React from "react";
import "./App.css";
import Chart from "react-apexcharts";

//import Car from "./dalsi/Rpi";

function App() {
  return <MyComponent />;
}

class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      options: {
        chart: {
          id: "basic-bar"
        },
        xaxis: {
          type: "category",
          categories: ["se", "aa"],
          labels: {
            show: true,
            rotate: -45,
            rotateAlways: false,
            hideOverlappingLabels: true,
            showDuplicates: false,
            trim: true,
            minHeight: undefined,
            maxHeight: 120,
            style: {
              colors: [],
              fontSize: "12px",
              fontFamily: "Helvetica, Arial, sans-serif",
              cssClass: "apexcharts-xaxis-label"
            },
            offsetX: 0,
            offsetY: 0,
            format: undefined,
            formatter: undefined,
            datetimeFormatter: {
              year: "yyyy",
              month: "MMM 'yy",
              day: "dd MMM",
              hour: "HH:mm"
            }
          }
        }
      },
      series: [
        {
          name: "series-1",
          data: []
        }
      ],
      error: null,
      isLoaded: false,
      items: []
    };
  }

  componentDidMount() {
    this.getData();

    setInterval(this.getData, 1000);
  }

  getData = () => {
    const newSeries = [];
    const next = [];
    fetch("http://89.176.128.27:44444/api/serial/data/?format=json")
      .then(response => response.json())
      .then(prijem =>
        this.setState({
          isLoaded: true,
          items: prijem
        })
      );
    //.then(dane => newSeries.push({ data: dane.map(item => item.cas) }));
    next.push({
      categories: this.state.items.map(itema => itema.teplota)
    });

    newSeries.push({
      data: this.state.items.map(item => item.teplota)
    });
    this.setState({
      xaxis: next,
      //options: this.props.state.options.xaxis,
      series: newSeries
    });

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
  };

  render() {
    const { error, isLoaded } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
          <div className="float-left">
            <h2>Data z RPI</h2>
            <h4>
              <span className="badge badge-secondary">CAS: </span>
              {this.state.items[0].cas}
            </h4>
            <h4>
              <span className="badge badge-secondary">TEPLOTA: </span>
              {this.state.items[0].teplota} &#8451;
            </h4>
            <h4>
              <span className="badge badge-secondary">TLAK: </span>
              {this.state.items[0].tlak} hPa
            </h4>
            <h4>
              <span className="badge badge-secondary">VLHKOST: </span>
              {this.state.items[0].vlhkost} %
            </h4>
            <h4>
              <span className="badge badge-secondary">CO2: </span>
              {this.state.items[0].co2} ppm
            </h4>
            <h2>Data z Meteo</h2>
            <h4>
              <span className="badge badge-secondary">TEPLOTA-VENKOVNI: </span>
              {this.state.items[0].teplotav} &#8451;
            </h4>
            <h4>
              <span className="badge badge-secondary">TEPLOTA-ZDANLIVA: </span>
              {this.state.items[0].teplotazdanliva} &#8451;
            </h4>
            <h4>
              <span className="badge badge-secondary">ROSNY-BOD: </span>
              {this.state.items[0].rosnybod} &#8451;
            </h4>
            <h4>
              <span className="badge badge-secondary">VLHKOST-VENKOVNI: </span>
              {this.state.items[0].vlhostv} %
            </h4>
            <h4>
              <span className="badge badge-secondary">SRAZKY: </span>
              {this.state.items[0].densrazky} mm
            </h4>
            <h4>
              <span className="badge badge-secondary">TLAK-VENKOVNI: </span>
              {this.state.items[0].tlakv} hPa
            </h4>
            <h4>
              <span className="badge badge-secondary">SMER-VETRU: </span>
              {this.state.items[0].smervetru}
            </h4>
            <h4>
              <span className="badge badge-secondary">RYCHLOST-VETRU: </span>
              {this.state.items[0].rychlostvetru} m/s
            </h4>
            <h4>
              <span className="badge badge-secondary">NARAZOVY-VITR </span>
              {this.state.items[0].narazovyvitr} m/s
            </h4>
          </div>

          <div className="float-left">
            <div className="app">
              <div className="row">
                <div className="mixed-chart">
                  <Chart
                    options={this.state.options}
                    series={this.state.series}
                    type="line"
                    width="500"
                  />
                </div>
              </div>
            </div>
          </div>
          <div className="float-left">
            <div className="app">
              <div className="row">
                <div className="mixed-chart">
                  <Chart
                    options={this.state.options}
                    series={this.state.series}
                    type="line"
                    width="500"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      );
    }
  }
}

export default App;
