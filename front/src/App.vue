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


<script>
import { useStorage } from "@vueuse/core";

export default {
  data() {
    return {
      localUser: useStorage("user", {}),
    };
  },
  computed: {
    loggedUser() {
      return this.localUser.name;
    },
  },
};
</script>
