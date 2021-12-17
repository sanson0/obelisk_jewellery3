# Introduction

This project is for an e-commerce jewellery store called Obelisk Jewellery. It utilizes Django full stack frameworks. Frameworks enable fast development of new projects.

This project is the milestone 4 project for Code Institute's Full Stack Development Diploma
# Reasons for site

The jewellery store Obelisk has been set up to enable shoppers to purchase a range of jewellery
## User stories
### Viewing and navigation
| As a | I want to be able to | So that I can|
| -----| -------------------- | -------------|
| Shopper | View a list of products | Select some to purchase |
| Shopper | View individual product details | Identify the price, description, product rating |
| Shopper | Quickly identify deals, clearance items and special offers | Take advantage of special savings on products I'd like to purchase |
| Shopper | View items by category | Spend less time finding items that I want |
| Shopper | Easily view the total purchases at any time | Avoid spending too much |
### Registration and user accounts
| As a | I want to be able to | So that I can|
| -----| -------------------- | -------------|
| Site user | Easily register for an account | Have a personal account and be able to view my profile |
| Site user | Easily login or logout | Access my personal account information |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
| Site User | Have a personalized user profile | View my personal order history and order confirmations, and save my payment information
## Sorting and searching
| As a | I want to be able to | So that I can|
| -----| -------------------- | -------------|
| Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sorted products |
| Shopper | Sort a specific category of product | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
| Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories such as "Earrings" or "Rings" |
| Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |
| Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available
## Purchasing and checkout
| As a | I want to be able to | So that I can|
| -----| -------------------- | -------------|
| Shopper | Easily select the size/ quantity of a product when purchasing | Ensure I don't accidentally select the wrong product, quantity or size |
| Shopper | See what payment methods are valid | Check I have the right payment method |
# Features
Features across pages and features for individual pages are listed. A link to the [wireframe](docs/obelisk_jewellery_wireframe.pdf) is provided. The wireframe shows mock-ups of the main pages of the app including views on devices of different screen widths.
## Features across all pages
### Header
The header contains the
* title
* Navbar with My account, basket, my orders, home, product management (superusers only) and logout
* Free delivery banner
* Categories navbar with necklaces, bracelets, rings brooches, earrings, combos and sale
* Search bar
### Footer
The footer contains the:-
* Statement 'Jewellery for every budget'
* Useful info Navbar with contact us, delivery options,, payment options, terms & conditions, returns & refunds and manufacture
* Payment methods
* Social media links
* Copyright statement
## Features on home page
The home page contains an image of an attractive piece of jewellery
## Features on product display page
The product display page appears when a category/ subcategory is clicked or the search bar is used. Each product is displayed including image, title, description, rating and price. The products are displayed side by side on desktop but one below the other on mobile view. There is a display of number of products found at the top of the page. There is a dropdown menu also at the top of the page which allows shoppers to sort the products by rating, by cost or alphabetically by title. There is a button to take the shopper back to the top of the page This allows the website visitor/ user to move back to the header quickly after scrolling through the products.
## Features on product selected page
The product selected page appears when a product is selected by clicking on it in the product display page. The product is displayed in a larger view and the view coontains the image, title, description, rating, price, size (rings only) and quantity selector. There are buttons at the bottom of the product information, one for 'keep shopping' and one for 'Add to basket'
## Features on basket page
The basket page appears when 'Add to basket' is clicked on the 'product selected' page. The product is displayed in a larger view and the view coontains the image, title, description, quantity, price and size (rings only). There are buttons for 'sign in', 'checkout' and 'delete item'. Signing in/ creating an account is optional but it allows the shopper to track orders and save card details for next time. There is a statement at the top of the page to inform shoppers of this.
## Features on the login page
This page contains a form with:-
* fields for username and password
* a checkbox allowing details to be saved ('Remember me')
* a link back to the home page
* a submit button entitled 'Sign In'
* a link to reset the password entitled 'Forgot password?'
## Features on the register account page
This page contains a form with:-
* fields for email and email again
* a field for the username
* fields for password and password again
* a link back to the home page
* a submit button entitled 'Sign In'
* At the top, a message 'Already have an account? Then please sign in' and the link to sign in.
## Features on checkout page
Contains order summary table with item and subtotal headers Under item header, name of product, size if applicable, quantity Under subtotal header, there is the subtotal amount Contains order total, delivery charge and grand total Contains a form where the shopper can fill out details such as
* Phone number
* Address
* Postcode
* Country
* Full name
* Email address
* Payment card number
* Payment card expiry date
* Payment card security code
* Postcode registered with card
## Features on confirmation page
Thank you for your order confirmation email order number order details
* title of product
* cost of product
* size of product if applicable Delivering to :-
* Full name
* Address
* County
* Town or city
* Postcode
* Country
* Phone number
* Order total
* Delivery cost
* Grand total
## Features on orders page
Products purchased are displayed with image, title and arrival date. This page is visible only if the shopper signed in before purchasing the products The orders page can be accessed from the navbar.
## Features on contact page
This page displays:-
* Email address of the company
* Registered address of the company
* Company phone number
## Features on delivery page
This page displays:-
* Free delivery threshold amount
* Information on standard delivery
* An option of express delivery
## Features on payment methods
This page displays all the payment options available.
## Features on terms & conditions
Terms and conditions are displayed as a block of text with date of latest update.
## Features on returns & refunds
A statement on returns and refunds is provided on this page. This is useful because it provides a cut off point of 30 days so products have to be returned before the 30 days are up and must not be damaged in any way and it provides a timescale for refunding payments.
## Features on manufacture page
This page provides customers with information on how the products are manufactured complete with image.
## Features on size comparison page
Ring sizes are given in different ways on jewellery sites. This page allows a comparison to be made with other systems of sizes.
## Features on add product page for superusers
This page contains a form with the following fields:-
* Select category
* SKU
* Name
* Description
* Has sizes
* Price
* Rating
* Image url
* Select image The form has a submit button entitled 'Add Product' and a cancel button which returns the superuser to the products page.
## Features on edit product page for superusers
This page contains a pre-filled form with the following fields:-
* Select category
* SKU
* Name
* Description
* Has sizes
* Price
* Rating
* Image url
* Select image with current image displayed and an option to remove the image The form has a submit button entitled 'Update Product' and a cancel button which returns the superuser to the products page.
## Future Features of the site
Provide a means of processing Paypal payments as this is a very popular method of payment
# Data
## Product app data
All items will have a: -
* Category
* Title
* Description
* Rating in terms of 1 to 5 stars
* Price
* Size if applicable (for rings only)
The only items that need sizes are the rings. The category containing rings has sizes. The category containing sale items does not because most items in it will not have a size. Individual rings with their size in the description will be included in the sale. This applies to the bag content.
| Field name | Data type |
| ---------- | --------- |
| Title | Short text |
| Price (£) | Number |
| Size (if applicable) | text |
| Rating | Number 1-5 with decimal point |
| Category | Short text|

