<template>
  <img src="@/assets/img/MUÑECAS.png" />
  <div class="dollCatalog">
    <article v-for="doll in catalog" :key="doll.id">
      <section>
        <img class="munecas" :src="doll.img" />
        <p>{{ doll.name }}</p>
        <p>{{ doll.price }}</p>
      </section>
    </article>
  </div>
</template>


<script>
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
      const response = await fetch("http://localhost:5000/api/:doll_id");
      this.doll_id = await response.json();
    },
  },
};
</script>
