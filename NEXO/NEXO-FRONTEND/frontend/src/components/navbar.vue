<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#"><span class="text text-primary">Nexo</span></a>
    
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
            <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6m2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0m4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4m-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10s-3.516.68-4.168 1.332c-.678.678-.83 1.418-.832 1.664z"/>
            </svg>
            Se Connecter
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="/login">Se connecter</a></li>
            <li><a class="dropdown-item" href="/signup">S'inscrire</a></li>
            <li><a class="dropdown-item" href="#"  @click.prevent="emit('show-cart')">Mon panier</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex" role="search" @submit.prevent="send_search">
        <input class="form-control me-2" type="search" placeholder="Cherchez un produit..." aria-label="Rechercher" v-model="search_name" />
        <button class="btn btn-outline-success" type="submit" >
            Rechercher
        </button>
      </form>
    </div>
  </div>
</nav>
</template>
<script setup>
import {ref} from "vue"
import axios from 'axios'
const search_name=ref('')
const emit = defineEmits(['search-results'])
const send_search=async()=>{
    try{
        const search= await axios.get('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/search/',{params:{search_name: search_name.value}})
        emit('search-results', search.data)
    }catch(error){
        console.log("messsage:",error)
    }
}

</script>

<style scoped>
.navbar {
  background-color: #ffffff !important;
  border-bottom: 1px solid #e8e8e5;
  box-shadow: 0 5px 18px rgba(16, 42, 67, 0.05);
  padding: 0.9rem 1.5rem;
}

.navbar-brand .text-primary {
  font-family: Georgia, 'Times New Roman', serif;
  font-weight: 800;
  font-size: 1.65rem;
  letter-spacing: 1px;
  color: #102a43 !important;
}

.nav-link.dropdown-toggle {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-weight: 500;
  color: #333 !important;
  transition: color 0.2s ease;
}

.nav-link.dropdown-toggle:hover {
  color: #666666 !important;
}

.dropdown-menu {
  border: none;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(16, 42, 67, 0.12);
  padding: 0.5rem;
  margin-top: 0.5rem;
}

.dropdown-item {
  border-radius: 6px;
  padding: 0.5rem 0.9rem;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.dropdown-item:hover {
  background-color: #102a43;
  color: #fff;
}

.form-control {
  border-radius: 3px 0 0 3px;
  border: 1px solid #d8d8d4;
  background-color: #f8fbfe;
  padding: 0.5rem 1rem;
}

.form-control:focus {
  border-color: #102a43;
  box-shadow: 0 0 0 0.2rem rgba(16, 42, 67, 0.1);
}

.btn-outline-success {
  border-radius: 0 3px 3px 0;
  border-color: #102a43;
  background-color: #102a43;
  color: #ffffff;
  font-weight: 500;
  padding: 0.5rem 1.25rem;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.btn-outline-success:hover {
  background-color: #ffffff;
  border-color: #102a43;
  color: #102a43;
}
</style>