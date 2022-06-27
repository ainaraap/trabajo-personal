<template>
  <img class="cabecera" src="@/assets/img/MUÑECAS.png" />

  <section>
    <article v-for="message in messages" :key="message.name">
      <div>
        <div class="messages">
          <p>Nombre: {{ message.name }}</p>
          <p>Teléfono: {{ message.phone }}</p>
          <p>Muñeca elegida: {{ message.message }}</p>
        </div>
      </div>
    </article>
  </section>
</template>

<script>
export default {
  name: "Messages",
  data() {
    return {
      messages: [],
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const response = await fetch("http://localhost:5000/api/messagesList");
      this.messages = await response.json();
    },
  },
};
</script>

<style scoped>
.cabecera {
  margin: -10px 1px;
  height: 100px;
}
div {
  margin: 1em;
}
.messages {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  border: 2px solid #4d5a91;
}
</style>