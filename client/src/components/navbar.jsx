import { Link } from 'react-router-dom';
import Accordion from './accordion';
import Status from './status';
function Navbar() {
  return (
    <nav className="flex justify-between align-middle px-8 bg-white">
      <h1 className="flex items-center">
        <Link to="/" className="text-xl font-medium">
          InnovFI Platform
        </Link>
      </h1>
      <div>
        <Accordion
          title={
            <Status
              fullName="Aymen Bergadi"
              title="Creative inventor"
              isActive
              avatarUrl="https://picsum.photos/48"
            />
          }
          options={['Preferences', 'Log out']}
        ></Accordion>
      </div>
    </nav>
  );
}

export default Navbar;
