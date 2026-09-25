<template>
  <section class="nexo-hero">
    <div class="nexo-hero__shape" aria-hidden="true"></div>

    <div class="nexo-hero__inner">
      <div class="nexo-hero__text">
        <div class="nexo-hero__eyebrow">
          <span class="nexo-hero__dot"></span>
          Nouveautés de la semaine
        </div>
        <h1 class="nexo-hero__title">
          Le marché où tout se connecte.
        </h1>
        <p class="nexo-hero__subtitle">
          Mode, maison, bijoux, artisanat local — découvrez des vendeurs
          indépendants et des pièces qu'on ne trouve pas ailleurs.
        </p>
      </div>

      <div class="nexo-hero__visual">
        <div class="nexo-hero__frame">
          <img
            class="nexo-hero__image"
            src="https://images.unsplash.com/photo-1556157382-97eda2d62296?fm=jpg&q=80&w=1200&auto=format&fit=crop"
            alt="Femme élégante en manteau bleu"
          />
        </div>
        <div class="nexo-hero__promo">
          <span class="nexo-hero__promo-value">-30%</span>
          <span class="nexo-hero__promo-label">promo</span>
        </div>
      </div>
    </div>
  </section>

  <section id="produits" class="products-section">
    <div class="container py-5">
      <div class="row g-4">

        <div
          class="col-xl-3 col-lg-4 col-md-6 col-sm-6"
          v-for="product in products_list"
          :key="product.id"
        >
          <div class="card product-card h-100 shadow-sm border-0">

            <div class="product-image">
              <img
                :src="imageUrl(product.image)"
                :alt="product.name"
              />
            </div>

            <div class="card-body d-flex flex-column">

              <h5 class="card-title">
                {{ product.name }}
              </h5>

              <p class="category">
                {{ product.category }}
              </p>

              <p class="description">
                {{ product.description }}
              </p>

              <div class="price">
                ${{ product.price }}
              </div>

              <button
                class="btn btn-primary add-cart-btn mt-auto"
                @click="addToCart(product)"
              >
                Ajouter au panier
              </button>

            </div>

          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, watch} from 'vue'
const products_list = ref([])
const wishlist_products=ref([])
const props = defineProps({
    search_results: Array,
    category:String
})
const apiBaseUrl =
  'https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev'
watch(
    () => props.search_results,
    (new_results) => {
        console.log(new_results)
        if (new_results && new_results.length > 0) {
            products_list.value = new_results
        }
    }
)
watch(
  ()=>props.category,
  (newCategory)=>{
    if (newCategory) {
      getCategoryProducts(newCategory)
    }
  }
)

const imageUrl = (imagePath) => {
  if (!imagePath) return ''

  if (imagePath.startsWith('http')) {
    return imagePath
  }

  if (imagePath.startsWith('/media/')) {
    return `${apiBaseUrl}${imagePath}`
  }

  if (imagePath.startsWith('media/')) {
    return `${apiBaseUrl}/${imagePath}`
  }

  return `${apiBaseUrl}/media/${imagePath}`
}

const add_to_cards = async () => {
  try {
    const response = await axios.get(
      `${apiBaseUrl}/show_products/`,
      {
        withCredentials: true
      } 
    )

    products_list.value = response.data

  } catch (error) {
    console.log('error:', error)
  }
}

const addToCart =async (product) => {
  console.log('Product added to cart:', product)
  wishlist_products.value.push(product)
  
  try{
    const csrfResponse = await axios.get('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/csrf/', {
      withCredentials: true
    })
    const csrfToken=csrfResponse.data.csrfToken
    const wishproducts= await axios.post('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/wishlist/',{product_id:product.id}, {withCredentials: true,headers: {'X-CSRFToken':csrfToken}})

  }catch(error){
    console.log('message:',error)
  }
}
const getCategoryProducts = async (category) => {
  try {
    const response = await axios.get(
      `${apiBaseUrl}/categories_clothes/`,
      {
        params: {
          category: category
        },
        withCredentials: true
      }
    )

    products_list.value = response.data

  } catch (error) {
    console.log('category error:', error)
  }
}

