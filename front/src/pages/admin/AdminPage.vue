<template>
  <img class="cabecera" src="@/assets/img/MUÑECAS.png" />

  <section>
    <input type="text" v-model="user" class="text-field" />
    <input type="password" v-model="password" class="text-field" />

    <button class="button" @click="onButtonClicked">Entrar</button>
  </section>
</template>

<script>
import { useStorage } from "@vueuse/core";
import { admin } from "@/services/auth.js";

export default {
  data() {
    return {
      user: "",
      password: "",
      auth: useStorage("auth", {}),
    };
  },
  methods: {
    async onButtonClicked() {
      const response = await admin(this.user, this.password);
      const loginStatus = response.status;
      console.log("response", response);

      if (loginStatus === 401) {
        alert("unauthorized");
      } else {
        const auth = await response.json();
        console.log("auth", auth);

        this.auth = auth;
        this.$router.push("/dollsCatalog");
      }
    },
  },
};
</script>




<style scoped>
.cabecera {
  margin: -10px 1px;
  height: 100px;
}

section {
  width: 280px;
  height: 260px;
  margin: auto;
  background: #ffd7cd;
  border-radius: 3px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
  text-align: center;
}

section .text-field {
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

section .button {
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

section .button:active {
  box-shadow: inset 0 0 2px rgba(0, 0, 0, 0.3), 0 1px 0 white;
}
</style>