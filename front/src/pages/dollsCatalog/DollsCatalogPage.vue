<template>
  <img class="cabecera" src="@/assets/img/MUÑECAS.png" />

  <section class="dollCatalog">
    <article v-for="doll in catalog" :key="doll.doll_id">
      <div class="munecacomp">
        <img class="munecas" :src="doll.img" />
        <div>
          <p>{{ doll.name }}</p>
          <p>{{ doll.price }}</p>
        </div>

        <router-link class="irDetalle" :to="`/dollDetail/${doll.doll_id}`"
          >Ver detalle</router-link
        >
      </div>
    </article>
  </section>
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
    openDollDetail(doll) {
      this.$router.push("/dollsCatalog/" + doll.doll_id);
    },
  },
};
</script>

<style scoped>
.cabecera {
  margin: -10px 1px;
  height: 100px;
}
.dollCatalog {
  display: grid;
  grid-template-columns: 2fr 2fr 2fr;
}

.irDetalle {
  text-decoration: none;
  padding: 0.5rem 0.5rem;
  border: 1px solid #4d5a91;
  border-radius: 4px;
  background-color: #4d5a91;
  color: #fff;

  font-size: 1.5rem;
  text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.5);
  box-shadow: 0 1px 0 rgba(255, 255, 255, 0.5) inset,
    0 1px 3px rgba(0, 0, 0, 0.2);
  background-image: -webkit-gradient(
    linear,
    left top,
    left bottom,
    color-stop(10%, rgb(160, 160, 160)),
    to(#4d5a91)
  );
  background-image: linear-gradient(#4d5a91 10%, #394b9c 100%);
}

.irDetalle:hover,
.irDetalle:focus {
  background-color: #4d5a91;
  background-image: -webkit-gradient(
    linear,
    left top,
    left bottom,
    color-stop(10%, #9983cb),
    to(#4d5a91)
  );
  background-image: linear-gradient(#b6b9c5 10%, #394b9c 100%);
}

.munecas {
  max-width: 13em;
  max-height: 13em;
  border: 1px solid #4d5a91;
  padding: 2em;
  background-color: #ffd7cd;
}
article {
  margin: 1em;
}
div {
  margin: 1em;
}
</style>