<template>
<body>
    <main>
        <div class="container main-content">
            <h1>E-commerce Footer</h1>
            <p>This content area aligns with the footer below.</p>
        </div>
    </main>
    
    <footer class="footer-ecom" role="contentinfo">
        <div class="container">
            <div class="footer-ecom__main">
                <div class="footer-ecom__links">
                    <h3 class="footer-ecom__heading">Contact Us</h3>
                    <ul>
                        <li><a href="#"></a></li>
                        <li><a href="#">Track Your Order</a></li>
                        <li><a href="#">Shipping & Delivery</a></li>
                        <li><a href="#">Returns & Exchanges</a></li>
                        <li><a href="#">FAQ</a></li>
                    </ul>
                </div>
                <div class="footer-ecom__links">
                    <h3 class="footer-ecom__heading">About Us</h3>
                    <ul>
                        <li><a href="#">Our Story</a></li>
                        <li><a href="#">Careers</a></li>
                        <li><a href="#">Press</a></li>
                        <li><a href="#">Store Locator</a></li>
                    </ul>
                </div>
                <div class="footer-ecom__links">
                    <h3 class="footer-ecom__heading">My Account</h3>
                    <ul>
                        <li><a href="#">Sign In / Register</a></li>
                        <li><a href="#">My Orders</a></li>
                        <li><a href="#">My Wishlist</a></li>
                        <li><a href="#">Account Settings</a></li>
                    </ul>
                </div>
                <div class="footer-ecom__newsletter">
                    <h3 class="footer-ecom__heading">Stay Connected</h3>
                    <p>Get exclusive deals, new product announcements, and more.</p>
                    <form class="footer-ecom__newsletter-form">
                        <label for="newsletter-email">Email Address</label>
                        <input type="email" id="newsletter-email" class="footer-ecom__newsletter-input" placeholder="your@email.com">
                        <button type="submit" class="footer-ecom__newsletter-button">Subscribe</button>
                    </form>
                </div>
            </div>
            <div class="footer-ecom__bottom">
                <p class="footer-ecom__copyright">&copy; 2025 YourStore Inc. All Rights Reserved.</p>
                <div class="footer-ecom__payment-icons" aria-label="Accepted payment methods">
                    <ul>
                        <li><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Credit Card</title><path d="M21.18,3.93H2.82A2.82,2.82,0,0,0,0,6.75v10.5A2.82,2.82,0,0,0,2.82,20.07H21.18A2.82,2.82,0,0,0,24,17.25V6.75A2.82,2.82,0,0,0,21.18,3.93Zm-18.36,3H21.18a.14.14,0,0,1,.14.14V9.6H2.68V7.07A.14.14,0,0,1,2.82,6.93Zm18.36,10.32H2.82a.14.14,0,0,1-.14-.14V12.42H21.32v4.69A.14.14,0,0,1,21.18,17.25Z"/></svg></li>
                        <li><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Bank Transfer</title><path d="M12,1.5,1.5,6.23v1.44H22.5V6.23Zm8.91,15.5H12.4v-9H10.6v9H2.09V9.6H.15v9a1.44,1.44,0,0,0,1.44,1.44H22.41a1.44,1.44,0,0,0,1.44-1.44v-9H21.09Z"/></svg></li>
                        <li><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Digital Wallet</title><path d="M19,4H5A3,3,0,0,0,2,7V17a3,3,0,0,0,3,3H19a3,3,0,0,0,3-3V7A3,3,0,0,0,19,4Zm1,13a1,1,0,0,1-1,1H5a1,1,0,0,1-1-1V7A1,1,0,0,1,5,6H19a1,1,0,0,1,1,1Z M17,11H7a1,1,0,0,0,0,2H17a1,1,0,0,0,0-2Z"/></svg></li>
                        <li><svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Secure Payment</title><path d="M18,9H17V6A5,5,0,0,0,7,6V9H6a3,3,0,0,0-3,3v7a3,3,0,0,0,3,3H18a3,3,0,0,0,3-3V12A3,3,0,0,0,18,9ZM9,6a3,3,0,0,1,6,0V9H9Zm10,13a1,1,0,0,1-1,1H6a1,1,0,0,1-1-1V12a1,1,0,0,1,1-1H18a1,1,0,0,1,1,1Z"/></svg></li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</body>
</template>
<style>
        :root {
            --footer-bg: #f5f5f7;
            --footer-text: #515154;
            --footer-heading: #1d1d1f;
            --footer-link-hover: #0066cc;
            --footer-border: #d2d2d7;
            --form-button-bg: #0071e3;
            --form-button-text: #ffffff;
        }

        /* Basic body styles */
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            background-color: #fff;
        }
        
        main {
            flex-grow: 1;
        }

        /* Shared container for alignment */
        .container {
            width: 90%;
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }

        .main-content {
            padding: 2rem 0;
        }

        /* FOOTER STYLES START HERE */
        
        .footer-ecom {
            background-color: var(--footer-bg);
            color: var(--footer-text);
            font-size: 0.875rem;
            line-height: 1.5;
            padding-top: 2.5rem;
            border-top: 1px solid var(--footer-border);
        }

        .footer-ecom__main {
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
            padding-bottom: 2.5rem;
            border-bottom: 1px solid var(--footer-border);
        }
        
        .footer-ecom__heading {
            color: var(--footer-heading);
            font-size: 0.9rem;
            font-weight: 600;
            margin: 0 0 1rem 0;
        }
        
        .footer-ecom__links ul { margin: 0; padding: 0; list-style: none; }
        .footer-ecom__links li:not(:last-child) { margin-bottom: 0.75rem; }
        .footer-ecom__links a { color: var(--footer-text); text-decoration: none; }
        .footer-ecom__links a:hover { color: var(--footer-link-hover); text-decoration: underline; }
        
        .footer-ecom__newsletter-form { display: flex; flex-direction: column; }
        .footer-ecom__newsletter-input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid var(--footer-border);
            border-radius: 6px;
            font-size: 1rem;
            margin: 0.5rem 0 0.75rem 0;
            box-sizing: border-box;
        }
        .footer-ecom__newsletter-button {
            background-color: var(--form-button-bg);
            color: var(--form-button-text);
            border: none;
            padding: 0.75rem;
            border-radius: 6px;
            font-weight: 500;
            cursor: pointer;
            transition: opacity 0.2s;
        }
        .footer-ecom__newsletter-button:hover { opacity: 0.85; }

        .footer-ecom__bottom {
            padding: 1.5rem 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1.5rem;
        }
        
        .footer-ecom__copyright { margin: 0; text-align: center; }
        
        .footer-ecom__payment-icons ul {
            margin: 0;
            padding: 0;
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1rem;
        }

        .footer-ecom__payment-icons svg {
            height: 24px;
            width: 38px;
            fill: currentColor; /* Makes icons inherit text color */
        }

        @media (min-width: 600px) {
            .footer-ecom__main { grid-template-columns: repeat(2, 1fr); }
        }
        
        @media (min-width: 992px) {
            .footer-ecom__main { grid-template-columns: 1fr 1fr 1fr 1.5fr; }
            .footer-ecom__bottom { flex-direction: row; justify-content: space-between; }
        }
    </style>