<template>
  <h1>Password Reset Confirm</h1>
  <div>{{$route.params.userId}}</div>
  <div>{{$route.params.token}}</div>
</template>

<script>
export default {
  name: 'PasswordResetConfirm',
}
</script>


<style scoped>
</style>

