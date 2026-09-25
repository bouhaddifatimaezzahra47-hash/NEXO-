<template>
  <main class="signup-page">
    <section class="signup-card" aria-labelledby="signup-title">
      <div class="logo">N</div>
      <p class="brand-name">Nexo</p>

      <h1 id="signup-title">Créer un compte</h1>
      <p class="intro">Inscrivez-vous pour découvrir vos produits préférés.</p>

      <form class="signup-form" @submit.prevent="checking">
        <div class="name-fields">
          <label for="first-name">Prénom</label>
          <input id="first-name" name="firstName" type="text" placeholder="Votre prénom" autocomplete="given-name" v-model="first_name" required>

          <label for="last-name">Nom</label>
          <input id="last-name" name="lastName" type="text" placeholder="Votre nom" autocomplete="family-name" v-model="last_name" required>
        </div>

        <label for="email">Adresse e-mail</label>
        <input id="email" name="email" type="email" placeholder="you@example.com" autocomplete="email" v-model="email" required>

        <label for="password">Mot de passe</label>
        <input id="password" name="password" type="password" placeholder="Au moins 8 caractères" minlength="8" autocomplete="new-password" v-model="password" required>

        <label class="terms" for="terms">
          <input id="terms" name="terms" type="checkbox" required>
          <span>J'accepte les <a href="#terms-of-service">conditions d'utilisation</a>.</span>
        </label>

        <button type="submit">Créer mon compte</button>
      </form>

      <p class="login-text">Vous avez déjà un compte ? <a href="/login">Se connecter</a></p>
    </section>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const first_name = ref('')
const last_name = ref('')
const email = ref('')
const password = ref('')
const router=useRouter()

const checking = async () => {
  if (password.value.length < 8) {
    alert('Le mot de passe doit contenir au moins 8 caractères')
    return
  }

  const data = {
    first_name: first_name.value,
    last_name: last_name.value,
    email: email.value,
    password: password.value
  }

  try {
    const csrfResponse = await axios.get('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/csrf/', {
      withCredentials: true
    })
    const csrfToken=csrfResponse.data.csrfToken
    const response=await axios.post('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/signup/', data, {
      withCredentials: true,
      headers: {
        'X-CSRFToken':csrfToken
      }
    })
    router.push('/login')
  } catch (error) {
    console.log("STATUS:", error.response?.status)
    console.log("RESPONSE:", error.response?.data)
  }
}
</script>


<style scoped>
:global(body) {
  margin: 0;
  background: #eef3f8;
  color: #20344d;
  font-family: Arial, sans-serif;
}

:global(#app) {
  width: 100%;
  max-width: none;
  min-height: 100vh;
  border: 0;
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

.name-fields {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px 12px;
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

.terms {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  margin: 4px 0 12px;
  color: #686863;
  font-size: 12px;
  font-weight: 400;
  line-height: 1.4;
}

.terms input {
  margin-top: 2px;
  accent-color: #102a43;
}

a {
  color: #102a43;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
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

.login-text {
  margin: 24px 0 0;
  color: #686863;
  font-size: 13px;
  text-align: center;
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