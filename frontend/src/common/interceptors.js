import axios from 'axios';

export default function setup() {
  axios.interceptors.request.use(
    (config) => {
      // console.log(config);
      return config;
    },
    (error) => {
      // console.log("request error caught");
      // console.log(error);
      return Promise.reject(error);
    }
  );

  axios.interceptors.response.use(
    (response) => response
    , (error) => {
      // console.log("reponse error caught");
      // console.log(error);
      return Promise.reject(error);
    }
  );
}