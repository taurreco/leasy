import axios from 'axios';

const ACCOUNT_ENDPOINTS_ENDPOINT = "/api/v1/accounts/";

const accounts = {
  namespaced: true,
  state() {
    return {
      endpointAccountEmailVerificationSent: '',
      endpointLogin: '',
      endpointLogout: '',
      endpointPasswordChange: '',
      endpointPasswordReset: '',
      endpointPasswordResetConfirm: '',
      endpointRegister: '',
      endpointResendEmail: '',
    };
  },
  getters: {
    getEndpointAccountEmailVerificationSent(state) {
      return state.endpointAccountEmailVerificationSent;
    },
    getEndpointLogin(state) {
      return state.endpointLogin;
    },
    getEndpointLogout(state) {
      return state.endpointLogout;
    },
    getEndpointPasswordChange(state) {
      return state.endpointRegister;
    },
    getEndpointPasswordReset(state) {
      return state.endpointPasswordChange;
    },
    getEndpointPasswordResetConfirm(state) {
      return state.endpointPasswordReset;
    },
    getEndpointRegister(state) {
      return state.endpointRegister;
    },
    getEndpointResendEmail(state) {
      return state.endpointResendEmail;
    },
  },
  mutations: {
    setEndpointAccountEmailVerificationSent(state, endpoint) {
      state.endpointAccountEmailVerificationSent = endpoint;
    },
    setEndpointLogin(state, endpoint) {
      state.endpointLogin = endpoint;
    },
    setEndpointLogout(state, endpoint) {
      state.endpointLogout = endpoint;
    },
    setEndpointPasswordChange(state, endpoint) {
      state.endpointRegister = endpoint;
    },
    setEndpointPasswordReset(state, endpoint) {
      state.endpointPasswordChange = endpoint;
    },
    setEndpointPasswordResetConfirm(state, endpoint) {
      state.endpointPasswordReset = endpoint;
    },
    setEndpointRegister(state, endpoint) {
      state.endpointRegister = endpoint;
    },
    setEndpointResendEmail(state, endpoint) {
      state.endpointResendEmail = endpoint;
    },
  },
  actions: {
    async loadEndpoints({ commit }) {
      const endpoints = (await axios.get(ACCOUNT_ENDPOINTS_ENDPOINT)).data;
      commit('setEndpointAccountEmailVerificationSent', endpoints["account-email-verification-sent"]);
      commit('setEndpointLogin', endpoints["login"]);
      commit('setEndpointLogout', endpoints["logout"]);
      commit('setEndpointPasswordChange', endpoints["password-change"]);
      commit('setEndpointPasswordReset', endpoints["password-reset"]);
      commit('setEndpointPasswordResetConfirm', endpoints["password-reset-confirm"]);
      commit('setEndpointRegister', endpoints["register"]);
      commit('setEndpointResendEmail', endpoints["resend-email"]);
    },
    async login({ getters }, { email, password }) {
      const response = await axios.post(getters.getEndpointLogin, { email, password });
      return response.status;
    },
    async logout({ getters }) {
      const response = await axios.post(getters.getEndpointLogout);
      return response.status;
    },
    async changePassword({ getters }, { newPassword1, newPassword2 }) {
      const data = {
        "new_password1": newPassword1,
        "new_password2": newPassword2,
      };
      const response = await axios.post(getters.EndpointChangePassword, data);
      return response.status;
    },
    async resetPassword({ getters }, { email }) {
      const response = await axios.post(getters.getEndpointPasswordReset, { email });
      return response.status;
    },
    async resetPasswordConfirm({ getters }, { newPassword1, newPassword2, uid, token }) {
      data = {
        "new_password1": newPassword1,
        "new_password2": newPassword2,
        uid,
        token
      };
      const response = await axios.post(getters.getEndpointPasswordResetConfirm, data);
      return response.status;
    },
    async register({ getters }, { email, password1, password2 }) {
      const response = await axios.post(getters.getEndpointRegister, { email, password1, password2 });
      return response.status;
    },
    async resendEmail({ getters }, { email }) {
      const response = await axios.post(getters.getEndpointRegister, { email });
      return response.status;
    },
  }

};

export default accounts;