<template>
  <section class="row align-items-center justify-content-center h-50">
    <div class="col-sm col-md-8 col-lg-6 col-xl-5">
      <div class="card">
        <div class="card-header text-center">
          Register
        </div>
        <div class="card-body">
          <h3 class="card-title text-secondary">Welcome to Leasy!</h3>
          <form @submit.prevent="validateRegister">
            <div class="row m-3">
              <div class="col m-0 pe-1 p-0">
                <label for="first-name" class="visually-hidden">First Name</label>
                <input type="text" class="form-control" id="first-name" placeholder="First Name" 
                  :class="{'border-danger': v$.firstName.$error && v$.$error}"
                  v-model="v$.firstName.$model">
                <p v-if="v$.firstName.$error && v$.$error" class="text-danger">
                  <small>Please enter a valid email address.</small>
                </p>
              </div>
              <div class="col m-0 ps-1 p-0">
                <label for="last-name" class="visually-hidden">Last Name</label>
                <input type="text" class="form-control" id="last-name" placeholder="Last Name" 
                  :class="{'border-danger': v$.lastName.$error && v$.$error}"
                  v-model="v$.lastName.$model">
                <p v-if="v$.lastName.$error && v$.$error" class="text-danger">
                  <small>Please enter a valid email address.</small>
                </p>
              </div>
            </div>
            <div class="m-3">
              <label for="email" class="visually-hidden">Email</label>
              <input type="text" class="form-control" id="email" placeholder="Email" 
                :class="{'border-danger': v$.email.$error && v$.$error}"
                v-model="v$.email.$model">
              <p v-if="v$.email.$error && v$.$error" class="text-danger">
                <small>Please enter a valid email address.</small>
              </p>
            </div>
            <div class="m-3">
              <label for="password1" class="visually-hidden">Password</label>
              <input type="password" class="form-control" id="password1" placeholder="Password" 
                :class="{'border-danger': (v$.password1.$error && v$.$error) }"
                v-model="v$.password1.$model">
              <p v-if="v$.password1.$error && v$.error" class="text-danger">
                <small>Passwords must be greater than {{v$.password.minLength}}</small>
              </p>
            </div>
            <div class="m-3">
              <label for="password2" class="visually-hidden">Confirm Password</label>
              <input type="password" class="form-control" id="password2" placeholder="Confirm Password" 
                :class="{'border-danger': (v$.password2.$error && v$.$error) }"
                v-model="v$.password2.$model">
              <p v-if="v$.password2.$error && v$.error" class="text-danger">
                <small>Passwords must be greater than {{v$.password.minLength}}</small>
              </p>
            </div>
            <div class="m-3 mx-5 text-center">
              <button type="submit" class="btn btn-primary w-100">Register</button>
            </div>
            <p class="text-center">Already have an account? 
              <router-link to="/login">Log in!</router-link>
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
import {required, email, minLength, sameAs } from "@vuelidate/validators";

export default {
  name: 'Login',
  setup() {
    return {
      v$: useVuelidate()
    }
  },
  data() {
    return {
      firstName: '',
      lastName: '',
      email: '',
      password1: '',
      password2: '',
    }
  },
  validationConfig() {
    return {
      $lazy: true,
    }
  },
  validations() {
    return {
      firstName: { required },
      lastName: { required },
      email: { required, email },
      password1: { required, minLength: minLength(12) },
      password2: { sameAs: sameAs(this.password1) }
    }
  },
  methods: {
    async validateRegister() {
      const isValidForm = await this.v$.$validate();
    
      if (!isValidForm) {
        this.v$.email.$touch();
        this.v$.password1.$touch();
        return;
      }

      const email = this.email;
      const password = this.password;
      const response = await this.register({email, password}).catch(() => {
        this.badCredentials = true;
      });

      if (response) {
        this.$router.push("/");
      }
    },
    ...mapActions("accounts", ["register"])
  }

}
</script>


<style scoped>
</style>

