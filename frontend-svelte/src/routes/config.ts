export const API_BASE_URL = process.env.NODE_ENV === 'production'
  // we use nginx as reverse proxy, so it redirects all requests to http://www.dataframetrainer.com:5000 to localhost:4999
  ? 'https://www.dataframetrainer.com:5000'
  : 'http://localhost:4999';
