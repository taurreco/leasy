import axios from 'axios';

const ACCOUNT_ENDPOINTS_ENDPOINT = "/api/v1/accounts/endpoints/";

const accounts = {
  namespaced: true,
  state() {
    return {
      currentUser: null, // firstName, lastName, email
      endpointAccountEmailVerificationSent: '',
      endpointCurrentUser: '',
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
    getCurrentUser(state) {
      return state.currentUser;
    },
    getEndpointCurrentUserDetail(state) {
      return state.endpointCurrentUserDetail;
    },
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
    setCurrentUser(state, user) {
      state.currentUser = user;
    },
    setEndpointAccountEmailVerificationSent(state, endpoint) {
      state.endpointAccountEmailVerificationSent = endpoint;
    },
    setEndpointCurrentUserDetail(state, endpoint) {
      state.endpointCurrentUserDetail = endpoint;
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
    async loadCurrentUser({ commit, getters, dispatch }) {
      if (!getters.getEndpointCurrentUserDetail) {
        await dispatch('loadEndpoints');

        if (!getters.getEndpointCurrentUserDetail) {
          commit('setCurrentUser', null);
        }

      }

      const userData = (await axios.get(getters.getEndpointCurrentUserDetail)).data;

      commit('setCurrentUser', {
        "firstName": userData["first_name"],
        "lastName": userData["last_name"],
        "email": userData["email"]
      });
    },
    async loadEndpoints({ commit, dispatch }) {
      const endpoints = (await axios.get(ACCOUNT_ENDPOINTS_ENDPOINT)).data;
      commit('setEndpointAccountEmailVerificationSent', endpoints["account-email-verification-sent"]);
      commit('setEndpointLogin', endpoints["login"]);
      commit('setEndpointLogout', endpoints["logout"]);
      commit('setEndpointPasswordChange', endpoints["password-change"]);
      commit('setEndpointPasswordReset', endpoints["password-reset"]);
      commit('setEndpointPasswordResetConfirm', endpoints["password-reset-confirm"]);
      commit('setEndpointRegister', endpoints["register"]);
      commit('setEndpointResendEmail', endpoints["resend-email"]);

      if (endpoints["current-user-detail"]) {
        commit('setEndpointCurrentUserDetail', endpoints["current-user-detail"]);
        await dispatch('loadCurrentUser');
      }
    },
    async login({ getters, dispatch }, { email, password }) {
      const response = await axios.post(getters.getEndpointLogin, { email, password });

      if (response.data && response.data.key) {
        await dispatch("loadEndpoints");
        await dispatch("loadCurrentUser");
      }

      return response;
    },
    async logout({ getters }) {
      const response = await axios.post(getters.getEndpointLogout);
      return response;
    },
    async changePassword({ getters }, { newPassword1, newPassword2 }) {
      const data = {
        "new_password1": newPassword1,
        "new_password2": newPassword2,
      };
      const response = await axios.post(getters.EndpointChangePassword, data);
      return response;
    },
    async resetPassword({ getters }, { email }) {
      const response = await axios.post(getters.getEndpointPasswordReset, { email });
      return response;
    },
    async resetPasswordConfirm({ getters }, { newPassword1, newPassword2, uid, token }) {
      const data = {
        "new_password1": newPassword1,
        "new_password2": newPassword2,
        uid,
        token
      };
      const response = await axios.post(getters.getEndpointPasswordResetConfirm, data);
      return response;
    },
    async register({ getters }, { email, password1, password2 }) {
      const response = await axios.post(getters.getEndpointRegister, { email, password1, password2 });
      return response;
    },
    async resendEmail({ getters }, { email }) {
      const response = await axios.post(getters.getEndpointRegister, { email });
      return response;
    },
  }

};

export default accounts;