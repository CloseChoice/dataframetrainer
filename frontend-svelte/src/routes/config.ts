export const API_BASE_URL = process.env.NODE_ENV === 'production'
  ? 'http://www.dataframetrainer.com:5000'
  : 'http://localhost:5000';