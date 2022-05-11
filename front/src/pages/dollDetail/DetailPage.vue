<template>
  <img src="@/assets/img/MUÑECAS.png" />
  <div class="dollDetail">
    <section>
      <p>{{ doll.img }}</p>
      <p>{{ doll.doll_id }}</p>
      <p>{{ doll.price }}</p>
      <p>{{ doll.size }}</p>
    </section>
  </div>
</template>


<script>
export default {
  name: "dollDetail",
  data() {
    return {
      doll: {},
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch("http://localhost:5000/api/dolls/:id");
      this.doll = await response.json();
    },
  },
};
</script>
