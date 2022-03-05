<template>
  <section class="row align-items-center justify-content-center h-50">
    <div class="col-sm col-md-8 col-lg-6 col-xl-5">
      <div class="card">
        <div class="card-header text-center">
          Login
        </div>
        <div class="card-body">
          <h3 class="card-title text-secondary">Welcome to Leasy!</h3>
          <form @submit.prevent="validateLogin">
            <div class="m-3">
              <label for="email" class="visually-hidden">Email</label>
              <input type="text" class="form-control" id="email" placeholder="Email" 
                :class="{'border-danger': (v$.email.$error && v$.$error) || badCredentials}"
                v-model="v$.email.$model" @focus="badCredentials = false">
              <p v-if="v$.email.$error && v$.$error" class="text-danger">
                <small>You must enter a valid email address.</small>
              </p>
            </div>
            <div class="m-3">
              <label for="password" class="visually-hidden">Password</label>
              <input type="password" class="form-control" id="password" placeholder="Password" 
                :class="{'border-danger': (v$.password.$error && v$.$error) || badCredentials }"
                v-model="v$.password.$model" @focus="badCredentials = false">
              <p v-if="v$.password.$error && v$.error" class="text-danger">
                <small>You must enter a valid password.</small>
              </p>
            </div>
            <div class="m-3 mx-5 text-center">
              <button type="submit" class="btn btn-primary w-100">Log in</button>
              <p v-if="badCredentials" class="text-danger">
                <small>Email or password was incorrect.</small>
              </p>
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
import useVuelidate from "@vuelidate/core";
import {required, email, minLength } from "@vuelidate/validators";

export default {
  name: 'Login',
  setup() {
    return {
      v$: useVuelidate()
    }
  },
  data() {
    return {
      badCredentials: false,
      email: '',
      password: '',
    }
  },
  validationConfig() {
    return {
      $lazy: true,
    }
  },
  validations() {
    return {
      email: { required, email },
      password: { required, minLength: minLength(12) }
    }
  },
  methods: {
    async validateLogin() {
      const isValidForm = await this.v$.$validate();
    
      if (!isValidForm) {
        this.v$.email.$touch();
        this.v$.password.$touch();
        return;
      }

      const email = this.email;
      const password = this.password;
      const response = await this.login({email, password}).catch(() => {
        this.badCredentials = true;
      });

      if (response) {
        this.$router.push("/");
      }
    },
    ...mapActions("accounts", ["login"])
  }

}
</script>


<style scoped>
</style>

