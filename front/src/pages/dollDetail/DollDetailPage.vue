<template>
  <img class="cabecera" src="@/assets/img/MUÑECAS.png" />
  <div class="detalle">
    <section>
      <img class="munecas" :src="doll.img" />
      <div class="descrip">
        <p>Nombre: {{ doll.name }}</p>
        <p>Precio: {{ doll.price }}</p>
        <p>Tamaño: {{ doll.size }}</p>
      </div>
    </section>
  </div>
</template>



<script>
import config from "../../config.js";

export default {
  name: "Detail",
  data() {
    return {
      doll: [],
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch(
        `${config.API_PATH}/dolls` + "/" + this.$route.params.doll_id
      );
      this.doll = await response.json();
    },
  },
};
</script>

<style scoped>
.detalle {
  display: grid;
  grid-template-columns: 1fr;
}
.cabecera {
  margin: -10px 1px;
  height: 100px;
}
section {
  margin: 0.5em 1em;
  padding: 10px;
}

.munecas {
  margin: 1em 1.5em 1em 25em;
  max-width: 15em;
  max-height: 15em;
  border: 4px solid #4d5a91;
  float: left;
}
.descrip {
  margin: 4em 25em 1.5em 1em;
  max-width: 20em;
  max-height: 20em;

  float: right;
}
</style>
