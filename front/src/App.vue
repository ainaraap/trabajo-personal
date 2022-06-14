<template>
  <div id="nav">
    <router-link to="/">Pagina principal</router-link> |
    <router-link to="/dollsCatalog">Catálogo</router-link>
  </div>
  <div id="admin">
    <router-link to="/admin">Admin</router-link>
  </div>
  <router-view />
</template>