All items will be assigned an SKU (Stock Keeping Unit) identifier, unique for each distinct product that can be purchased.

The site will have the ability to search words in the title and description of each item for key words such as metal type, gem name, colours, shapes.

The site will contain categories of jewellery. Main categories include necklaces, bracelets, rings, brooches, earrings, combinations (matching necklace, earrings and ring) and sale items The products are all sorted these categories (some will be added to the sale category)

The site has CRUD ability (Create, Read, Update and Delete) because the superusers of the site need to be able to add, update and delete products on the site, plus everyone needs to be able to read data on the site (shoppers as well as superusers).
## Checkout app data
All orders will have a: -
* Order number
* User profile
* Full name
* Email
* Phone number
* Country
* Postcode
* Town or city
* Street address
* County
* Date
* Delivery cost
* Order total
* Grand total
## Profile app data
All profiles will have a:-
* Street address
* Town or city
* County
* Postcode
* Country
* Phone number
## Home app data
The home app will contain:-
* Contact phone number
* Contact address
* Refund information
* Terms and conditions information
## Bag app data
* Display message
## Databases
Django officially supports five database backends: PostgreSQL, MySQL, MariaDB, SQLite and Oracle.

The type used in this project is PostGreSQL when deployed, although the database used during development is SQLite. Product data was transferred between the databases during the deployment process, see the deployment section for details on how this was done. PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads. PostgreSQL runs on all major operating systems, has been ACID-compliant since 2001.

In computer science, ACID (atomicity, consistency, isolation, durability) is a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps. In the context of databases, a sequence of database operations that satisfies the ACID properties (which can be perceived as a single logical operation on the data) is called a transaction.

PostgreSQL comes with many features aimed to help developers build applications, administrators to protect data integrity and build fault-tolerant environments, and help manage data no matter how big or small the dataset. In addition to being free and open source, PostgreSQL is highly extensible. Data types can be defined, custom functions built out, even code written from different programming languages without recompiling the database.

