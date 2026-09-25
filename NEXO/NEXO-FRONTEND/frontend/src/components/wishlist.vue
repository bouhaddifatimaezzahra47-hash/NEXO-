
<template>
    <div class="container py-5">
        <h2 class="mb-4">Mon Panier</h2>

        <div v-if="products.length === 0" class="text-center py-5">
            <p class="text-muted">Votre panier est vide.</p>
        </div>

        <div v-else class="wishlist-list">
            <div
                v-for="product in products"
                :key="product.id"
                class="wishlist-item"
            >
                <img
                    :src="imageUrl(product.image)"
                    :alt="product.name"
                    class="product-image"
                >

                <div class="product-info">
                    <h5>{{ product.name }}</h5>
                    <p>{{ product.description }}</p>
                    <strong class="price">{{ product.price }} $</strong>
                </div>

                <button class="delete-btn" @click="delete_product(product)">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="16"
                        height="16"
                        fill="currentColor"
                        class="bi bi-trash3-fill"
                        viewBox="0 0 16 16"
                    >
                        <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998-.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
                    </svg>
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const products = ref([])

const apiBaseUrl =
    'https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev'

const imageUrl = (imagePath) => {
    if (!imagePath) return ''
    if (imagePath.startsWith('http')) return imagePath
    if (imagePath.startsWith('/media/')) return `${apiBaseUrl}${imagePath}`
    if (imagePath.startsWith('media/')) return `${apiBaseUrl}/${imagePath}`
    return `${apiBaseUrl}/media/${imagePath}`
}

const get_infos = async () => {
    try {
        const get_data = await axios.get(
            `${apiBaseUrl}/send_wishlist/`,
            { withCredentials: true }
        )

        products.value = get_data.data

    } catch (error) {
        console.log('message: ', error)
    }
}

const delete_product=async(product)=>{
    const csrfResponse = await axios.get('https://laughing-train-pjqw77jj97j4cgj4-8000.app.github.dev/csrf/', {
      withCredentials: true
    })
    const csrfToken=csrfResponse.data.csrfToken
    try{
        const send_infos= await axios.post(`$(apiBaseUrl)/delete_product/`,product_id=product.id, {withCredentials: true,
        headers: {'X-CSRFToken':csrfToken  }})}
    catch(error){
            console.log('message:',error)
        }
    products.value = products.value.filter(
    p => p.id !== product.id)
           

}

onMounted(() => {
    get_infos()
    

})
</script>

<style scoped>
.wishlist-list {
    max-width: 900px;
}

.wishlist-item {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 15px;
    margin-bottom: 15px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(16, 42, 67, 0.1);
}

.product-image {
    width: 80px;
    height: 80px;
    object-fit: cover;
    border-radius: 8px;
    flex-shrink: 0;
}

.product-info {
    flex: 1;
}

.product-info h5 {
    margin: 0 0 5px;
}

.product-info p {
    margin: 0 0 8px;
    color: #777;
}

.price {
    color: #0d6efd;
}

.delete-btn {
    border: none;
    background: transparent;
    color: #dc3545;
    padding: 8px;
    cursor: pointer;
}

.delete-btn:hover {
    color: #a71d2a;
}
</style>


