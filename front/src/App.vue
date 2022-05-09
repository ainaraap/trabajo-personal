<template>
  <div id="nav">
    <router-link to="/">Home</router-link>|
    <router-link to="/dollsCatalog">Dolls</router-link>
  </div>
  <router-view />
</template>

<style scoped>
#nav {
  margin: -10px;
  text-align: end;
  
}
</style>