import { createStore } from 'vuex';
import accounts from './accounts';

const store = createStore({
  modules: {
    accounts,
  },
  state() {
    return {
      apiRoot: "api/v1/"
    };
  },
  getters: {
    getApiRoot(state) {
      return state.apiRoot;
    }
  }
});

export default store;