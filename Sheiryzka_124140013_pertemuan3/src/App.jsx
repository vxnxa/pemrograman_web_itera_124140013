import { NavLink, Route, Routes } from 'react-router-dom';
import Home from './pages/Home/Home';
import Stats from './pages/Stats/Stats';

function App() {
  return (
    <div className="container">
      <header className="header">
        <h1>Jejak Halaman</h1>
        <nav>
          <NavLink to="/" end>Beranda</NavLink>
          <NavLink to="/stats">Statistik</NavLink>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/stats" element={<Stats />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;