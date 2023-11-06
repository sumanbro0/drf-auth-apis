import { cookies } from 'next/headers'
import Products from '../components/products';

const Home = async () => {
  const cookie = cookies()

  const session = cookie.get("sessionid")
  if (session != null) {
    const response = await fetch('http://127.0.0.1:8000/api/profile', {
      method: 'GET',
      credentials: 'include',
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json",
        'Cookie': `sessionid=${session.value}`,
      }
    })
    const data = await response.json()
    console.log(data)
  }

  return (
    <div>
      <h1 className="text-white text-center font-extrabold text-9xl">Hello,World</h1>
      <Products />
    </div>
  );
};

export default Home;
