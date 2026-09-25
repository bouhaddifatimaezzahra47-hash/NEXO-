<template>
    <div class="d-flex flex-column flex-shrink-0 p-3 bg-light sidebar" style="width: 280px;">
    <a href="/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none brand">
      <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"></use></svg>
      <span class="fs-4">Categories</span>
    </a>
    <hr>
    <ul class="nav nav-pills flex-column mb-auto">
      <li class="nav-item">
        <a href="#" class="nav-link" :class="{active: activeCategory === 'home'}" @click.prevent="setActive('home')">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#home"></use></svg>
          Accueil
        </a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link link-dark" :class="{active: activeCategory === 'femmes'}" @click.prevent="setActive('femmes','vetements_femme')">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#speedometer2"></use></svg>
          Vetements femmes
        </a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link link-dark" :class="{active: activeCategory === 'hommes'}" @click.prevent="setActive('hommes','vetements_homme')">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#table"></use></svg>
            Vetements hommes
        </a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link link-dark" :class="{active: activeCategory === 'bijoux'}" @click.prevent="setActive('bijoux','Bijoux_Accessoires')">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#people-circle"></use></svg>
          Bijoux et Accessoires
        </a>
      </li>
      <li class="nav-item">
        <a href="#" class="nav-link link-dark" :class="{active: activeCategory === 'maison'}" @click.prevent="setActive('maison','Maison_jardin')">
          <svg class="bi me-2" width="16" height="16"><use xlink:href="#people-circle"></use></svg>
            Maison et Jardin
        </a>
      </li>
    </ul>
    <hr>
    <div class="dropdown">
      <a href="#" class="d-flex align-items-center link-dark text-decoration-none dropdown-toggle profile-link" id="dropdownUser2" data-bs-toggle="dropdown" aria-expanded="false">
        <span class="avatar me-2">
          <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16">
          <path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
          <path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8m8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1"/>
          </svg>
        </span>
        <strong>Mon profil</strong>
      </a>
      <ul class="dropdown-menu text-small shadow" aria-labelledby="dropdownUser2">
        <li><a class="dropdown-item" href="#" @click.prevent="emit('show-cart')">Mon Panier</a></li>
        <li><a class="dropdown-item" href="add_products">Vendre Un Produits</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item text-danger" href="#" @click.prevent="logout">Se déconnecter</a></li>
        <li><a class="dropdown-item text-danger" href="#" @click.prevent="delete_account">Supprimer le compte</a></li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useRouter} from 'vue-router'
const activeCategory = ref('home')
const router=useRouter()

const emit = defineEmits(['show-cart','category-selected'])

const setActive = (category,djangocategory) => {
    activeCategory.value = category
    emit('category-selected',djangocategory)
}
const logout=async()=>{
  try{
    const bringcsrftoken =await axios.get('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/csrf/',{withCredentials:true})
		const csrfToken=bringcsrftoken.data.csrfToken
		const response =await axios.post('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/logout/',{},{withCredentials:true,headers:{'X-CSRFToken':csrfToken}})
    router.push('/login')
    
  }catch(error){
    console.log('error',error)
  }
}
const delete_account=async()=>{
  try{
    const bringcsrftoken =await axios.get('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/csrf/',{withCredentials:true})
		const csrfToken=bringcsrftoken.data.csrfToken
		const response =await axios.post('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/delete_acount/',{},{withCredentials:true,headers:{'X-CSRFToken':csrfToken}})
    router.push('/signup')
    
  }catch(error){
    console.log('error',error)
  }
}
</script>

<style scoped>
.sidebar {
  background-color: #f4f7fb !important;
  border-right: 1px solid #e3e3df;
  min-height: 100vh;
}

.brand {
  font-family: Georgia, 'Times New Roman', serif;
  color: #102a43 !important;
  font-weight: 700;
  letter-spacing: 0.8px;
}

.brand svg {
  color: #102a43;
}

hr {
  border-color: #deded9;
  opacity: 1;
}

.nav-link {
  display: flex;
  align-items: center;
  border-radius: 4px;
  padding: 0.65rem 1rem;
  margin-bottom: 0.25rem;
  font-weight: 500;
  color: #4f4f4b;
  transition: background-color 0.2s ease, color 0.2s ease, transform 0.15s ease;
}

.nav-link svg {
  color: #6c757d;
  transition: color 0.2s ease;
}

.nav-link:hover {
  background-color: #e8e8e4;
  color: #102a43;
  transform: translateX(2px);
}

.nav-link:hover svg {
  color: #102a43;
}

.nav-link.active {
  color: #fff !important;
  background-color: #102a43 !important;
  box-shadow: 0 5px 12px rgba(16, 42, 67, 0.18);
}

.nav-link.active svg {
  color: #fff !important;
}

.profile-link {
  padding: 0.6rem 0.75rem;
  border-radius: 10px;
  font-weight: 500;
  color: #102a43 !important;
  transition: background-color 0.2s ease;
}

.profile-link:hover {
  background-color: #e8e8e4;
}

.avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: #102a43;
  color: #fff;
}

.dropdown-menu {
  border: none;
  border-radius: 12px;
  padding: 0.5rem;
  box-shadow: 0 10px 30px rgba(16, 42, 67, 0.14);
}

.dropdown-item {
  border-radius: 8px;
  padding: 0.55rem 0.9rem;
  font-size: 0.9rem;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.dropdown-item:hover {
  background-color: #102a43;
  color: #fff;
}

.dropdown-item.text-danger:hover {
  background-color: #dc3545;
  color: #fff;
}
</style>