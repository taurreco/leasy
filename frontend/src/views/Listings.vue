<template>
  <h1>Listings</h1>
  <div v-for="listing in getListings" :key="listing.id" class="border">
    <h2>{{listing.name}}</h2>
    <p>{{listing.lister_first_name}}</p>
    <p>{{listing.address}}</p>
    <p>{{listing.description}}</p>
    <p>${{listing.rent}}/month</p>
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

