
<h1 align="center">Yara Beach Excursions and Rentals </h1>

<h2 align="center">Code Institute - Milestone Project 4</h2>

![alt text](documentation/readme-images/mockup-yarabeach-image.png "Mockup of Yara Beach website when viewed on a desktop, tablet and mobile device.")
<sub>_Created using_ [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop/landpa.html?gclid=CjwKCAjwwL6aBhBlEiwADycBIKPGhQtahSxttLjZVTUJ7djn4sFEDI1p6gUoIk5PJzHRyigcU7Rm-BoCQtcQAvD_BwE&mv=search&mv=search&sdid=GVTYXZY8&ef_id=CjwKCAjwwL6aBhBlEiwADycBIKPGhQtahSxttLjZVTUJ7djn4sFEDI1p6gUoIk5PJzHRyigcU7Rm-BoCQtcQAvD_BwE:G:s&s_kwcid=AL!3085!3!594259336243!e!!g!!adobe%20photoshop!17011954559!138864791987/)</sub>
<br>

Yara Beach is an e-commerce website. Yara is the actual name of the owner, who is my friend from the beautiful island of the Dominican Republic. During the process of building my portfolios through the Code Institute, I decided that my last project or portfolio would be a real-use website. So I contacted my friend Yara, who has a business called Yara Beach. I told her I'd create a website for her to attract more customers and increase sales. She was so happy to hear that and agreed, so I asked her what it was that she needed the website to have based on her customers' needs. She sells excursions and rentals through Airbnb and Booking.com. She needed a combined website for excursions and rentals, and waala, here we have the Yara Beach website, where she will be able to keep track of her customers when they register and see all the oncoming bookings, e.g., today's bookings, future bookings, and previous bookings for excursions and rentals. Customers will be able to view all their current bookings, previous bookings, and future bookings for both excursions and rentals as well. Customers will be able to leave review ratings and view beautiful product details with many images showcasing the products. The owner will be able to add products, delete products, edit products, and put products on active or inactive status.

