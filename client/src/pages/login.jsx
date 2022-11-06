import { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import Button from '../components/button';
import Input from '../components/input';
import { fetchClient } from '../fetch';
import LoginLayout from '../layouts/login';
import { useAuth } from '../userContext';

// const { Title } = Typography;

function Login() {
  const { doLogin } = useAuth();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const navigator = useNavigate();
  const location = useLocation();

  let from = location.state?.from?.pathname || '/';

  function handleLogin(e) {
    setLoading(true);
    e.preventDefault();
    const userCreds = {
      email: e.target.email.value,
      password: e.target.password.value,
    };
    console.log(userCreds);
    // fetchClient('auth/login', { method: 'POST', body: userCreds })
    //   .then((res) => {
    //     localStorage.setItem('token', res.accessToken);
    //     message.success('Les informations de connexion sont correctes');
    //     doLogin();
    //     navigator(from, { replace: true });
    //   })
    //   .catch((err) => {
    //     setError(err.message);
    //     message.error(err.message);
    //     console.log(err.message);
    //   })
    //   .finally(() => setLoading(false));
  }

  return (
    <LoginLayout>
      <div className="flex flex-col gap-2 mb-4">
        <h1 className="text-2xl font-semibold mb-4">Login</h1>
        <p>Login with your data that you entered during your registration</p>
        <p>
          Don't have an account?{' '}
          <Link to="/register" className="text-secondary underline">
            register
          </Link>
        </p>
      </div>
      <form onSubmit={handleLogin} className="flex flex-col gap-4">
        <div>
          <label htmlFor="email" className="block">
            Email
          </label>
          <Input
            placeholder="Email adress"
            size="large"
            name="email"
            id="email"
            className="w-full"
          />
        </div>
        <div>
          <label htmlFor=""></label>
          <Input
            placeholder="Password"
            size="large"
            type="password"
            name="password"
          />
        </div>
        <div className="flex justify-between">
          <div>
            <Input type="checkbox" id="keepLogin" name="keepLogin" />
            <label htmlFor="keepLogin" className="ml-2">
              Keep logged in?
            </label>
          </div>
          <Link className="text-secondary">Forgot password?</Link>
        </div>
        <Button htmlType="submit" shape="rounded">
          Login
        </Button>
      </form>
    </LoginLayout>
  );
}

export default Login;
