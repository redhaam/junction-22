import { Link } from 'react-router-dom';
import Button from '../components/button';
import Card from '../components/card';
import Navbar from '../components/navbar';
import FileUpload from '../icons/fileUpload';

function Start() {
  return (
    <div className="bg-gray-200 h-screen overflow-y-auto pb-8 ">
      <Navbar />
      <h1 className="text-4xl font-semibold mt-6 mb-12 text-center">
        <span className="text-blue-700"> Start</span> your journey
      </h1>
      <section className="container grid grid-cols-5 gap-4 mb-12">
        <Card
          title="Title 1"
          icon={<FileUpload size="large" />}
          description="lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum"
          footer="learn more"
        ></Card>{' '}
        <Card
          title="Title 1"
          icon={<FileUpload size="large" />}
          description="lorem ipsum lorem ipsum lorem ipsum lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum lorem ipsum lorem ipsum lorem ipsum"
          footer="learn more"
        ></Card>{' '}
        <Card
          title="Title 1"
          icon={<FileUpload size="large" />}
          description="lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum"
          footer="learn more"
        ></Card>{' '}
        <Card
          title="Title 1"
          icon={<FileUpload size="large" />}
          description="lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum"
          footer="learn more"
        ></Card>{' '}
        <Card
          title="Title 1"
          icon={<FileUpload size="large" />}
          description="lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum"
          footer="learn more"
        ></Card>
      </section>
      <div className="flex justify-center">
        <Link to="/login">
          <Button shape="rounded" className="w-64">
            Get started{' '}
          </Button>
        </Link>
      </div>
    </div>
  );
}

export default Start;
