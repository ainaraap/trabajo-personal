<template>
  <img src="@/assets/img/MUÑECAS.png" />
  <div class="dollCatalog">
    <article v-for="doll in catalog" :key="doll.id">
      <section>
        <p>{{ doll.doll_id }}</p>
        <p>{{ doll.photo }}</p>
        <p>{{ doll.price }}</p>
        <p>{{ doll.size }}</p>
      </section>
    </article>
  </div>
</template>

<script>
export default {
  name: "Dolls",
  data() {
    return {
      catalog: [],
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch("http://localhost:5000/api/dolls");
      this.catalog = await response.json();
    },
  },
};
</script>

<style scoped>

img {
  margin: 1px;
}
section {
  border: 2px solid black;
  margin: 1em 10em;
  padding: 1em;
}
</style>