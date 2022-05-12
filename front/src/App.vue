<template>
  <div id="nav">
    <router-link to="/">Pagina principal</router-link>|
    <router-link to="/dollsCatalog">Catálogo</router-link>
  </div>
  <router-view />
</template>

<style scoped>
#nav {
  
  text-align: center;
  padding: 10px 50px 25px 10px;
  
}
</style>