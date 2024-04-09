import logo from "./logo.svg";
import "./App.css";
import BarChart from "./modelA";

function App() {
  const dummyData = [
    { category: "A", value: 10 },
    { category: "B", value: 25 },
    { category: "C", value: 15 },
  ];

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <BarChart
          data={dummyData}
          width={600}
          height={400}
          colors={["steelblue", "tomato", "lightgreen"]}
          margin={{ top: 20, right: 20, bottom: 30, left: 40 }}
        />
      </header>
    </div>
  );
}

export default App;
