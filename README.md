Gadget360 Website

A live version of the site is available [LIVE SITE](https://heroku-milestone4-gadget360.herokuapp.com/)  

Gadget360 is an online gadget and electric appliances website where users can browse the different products, add to their shopping cart, remove what they do not need from the cart & totally empty it if required. Also, the users can make a wishlist as well as review products. This website is designed to be intuitive and easy to navigate and use, promoting a simple layout with effective and purposeful features.

<h2 align="center"><img src=""></h2>


User Experience (UX)
User stories

**- First Time Visitor Goals:**
1.  As a first time visitor, I want to easily understand the main purpose of the website.
2.  As a visitor, I want to be able to register, be able to login and log out.
3.  As a visitor I want to see all the products that the company deals with.
4.  As a visitor i want to be able to view products in their specific categories and also be able sort them  as per their price, title etc.
5.  As a visitor i want to be able to search the products that I need from the many products that are available.
6.  As a visitor i want to be able to see the details of the product that I have selected.
7.  As a visitor i want to be able to add, edit, delete products to and from the shopping cart.
8. As a visitor I want to be able to pay for the products that I purchase online through an effective and secure payment system..
 

**- Returning Visitor Goals:**

1.  As a returning Visitor, I would like to be able to leave reviews after I have used the product.
2.  As a returning Visitor, I want to be able to view my previous order history to see what items I had ordered and if they were delivered as per order.


**Project Requirements:**


## Design
    #### Colour Scheme
    -   The colors used for the website are orange and dark grey on a white background which gives more of a warm effect and the color combination is very soothing to the eye.
    #### Typography
    -   The Electrolize font has been used for this website as it gives the impression of a more modern website dealing with products from the future. 
    #### Imagery
    -   

*   ### Wireframes

    -   Home Page Wireframe - [View]()
    -   Login Page Wireframe - [View]()
    -   Registration Page Wireframe - [View]()
    -   My Profile Page Wireframe - [View]()
    -   Recipe Details Page Wireframe - [View]()

    -   Mobile Home Wireframes - [View]()

    - Information: The above wireframes were designed in the initial process. But as the project went on, changes were made to make every content look better and more attractive.

## Features

-   The website is responsive on all device sizes ranging from desktop to tablet & mobiles.

-   Interactive elements.

-   Defence coding has been utilised wherever possible. If the user has entered info which is not as per criteria, errors will be generated.

-   Database connectivity.

## Project implementation

-   The Homepage: When the users click on the website link, they are taken directly to the homepage which provides them the option to click diretly from a product link displaed in its respective category. Also there is a call to action button (BUY NOW) which promps the user to click on it. The navigation has the Members Area which when clicked reveals a dropdown menu to sign up or login.

- The Products page: The products page lists all the products available in the online shop. The users can search for a specific item by entering the search term in the search bar.

- The Product details page: Once clicked on the product, the users can view the full product details as well as the option to add the item to the cart. On the same page, there is also an option for the users to leave any reviews about the product or view any reviews left by other users.

- The Cart - The cart provides the users the ability to edit and delete items as per their requirement as well as a link to the checkout page.

- At the checkout page, the users make payments via the stripe interface and their order number is generated thus confirming their purchase.

## Future implementation

-   Option to process returns.
-   Adding a rating feature.
-   Chatbot functionality

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Bootstrap4:](https://getbootstrap.com/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Electrolize' font into the style.css file which is used for the navbar.
3. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
4. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
5. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
7. [Figma:](https://figma.com/)
    - Figma was used to create the wireframes during the design process.
8. [Django:](https://www.djangoproject.com/)
    - Django was the web framework used to build the web application.
9. [PostgreSQL:](https://www.postgresql.org)
    -PostgreSQL was used to store and retreive data from the database.
10. [Stripe:](https://www.stripe.com/)
    -Stripe was the platform used for making online payments.


## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results]()
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results]()
-   [PEP8 Compliance](http://pep8online.com/) - [Results]()

### Testing User Stories from User Experience (UX) Section

#### First Time Visitor Goals

1.  Understand the main purpose of the website - The website is easily navigable. All the necessary icons are located on the Homepage itself and there is ease in moving from page to page.
2.  Able to register, be able to login and log out - The functionalities of adding, editing deleting & viewing items exists on the site.
3.  See all the products that the company deals with - There is a link which gives a view of all products on the website.
4.  Search the products that I need from the many products that are available.
5.  See the details of the product that I have selected.
6.  CRUD Functionality -  add, edit, delete products to and from the shopping cart.
7. Payment system - The most secure payment system provided by stripe has been integrated in the website.

   #### Returning Visitor Goals

1.  Leave reviews on the website - The review functionality exists in the product detail page. Youu will need to be logged in to review.
2.  Order history - The order history can be viewed in the profile page and it gives all information regarding the product, quantity, price etc.


### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop & Samsung S20 Plus.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   The Add to Wishlist functionality was being worked on but could not be implemented.
-   Sorting and filtering functionality not implemented.

### Additional Information

To access the admin, the username is testusermain and password is testuserpass123.


## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone
```

7. Press Enter. Your local clone will be created.

```
$ git clone 
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

- Codemy.net for the freely available and easily understandable youtube tutorials.
- Code Institute course material which was also of great help.


### Content

-   All content was written by the developer.


### Media

-  The background image was freely available from the internet, taken specifically from [Zoom](https://explore.zoom.us/)

- The media files for the products were copied from the Amazon website.

### Acknowledgements

-   My Mentors Medale Oluwafemi & Victor Miclovich for continuous helpful feedback.

-   Tutor support at Code Institute for their support.