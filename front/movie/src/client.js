import axios from 'axios'
if (process.env.NODE_ENV === 'development') {
  // import mockserver from 'axios-mock-server'
}

const client = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  responseType: 'json'
});

export default client
