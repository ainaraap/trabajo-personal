<template>
  <div class="home">
    <img src="@/assets/img/MUÑECAS.png" />
    <section>
      <router-link to="/dollsCatalog">
        <button class="catalog">VER CATALOGO</button></router-link
      >
    </section>
  </div>
</template>

<script>
</script>

<style scoped>
img {
  margin: 50px;
  height: 200px;
}
.catalog {
  margin: 10px;
  text-decoration: none;
  padding: 0.6rem 1rem;
  border: 1px solid #4d5a91;
  border-radius: 4px;
  background-color: #4d5a91;
  color: #fff;

  cursor: pointer;

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

.catalog:hover,
.catalog:focus {
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
</style>
