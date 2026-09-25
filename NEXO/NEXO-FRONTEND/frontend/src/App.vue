
<template>
  <router-view v-if="route.path === '/signup' || route.path === '/login' || route.path==='/add_products'" />
  <template v-else>
    <div class="app">
    <header class="header">
        <navbar @search-results="receiveSearchResults" @show-cart="showCart" />
    </header>
    <aside class="aside">
    <sidenavbar @show-cart="showCart"  @category-selected="changeCategory"/>
    </aside>
    <main class="main">
    <wishlist v-if="show_cart" />
    <show_products :search_results="search_results":category="selectedCategory"/>
    <Appfooter />
    </main>
    
    
  </div>
  </template>
</template>

<script setup>
import {useRoute} from 'vue-router'
import {ref} from 'vue'
import Appfooter from './components/Appfooter.vue'
import sidenavbar from './components/sidenavbar.vue'
import navbar from './components/navbar.vue'
import homeproducts from './components/homeproducts.vue'
import wishlist from './components/wishlist.vue'
import show_products from './components/show_products.vue'
const route=useRoute()
const search_results = ref([])
const show_cart = ref(false)
const selectedCategory=ref('')
const showCart = () => {
    show_cart.value = true
}
const receiveSearchResults = (results) => {
  search_results.value = results
}
const changeCategory = (category) => {
  selectedCategory.value = category
  show_cart.value = false
}
</script>
<style>
* {
  box-sizing: border-box;
}

html,
body,
#app {
  margin: 0;
  width: 100%;
  height: 100%;
}
body {
  overflow: hidden;
}

.app {
  width: 100%;
  height: 100vh;
}
.header {
  position: fixed;

  top: 0;
  left: 0;
  right: 0;

  height: 90px;

  z-index: 1000;

  background-color: white;
}
.aside {
  position: fixed;

  top: 90px;
  left: 0;
  bottom: 0;

  width: 280px;

  z-index: 900;

  background-color: #f8f9fa;

  overflow-y: auto;
}
.main {
  position: fixed;

  top: 90px;
  left: 280px;
  right: 0;
  bottom: 0;

  padding: 30px;

  overflow-y: auto;
  overflow-x: hidden;

  background-color: white;
}

</style>

