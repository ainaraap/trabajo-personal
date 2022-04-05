<template>
  <div class="home">
    <img src="@/assets/img/MUÑECAS.png" />
    <router-link to="/dollsCatalog"> <button>CATALOGO</button></router-link>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      catalog: {}
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      const response = await fetch('http://localhost:5000/api/dolls')
      this.catalog = await response.json()
    }
  }


}
</script>

<style scoped>
h1 {
  font-style: italic;
}
</style>