One of the most powerful parts of Django is the automatic admin interface. It reads metadata from models to provide a quick, model-centric interface where trusted users can manage content on the site. The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building the entire front end around. To create a user to login with, the createsuperuser command was used. By default, logging in to the admin requires that the user has the is_staff attribute set to True.
## Site Data
### Returns & Refunds
Thanks for purchasing our products at Obelisk Jewellery operated by Obelisk Ltd. In order to be eligible for a refund, you have to return the product within 30 calendar days of your purchase. The product must be in the same condition that you receive it and undamaged in any way.

After we receive your item, we will inspect it and process your refund. The money will be refunded to the original payment method you've used during the purchase. For credit card payments it may take 5 to 10 business days for a refund to show up on your credit card statement.

If the product is damaged in any way, or you have initiated the return after 30 calendar days have passed, you will not be eligible for a refund.

If anything is unclear or you have more questions feel free to contact our customer support team.

Sample Return and Refund Policy Template [Free Download](https://www.websitepolicies.com) from websitepolicies.com
### Terms & Conditions
#### What is a Terms and Conditions Agreement?
A terms and conditions agreement outlines the website administrator’s rules regarding user behaviour, and provides information about the actions the website administrator can and will perform. Your terms and conditions text is a contract between your website and its users. In the event of a legal dispute, arbitrators will look to this agreement to determine whether each party acted within their rights.

Terms and conditions are not required by law, but are extremely important to the long-term success and viability of your website. Terms and conditions give you control over your site and legal reinforcement if users try to take advantage of your operations.

Creating the best terms and conditions page possible will protect your business from the following: Abusive users — Terms and conditions allow you to establish what constitutes appropriate activity on your site or app, so you can remove abusive users and content that violates your guidelines. Intellectual property theft — Asserting your claim to the creative assets of your site in your terms and conditions will prevent ownership disputes and copyright infringement. Potential litigation — If a user lodges a legal complaint against your business, showing that they were presented with clear terms and conditions before they used your site will help you immensely in court.

In short, terms and conditions give you control over your site and legal reinforcement if users try to take advantage of your operations.

A generic copy of some terms & conditions is taken from the website [Termly](https://termly.io)
## Payment methods
There are four payment methods: -
* Paypal
* Visa
* Mastercard
* American Express
## Delivery options
Free Standard Delivery over £50, otherwise standard delivery of 10% This takes 5-7 working days Express Delivery £6 Delivery next working day
## Manufacture
[Image](https://cdn.pixabay.com/photo/2018/03/31/12/23/hand-3278027_960_720.jpg)
Our goods are hand crafted to the highest standard. We strive to create quality items for every budget. We use a large range of raw materials, particularly gems. This makes our jewellery pieces stand out from the crowd, they are so different from pieces bought from well-known, larger companies.

We hope you enjoy your purchases from us!
# Technologies used
* [HTML](https://html.com)
* [CSS](https://www.w3schools.com/Css)
* [JavaScript](https://www.javascript.com)
* [Jquery](https://jquery.com)
* [Python](https://www.python.org)
* [Bootstrap](https://getbootstrap.com)
* [Django](https://www.djangoproject.com)
* [Stripe](https://stripe.com)
# Deployment
The deployment process for this project is set out in this [link](docs/Deployment.pdf)
# Testing
## Manual testing
See [link](docs/Manual_testing.pdf) for explanation of manual testing.
## Responsiveness
See this [link](docs/Responsive_design.pdf) for results of responsiveness testing.
## Web browsers
The project should be tested on different web browsers eg. Chrome, Avast, Microsoft Bing, Firefox
## Testing tools
Testing tools are listed:-
* HTML code validator, see [results](docs/HTML_Validation.pdf)
* CSS code validator, see [results](docs/CSS_Validation.pdf)
* JShint, see [results](docs/JShint.pdf)
* Lighthouse performance analysis (in Chrome browser), see [results](docs/Lighthouse.pdf)
# Bugs and improvements
## Problem: - toasts not working
It was difficult to get toasts working in this project. All the Bootstrap components are from Bootstrap 5.1 and it is important to keep all components and links consistent. The solution to the problem is shown in this [link](docs/Toasts.pdf).
## Improvement to image layout
There is a difficulty with very different image sizes for items which could sometimes escape the confines of one product entry and bleed across into other product entries. This was solved by setting limits on the width of each image while restricting the height to the same value for all images. This is an easy problem to fix but makes a big difference to the appearance of the website and takes care of the difficulty of large variations in ratio of height and width of images.
# Credits
## Media
IMG 2 GO site was used to reduce file sizes of images for inclusion in the project.
Pixabay was used to obtain photos of jewellery Individual photos used in the project database have their urls listed below.
https://cdn.pixabay.com/photo/2017/07/08/18/38/decor-2485239__340.png

https://cdn.pixabay.com/photo/2017/07/08/17/54/decor-2485081_960_720.png

https://cdn.pixabay.com/photo/2017/07/08/18/54/decor-2485268_960_720.png

https://cdn.pixabay.com/photo/2017/07/08/00/34/decor-2483241_960_720.png

https://cdn.pixabay.com/photo/2017/03/09/20/28/flower-2130758_960_720.png

https://cdn.pixabay.com/photo/2017/03/10/18/32/brooch-2133460_960_720.png

https://cdn.pixabay.com/photo/2018/05/17/23/52/heart-3410020_960_720.png

https://cdn.pixabay.com/photo/2017/03/09/20/31/brooch-2130764__480.png

https://cdn.pixabay.com/photo/2017/07/03/16/24/insect-2468230_960_720.jpg

https://cdn.pixabay.com/photo/2017/10/04/20/05/sowa-2817399__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/01/bloodstone-665716_960_720.jpg

https://cdn.pixabay.com/photo/2014/11/16/12/17/pearls-533337_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/12/01/46/lapis-669522_960_720.jpg

https://cdn.pixabay.com/photo/2017/01/12/16/35/necklace-1975105__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/01/necklace-665715_960_720.jpg

https://cdn.pixabay.com/photo/2019/11/22/07/35/jewelry-4644297__340.jpg

https://cdn.pixabay.com/photo/2015/03/12/01/45/lapis-669521_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/12/01/44/mystic-topaz-669519_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/04/red-665724__340.jpg

https://cdn.pixabay.com/photo/2015/05/26/09/48/chain-784422__340.jpg

https://cdn.pixabay.com/photo/2015/03/12/01/12/amber-669473__340.jpg

https://cdn.pixabay.com/photo/2014/11/05/19/26/woman-518275_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/02/fluorite-665718_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/02/agate-665719_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/13/53/gemstone-665696_960_720.jpg

https://cdn.pixabay.com/photo/2017/03/03/16/14/heart-2114333__340.png

https://cdn.pixabay.com/photo/2015/03/09/14/12/amazonite-665747__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/09/59/bronzite-665310_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/12/01/40/rose-quartz-669513_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/12/01/42/apatite-669515_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/03/ankh-665720_960_720.jpg

https://cdn.pixabay.com/photo/2015/08/26/19/25/pendant-908943__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/10/00/pink-665316__340.jpg

https://cdn.pixabay.com/photo/2013/02/04/17/31/moonstone-77862_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/11/24/druzy-665486__340.jpg

https://cdn.pixabay.com/photo/2016/04/12/16/44/bracelet-1324818_960_720.jpg

https://cdn.pixabay.com/photo/2016/12/27/09/36/bracelet-1933601_960_720.jpg

https://cdn.pixabay.com/photo/2017/03/05/01/41/jewelry-2117472_960_720.jpg

https://cdn.pixabay.com/photo/2016/02/13/22/48/bracelet-1198737__340.jpg

https://cdn.pixabay.com/photo/2016/02/13/22/52/bracelet-1198740_960_720.jpg

https://cdn.pixabay.com/photo/2013/11/27/15/58/accessory-219346_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/10/01/solar-quartz-geode-665322_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/11/25/druzy-665487_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/15/moss-agate-gemstone-bracelet-665755_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/14/gemstone-bracelet-665753_960_720.jpg

https://cdn.pixabay.com/photo/2018/04/21/22/53/heart-3339762_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/14/00/tigers-eye-665712_960_720.jpg

https://cdn.pixabay.com/photo/2018/01/31/07/26/paper-3120474_960_720.jpg

https://cdn.pixabay.com/photo/2021/02/04/20/27/bracelet-5982564_960_720.jpg

https://cdn.pixabay.com/photo/2021/02/04/20/26/bracelet-5982558_960_720.jpg

https://cdn.pixabay.com/photo/2020/04/04/20/43/bracelet-5003797__340.png

https://cdn.pixabay.com/photo/2018/02/19/18/20/bracelet-3165768__340.jpg

https://cdn.pixabay.com/photo/2015/08/06/18/42/stainless-878333__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/13/59/snowflake-obsidian-665711__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/10/15/glass-665379_960_720.jpg

https://cdn.pixabay.com/photo/2015/07/20/15/11/earrings-852892_960_720.jpg

https://cdn.pixabay.com/photo/2011/11/16/11/28/earrings-10332_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/12/01/27/aventurine-669488__340.jpg

https://cdn.pixabay.com/photo/2015/07/20/15/12/earrings-852901_960_720.jpg

https://cdn.pixabay.com/photo/2017/07/08/21/20/decor-2485680_960_720.png

https://cdn.pixabay.com/photo/2015/03/09/10/05/ammonite-665339_960_720.jpg

https://cdn.pixabay.com/photo/2013/11/06/09/59/earrings-206363_960_720.jpg

https://cdn.pixabay.com/photo/2019/02/07/20/36/ring-3982105_960_720.jpg

https://cdn.pixabay.com/photo/2015/02/28/11/33/ring-653435_960_720.jpg

https://cdn.pixabay.com/photo/2016/02/13/22/54/ring-1198744__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/09/37/rhodochrosite-665274__340.jpg

https://cdn.pixabay.com/photo/2016/02/18/16/21/ring-1207474_960_720.jpg

https://cdn.pixabay.com/photo/2016/02/13/22/42/ring-1198732_960_720.jpg

https://cdn.pixabay.com/photo/2015/06/01/10/18/flowers-793119_960_720.jpg

https://cdn.pixabay.com/photo/2017/06/13/02/22/ring-2397457_960_720.jpg

https://cdn.pixabay.com/photo/2018/06/29/05/42/ring-3505305__340.png

https://cdn.pixabay.com/photo/2015/03/09/13/49/chrysoprase-665688_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/09/36/chrysoprase-665271_960_720.jpg

https://cdn.pixabay.com/photo/2015/03/09/09/35/rutilated-quartz-665262__340.jpg

https://cdn.pixabay.com/photo/2018/05/14/14/40/ring-3400224_960_720.png

https://cdn.pixabay.com/photo/2014/01/17/14/28/gem-246922_960_720.jpg

https://cdn.pixabay.com/photo/2017/03/29/23/38/amethyst-2186842__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/11/36/drusy-665522__340.jpg

https://cdn.pixabay.com/photo/2018/05/23/18/08/ring-with-ornament-3424669__340.png

https://cdn.pixabay.com/photo/2015/09/02/10/46/jewelry-918247_960_720.jpg

https://cdn.pixabay.com/photo/2015/08/09/09/35/jewelry-881324_960_720.jpg

https://cdn.pixabay.com/photo/2017/05/28/18/11/fashion-2351694_960_720.jpg

https://cdn.pixabay.com/photo/2017/06/03/22/26/fashion-jewelry-2369877_960_720.jpg

https://cdn.pixabay.com/photo/2014/01/28/09/07/fused-glass-253622_960_720.jpg

https://cdn.pixabay.com/photo/2014/01/28/09/11/fused-glass-253623__340.jpg

https://cdn.pixabay.com/photo/2020/10/10/22/45/accessories-5644343_960_720.jpg

https://cdn.pixabay.com/photo/2021/09/07/07/41/necklace-6603177_960_720.jpg

https://cdn.pixabay.com/photo/2015/07/20/15/12/earrings-852898_960_720.jpg

https://cdn.pixabay.com/photo/2017/07/08/21/14/decor-2485655_960_720.png

https://cdn.pixabay.com/photo/2015/03/09/10/11/mystic-665373__340.jpg

https://cdn.pixabay.com/photo/2014/04/28/22/00/gems-334067__340.jpg

https://cdn.pixabay.com/photo/2017/10/29/20/27/earrings-2900740__340.jpg

https://cdn.pixabay.com/photo/2015/03/09/10/05/topaz-665340__340.jpg

Boutique Ado project Chris Z from Code Institute

[Stack overflow](https://stackoverflow.com) provided code for the star rating for the products.

Terms and conditions website [Termly](https://termly.io)

[Tutorials point](https://www.tutorialspoint.com) for Django social media share

[Diff checker](https://www.diffchecker.com) is useful for debugging as it finds differences between chunks of code.

Sample Return and Refund Policy Template [Free Download] from [websitepolicies.com](https://www.websitepolicies.com)

[HTML Validator](https://validator.w3.org)

[CSS Validator](https://jigsaw.w3.org/css-validator)

[Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/) performance checker in developer tools in Chrome
