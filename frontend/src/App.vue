<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Leasy</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#leasy-nav" aria-controls="leasy-nav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="leasy-nav">
          <ul class="navbar-nav mb-2 mb-lg-0 ms-auto">
            <li class="nav-item">
              <router-link to="/" custom v-slot="{ href, isActive }">
                <a :href="href" class="nav-link" :class="{'active': isActive}">Home</a>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/listings" custom v-slot="{ href, isActive }">
                <a :href="href" class="nav-link" :class="{'active': isActive}">Listings</a>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/contact" custom v-slot="{ href, isActive }">
                <a :href="href" class="nav-link" :class="{'active': isActive}">Contact</a>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/login" custom v-slot="{ href, isActive }">
                <a :href="href" class="nav-link" :class="{'active': isActive}"><span class="rounded bg-primary text-light p-2">Log in</span></a>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view></router-view>
    <footer class="bg-dark container-fluid text-light position-absolute bottom-0">
      <p class="text-center m-0 p-2">&copy; Leasy. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
</style>
