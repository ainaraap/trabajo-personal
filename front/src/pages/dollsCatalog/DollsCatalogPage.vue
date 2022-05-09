<template>
  <img src="@/assets/img/MUÑECAS.png" />
  <div class="dollCatalog">
    <article v-for="doll in catalog" :key="doll.id">
      <section>
        <p>{{ doll.img }}</p>
        <p>{{ doll.doll_id }}</p>
        <p>{{ doll.price }}</p>
        <p>{{ doll.size }}</p>

        <button class="boton-detalle">VER DETALLE MUÑECA</button>
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
  padding: 10px;
}
.boton-detalle {
  background-color: #9781c9;
  padding: 10px;
  border-radius: 10%;
  border-color: #381a3f;
  margin: 10px;
}

</style>