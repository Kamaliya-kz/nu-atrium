import { useEffect, useState } from "react";

interface Reading {
  id: number;
  place: string;
  temperature: number;
  brightness: string | null;
  noise: string | null;
  measured_at: string;
}

function App() {

  const sortByDate = () => {
  const sorted = [...readings].sort(
    (a, b) =>
      new Date(a.measured_at).getTime() -
      new Date(b.measured_at).getTime()
  );

  setReadings(sorted);
};
   const sortByTempAsc = () => {
  const sorted = [...readings].sort(
    (a, b) => a.temperature - b.temperature
  );

  setReadings(sorted);
};

  const sortByTempDesc = () => {
  const sorted = [...readings].sort(
    (a, b) => b.temperature - a.temperature
  );

  setReadings(sorted);
};

  const bestStudy = () => {

    console.log("Show best study conditions");

  };

  const bestActivity = () => {

    console.log("Show best activity conditions");

  };
  
  const [readings, setReadings] = useState<Reading[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/readings")
      .then((res) => res.json())
      .then((data) => setReadings(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h1>NU Atrium Monitor</h1>
      <div className="buttons">
  <button onClick={sortByDate}>📅 Date</button>
  <button onClick={sortByTempAsc}>🌡 Temp ↑</button>
  <button onClick={sortByTempDesc}>🌡 Temp ↓</button>
  <button onClick={bestStudy}>🎓 Study</button>
  <button onClick={bestActivity}>🏃 Activity</button>
</div>
      {readings.map((reading) => (
        <div key={reading.id}>
          <h3>{reading.place}</h3>
          <p>🌡 {reading.temperature}°C</p>
          <p>💡 {reading.brightness ?? "-"}</p>
          <p>🔉 {reading.noise ?? "-"}</p>
          <p>{reading.measured_at}</p>
        </div>
      ))}
    </div>
  
  )
}

export default App;