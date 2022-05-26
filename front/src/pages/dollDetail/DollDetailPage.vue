<template>
  <img src="@/assets/img/MUÑECAS.png" />
  <div class="detalle">
    <section>
      <img class="munecas" :src="doll.img" />
      <p>{{ doll.name }}</p>
      <p>{{ doll.price }}</p>
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
img {
  margin: 1px;
}
section {
  margin: 0.5em 1em;
  padding: 10px;
}

.munecas {
  max-width: 20em;
  max-height: 20em;
  border: 4px solid #4d5a91;
}
</style>
