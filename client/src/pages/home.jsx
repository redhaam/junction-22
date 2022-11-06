import Button from '../components/button';
import wave from '../../public/wave.svg';
import illustration from '../../public/Illustration.svg';
import logo from '../../public/logo.svg';
import { Link } from 'react-router-dom';
function Home() {
  return (
    <div className="min-h-screen flex flex-col justify-between items-stretch">
      <div
        className="flex flex-row justify-between items-center py-5 px-40	"
        id="navbar"
      >
        <div
          className=" gap-x-20 flex flex-row justify-start items-center"
          id="navigation"
        >
          <Link className="cursor-pointer text-left text-lg ">
            <img src={logo} alt="" />
          </Link>
          <Link className="cursor-pointer text-left text-lg text-gray-400 hover:text-black">
            Our mission
          </Link>
          <Link className="cursor-pointer text-left text-lg text-gray-400 hover:text-black">
            About Us
          </Link>
          <Link className="cursor-pointer text-left text-lg text-gray-400 hover:text-black">
            Contact
          </Link>
        </div>
        <div
          className="w-1/5 flex flex-row justify-end items-center gap-x-10"
          id="login-signup"
        >
          <Link
            to="/register"
            className="cursor-pointer hover:text-black text-gray-400 decoration-stone-400"
          >
            Sign Up
          </Link>
          <Link to="/login" className=" w-2/4 ">
            {' '}
            <Button className="w-full" prefix="" suffix="" shape="rounded">
              Log In
            </Button>
          </Link>
        </div>
      </div>

      <div className="flex flex-row justify-between items-center mx-0 px-40 py-30 pb-0">
        <div id="home-page-detail" className="w-2/5">
          <h1 id="home-title" className="text-7xl text-left my-5">
            Let’s <span className="text-sky-500 font-bold">Build</span> Great
            Experiences
          </h1>
          <p id="home-content" className="text-xl my-5 w-5/6 text-gray-700">
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ex,
            consequatur. Cumque illo quidem, suscipit minus ipsa pariatur!
            Natus, laborum laudantium quam alias quibusdam doloribus! Quas ex at
            ea aut voluptatum.
          </p>
          <Link to="/start">
            <Button className="w-1/3 my-5" prefix="" suffix="" shape="rounded">
              Get Started
            </Button>
          </Link>
        </div>
        <div className="w-2/4">
          <img src={illustration} alt="" />
        </div>
      </div>
      <footer>
        <img className="" src={wave} alt="" />
      </footer>
    </div>
  );
}

export default Home;
