<template>
  <h1>Listings</h1>
  <div v-for="listing in getListings">
    {{listing.name}}
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex';

export default {
  name: 'Listings',
  async mounted() {
    await this.loadEndpoints();
    await this.loadListings();
  },
  computed: {
    ...mapGetters("listings", ["getListings"])
  },
  methods: {
    ...mapActions("listings", ["loadEndpoints", "loadListings"])
  }
}
</script>


<style scoped>
</style>

