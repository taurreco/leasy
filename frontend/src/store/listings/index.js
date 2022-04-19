import axios from 'axios';

const LISTINGS_ENDPOINTS_ENDPOINT = "/api/v1/listings/endpoints/";

const accounts = {
  namespaced: true,
  state() {
    return {
      endpointListings: "",
      listings: [],
    };
  },
  getters: {

    /**
     * @param {State} state
     * @returns {String}
     */
    getEndpointListings(state) {
      return state.endpointListings;
    },

    /**
     * @param {State} state 
     * @returns {Dict[]} 
     */
    getListings(state) {
      return state.listings;
    },
  },

  mutations: {
    /**
     * @param {State} state
     * @param {String} endpoint
     */
    setEndpointListings(state, endpoint) {
      state.endpointListings = endpoint;
    },

    /**
     * 
     * @param {State} state 
     * @param {Dict[]} listings 
     */
    setListings(state, listings) {
        state.listings = listings;
    }
  },
  actions: {
    async loadEndpoints({ commit }) {
      const endpoints = (await axios.get(LISTINGS_ENDPOINTS_ENDPOINT)).data;
      commit('setEndpointListings', endpoints["listings-list"]);
    },
    async loadListings({commit, getters}) {
      const listings = (await axios.get(getters.getEndpointListings)).data;
      commit('setListings', listings)
    }
  }
};

export default accounts;