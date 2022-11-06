import { fetchClient } from '../fetch';
import { useAuth } from '../userContext';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import Button from '../components/button';
import Input from '../components/input';
import logo from '../../public/logo.svg'
// const { Title } = Typography;
function Register() {
  const [loading, setLoading] = useState(false);
  const { doLogin } = useAuth();

  function handleRegister(e) {
    e.preventDefault();
    const passwordConfirm = e.target.passwordConfirm.value;
    const userInfo = {
      firstName: e.target.firstName.value,
      lastName: e.target.lastName.value,
      email: e.target.email.value,
      password: e.target.password.value,
    };
    if (userInfo.password < 8) {
      alert('Le mot de passe doit contenir au moins 8 charactères');
      return;
    }
    if (passwordConfirm != userInfo.password) {
      alert('veuillez confirmer votre mot de passe');
      return;
    }

    setLoading(true);
    fetchClient('auth/register', { method: 'POST', body: userInfo })
      .then((res) => {
        localStorage.setItem('token', res.accessToken);
        alert('Compte créé avec succés');
        doLogin();
      })
      .catch((err) => message.error(err.message))
      .finally(() => setLoading(false));
  }

  return (
  <div >
    <div id="aside">
      <img src="" alt="" /> 
    </div>
    
    <form action="" className='flex flex-col justify-center gap-10 items-stretch w-1/3 m-auto'>
      
      <div className='flex flex-row justify-start gap-5 items-center'>
        <img src={logo} alt="" />
        <h2 className='text-2xl font-thin '>Platform</h2>
      </div>
      
      <h1 className='font-bold text-5xl tracking-tight text-center'>Register</h1>
      
      <div className='flex flex-row justify-between '>
        <div className='flex flex-col-reverse justify-start gap-2 '>
          <Input id="first-name" type="text" placeholder="first name goes here "></Input>
          <label htmlFor="first-name" >First Name</label>
        </div>
        
        <div className='flex flex-col-reverse justify-start gap-2 '>
          <Input id="last-name" type="text" placeholder="last name goes here "></Input>
          <label htmlFor="last-name">Last Name</label>
        </div>
      </div>
      
      <div className='flex flex-col-reverse justify-start gap-2 '>
        <Input id="email" type="email" placeholder="email goes here: example@example.com "></Input>
        <label htmlFor="email">Email</label>
      </div>
      
      <div className='flex flex-col-reverse justify-start gap-2 '>
        <Input id="phone" type="tel" placeholder="phone number goes here: 749929682 "></Input>
        <label htmlFor="phone"> Phone Number</label>
      </div>
     

      <div className='flex flex-row justify-between'>
        <div className='flex flex-col-reverse justify-start gap-2 '>
          <Input id="password" type="password" placeholder="password goes here "></Input>
          <label htmlFor="password">Password</label>
        </div>
        
        <div className='flex flex-col-reverse justify-start gap-2 '>
          <Input id="confirm-password" type="password" placeholder="confirme your password"></Input>
          <label htmlFor="confirm-password">Confirme Password</label>
        </div>
      </div>

      <Button htmlType='submit'>Sign up</Button>
    </form>
    
  </div>
  );
}

export default Register;
