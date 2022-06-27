<template>
  <img class="cabecera" src="@/assets/img/MUÑECAS.png" />

  <form @submit.prevent="onButtonClicked">
    <input type="text" v-model="name" class="text-field" placeholder="Nombre" />
    <input
      type="text"
      v-model="phone"
      class="text-field"
      placeholder="Teléfono"
    />
    <textarea
      type="text"
      v-model="message"
      class="text-field"
      placeholder="Que muñeca quieres"
    />
    <button class="submit">Enviar</button>
  </form>
</template>

<script>
export default {
  name: "Form",
  data() {
    return {
      name: "",
      phone: "",
      message: "",
    };
  },
  methods: {
    async onButtonClicked() {
      const settings = {
        method: "POST",
        body: JSON.stringify({
          name: this.name,
          phone: this.phone,
          message: this.message,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      };
      await fetch("http://localhost:5000/api/messagesList", settings);
      alert("Enviado correctamente");
    },
  },
};
</script>

<style scoped>
.cabecera {
  margin: -10px 1px;
  height: 100px;
}

form {
  width: 280px;
  height: 260px;
  margin: auto;
  background: #ffd7cd;
  border-radius: 3px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
  text-align: center;
}

form .text-field {
  border: 1px solid #a6a6a6;
  width: 230px;
  height: 40px;
  border-radius: 3px;
  margin-top: 10px;
  padding-left: 10px;
  color: #6c6c6c;
  background: #fcfcfc;
  outline: none;
}

form .submit {
  border-radius: 3px;
  border: 1px solid #336895;
  box-shadow: inset 0 1px 0 #8dc2f0;
  width: 242px;
  height: 40px;
  margin-top: 20px;

  cursor: pointer;
  color: black;
  font-weight: bold;
  text-shadow: 0 -1px 0 #336895;
  background-color: #9983cb;

  font-size: 13px;
}

form .submit:active {
  box-shadow: inset 0 0 2px rgba(0, 0, 0, 0.3), 0 1px 0 white;
}
</style>