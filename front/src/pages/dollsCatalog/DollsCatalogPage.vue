<template>
  <img src="@/assets/img/MUÑECAS.png" />
  <div class="dollCatalog">
    <article v-for="doll in catalog" :key="doll.id">
      <section>
        <img class="munecas" :src="doll.img" />
        <p>{{ doll.name }}</p>
        <p>{{ doll.price }}</p>

        <router-link to="/dollDetail">
          <button class="boton-detalle">VER DETALLE MUÑECA</button>
        </router-link>
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
.dollCatalog {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
img {
  margin: 1px;
}
section {
  border: 1px solid #4d5a91;
  margin: 0.5em 1em;
  padding: 10px;
}
.boton-detalle {
  background-color: #9781c9;
  padding: 10px;
  border-radius: 10%;
  border-color: #381a3f;
  margin: 10px;
}
.munecas {
  max-width: 15em;
  max-height: 15em;
  border: 4px solid #4d5a91;
}
</style>