import logo from './logo.svg';
import './App.css';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/home';
import Login from './pages/login';
import Register from './pages/register';
import { UserProvider } from './userContext';
import Button from './components/button';
import Input from './components/input';
import Start from './pages/start';
import Submit from './pages/submit';

function App() {
  return (
    <div className="App">
      <UserProvider>
        <Routes>
          <Route path="" element={<Home />} index />
          <Route path="login" element={<Login />} />
          <Route path="register" element={<Register />} />
          <Route path="start" element={<Start />} />
          <Route path="submit" element={<Submit />} />
        </Routes>
      </UserProvider>
    </div>
  );
}

export default App;
