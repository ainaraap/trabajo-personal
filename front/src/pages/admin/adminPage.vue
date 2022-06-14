<template>
  <img class="cabecera" src="@/assets/img/MUÑECAS.png" />

  <body>
    <form>
      <input
        type="text"
        name="username"
        class="text-field"
        placeholder="Usuario"
      />
      <input
        type="password"
        name="password"
        class="text-field"
        placeholder="Contraseña"
      />

      <button class="button" @click="onButtonClicked">Entrar</button>
    </form>
  </body>
</template>






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

form .button {
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

form .button:active {
  box-shadow: inset 0 0 2px rgba(0, 0, 0, 0.3), 0 1px 0 white;
}
</style>