onMounted(() => {
  add_to_cards()
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Sora:wght@400;500;600&display=swap');

/* ---------- Hero ---------- */
.nexo-hero {
  position: relative;
  overflow: hidden;
  background: #f8f8f6;
  font-family: 'Sora', sans-serif;
  padding: 5rem 0 6rem;
}

.nexo-hero__shape {
  position: absolute;
  top: 0;
  right: 0;
  width: 55%;
  height: 100%;
  background: linear-gradient(160deg, #173b63 0%, #0b1f36 100%);
  clip-path: polygon(28% 0, 100% 0, 100% 100%, 0% 100%);
  z-index: 0;
}

.nexo-hero__inner {
  position: relative;
  z-index: 1;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 5vw;
  display: flex;
  align-items: center;
  gap: 3rem;
  flex-wrap: wrap;
}

.nexo-hero__text {
  flex: 1 1 420px;
  max-width: 480px;
}

.nexo-hero__eyebrow {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: #102a43;
  margin-bottom: 1.1rem;
}

.nexo-hero__dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #102a43;
  display: inline-block;
}

.nexo-hero__title {
  font-family: 'Fraunces', serif;
  font-size: clamp(2.2rem, 3.8vw, 3.1rem);
  font-weight: 600;
  line-height: 1.15;
  color: #102a43;
  margin: 0 0 1.15rem;
}

.nexo-hero__subtitle {
  font-size: 1.02rem;
  line-height: 1.65;
  color: #5f5f5b;
  margin: 0;
  max-width: 42ch;
}

.nexo-hero__visual {
  position: relative;
  flex: 1 1 320px;
  max-width: 420px;
  display: flex;
  justify-content: center;
}

.nexo-hero__frame {
  border-radius: 20px;
  padding: 10px;
  background: #ffffff;
  box-shadow: 0 25px 50px rgba(16, 42, 67, 0.2);
}

.nexo-hero__image {
  width: 100%;
  height: 420px;
  object-fit: cover;
  border-radius: 14px;
  display: block;
}

.nexo-hero__promo {
  position: absolute;
  bottom: -16px;
  left: -16px;
  background: #ffffff;
  color: #102a43;
  border-radius: 14px;
  padding: 0.7rem 1.1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  line-height: 1.1;
  box-shadow: 0 12px 24px rgba(16, 42, 67, 0.16);
}

.nexo-hero__promo-value {
  font-size: 1.15rem;
  font-weight: 700;
}

.nexo-hero__promo-label {
  font-size: 0.7rem;
  color: #5f5f5b;
}

@media (max-width: 860px) {
  .nexo-hero__shape {
    clip-path: none;
    width: 100%;
    height: 55%;
    top: auto;
    bottom: 0;
    opacity: 0.06;
    background: #102a43;
  }
  .nexo-hero__inner {
    flex-direction: column;
    text-align: center;
  }
  .nexo-hero__eyebrow {
    justify-content: center;
  }
  .nexo-hero__subtitle {
    margin-left: auto;
    margin-right: auto;
  }
  .nexo-hero__promo {
    left: 50%;
    transform: translateX(-50%);
  }
}

/* ---------- Products ---------- */
.products-section {
  background-color: #eef3f8;
  min-height: 100vh;
}

.product-card {
  border-radius: 4px;
  overflow: hidden;
  background: #ffffff;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 16px 30px rgba(16, 42, 67, 0.13) !important;
}

.product-image {
  height: 220px;
  width: 100%;
  background: #f5f8fc;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 18px;
}

.product-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.2s ease;
}

.product-card:hover .product-image img {
  transform: scale(1.04);
}

.card-body {
  padding: 20px;
}

.card-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 6px;
  color: #102a43;
}

.category {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.02em;
  color: #666660;
  margin-bottom: 8px;
}

.description {
  font-size: 14px;
  color: #686863;
  line-height: 1.5;
  margin-bottom: 12px;
}

.price {
  font-size: 18px;
  font-weight: 700;
  color: #102a43;
  margin-bottom: 15px;
}

.add-cart-btn {
  width: 100%;
  border: 1px solid #102a43;
  border-radius: 3px;
  background: #102a43;
  color: #ffffff;
  font-weight: 600;
  letter-spacing: 0.01em;
  padding: 0.7rem 1rem;
  transition: background-color 0.2s ease, color 0.2s ease, transform 0.2s ease;
}

.add-cart-btn:hover,
.add-cart-btn:focus-visible {
  border-color: #333333;
  background: #ffffff;
  color: #102a43;
  transform: translateY(-1px);
}

.add-cart-btn:focus-visible {
  outline: 2px solid #102a43;
  outline-offset: 3px;
}
</style>