This project was mainly created to satisfy the final Milestone Project requirements of the Full
Stack Web Development Program at the [Code Institute](https://codeinstitute.net/).
This full-stack website, with its fully-implemented authentication mechanism and
payment system and control of a centrally-owned dataset, was constructed using
[HTML5](http://en.wikipedia.org/wiki/HTML5), [CSS3](http://en.wikipedia.org/wiki/CSS),
[JavaScript](https://en.wikipedia.org/wiki/JavaScript), the JavaScript library
[jQuery](https://jquery.com/) , [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>),
[Django](https://www.djangoproject.com/), [Heroku Postgres](https://www.heroku.com/postgres) database
and the [Stripe](https://stripe.com/) payment platform.

[Click here to visit the site.](https://yara-beach.herokuapp.com/)

To test the site's checkout process please use the test credit card number provided in
the [Stripe Documentation](https://stripe.com/docs/testing):

- Card Number: 4242 4242 4242 4242
- Expiration Date: Any date (e.g. 02/04)
- CVC: Any three digits

<br>

## **Table of Contents**

1. [**User Experience (UX)**](#ux)
   - [Project Goals](#project-goals)
   - [User Stories](#user-stories)
     - [Prospective User](#prospective-user)
     - [Existing User](#existing-user)
     - [Site Owner](#site-owner)
2. [**User Centered Design**](#user-centered-design)
   - [1) The Strategy Plane](#1-strategy-plane)
   - [2) The Scope Plane](#2-scope-plane)
   - [3) The Structure Plane](#3-structure-plane)
     - [Planning](#planning)
     - [Existing Features](#existing-features)
       - [Favicon](#favicon)
       - [Title](#title)
       - [Navbar](#navbar)
       - [Django Messages](#django-messages)
       - [Pagination Links](#pagination-links)
       - [Excursion Cards](#excursion-cards)
       - [Rental Cards](#rental-cards)
       - [Footer](#footer)
       - [Home Page Features](#home-page-features)
       - [Contact Page Features](#contact-page-features)
       - [Rental page app features](#rental-page-app-features)
       - [Excursion page app features](#excursion-page-app-features)
       - [Login page features](#login-page-features)
       - [Product Detail Page Features](#product-detail-page-features)
       - [Register page feature](#register-page-feature)
       - [Cart Page Features](#cart-page-features)
       - [Checkout Page Features](#checkout-page-features)
       - [Checkout Success Page Features](#checkout-success-page-features)
       - [Change Password page feature](#change-password-page-feature)
       - [Customer Excursion Bookings page features](#customer-excursion-bookings-page-features)
       - [Cutomer Rental Bookings page features](#customer-rental-bookings-page-features)
       - [Admin navbar](#admin-navbar)
       - [Administrator dashboard page features](#administrator-dashboard-page-features)
       - [Administrator Excursion page features](#administrator-excursion-page-features)
       - [Administrator Rental page features](#administrator-rental-page-features)
       - [Administrator add rental page features](#administrator-add-rental-page-features)
       - [Administrator edit rental page features](#administrator-edit-rental-page-features)
       - [Administrator delete rental page features](#administrator-delete-rental-page-features)
       - [Administrator add excursion page features](#administrator-add-rental-page-features)
       - [Administrator edit excursion page features](#administrator-edit-rental-page-features)
       - [Administrator delete excursion page features](#administrator-delete-rental-page-features)
       - [404 and 500 Page Features](#404-and-500-page-features)
     - [Features Left to Implement](#features-left-to-implement)
   - [4) The Skeleton Plane](#4-skeleton-plane)
     - [Wireframes](#wireframes)
   - [5) The Surface Plane](#5-surface-plane)
     - [Design](#design)
     - [Colour Scheme](#colour-scheme)
     - [Logo Design](#logo-design)
     - [Icons](#icons)
     - [Typography](#typography)
3. [**Development**](#development)
   - [Information Architecture](#information-architecture)
     - [Data Schema](#data-schema)
     - [Data Models](#data-models)
4. [**Technologies Used**](#technologies-used)
5. [**Testing**](#testing)
6. [**Deployment**](#deployment)
   - [Local Deployment](#local-deployment)
   - [Heroku Deployment](#heroku-deployment)
     - [AWS](#set-up-an-amazon-web-services-account)
     - [S3](#set-up-the-simple-storage-service-bucket)
7. [**Credits**](#credits)
   - [Content](#content)
   - [Media](#media)
   - [Acknowledgements](#acknowledgements)

<br>

---

## UX

Yara Beach sees the need to provide the user with a website where they can find all their needs in one place, e.g., excursions and rentals. On Yara Beach, users are able to book a place to stay in the Dominican Republic as well as excursions before or during their holidays, all on the same platform.
<br>

### Project Goals
The goals of this project are to
- Make Yarabeach a global outreach.
- ability to optimise (time, expenses , human labour, infrastructure, and more) for Yarabeach.
- We get a higher margin because it is our own platform and we do not have to pay for a percentage, e.g., at Arbnb or Booking.com.
- ability to catch a customer in its natural habitat and communicate with the customer directly without restriction.
- Getting international customers
- personalization of the buying experience,
- A catalogue of rentals and excursions
- reviews and ratings for rentals and excursions, which determine what the customer likes and dislikes.
- Make Yarabeach brand recognition international.
- Have the visitors contact us for any queries.

<br>

##### back to [top](#table-of-contents)

---

### User Stories

#### Prospective User

I am a future Yarabeach site member  I want to be able to:

- Immediately comprehend the purpose behind the Yarabeach site.
- Easily see what products are available.
- Search for specific excursions and rentals filtered by newest, oldest, price range from low to high, and high to low,
- Easily filter in rental app by rental type: Room, House and villa.
- Have a navigation bar where I can directly type in the product I'm looking for and it will immediately appear.
- I should be able to navigate to different apps easily.
- If I am in a certain app, I should be able to see the title of the app so I can see where I am.
- See all related images of excursions or rentals related to the app.
- See more details once I click on the rentals or excursions.
- Be able to read a well-documented description of each product.
- Read excursion or rental reviews.
- Add products to my shopping cart with ease.
- Be presented with a constant visual reminder of my shopping cart total and the number of items already added.
- Be able to edit my shopping cart, increasing or decreasing the number of children and adults going on an excursion or rental, updating the date that has been selected or deleting it altogether, at will.
- Pay for my items using a secure credit card payment system.
- I immediately receive visual feedback when my payment has been accepted.
- Receive a detailed email confirming my purchase and order number so I can easily print it and show it on arrival.
- Easily locate any social media accounts connected to the site.
- Navigate through the site with ease.
- Easily register to become a site member.
- Easily get in contact with Yarabeach if I have any questions.


#### Existing User

I am an existing Yarabeach site member. I want to be able to:
- Log in to the site.
- Navigate through the site with ease.
- Log out of the site.
- Reset my password securely.
- Add items to my shopping cart with ease.
- Be able to edit my shopping cart, increasing or decreasing the number of children and adults going on an excursion or rental, updating the date that has been selected or deleting it altogether, at will.
- Purchase my desired products using a secure online payment system.
- Be presented with a constant visual reminder of my shopping cart total and the number of items already added.
- Receive a detailed email confirming my purchase and order number so I can easily print it and show it on arrival.
- View my order history.
- View my future orders
- View my order with today's date.
- Search for specific excursions and rentals filtered by newest, oldest, price range from low to high, and high to low,
- In the rental app, be able to easily filter by rental type: Room, House, or Villa.
- Review and rate an excursion or rental previously booked.
- Navigate with ease through the site.
- Contact the Yarabeach owner.
- Read detailed descriptions of excursions and rentals.
- Have a navigation bar where I can directly type in the product I'm looking for and it will immediately appear.

#### Site Owner

As the owner of the Yarabeach website, I would like to:
- Provide users with an effective and user-friendly platform where they can see what products Yara Beach has to offer.
- Provide visitors with visually appealing images of the products on offer.
- Provide visitors with information about the excursions or rentals, such as title, description, price, and a nice form to add to the cart.
- Provide visitors with excursions or rental images , not just one standard image, and the ability to click and navigate through them.
- Provide site users with an easy way to add their desired product to their cart.
- Provide users with a visual representation of their cart total and the number of products already added, visible on all screens in the app.
- Provide users with an updated total when they add or remove products from their cart.
- Provide users with an easy-to-use and secure online payment process.
- Present the reviews and ratings in a visually appealing format.
- Present how many reviews an item has.
- Provide the user with the ability to search for specific excursions and rentals filtered by newest, oldest, price range from low to high, and high to low.
- In the rental app, provide a way to easily filter by rental type: room, house, or villa.
- Provide prospective members with the ability to sign-up easily.
- Provide visible contact details so that all site visitors can contact the Yarabeach with ease.
- Be able to add new excursions or rentals to the website with ease.
- Be able to edit existing excursions or rentals with ease.
- Delete or discontinue excursions or rentals that are no longer available, removing their images and information from the website.
- Be able to activate a product if I want to see it live, or inactive a product for any reason without deleting it.
- Provide site visitors with the ability to edit the shopping cart, increasing or decreasing the number of children and adults going on an excursion or rental, updating the date that has been selected or deleting it altogether, at will.
- Be a ble to have an administrator page where I can add excursions or rentals.
- Be a ble to have an administrator page where I can edit excursions or rentals.
- Be a ble to have an administrator page where I can delete excursions or rentals.
- Be able to have an admin dashboard where we can see the total number of users we have
- Be able to have an admin dashboard where we can see the total number of rental bookings for the day.
- Be able to have an admin dashboard where we can see the total number of excursion bookings for the day.
- In the dashboard, be able to have a description of the excursions bookings of the day. so we can prepare for their arrival.
- In the dashboard, be able to see a description of the rental bookings for the day. so we can prepare for their arrival.
- In the dashboard,  be able to see the future excursion bookings.
- In the dashboard,  be able to see the previous excursion bookings.
- In the dashboard,  be able to see the future rental bookings.
- In the dashboard,  be able to see the previous rental bookings.
- In the excursions and rentals admin list, they show a link where we can go directly and see the product.
- Have a beautiful CKeditor that we can easily add a description of the product to in admin.
- Have the ability to add and see more images on edit admin.
- Have the ability to see the status of the product on the excursion and rental list.
- Have the ability to see the user's contact info like email, full name, phone number, and booking number.
- Have easy access to the home customer page and the admin page and vice versa.
- Provide a detailed email confirming the customer's purchase and order number so they can easily print it and show it on arrival.
- Provide the user with the search bar where they can type in any product they wish to see.
- Provide a user with a pagination so that they know where they are and if there are more products.

<br>

##### back to [top](#table-of-contents)

---
## User Centered Design

### 1 Strategy Plane


The User Stories that we just wrote above were used to maintain a focus on user needs and business goals during the design process.


The Yara Beach website is a Business-To-Consumer (B2C) model aiming to provide a beautiful holiday experience, including stays and excursions.


Yara Beach is not exactly a holiday package because you can not buy rentals and excursions under just one price. In the meantime, this sounds beautiful and we will use it in the future. I spoke to Yara, the future owner of this website, and this is what she had to say: "Our aim was never to sell excursions at the same time as rentals. We use booking.com and Airbnb to show our catalogue of rentals, but when customers contact us, they always have queries about excursions. They often ask if we sell any excursions like boogies, the famous Sahona island, etc., so we end up contacting a real excursion company and making very good deals with them for our customers, so they can have all the packages we offer. It is important to say that our own customers have been deceived on the beach by people who were selling them fake excursions. They have informed us about this problem, and this is how we came to the conclusion of offering our customers excursions as well before they arrive. so they will not be deceived anymore."

<br>

##### back to [top](#table-of-contents)

---

### 2 Scope Plane

The key features of the website were developed based on user needs.

Users should be able to do the following on the website:

- Navigate and interact with the site with ease.
- Ensure the interactivity is intuitive.
- Ensure the layout and design are responsive to all media sizes.
- Allow users to create an account, confirm their email address, change their password, -  log in, and log out.
- Contact the store with any queries.
- Easily access the site’s social media channels.
- Be able to type in  search bar any product they wish to see, according to the app.
- In rentals, users should be able to sort by newest, oldest, price low to high, price high to low, all rooms, all apartments, all villas.
- In Excursions, users should be able to sort by newest, oldest,price low to high,price high to low, all rooms, all apartments, all villas.
- The admin user should be able to go from customer page to admin and admin to customer page. 
- A super user should be allowed to see the admin panel.
- An authenticated user or an anonymous user should not be allowed to edit, delete, add products, or even go to admin pages.
- Read a description of the product.
- - See the reviews and rate the product.
- Upload a rental review for a rental they themselves purchased through the site.
- Upload an excursion review for an excursion they themselves purchased through the site.
- Add an excursion to their cart.
- Add a rental to their cart.
- Excursions should be removed from their carts.
- Take the rentals out of their carts.
- Update the excursion cart, e.g., excursion date, adult quantity, child quantity, and automatically update the subtotal price and the total.
- Update the rental cart, e.g., echeck-in,checkout, adult quantity, child quantity, and automatically update the subtotal price and the total.
- Have the link handy if you want to keep shopping. and a link that sends them to checkout if there are items in the cart.
- In rental checkout, users should be able to see a detailed view of the item they are about to be charged for. It should contain the following: the title, subtotal, image of the product, check-in, checkout, how many adults and children, rental type, and the total price.
- In excursion checkout, users should be able to see a detailed view of the item they are about to be charged for. It should contain the following: the title, subtotal, image of the product, excursion date, how many adults and children, rental type, and the total price.
- Next to the product view details of items, there should be a field to enter the user's contact information and a field for payment. There is also a button with the total to pay and process the payment.
- Receive immediate visual feedback that their payment has been processed and their order confirmed, containing the order numbers for every item and the amount paid. We also informed them that we had sent an email with all the booking information and a link to go home.
- Receive an email confirming their order with all the details.
- In the user's profile, they should then be able to go to excursions bookings or rentals bookings to see their order history.
- In order's histoy, they should be able to see today's bookings, future bookings, and previous bookings.

<br>

##### back to [top](#table-of-contents)

---

### 3 Structure Plane

#### Planning
Competitive Yara Beach website research includes
[Airbnb](https://www.airbnb.co.uk/),
[Booking.com](https://www.booking.com/),
[Biator](https://www.viator.com//),
[Everythingpuntacana](https://everythingpuntacana.com/),
[Jackana](https://jackcana.tours/),
revealed structural commonalities that Yarabeach  would be expected to follow in order to create an intuitive shopping experience  for the holiday makers


The most prominent navigation buttons on the mobile navbar on these sites, visible at all times, were the following:
- **site logo**, which operates as a **Home Button**,
- the **dropdown menu toggle**, which reveals and hides the other menu items on mobile.
- the **User Profile icon**, allowing users to **login**/**logout** or **access their account**. View all bookings
- the **Search bar** 
- the **Sort by button**, which does all the filters.
- the **Shopping Cart**. 
- the **Contact**, which contacts the store with any queries.

<br>

##### back to [top](#table-of-contents)

---

#### Existing Features

After identifying the needs of the site's users and after visiting other similar sites, the following website design and features were chosen:

##### Favicon

A **website logo as favicon**, displayed on the web browser's tab,
allows the desktop user to identify the website by sight.

##### back to [top](#table-of-contents)
---

##### Title

The **Title**, displayed on the web browser's tab at all times,
contains the business's title.

--- 

##### Navbar
The navbar contains all the links to navigate through the pages.
The **home page** navbar contains the **excursions** app link, the **rental** app link, a user dropdown button, and a contact link.
The **rental** page navbar contains the links back to the **home page**, sort by **dropdown for rentals**, a user dropdown button, contact link, and a search bar with a button to the right.
The **excursion** page navbar contains the link back to the home app, sort by **dropdown for excursions**, a user dropdown button, a contact link, and a search bar with a button to the right.


- The **Account user icon with the user name** opens a dropdown menu with links related to what the user's status is. For instance, anonymous user, authenticated user, and superuser.

<br>

| Logged-Out User | Logged-In User     | Superuser       |
| :-------------- | :-------------     | :-----------    |
| Sign in         |    Logout          | Logout          |
| Register        | change Password    | change Password |
|                 | Excursions Bookings| Admin Board     |
|                 | Rentals Bookings   |                 |


##### back to [top](#table-of-contents)

---

##### Django Messages

**Dajngo message** have been used throughout the site to display
alert messages to the user, to provide feedback and to assist them in
achieving their aims. These messages are color-coded using bootstrap alert classes for ease of understanding, in red for error messages, and green for success messages. 

##### back to [top](#table-of-contents)

---

##### Pagination Links


**Pagination** has been added to the 'Excursion' and 'Rental' pages because the amount of content on these pages varies greatly from request to request.
The items returned are broken into discrete pages which can be accessed using the pagination links displayed at the bottom of the subset being displayed. 
The left-angle character brings the user to the 'previous page'; 
page numbers allow users to jump to a numbered page; and the right-angle character links to the 'next page' in the series. 
The number of links rendered has been capped at three, either side of the current page. To make the user's current position explicit, the current page link is styled as bootstrap default pagination with a square blue background and white number.

<br>

##### back to [top](#table-of-contents)

---

##### Excursion Cards

The excursion cards are very modern, with a square round and a border radious around the image. At the button of the image there is the title, which all has the same side. At the button of the title there are stars representing the ratings, with the number of reviews next to it. Finally, at the button of the stars, the price of the excursions.

##### Rental Cards

The rental cards are very modern  with a square round and a border radious around the image. At the button of the image there is the title, which all has the same side. and at the end of the title there is a **badge** showing the type of rental: **Villa**, **Rooms**, or **Apartment** At the button of the badge there are stars representing the ratings, with the number of reviews next to them. Finally, at the button of the stars, the price of the rental.

##### back to [top](#table-of-contents)

---

##### footer
The footer is statically positioned at the bottom of the page. Similar to the header, the footer's content stays in line when the content exceeds the viewport of the device. The footer contains a Facebook link for the site, as well as an Instagram link, a Twitter link, and also a TikiTok link.

##### back to [top](#table-of-contents)

---
##### Home page features

The home page first displays  navigation bar with a beautiful logo of Yara Beach to the left and all the links to the right. At the bottom of the navbar, there is a carousel presenting different images, and at the same time, it has letters actively with the effect of typing in order to inform the user about Yarara Beach excursions and rentals.
At the bottom of the carousel, the home page has two sections full of cards. One section has four card excursions, and at the bottom of the cards there is a button with links directing the users to view all the excursions and potentially book one. In the second section, there is another link, but this time it sends the user to all rentals.
At the bottom of the page, we found the footer. The page is very responsive when it comes to different devices. It is composed of 4 cards vertically if it's a large device like a monitor or computer, and if it's a tablet device, it has 3 cards. A mini table has 2 cards, and a mobile of 750px down the home page just displays 1 card.

##### back to [top](#table-of-contents)

---

##### Contact Page Features
The contact page contains a header title, a sentence encouraging the user to email the administrator, 3 text inputs, and a big textarea. Also, in the right corner, there is a button with the value **submit** continuously **flashing**. The footer is at the button and the navbar is at the top.

##### back to [top](#table-of-contents)

---

##### Rental page app features
The rental page app has a title to let the user know where they are located. At the top of the title, we found the rental navbar containing the all-time visible cart with the current values. On the right-hand side, we found a search bar with a button. The navbar contains a sort by that filters by newest, oldest, price low to high, price high to low, all rooms, all apartments, and all villas. After the title, we have all the cards belonging to rentals. After the cards, we have the pagination and the footer at the bottom.

##### back to [top](#table-of-contents)

---
##### Excursion page app features
The excursion page app has a title to let the user know where they are located. At the top of the title, we found the excursion navbar containing the all-time visible cart with the current values. On the right-hand side, we found a search bar with a button. The navbar contains a sort by that filters by newest, oldest, price low to high, and price high to low. After the title, we have all the cards belonging to excursions. After the cards, we have the pagination and the footer at the bottom.

##### back to [top](#table-of-contents)

---

##### Login page features
The logging or sign-in page contains an image stating "Sign in with Google." At the bottom of the Google sign-in image is a title saying "sign in with a form". At the bottom of the sign in title form we have 2 fields: one for the user name and another for the password. A radio input with a paragraph saying " remember me". After that, there is a button to submit the form  and below that there are two paragraphs. One says, "Don't have an account? sign up, while the other says "Forgot your password ? Reset Password".

##### back to [top](#table-of-contents)

---

##### Register page feature

The signup page contains a big title saying "Register Account." At the bottom of the title, there are five fields input: two for email and confirming the email, one for username, and two for a password and confirming the password. Then there is a button to submit the form and a paragraph saying "Already have an account? "Sign in."

##### back to [top](#table-of-contents)

---

##### back to [top](#table-of-contents)

#####  Product Detail Page Features

The **excursion** detail page has the excursion navbar described above, and a big title of the excursion . Then on desktop, it is divided into two sides, one for the images  that is the left side) and the other for a form to the right. Below the image, there are many other images that the user can click to view on the main image. It has arrows that move to the left or the right so the user can see the images that are hidden. The form has the price on the top. Then there are four inputs: one for the date, one for adults with how many adults are going on the excursions, one for how many children are going on the excursions, and one for the location that they want to choose. Then we have 2 buttons: a left-side button that tells the customers that they can keep shopping and the other side button that tells them to add to the cart. At the bottom of the form and images, there is a big title called "Overview," and below you can view the details of the item. The customer reviews are listed below the summary title, along with the number of reviews for the item. There is also the ability to create a new review if it is an authenticated user or to sign up if it is not . The review appears in a nice standard format . The review includes the name of the user who posted the review , the rating of stars given, the date that it was posted and the review.

--- 
The **rental** details page is very similar to the excursion page. The only difference is that in rental, the price does not say price but night. We also have the check-in field and checkout field.

---

##### back to [top](#table-of-contents)

#####  Cart Page Features

The cart page feature has 2 horizontal rule lines and in the middle a big title saying "Shopping Cart" with a cart icon. If the cart is empty, then I display a message saying that the cart is empty. and provide a button to go shopping based on where I am in the app. If I am in a rental, then the link will take me to the rental, and if I am in the excursion app, then it will take me to the excursion app. If the cart is not empty and we are in the excursion app, then we have 2 cards, one to the right, which show the summary and 2 buttons, one to go to checkout and the other one to keep shopping. The cart to the left shows the item details. If it is the excursion app, then it shows the description, excursion date, quantity, pickup, price, and subtotal. with an update button and a delete button. If it is a rental, we have a description, check-in date, checkout, how many days, quantity for adults and quantity for children, price subtotal, and the update button and the delete button. We can also edit all the items in the cart


---

##### back to [top](#table-of-contents)

#####  Checkout Page Features

The checkout page is divided into 2 parts: A cart to the right with the details of the item contains the title, number of items, subtotal, image of the item, number of adults, number of children, date of the excusion, and the total price to pay. On the left we have 3 fields: at the top of the left side we have contact information like phone number and full name; below there is the payment input field, coming directly from Stripe; and a button to submit the page. If we are in the rental checkout, then we have the check-in date and checkout date, and the type of rental.

---

##### back to [top](#table-of-contents)


##### Checkout Success Page Features

On the checkout success page, use a cart with the site colour badge at the top and a tick icon. At the button of the badge is a message telling the user that the payment has been successful, the booking number, the total amount paid, and a message telling them to go to email so they can see the order details. and last, a button to go home.

---

##### back to [top](#table-of-contents)

##### Change Password page feature

The change password page has three fields: one is for the current password, two for the new password. a title indicating that it is a change password form and a button to submit the form saying change password.

---

##### back to [top](#table-of-contents)

##### customer Excursion Bookings page features

The customer's excursion booking page has 3 main sections. One section is for today's bookings, another one is for future bookings, and the last one is for previous bookings. It contains a table with all the details of the excursions.

##### customer Rental Bookings page features

The customer's rental booking page has 3 main sections. One section is for today's bookings, another one is for future bookings, and the last one is for previous bookings. It contains a table with all the details of the rentals.

---

##### back to [top](#table-of-contents)

##### Admin navbar

The admin navbar does not have much different from the customer navbar, but the only differences are in the colour of the navbar, a dashbard link, excursion link, and rentals containing the crud functionality and a link to access the customer page.


##### Administrator dashboard page features
The administrator dashboard page It has an admin navbar, a big title informing the user that the page is the admin,
Below the title, we have 3 colour cards. The left-side card has the total number of users; the middle one has the total rental bookings for the day; and the right side has the total excursion bookings for the day . Below the colour cards, there can be today's rental and excursion bookings; then we have the excursion and rental future bookings; and last, we have the excursion and rental previous bookings. and on the button we can find the footer.


##### Administrator Excursion page features

The administrator excursion page has the admin navbar, below has the h2 title with a button in order to add more excursions. There are tables with the excursions that already exist. Those table buttons contain edit and delete functionality. The table also contains the status of the item, the image, the date created, the title (which links to excursion details), and the price of the excursion. Then we have the footer below.

#####  Administrator Rental page features

The administrator rental page has the admin navbar. Below it has the h2 title with a button in order to add more rentals. There are tables with the rentals that already exist. Those table buttons contain edit and delete functionality. The table also contains the status of the item, the type of rental, the image, the date created, the title (which links to excursion details), and the price of the excursion. Then we have the footer below.


#####  Administrator add rental page features

The Administrator adds the rental page has the admin navbar, a h2 title, Below there are 7 fields: title field, price field, main image field, image name field, a beautiful full CKeditor, ACCOM type field, Status dropdown field, an add rental button, and a cancel button to go back to the admin rental page.

#####  Administrator edit rental page features

The Administrator edits the rental page. It has the admin navbar, a h2 title, and 9 fields: title field, price field, main image field with the current field and the chooses image field, image name field, a beautiful full CKeditor, ACCOM type field, and a status dropdown field. It also has an image field in order to add more images to the rentals, a rental button to submit it, and a cancel button to go back to the admin rental page.

#####  Administrator delete rental page features
The administrator deletes  rental page has a card confirming if we really want to delete the item. It has two buttons, one for deleting and another for cancelling the deletion intent.

---

##### back to [top](#table-of-contents)

#####  Administrator add excursion page features

The Administrator adds the excursion page has the admin navbar, a h2 title, Below there are 6 fields: title field, price field, main image field, image name field, a beautiful full CKeditor, an excursion button to submit the form, and a cancel button to go back to the admin excursion page.

#####  Administrator edit excursion page features

The Administrator edits the excursion page. It has the admin navbar, a h2 title, and 8 fields: title field, price field, main image field with the current field and the chooses image field, image name field, a beautiful full CKeditor, and a status dropdown field. It also has an image field in order to add more images to the excursion, an excursion button to submit it, and a cancel button to go back to the admin excursion page.

#####  Administrator delete excursion page features

The administrator deletes  excursion page has a card confirming if we really want to delete the item. It has two buttons, one for deleting and another for cancelling the deletion intent.

---

##### back to [top](#table-of-contents)

##### 404 and 500 Page Features
Once the user navigates to a wrong path inside the Yara Beach site, or the user experience a 500 error message it will be redirected to a beautiful image which contains a button to return home safely.

---

##### back to [top](#table-of-contents)


#####  Features Left to Implement

- Add a graph to the administrator so they know how much money they make every month, how much money they made last year, and the next year's predicted revenue.
- On the home page, he ranks first for excursions and fourth for rentals.
- On the contact page, add a WhatsApp contact link so customers can contact or message the administrator directly.
- Give the user the ability to update their profile, e.g., adding images, changing age, etc.
- Give the admin a separate form so they can add different types of employee users, like editors, other superusers, etc.



---

##### back to [top](#table-of-contents)

### 4 Skeleton Plane

The UI wireframing tool, [Balsamiq](https://balsamiq.com/) was used to create wireframes.
for each page as they will appear on mobile, tablet, and desktop devices.
The main content areas on each page were designed for functionality and consistency.

The site has been designed to accommodate the growing number of holidaymakers who use mobile devices.
uses responsive web design. Yara Beach was designed with a mobile-first design.
beginning with the product design from the mobile end, which has more
and then expanding its features to create a tablet and desktop version.


---

##### back to [top](#table-of-contents)

#### Wireframes

- [Home Page](documentation/wireframes/home.png)
  ![alt text](documentation/wireframes/home.png "Home Page.")

- [Login Page](documentation/wireframes/sign-in.png)
  ![alt text](documentation/wireframes/sign-in.png "Login Page.")

- [Registration Page](documentation/wireframes/register-account.png)
  ![alt text](documentation/wireframes/register-account.png "Registration Page.")

- [Contact Page](documentation/wireframes/contact.png)
  ![alt text](documentation/wireframes/contact.png "Contact Page.")

- [Add Rental Page](documentation/wireframes/add-rental.png)
  ![alt text](documentation/wireframes/add-rental.png "Add Rental Page")

- [Add Excursion Page](documentation/wireframes/add-excursion.png)
  ![alt text](documentation/wireframes/add-excursion.png "Add Excursion Page")

- [Checkout Page](documentation/wireframes/checkout-page.png)
  ![alt text](documentation/wireframes/checkout-page.png "Checkout Page")

- [Shoopping Cart Page](documentation/wireframes/shoopping-cart-page.png)
  ![alt text](documentation/wireframes/shoopping-cart-page.png "Shoopping Cart Page")

- [Comfirm Delete Item Page](documentation/wireframes/comfirm-delete-item.png)
  ![alt text](documentation/wireframes/comfirm-delete-item.png "Comfirm Delete Item Page")

- [Customer Booking Excursions Page](documentation/wireframes/customer-booking-excursions.png)
  ![alt text](documentation/wireframes/customer-booking-excursions.png "Customer Booking Excursions Page")


- [Customer Booking Rental Page](documentation/wireframes/customer-booking-rentals.png)
  ![alt text](documentation/wireframes/customer-booking-rentals.png "Customer Booking Rental Page")


- [Dashboard Admin Page](documentation/wireframes/dashboard-admin.png)
  ![alt text](documentation/wireframes/dashboard-admin.png "Dashboard Admin Page")

- [Dashboard Admin Page](documentation/wireframes/dashboard-admin.png)
  ![alt text](documentation/wireframes/dashboard-admin.png "Dashboard Admin Page")

- [Dashboard Admin Page](documentation/wireframes/dashboard-admin.png)
  ![alt text](documentation/wireframes/dashboard-admin.png "Dashboard Admin Page")

- [Edit Excursion Page](documentation/wireframes/edit-excursion.png)
  ![alt text](documentation/wireframes/edit-excursion.png "Edit Excursion Page")


- [Edit Rental Page](documentation/wireframes/edit-rental.png)
  ![alt text](documentation/wireframes/edit-rental.png "Edit Rental Page")

- [Edit Rental Page](documentation/wireframes/edit-rental.png)
  ![alt text](documentation/wireframes/edit-rental.png "Edit Rental Page")

- [Excursion Admin Page](documentation/wireframes/excursion-admin.png)
  ![alt text](documentation/wireframes/excursion-admin.png "Excursion Admin Page")

- [Rental Admin Page](documentation/wireframes/rental-admin.png)
  ![alt text](documentation/wireframes/rental-admin.png "Rental Admin Page")

- [Success Checkout Page](documentation/wireframes/success-checkout-page.png)
  ![alt text](documentation/wireframes/success-checkout-page.png "Success Checkout Page")

- [Reset Password Page](documentation/wireframes/reset-password.png)
  ![alt text](documentation/wireframes/reset-password.png "Reset Password Page")

- [Rental Page](documentation/wireframes/rental.png)
  ![alt text](documentation/wireframes/rental.png "Rental Page")


- [Excursions Page](documentation/wireframes/excursions.png)
  ![alt text](documentation/wireframes/excursions.png "Excursions Page")

<br>

##### back to [top](#table-of-contents)

---

### 5 Surface Plane

#### Design

The target audience for the Yarabeach website is holidaymakers of all ages. However, the project design is a combination of my own design implemented with the bootstrap framework. The colour makes the website stand out and gives a clear meaning of what the website is about, as it is commonly found on websites related to tropical weather and vacations. Its goal is to be captivating, alluring, and cohesive.To give those families the sense that the holiday is right next door, we have chosen orange because (orange-pantone) the colour is bright and vibrant and fun, bursting with youthfulness, energy, and happiness. They inspire creativity and uplift people's moods.

<br>

##### back to [top](#table-of-contents)

---

#### Colour Scheme

![alt text](documentation/readme-images/Yara-beach-colors.png "Yara Beach Main colour palette.")

The **orange pantone** is the main colour of the Yara Beach site. As previously described, the colour is bright and vibrant and fun, bursting with youthfulness, energy, and happiness. They inspire creativity and uplift people's moods. This colour is used in the logo, all the buttons, contact title and paragraph. The second colour most often used on the site is the **culture color**. It is basically a light grey. This colour represents neutrality and balance, and it is used for the body background of the site. The third most used colour is **Gunmetal**. This colour is serious, given the depth of its shades of grey and blue. Gunmetal brings a certain level of authority and timelessness to Yara Beach designs. It is used for the footer and the administrator navbar. The fourth most used colour on the site is the **white colour**, which represents purity, simplicity, and cleanliness. This colour is used as the colour of the test when it is on a button. in the text of the footer and in the table headers.


##### back to [top](#table-of-contents)

---

During the development process, this colour palette was extended in order to provide visual contrast and interest, as well as for functional purposes. For example, the colour red was used to draw attention with an error message, as well as the colour green with success messages.

![alt text](documentation/readme-images/yarabeach-second-palettes-colors.png "Yara Beach second colour palette.")


##### Logo design

The logo of the site is located on the left side of the navbar in the bootstrap standard place. The logo is the name of the owner with the word beach and a beautiful image of a palm tree. People mostly go to the Dominican Republic because of the beach and its beautiful landscape composed of lots of palm trees, so by incorporating both the name of the beach and palm trees, the customers can understand at a glance that it is about holidays, which also makes the brand well known by its users.

![alt text](documentation/readme-images/Yara-logo.png "Yara beach Logo.")
<sub>_Created using_ [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop/landpa.html?gclid=CjwKCAjwwL6aBhBlEiwADycBIKPGhQtahSxttLjZVTUJ7djn4sFEDI1p6gUoIk5PJzHRyigcU7Rm-BoCQtcQAvD_BwE&mv=search&mv=search&sdid=GVTYXZY8&ef_id=CjwKCAjwwL6aBhBlEiwADycBIKPGhQtahSxttLjZVTUJ7djn4sFEDI1p6gUoIk5PJzHRyigcU7Rm-BoCQtcQAvD_BwE:G:s&s_kwcid=AL!3085!3!594259336243!e!!g!!adobe%20photoshop!17011954559!138864791987/)</sub>

#### Icons
Icons were used within the site in order to help the user understand the content more easily.
They were taken from [Font Awesome](https://fontawesome.com/) and chosen to be self-explanatory.


#### Typography
After an intensive search for the right font, I encountered Montserrat, the most commonly used font for holiday websites. This font I have used to be a company with Georgia and Serif in case Montserrat does not load. I have used this font for the body of the website.

<br>

##### back to [top](#table-of-contents)

---

### Development

## Information Architecture

A relational database was used to store the collection of data for this project. [SQLite](https://www.sqlite.org/) was used at the start of development, but I wanted to dig deeper into the tables of the DB, so I decided to go for posgreSQL in local development as well. Then I used Heroku [PostgreSQL] (https://www.postgresql.org/) in production, and a relational database structure was suitable for this project as it allowed multiple tables to be created, with data easily interconnected through the use of foreign keys.

Note: The .sqlite3 development database file, was added to the .gitignore file before the initial commit in order to stop it being pushed to GitHub.



### Data Schema


The following Entity Relationship Diagram, created using [drawsql](https://drawsql.app/),
illustrates the relationships between the models.

![alt text](documentation/readme-images/data_schema.png "Yara beach DB Diagram.")

##### back to [top](#table-of-contents)

---

### Data Models

The Yara beach website relies on 9 database models and six apps:



#### User Model

Django User model is a part of Django’s authentication system
Django.contrib.auth.models.
Information about its fields, attributes and methods are
located [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/).

| Title         | Key in db  | Data Type     | Type Validation                         |
| :------------ | :--------- | :------------ | :-------------------------------------- |
| User ID       | id         | AutoField     | primary_key=True                        |
| Username      | username   | CharField     | max_length=150, null=False, blank=False |
| First Name    | first_name | CharField     | max_length=30                           |
| Last Name     | last_name  | CharField     | max_length=30                           |
| Email Address | email      | CharField     |                                         |
| Password      | password   | PasswordField | null=False, blank=False                 |

<br>


#### Excursions Model

| Title                   | Key in db               | Data Type    | Type Validation                                             |
| :---------------------- | :---------------------- | :----------- | :-----------------------------------------------------------|
| Excursions ID           | id                      | AutoField             | primary_key=True                                   |
| User                    | user                    | ForeignKey            | [ref: - User.id]                                   |
| Price                   | price                   | DecimalField          | max_digits=7, decimal_places=2, null=False,        |
| Main Image              | image                   | ImageField            | max_length=80, null=True, blank=True               |
| Image Name              | image_name              | CharField             | max_length=201, null=True, blank=True              |
| Description             | description             | RichTextUploadingField| null=False, blank=False,                           |
| Date Created            | date_created            | DateTimeField         | auto_now_add=True, null=True                       |
| Status                  | status                  | CharField             | choices=CHOICES, default='Inactive', max_length=20 |

<br>



#### Photos Model

| Title                   | Key in db               | Data Type    | Type Validation                                             |
| :---------------------- | :---------------------- | :----------- | :-----------------------------------------------------------|
| Photos ID               | id                      | AutoField             | primary_key=True                                   |
| Excursion               | id                      | ForeignKey            | [ref: - Excursions.id]                             |
| Main Image              | image                   | ImageField            | max_length=80, null=True, blank=True               |
| Image Name              | image_name              | CharField             | max_length=201, null=True, blank=True              |

<br>

#### Review Model

| Title                   | Key in db               | Data Type    | Type Validation                                             |
| :---------------------- | :---------------------- | :----------- | :-----------------------------------------------------------|
| Review ID               | id                      | AutoField             | primary_key=True                                   |
| Title                   | title                   | CharField             | max_length=255, null=True, blank=True,             |
| Rating                  | rating                  | IntegerField          | max_length=80, null=True, blank=True               |
| Rental                  | id                      | ForeignKey            | [ref: - Rentals.id]                                |


#### Rentals Model

| Title                   | Key in db               | Data Type    | Type Validation                                             |
| :---------------------- | :---------------------- | :----------- | :---------------------------------------------------------- |
| Rentals ID              | id                      | AutoField             | primary_key=True                                   |
| User                    | user                    | ForeignKey            | [ref: - User.id]                                   |
| Price                   | price                   | DecimalField          | max_digits=7, decimal_places=2, null=False,        |
| Main Image              | image                   | ImageField            | max_length=80, null=True, blank=True               |
| Image Name              | image_name              | CharField             | max_length=201, null=True, blank=True              |
| Description             | description             | RichTextUploadingField| null=False, blank=False,                           |
| Date Created            | date_created            | DateTimeField         | auto_now_add=True, null=True                       |
| ACCOM Type              |ACCOM_type               | CharField             | choices=CHOICES, default='Room', max_length=20     |
| Status                  | status                  | CharField             | choices=CHOICES, default='Inactive', max_length=20 |

<br>

#### Photos Model

| Title                   | Key in db               | Data Type    | Type Validation                                             |
| :---------------------- | :---------------------- | :----------- | :-----------------------------------------------------------|
| Photos ID               | id                      | AutoField             | primary_key=True                                   |
| Excursion               | id                      | ForeignKey            | [ref: - Rentals.id]                             |
| Main Image              | image                   | ImageField            | max_length=80, null=True, blank=True               |
| Image Name              | image_name              | CharField             | max_length=201, null=True, blank=True              |

<br>

#### Review Model

| Title                   | Key in db               | Data Type    | Type Validation                                             |
| :---------------------- | :---------------------- | :----------- | :-----------------------------------------------------------|
| Review ID               | id                      | AutoField             | primary_key=True                                   |
| Title                   | title                   | CharField             | max_length=255, null=True, blank=True,             |
| Rating                  | rating                  | IntegerField          | max_length=80, null=True, blank=True               |
| Rental                  | id                      | ForeignKey            | [ref: - Rentals.id]                                |


##### back to [top](#table-of-contents)

---


## Technologies Used

- Languages:

  - [HTML5](http://en.wikipedia.org/wiki/HTML5). Used to create the structure of the Yara Beach website and the custom 404 and 500 pages.
  - [CSS3](http://en.wikipedia.org/wiki/CSS). Used to add style to the website.
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript). Used to create the dynamic, interactive elements of the website such as the Bootstrap accordions.
  - [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>). Used to create and run the web application.

- Websites

  - [Am I Responsive](http://ami.responsivedesign.is/). Used to create the mock-up image showing the site as it would behave when viewed on desktop, mobile and tablet devices.
  - [AWS](https://aws.amazon.com/). Amazon Web Services - Simple Storage Service (S3) was used to host the media and static files.
  - [Code Beautify](https://codebeautify.org/markdown-formatter). Used to format the README.md and TESTING.md markdown files.
  - [Code Institute](https://codeinstitute.net/). Used to review concepts covered in preceding modules and walk-through projects.
  - [Coolors](https://coolors.co/ffbe0b-fb5607-ff006e-8338ec-3a86ff). Used to analyse the site logo to isolate the colours within and to construct the colour palette for the site.
  - [Drawsql](https://drawsql.app/). Used to create the Entity Relationship diagram used in the README.md file.
  - [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools). Used to test the responsiveness of the site.
  - [Font Awesome](https://fontawesome.com/). Used to source the free icons that were used for the social media links in the footer and for the profile, home, review, edit, delete, buy, reset, clear and search buttons.
  - [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools). Used throughout the project to test the responsiveness of elements, to target and apply CSS styles during the design phase and to test the site's performance once built.
  - [Google Fonts](https://fonts.google.com/). Used to choose and source the font used in the body of the site.
  - [Github](https://github.com/). Used as a respository for the different versions of the build produced throughout development.
  - [Gitpod](https://www.gitpod.io/). An online IDE used to build and develop the website.
  - [Heroku](https://www.heroku.com/). The cloud platform used to host the deployed site.
  - [jQuery](https://jquery.com/). This JavaScript library was used to traverse the DOM and used for dynamic event handling.
  - [PEP8online](http://pep8online.com/). Used to check the python files for PEP8 compliance.
  - [RandomKeyGen](https://randomkeygen.com/). Used to generate the Secret Keys.
  - [Slack](https://slack.com/intl/en-ie/). Used during development and testing to find the solutions to problems enountered.
  - [Stack Overflow](https://stackoverflow.com/). Used to search for the answers to problems encountered during the development and testing of the website.
  - [Stripe](http://www.stripe.com). Payment processing platform used to validate and authenticate payments and, potentially, to receive payments made over the internet.
  - [TinyPNG](https://tinypng.com/). Used to compress the site logos and background-images to improve performance results.
  - [Unsplash](https://www.unsplash.com). Used to source the non-product site images.
  - [Vecteezy](https://www.vecteezy.com). Used for the custom 404 and 500 page backgrounds.
  - [WebFormatter](https://webformatter.com/). Used to format the CSS, JavaScript and HTML files before submission.
  - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). Used to validate the CSS files.
  - [W3C HTML Validation Service](https://validator.w3.org/). Used to validate the HTML files.
  - [Adobe Photoshop](https://www.adobe.com/). was used for creating the Yara Beach logo and the hero image for the README.md file.

- Frameworks

  - [Bootstrap](https://getbootstrap.com/). Used to structure the website layout and ensure that it was responsive on all devices.
  - [Django](https://www.djangoproject.com/). Python web framework used to create the web app.

- Databases

  - [SQLite](https://www.sqlite.org/). Used during development to host the collection of data.
  - [Heroku Postgres](https://www.heroku.com/postgres). Used during production to store the product information, user information, and other data.
- Apps:
  - [Balsamiq](https://balsamiq.com/). Used to create the project wireframes.
  - [Inkscape](https://inkscape.org/). Used to edit the Vecteezy svgs.
  - [Microsoft Excel](https://www.microsoft.com/en-ie/microsoft-365/excel). Used to create the fixture files and convert them to .csv files. Also used to create the testing spreadsheets.
  - [Microsoft Excel](https://www.microsoft.com/en-ie/microsoft-365/excel). Used to create the fixture files and convert them to .csv files. Also used to create the testing spreadsheets.

- Other Tools and Libraries:
  - [Black](https://pypi.org/project/black/). Used to format the python code.
  - [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). A Python Software Development Kit (SDK) for AWS.
    Used to provide direct CRUD functionality of AWS resources from the Python scripts.
  - [Coverage](https://pypi.org/project/coverage/). Used to measure code coverage during automated-test execution.
  - [Dj_database_url](https://pypi.org/project/dj-database-url/) used to configure the Django application, swapping
    the local database with one managed by a third party without changing the app’s code.
  - [Gunicorn](https://gunicorn.org/). Used as a Web Server Gateway Interface (WSGI).
  - [Pipenv](https://pypi.org/project/pipenv/). Used to install Python packages.
  - [Pillow](https://pillow.readthedocs.io/en/stable/). Python Imaging Library (PIL), used to add image processing
    capabilites such as opening, manipulating, and saving images.
  - [Psycopg2](https://pypi.org/project/psycopg2/). Python PostgreSQL database adapter.
<br>

##### back to [top](#table-of-contents)

---

## Testing


## Testing

A detailed description of the testing process and the results achieved can be found in the [TESTING.md](TESTING.md) document.

<br>

##### back to [top](#table-of-contents)

---

## Deployment

### Local Deployment

To run this project on your own Integrated Development Environment (IDE) ensure that the
following are installed on your machine:

- Pipenv
- Python 3
- Git

- Download postgresq (Refer to the [postgresq](https://www.postgresql.org/download) for more help.) or just use the default db.sqlite3

Accounts with the following services are also used within this project:

- [Stripe](https://www.stripe.com)
- [AWS](https://aws.amazon.com/)
- [Gmail](https://mail.google.com/)


<br>

### To clone the repository:

1. Log in to Github.

2. Navigate to the main page of the repository.

3. Select the Code button from the navigation bar below the repository title.

![alt text](documentation/readme-images/clone-or-download-menu.png "Clone or Download Menu in GitHub.")

<br>

4. Under the heading Clone select 'HTTPS'.

5. Click the image of a clipboard to the right of the URL in order to copy the address.

6. Open a terminal window in your selected IDE.

7. Navigate to the desired directory in which you wish to place the cloned directory.

8. Type git clone, space, and then paste the copied URL.


```
https://github.com/Gersondelacruzdeveloper/yara-beach.git
```

9. Press 'Enter' to create the clone.

(Alternative you can select "Download ZIP" from the dropdown menu, extract the zip file to your chosen folder and use your IDE of choice to access it.)

<br>

10. Within your terminal window install the required dependencies needed to run the application using the following command:

```
$ pip3 install -r requirements.txt
```
## or

```
$ pipenv install -r requirements.txt
```

11. Within your IDE create a file to hold your environment variables and call it env.py or set the variables
    within your IDE settings if that is supported.


```
ALLOWED_HOSTS = env.list("ALLOWED_HOST")
```

| Key               | Value                        |
| ----------------- | ---------------------------- |
| DEBUG             | True                         |
| DEPLOYED          | False                        |
| STRIPE_PUBLIC_KEY | <YOUR_STRIPE_PUBLIC_KEY>     |
| STRIPE_SECRET_KEY | <YOUR_STRIPE_SECRET_KEY>     |
| ALLOWED_HOSTS     | <ALLOWED_HOSTS>              |
| SECRET_KEY        | <DJANGO_SECRET_KEY>          |
| STRIPE_CURRENCY   | <STRIPE_CURRENCY>            |

If using env.py, add it to your .gitignore file to ensure this file is never pushed to GitHub.


12. Migrate the models and create the database by typing the following commands into the terminal:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

13. Create a superuser for accessing the Django admin view by typing the following
    command and then inputting an email address, username and password.


```
python3 manage.py createsuperuser
```

16. You will then be able to run the app locally by typing

```
python3 manage.py runserver
```


17. You can access the Admin interface by adding '/admin' to the end of the url
    and logging in with the credentials of the Superuser that you created.

<br>

##### back to [top](#table-of-contents)

---

<br>


## Heroku Deployment

Before creating the Heroku application:

Before creating the Heroku application:

1. Within your IDE, create a requirements.txt file that contains the applications and dependencies required to run the app using the command:

```
pip3 freeze --local > requirements.txt
```

2. Create a Procfile, which specifies the commands that are executed by the app on startup:

```
echo web: python app.py > Procfile
```

3. Add the new files to the staging area in git and then commit the files to the local repository:

```
git add -A
git commit -m "feat: Add requirements.txt file and Procfile."
```

4.  Upload the local repository content to the remote repository:

```
git push
```

<br>

### Deployment procedure followed:
1. Navigated to the [Heroku](https://www.heroku.com/) site.
2. Logged in to the site.
3. Created a new app on the Heroku website by clicking the "New" button on the dashboard. 
![alt text](documentation/readme-images/heroku-new-app-btn.png "New App button in Heroku.")

<br>

4. Named the Heroku App and set the region to Europe.

5. 'Deploy' was selected from the dashboard of the newly created application.  In the 'Deployment method' section GitHub was selected.
![alt text](documentation/readme-images/heroku-new-app-form.png "Deploy to GitHub in Heroku.")

<br>


5. A new Postgres database was provisioned for the app.  
   This was located by searching for Postgres in the 'Add-ons' search bar on the 'Resources' tab on Heroku,
   ![alt text](documentation/readme-images/heroku-resources-tab.png "Heroku Resources tab.")


<br>


The 'Hobby Dev - Free' plan was chosen for this project.


<br>
![alt text](documentation/readme-images/heroku-postgres-provision-form.png "Postgres provision form on Heroku.")

<br>


6. Set up the new database.

- The PostgreSQL database adapter [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
  was installed.

```
pip3 install psycopg2-binary
```

- The Django utility [dj_database_url](https://pypi.org/project/dj-database-url/) was installed.
  This utilizes the DATABASE_URL environment variable to configure the Django application, swapping
  the local database with one managed by a third party (such as Amazon) without changing the app’s code.

```
pip3 install dj_database_url
```

- In settings.py [dj_database_url](https://pypi.org/project/dj-database-url/) was imported.  
  The default database url was commented out and the Postgres database URL was passed to dj_database_url.

```
{.python3}
import dj_database_url

DATABASES = {
        "default": dj_database_url.parse("<your Postrgres database URL>")
    }
```

- This url can be located under the 'Config Variables' heading on the 'Settings' tab on Heroku.


![alt text](documentation/readme-images/heroku-settings-tab.png "Heroku Settings tab.")



7. Requirements were updated.  
   To make sure that Heroku installed all of the app's requirements, these new dependencies
   were added to the requirements.txt file.

```
pip3 freeze > requirements.txt
```

8. Models were migrated to the new Postgres database.

```
python3 manage.py showmigrations
python3 manage.py migrate
```

9. A superuser, with admin rights, was created.

```
python3 manage.py createsuperuser
```


- An email address, username and password were chosen.

10. Within settings.py the file the new database settings were removed and the original default setting was un-commented.

- This was done so that the database URL did not go into version control.
  An 'if' 'else' block was added to check whether the side was deployed or not If that is the case, as it is when the app is running on Heroku,
  DATABASES points to the Postgres database, otherwise, the app connects to SQLite3 or the local posgresQL

```{.python3}
if DEPLOYED:
    DATABASES = {"default": env.dj_db_url("DATABASE_URL")}
else:
    DATABASES = {
    "default": {
        'ENGINE': env.str("LOCAL_DB_ENGINE"),
        'NAME': env.str("LOCAL_DB_NAME"),
        'USER': env.str("LOCAL_DB_USER"),
        'PASSWORD': env.str("LOCAL_DB_PASSWORD"),
        'HOST': env.str("LOCAL_DB_HOST"),
        'PORT': env.str("LOCAL_DB_PORT"),
    }
}

```

11. [Gunicorn](https://gunicorn.org/), the Python WSGI HTTP Server for UNIX, was installed to act as the webserver.


```
pip3 install gunicorn
```

- This new dependency was added to the requirements.txt file.

```
pip3 freeze > requirements.txt
```


12. The [Procfile](https://devcenter.heroku.com/articles/procfile) was created in the root directory.  
    This file specifies the commands that are executed by the app on startup.
    In this case, create a web dyno which will run [gunicorn](https://gunicorn.org/) and serve the Django app.

```
web: gunicorn config.wsgi --log-file -
```


13. After logging in to Heroku at the command line Collectstatic was temporarily
    disabled so that Heroku did not try to collect static files when the app was deployed.


```
heroku login -i

heroku config:set DISABLE_COLLECTSTATIC=1 --app <app name>
```

14. Within settings.py, the hostname of the Heroku app and the localhost were added
    to the list of allowed hosts.


15. Deployed to Heroku, without any static files.  
    As the Heroku app had been created on the website rather than at the command line, it was necessary
    to initialize the Heroku Git Remote first.


```
heroku git:remote -a <app name>

git push heroku master
```

16. Automatic deployments were set up.

- The 'Deploy' tab was selected on the Heroku dashboard.

- Making sure that the correct GitHub profile was displayed, the Dargan Health Foods repository was entered into the search box.

- When found, the button 'Connect' was clicked.
- Next, 'Enable Automatic Deploys' was selected to ensure that every time code was pushed to GitHub
  it would automatically deploy to Heroku as well.

- Within the 'Deployment method' section GitHub was selected.
  ![alt text](documentation/readme-images/heroku-deploy-connect-to-github.png "Deploy to GitHub in Heroku.")

<br>



17. The configuration variables were set in Heroku within the local environment.

- Within the 'Settings' tab for the app the button 'Reveal Config Vars' was clicked.
- The following configuration variables were added (some information has been redacted for security purposes).
  [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
  was used to generate the secret keys.
  <br>

| Key                     | Value                                        |
| :----------------       | :------------------------------------------- |
| DATABASE_URL            | <YOUR_DATABASE_URL> (Set by Heroku Postgres) |
| STRIPE_PUBLIC_KEY       | <YOUR_STRIPE_PUBLIC_KEY>                     |
| STRIPE_SECRET_KEY       | <YOUR_STRIPE_SECRET_KEY>                     |
| STRIPE_WH_SECRET        | <YOUR_STRIPE_WH_SECRET>                      |
| SECRET_KEY              | <YOUR_SECRET_KEY>                            |
| ALLOWED_HOST            | <ALLOWED_HOST_LIST>                          |
| AWS_ACCESS_KEY_ID       | <AWS_ACCESS_KEY_ID>                          |
| AWS_S3_REGION_NAME      | <AWS_S3_REGION_NAME>                         |
| AWS_SECRET_ACCESS_KEY   | <AWS_SECRET_ACCESS_KEY>                      |
| AWS_STORAGE_BUCKET_NAME | <AWS_STORAGE_BUCKET_NAME>                    |
| DEBUG                   | FALSE                                        |
| DEPLOYED                | TRUE                                         |
| EMAIL_BACKEND           | <EMAIL_BACKEND>                              |
| EMAIL_HOST              | <EMAIL_HOST>                                 |
| EMAIL_HOST_PASSWORD     | <EMAIL_HOST_PASSWORD>                        |
| EMAIL_HOST_USER         | <EMAIL_HOST_USER>                            |
| EMAIL_PORT              | <EMAIL_PORT>                                 |
| EMAIL_USE_TLS           | <EMAIL_USE_TLS>                              |
| STRIPE_CURRENCY         | <STRIPE_CURRENCY>                            |
| EMAIL_HOST_USER         | <EMAIL_HOST_USER>                            |

<br>


<br>

##### back to [top](#table-of-contents)

---

#### Set Up an Amazon Web Services Account

- Amazon Web Services (AWS) Simple Storage Service (S3) was used to store all of the static
  files, JavaScript files, CSS files and product images for the site.

19. An account was created on [AWS](aws.amazon.com).
    This process involved inputting an email, password, username, phone number
    (for verification purposes) and credit card details (for billing).

20. Once signed in, the S3 Services link was located on the AWS Management Console.
    ![alt text](documentation/readme-images/aws-management-console.png "AWS Management Console.")

<br>

##### back to [top](#table-of-contents)

---

#### Set Up the Simple Storage Service Bucket

21. A new Bucket was created to store the files.
    ![alt text](documentation/readme-images/aws-create-bucket.png "AWS S3 Create Bucket.")

<br>

- This bucket was named to match the Heroku app name.
- The closest region was chosen: EU(Ireland) eu-west-1.
- The 'Block all public access' checkbox was unchecked.
- The checkbox to acknowledge that the bucket will be public was selected.
  ![alt text](documentation/readme-images/aws-bucket-public-access-form.png "AWS S3 Bucket Public Access Form.")

<br>


22. Once created the **Bucket 'Properties'** were set.


- Static Website Hosting was turned on.
 ![alt text](documentation/readme-images/aws-bucket-properties-static-website-hosting.png "AWS S3 Bucket Static Website Hosting Properties box.")


<br>

23. **Bucket 'Permissions'** were set up to allow full access to all resources within the bucket.

- The following Cross Origin Resource Settings (CORS) Configuration was used.

```{.python3}
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```


- A Security Policy was created for the Bucket using the AWS S3 Bucket Policy Generator.
  ![alt text](documentation/readme-images/aws-bucket-policy-generator.png "AWS S3 Bucket Policy Generator.")



<br>
- The Access Control List permission was set for 'Everyone', under the 'Public Access 
Section'.


![alt text](documentation/readme-images/aws-bucket-access-control-list.png "AWS S3 Bucket Access Control List.")
<br>



<br>

##### back to [top](#table-of-contents)

---

#### Set up an Identity and Access Management (IAM) Group and User

24. AWS Identity and Access Management (IAM) was used to created a User to access
    the Bucket.

- A new Group called 'manage-dargan-health-foods' was created.
- A Policy outlining access to the bucket and its contents was created.

```{.python3}
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::yara-beach",
                "arn:aws:s3:::yara-beach/*"]
        }
    ]
}
```


- The Policy was attached to the Group.
- A new User with 'Programmatic Access' was created and attached to the Group.

25. The S3 Bucket was connected to Django.

- Within the IDE two new packages were installed.

```
pip3 install boto3

pip3 install django-storages
```

- These new dependencies were added to the requirements.txt file.

```
pip3 freeze > requirements.txt
```

- [Django-storages](https://django-storages.readthedocs.io/en/latest/) was
  added to the list of INSTALLED_APPS within settings.py. This collection of
  custom storage backends for Django includes Amazon S3.

```{.python3}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # Third-party apps installed app
    'allauth.socialaccount.providers.google',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    "crispy_forms",
    "crispy_bootstrap5",
    'ckeditor',
    'ckeditor_uploader',
    'storages',
    # My apps
    'home',
    'excursions',
    'rentals',
    'administrator',
    'cart',
    'checkout',
]
```

27. Media files were added to the S3 Bucket.


- Within the Yara beach bucket 2 folders called 'Rental' and 'excursion were create and inside them all the images.

  ![alt text](documentation/readme-images/aws-bucket-s3-create-folder.png "Creating a folder within the S3 bucket.")
<br>


## Credits

### Content

The following [Bootstrap](https://getbootstrap.com/) components were used and modified:

- [Badge](https://getbootstrap.com/docs/5.2/components/badge/)

- [Card](https://getbootstrap.com/docs/5.2/components/card/)

- [Dropdowns](https://getbootstrap.com/docs/5.2/components/dropdowns/)

- [Modal](https://getbootstrap.com/docs/5.2/components/modal/)

- [Navbar](https://getbootstrap.com/docs/5.2/components/navbar/)

- [Pagination](https://getbootstrap.com/docs/5.2/components/pagination/)


The succes page was taken from here [schauhan](schauhan)

http://www.schauhan.in/bootstrap-payment-success-page-templates/


#### Excursion and Rental Information and Media

- Excursion information, where available, including the product descriptions and ingredients were provided by the following companies:

- [viator](https://www.viator.com/)


- Rental information, where available, including the product descriptions and ingredients were provided by the following companies:

- [airbnb](https://www.airbnb.co.uk/)

*** All images and descriptions taken from the viator and airbnb will be deleted once the project has been accessed..**


## Code

* Typing effect was taken and modified from [codepen](https://codepen.io/denic/pen/GRoOxbM)]

https://codepen.io/denic/pen/GRoOxbM

* HTML/CSS: Implementation and utilisation of Grid CSS layout was assisted by [CSS-Tricks](https://css-tricks.com/snippets/css/complete-guide-grid/).
]
* HTML/CSS: Implementation and utilisation of Grid CSS layout was assisted by [W3school](https://www.w3schools.com/css/css_grid.asp).


---
### Acknowledgements

- [Code Institute](https://codeinstitute.net/) and their helpful tutors.
- Many thanks to my project mentor [Gurjot Singh](https://www.linkedin.com/in/gurjot-singh-64466b199/) for his help and guidance during the design and build process.

- The [Code Institute](https://codeinstitute.net/) community on [Slack](https://slack.com/intl/en-ie/) for their support.
- A very special thanks to my wife Theresa for her unfailing patience and support throughout this project.
- Thanks to my family and my friends who were so willing and helpful when it came to testing the site.
<br>


# Disclaimer

This Milestone project is for educational purposes only.

---