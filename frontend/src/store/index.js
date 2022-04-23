import { createStore } from 'vuex';
import accounts from './accounts';
import listings from './listings';

const store = createStore({
  modules: {
    accounts,
    listings,
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