import { Link } from 'react-router-dom';
import Button from '../components/button';
import Input from '../components/input';
import ApplicationLayout from '../layouts/application';

function Submit() {
  return (
    <ApplicationLayout>
      <form className="flex flex-col gap-6 p-8 relative">
        <h2 id="submit" className="text-3xl font-medium">
          Personal information
        </h2>

        <div className="flex gap-6">
          <div className="w-8/12">
            <div>
              <label htmlFor="firstName" className="w-full mb-1">
                Last name
              </label>
              <Input id="lastName" className="w-full" name="lastName" />
            </div>{' '}
            <div>
              <label htmlFor="firstName" className="w-full mb-1">
                First name
              </label>
              <Input id="lastName" className="w-full" name="lastName" />
            </div>
          </div>
          <div className="w-4/12 bg-white">
            <input type="file" name="profilePicture" id="profilePicture" />
          </div>
        </div>
        <div>
          <div>
            <label htmlFor="email" className="w-full mb-1">
              Email
            </label>
          </div>
          <Input type="email" name="email" className="w-full" />
        </div>
        <div>
          <label htmlFor="phone" className="w-full mb-1">
            Phone number
          </label>
          <Input type="tel" name="phone" className="w-full" />
        </div>

        <div className="flex gap-4">
          <div className="w-6/12">
            <label htmlFor="city" className="w-full mb-1">
              City
            </label>
            <Input type="text" name="city" className="w-full" />
          </div>
          <div className="w-6/12">
            <label htmlFor="country" className="w-full mb-1">
              Country
            </label>
            <Input type="tel" name="country" className="w-full" />
          </div>
        </div>
      </form>
    </ApplicationLayout>
  );
}

export default Submit;
