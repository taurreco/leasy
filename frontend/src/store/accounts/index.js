const accounts = {
  state() {
    return {
      endpointRegister: '',
      endpointLogin: '',
      endpointLogout: '',
    };
  },
  getters: {
    getEndpointRegister(state) {
      return state.endpointRegister;
    },
    getEndpointLogin(state) {
      return state.endpointLogin;
    },
    getEndpointLogout(state) {
      return state.endpointLogout;
    },
  }

};

export default accounts;