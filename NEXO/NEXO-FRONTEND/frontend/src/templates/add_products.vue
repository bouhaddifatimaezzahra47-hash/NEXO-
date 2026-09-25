<template>
    <div class="container">
          <h4 class="mb-3">Ajouter Un Produit</h4>
          <form class="needs-validation"  @submit.prevent="validate_product">
            <div class="row">
              <div class="container">
                <label for="firstName"> Nom Du Produit </label>
                <input type="text" class="form-control" id="firstName" placeholder="" value="" v-model="product_name" required="">
                <div class="invalid-feedback">
                  Le nom du produit est requis.
                </div>
              </div>
            </div>
            <div class="row">
              <div class="container">
                <label for="description"> Description Du Produit </label>
                <input type="text" class="form-control" id="firstName" placeholder="" value="" v-model="product_description" required="">
                <div class="invalid-feedback">
                  La description est requise.
                </div>
              </div>
            </div>
            <div class="row">
              <div class="container">
                <label for="description"> Le Prix Du Produit </label>
                <input type="number" class="form-control" id="price" placeholder="" value="" v-model="product_price" required="">
                <div class="invalid-feedback">
                  Le prix est requis.
                </div>
              </div>
              <div class="row">
              <div class="container">
                <label for="description"> La Somme Des Articles Disponible  </label>
                <input type="number" class="form-control" id="price" placeholder="" value="" v-model="stock" required="">
                <div class="invalid-feedback">
                  La quantité est requise.
                </div>
              </div>
              </div>
              <div class="row">
              <div class="container">
                <label for="description"> La catégorie </label>
                <select name="pets" id="pet-select" v-model="category">
                      <option value="">--Choisissez une catégorie--</option>
                      <option value="vetements_femme">Vêtements femme</option>
                      <option value="vetements_homme">Vêtements homme</option>
                      <option value="Bijoux_Accessoires">Bijoux et accessoires</option>
                      <option value="Maison_jardin">Maison et jardin</option>
                    </select>

                <div class="invalid-feedback">
                  La catégorie est requise.
                </div>
              </div>
              </div>
            </div>
            <div class="row">
              <div class="container">
                <label for="description"> L'image  Du Produit </label>
                <input type="file" class="form-control" id="image" placeholder="" value=""accept="image/*" @change="handleImage"  required="">
                <div class="invalid-feedback">
                  L'image est requise.
                </div>
              </div>
            </div>
            <div class="row">
              <div class="container">
                <label for="description"> Mot de passe</label>
                <input type="password" class="form-control" id="psw" placeholder="" value=""accept="image/*"  v-model="password" required="">
                <div class="invalid-feedback">
                  Le mot de passe est requis.
                </div>
              </div>
            </div>

            <div class="mb-3">
              <label for="username">Nom d'utilisateur</label>
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text">@</span>
                </div>
                <input type="text" class="form-control" id="username" placeholder="Nom d'utilisateur" v-model="username" required="">
                <div class="invalid-feedback" style="width: 100%;">
                  Le nom d'utilisateur est requis.
                </div>
              </div>
            </div>
            <button class="btn btn-primary btn-lg btn-block" type="submit" >Ajouter</button>
          </form>
        </div>
</template>
<script setup>
import {ref} from 'vue'
import axios from 'axios'
import {useRouter} from 'vue-router'
const product_name=ref('')
const product_description=ref('')
const product_price=ref('')
const product_img=ref(null)
const username=ref('')
const password=ref('')
const stock=ref('')
const category=ref('')
const route= useRouter()
const handleImage = (event) => {
  product_img.value = event.target.files[0]
}


const validate_product=async()=>{
  try{
    const formData = new FormData()
    formData.append('name', product_name.value)
    formData.append('description', product_description.value)
    formData.append('price', product_price.value)
    formData.append('username', username.value)
    formData.append('password', password.value)
    formData.append('stock', stock.value)
    formData.append('category', category.value)
    if (product_img.value) {
      formData.append('image', product_img.value)
    }
    const get_cookie= await axios.get('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/csrf/',{withCredentials:true})
    const csrfToken= get_cookie.data.csrfToken
    console.log("csrf token:", csrfToken)
    const Response= await axios.post('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/add_products/',formData,{withCredentials:true, headers:{'X-CSRFToken':csrfToken}})
    route.push('/App')
  }catch(error){
    console.log("STATUS",error.response?.status)
    console.log("Response", error.response?.data)
  }


}

</script>

<style scoped>
.container {
  max-width: 450px;
}

label {
  font-size: 0.9rem;
  color: #495057;
  margin-bottom: 0.2rem;
  display: inline-block;
}

.form-control,
select {
  border-radius: 6px;
}

.form-control:focus {
  border-color: #0d6efd;
  box-shadow: 0 0 0 0.15rem rgba(13, 110, 253, 0.15);
}

.btn-primary {
  border-radius: 6px;
}
</style>