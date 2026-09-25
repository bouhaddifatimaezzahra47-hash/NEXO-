<template>
	<main class="signup-page">
    <section class="signup-card" aria-labelledby="signup-title">
      <div class="logo">N</div>
      <p class="brand-name">Nexo</p>

      <h1 id="signup-title">Connexion</h1>
      <p class="intro">Connectez-vous pour accéder à votre compte.</p>

      <form class="signup-form" @submit.prevent="check_infos">
        <label for="username">Prénom</label>
        <input id="username" name="username" type="text" placeholder="Votre prénom" autocomplete="given-name" v-model="check_username" required>

        <label for="password">Mot de passe</label>
        <input id="password" name="password" type="password" placeholder="Au moins 8 caractères" minlength="8" autocomplete="new-password" v-model="check_password" required>
    		<button type="submit">Se connecter</button>
      </form>
    </section>
  </main>
</template>
<script setup>
import {ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { router } from '../main'
const check_username=ref('')
const check_password=ref('')
const check_infos =async()=>
{
	const check_data={
		username:check_username.value,
		password:check_password.value
	}
	try{
		const bringcsrftoken =await axios.get('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/csrf/',{withCredentials:true})
		const csrfToken=bringcsrftoken.data.csrfToken
		const response =await axios.post('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/login/',check_data,{withCredentials:true,headers:{'X-CSRFToken':csrfToken}})
    router.push('/App')
    

	}catch(error){
		console.log("STATUS",error.response?.status)
		console.log("RESPONSE",error.response?.data)
	}
}

</script>
<style scoped>
.logo {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 10px;
  border-radius: 4px;
  background: #102a43;
  color: #fff;
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 21px;
  font-weight: 700;
}
.brand-name {
  margin: 0 0 28px;
  color: #102a43;
  font-family: Georgia, 'Times New Roman', serif;
  font-size: 20px;
  font-weight: 700;
  text-align: center;
}
h1 {
  margin: 0;
  font-size: 28px;
  line-height: 1.2;
  text-align: center;
}

.intro {
  margin: 10px 0 28px;
  color: #686863;
  font-size: 14px;
  text-align: center;
}
.signup-form {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.signup-page {
  min-height: 100vh;
  background: #eef3f8;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px 16px;
  box-sizing: border-box;
}

.signup-card {
  width: 100%;
  max-width: 420px;
  padding: 36px;
  box-sizing: border-box;
  border: 1px solid #deded9;
  border-radius: 4px;
  background: #fff;
  box-shadow: 0 18px 40px rgba(16, 42, 67, 0.1);
}
label {
  color: #223b58;
  font-size: 13px;
  font-weight: 600;
}
input:not([type="checkbox"]) {
  width: 100%;
  box-sizing: border-box;
  margin-bottom: 10px;
  padding: 12px;
  border: 1px solid #d5d5d0;
  border-radius: 3px;
  background: #f8fbfe;
  color: #20344d;
  font: inherit;
  outline: none;
}
input:not([type="checkbox"]):focus {
  border-color: #102a43;
  box-shadow: 0 0 0 3px rgba(16, 42, 67, 0.1);
}
button {
  padding: 13px;
  border: 1px solid #102a43;
  border-radius: 3px;
  background: #102a43;
  color: #fff;
  cursor: pointer;
  font: 600 14px Arial, sans-serif;
}

button:hover {
  background: #ffffff;
  color: #102a43;
}
@media (max-width: 480px) {
  .signup-card {
    padding: 28px 20px;
  }

  .name-fields {
    grid-template-columns: 1fr;
    gap: 0;
  }
}
</style>
