import { API_URL } from './config';

function fetchClient(
  url,
  { headers, body, ...otherOptions } = { body: undefined, headers: {} }
) {
  const token = localStorage.getItem('token');
  const bodyStr = body ? JSON.stringify(body) : undefined;

  const fetchOptions = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      Accept: 'application/json',
      Authorization: token ? `Bearer ${token}` : undefined,
      ...headers,
    },
    ...otherOptions,
    body: bodyStr,
  };
  return fetch(`${API_URL}/${url}`, fetchOptions).then(async (res) => {
    const requestSucess = res.ok;
    const body = await res.json();
    if (requestSucess) return body;
    else throw new Error(body.detail);
  });
}

export { fetchClient };
