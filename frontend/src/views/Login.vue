<template>
  <section class="row align-items-center justify-content-center h-50">
    <div class="col-sm col-md-8 col-lg-6 col-xl-5">
      <div class="card">
        <div class="card-header text-center">
          Login
        </div>
        <div class="card-body">
          <h3 class="card-title text-secondary">Welcome to Leasy!</h3>
          <form @submit.prevent="loginUser">
            <div class="m-3">
              <label for="email" class="visually-hidden">Email</label>
              <input type="text" class="form-control" id="email" placeholder="Email" v-model="email">
            </div>
            <div class="m-3">
              <label for="password" class="visually-hidden">Password</label>
              <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
            </div>
            <div class="m-3 mx-5 text-center">
              <button type="submit" class="btn btn-primary w-100">Log in</button>
            </div>
            <p class="text-center">Don't have an account? 
              <router-link to="/register">Sign up!</router-link>
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>

</template>

<script>
import { mapActions } from "vuex";

export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    async loginUser() {
      console.log("log in user");
      const email = this.email;
      const password = this.password;
      await this.login({email, password});
      this.$router.push("/");
    },
    ...mapActions("accounts", ["login"])
  }

}
</script>


<style scoped>
</style>

