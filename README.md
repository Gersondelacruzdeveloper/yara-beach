
<h1 align="center">My Online Recipes</h1>

<h2 align="center">Code Institute - Milestone Project 3</h2>

<img src="./myonlinerecipes/static/documentation/readme-images/main_readme_file_image.png" height="auto" width="100%" alt="Mockup of myonlinerecipe pages when viewed on a desktop, tablet and mobile device."/>

My online recipes website help you to create, save and share your recipes with others. I love cooking, when I was nine years old, I started to write recipes in my school notebook, all the recipes from my beautiful Grandma that in piece rest, I stored them there, as well as others recipes that I encounter on my cooing journey. by the time I was 20 years old, I had realised that I had over 15 school notebooks and accessing all those recipes was a nightmare, flipping pages trying to find these recipes, so now thanks to code Institute I have created this beautiful recipes website that allow me not just save all my recipes but also share it with the world. I do not have to struggle to carry my notebooks anymore when I am travelling because it is all online. I also do not have to struggle to find a recipe that I have saved, as I just need to type the words from the title or the ingredients. and the website will give me all the relevant recipes I have and other recipes other people have shared as well. Also, the beauty of this is that anyone can come to this website and save their recipes free of charge. Furthermore there is a comment section at the bottom of each recipe so people can leave their opinion of what they like and what they do not like about that specific recipe.


The project was developed using **HTML5**, **CSS3**, **JavaScript**, **Python**, **Bootstrap**, **Flask**, and utilises a relational database -> **PostgresSQL**.

[Click here to visit the site.](https://myonlinerecipes.herokuapp.com/)

## Table of contents
- [Project Goals](#project-goals)
1. [**User (UX)**](#User-experience)
     1. [Strategy](#strategy)
     2. [Scope Plane](#Scope-Plane)
     3. [Structure](#structure)
     4. [Skeleton](#skeleton)
     5. [Surface](#surface)
2. [Features](#features)
     1. [Existing Features](#existing-features)
     2. [Future Feature Considerations](#future-feature-considerations)
3. [**Technologies Used**](#technologies-used)
4. [**Testing**](#testing)
    1. [Performance](#performance)
    2. [HTML Validation](#html-validation)
    3. [CSS Validation](#css-validation)
    4. [Manual Testing](#manual-testing)
    5. [Responsiveness](#responsiveness)
    6. [Tested User Stories](#tested-user-stories)
    7. [Bugs](#bugs)
5. [**Deployment**](#deployment)
    1. [How this Project was Deployed](#how-this-project-was-deployed)
    2.  [How to Run this Project in your Browser](#how-to-run-this-project-in-your-browser)
    3. [Cloning the Repository](#Cloning-the-Repository)
    4. [Manually Downloading the Repository](#Manually-Downloading-the-Repository)
    5. [ Opening the Repository](#Opening-the-Repository)
6. [**Credits**](#credits)
    1. [Content](#content)
    2. [Media](#media)
    3. [Code](#code)
7. [Acknowledgements](#acknowledgements)
8. [Disclaimer](#disclaimer)

  <br><br>

### Project Goals
The goals of this project are to:
- To create a site where users can easily access recipes, create, save, edit, delete and share their own if they decide to.
-	Make MyOnlineRecipes website to be a reputable website by creating a professional and intuitive interface.
-	Create a website that is visually appealing and fully responsive on all devices and screen sizes.
- To display information in user-friendly way, contributing to an overall good user experience.
-	Present information about MyOnlineRecipes site so that visitors immediately comprehend what service it provides to its members. 
-	Allow visitors to easily contact the website administrator with any questions.
-	Encourage new members to sign up to the site.
-	Create an interactive website where a community can leave comments on the recipe as long as they have an account and logged in.
-	Store the users’ data so that it is can be accessed when required.
---
##  User Experience

### Strategy

- The User centred Design process started with the creation of the User Stories. these influenced subsequent feature, layout, and design decisions.

#### User Stories

#### Prospective User

As a potential MyOnlineRecipes site user I want to be able to: 

- Immediately comprehend the purpose behind the MyOnlineRecipes site and view some of the recipes.
- Navigate throughout the site with eases.
- Easily create an account and sign in to it.
- Log out of my account once finished on the website.
- Experience good responsive design, so I can access the site on different devices.
- Change my password in case somebody else has access to it.
- Contact the admin.
- See a variety of recipes for different meals of the day
- Enjoy stylish, clean design and style that is inline with the subject of the site

#### As a returning or registered user

As a registered user of MyOnlineRecipes site I want to be able to:

- Log into my account.
- Save private recipes that only I can see.
- Have the option to share my recipes with other users
- Create my own recipes.
- Edit the recipes I have added.
- Delete the recipes I have added.
- Have a rich text editor which enable me to writing beatiful content.
- Contact admin with queries or feedback.
- Comments on recipes, so I can share my opinion with other users.
- Find social media links, so I can follow them on different platforms.


#### Site Owner
As the owner of MyOnlineRecipes website I would like to:

-	Provide site members with an effective and user-friendly platform where they can read comments written by other members so that they make more informed choices when choosing a recipes to make.
- Provide site members with the option to share their recipes the others users.
- Present the commets in a visually appealing format.
- Provide site members with the ability to search the site for a specific recipes by entering the title or Ingridients into a search box within the site.
- Provide users with the ability to add general infomation about the recipes if the decide to, these include the recipes author’s name, title, Images, Ingredients, method or step by step process to make the recipes, service size, cooking time, date created, calories, fat, protein, carbohidrates, and salt. most of of the this field will be optional.
- Provide the user with a beatiful image cover in case they decide not put add an image to the recipes.
- Provide prospective members with the ability to sign-up easily
-	Provide visible contact details so that all site visitors can contact the site administrator with ease


###  Scope Plane

### **Existing Features**

The key features of the website were developed based on user needs. 

Users should be able to do the following on the website:

-	Easy navigation by using navigation bar. Nav links are clearly idenfied both on desktop and when sidenav is expanded on smaller devices.
- Responsive design allowing users to use site across all devices.
- Site layout is responsive to all media sizes.
- Users of the site can create an account.
- Users can login into their existing account.
-	Users can write a recipe comment as long as they are registered.
- Users can contact the site owner through a contact form
- Recipes can be created, read, updated and deleted (CRUD) by the users.
- On the create recipe form, there is a rich text editor which enable users to write beatiful content
- Users of the site, either logged in or not, can search the recipes either by text input or filtering the ingredients they want the recipe to have.
- Logged in users have the options to either share their recipes or keep it private by toggle the button (Share ?).
- Logged in users have access to their profile, and view all the the recipes they have created and also view the recipes that other
 people have decided to share.
- Recipe information includes the same as describe in the Site Owner e.g: recipes author’s name, title, Images, Ingredients, method or step by step process to make the recipes, service size, cooking time, date created, calories, fat, protein, carbohidrates, and salt.
- Flash messages appear when users create, edit, delete or update the recipe.
- Easily access the site’s social media channels.
- navigate through pagination on the recipe pages.
- Change their password securily by email.

### Structure

### Informational Architecture

After identifying the needs of the site's users and after visiting other recipes site and recommendation websites the following website design and features were chosen:

##### Header

The header of the page contains the **NavBar**, the  **Logo**, the following links located to the left: **Home page**, **My Recipes**, **contact**, **Dropdown menu with the name of the user and a list of options to logout or change password**. To the right there is a  search box with a button to search for recipes. The header It is a static element, and is fixed to the top of the page at all times. When the site get 750px down (mobile) the header content change from inline to column.  When the user is not a member the only thing they can see is the Home, Contact, Login Sign Up.

##### Home 
The Home page display all non-private recipes of the site and it is very responsive when it comes to a different device, it is composed of 5 cards if its a large device like a monitor or computer, and if it is a tablet device it has 3 cards, mini table with 2 cards, mobile of 750px down the home page just display 1 card. each card contains. an image, title, recipe owner name, and a comment sign along with the number of comments that recipe has.

##### Contact page 
The contact page contains a header title, a sentence encouraging the user to email the administrator, 3 texts input and a big texterea. also in the right corner, the is a button with the value of submit.

##### My Recipes page 
The My Recipes page which is only available for registered users, contains almost the same layout as the home page, except that on every card there are two buttons one for edit and another one for delete. at top of the page below, the header title,  there is a button with a plus sign where the user can click and add their recipes.

##### Login page 
The Loging page contains a card with a header title, two fields: one for the password and another one for the username, and a button below with a login text, below the button there is a sentence with the link of sign up and another one with the link to reset the password in case they have forgotten. each input field has a beautiful icon: one is a user icon and the other one is a key icon.

##### Sign up page 
The signup page contains the same as the login page exept that it contains 2 more input fields, which are the email and the comfirmation of the second password, also it has a sentence with a login link,  in case the user already has the credentioal to login. 

##### 404 page
Once the user navigates to a wrong path inside myonlinerecipes site, it will be redirected to a beautiful image which contains a button to return home, the header of the image saying 404 and a sentence letting the user know that he went to a run URL.

##### footer
The footer is statically positioned at the bottom of the page. Similar to the header, contrary to the header the footer's content stay in line when the content exceeds the viewport of the device. The footer contains a link to the project’s GitHub repository, the facebook  link of the site as well as the instagram link, and  also a link to my personal linkedIn profile.

### Skeleton

The UI wireframing tool, [Balsamiq](https://balsamiq.com/), was used to create wireframes for each page of the game as it would appear on desktop, tablet, and mobile devices.

The main content areas were expressed in similar ways to create consistency across the site. A home page featuring the name of the game and a start bottom, a main screen with all cards identical. Top left-hand corner features a flag poll that counts down, top right of the screen shows the game points, a contact page, and a footer, which contains very important information: copy right, LinkedIn link, GitHub link, all of these were included at the bottom of every page to help users navigate through the game efficiently.

<br>

#### Wireframes

##### Desktop

- [Home Page wireframe: ](./myonlinerecipes/static/documentation/wireframes/Home-desktop.png)

- [Contact Page wireframe: ](./myonlinerecipes/static/documentation/wireframes/contactpage-desktop.png)

- [Login page wireframe: ](./myonlinerecipes/static/documentation/wireframes/loginpage-destop.png)

- [Add Recipes form wireframe: ](./myonlinerecipes/static/documentation/wireframes/Addrecipeform-desktop.png)

- [My Recipes page wireframe: ](./myonlinerecipes/static/documentation/wireframes/myrecipespage-desktop.png)

- [Register account page wireframe: ](./myonlinerecipes/static/documentation/wireframes/Registeraccountpage-desktop.png)


##### Tablet
- [Home Page wireframe: ](./myonlinerecipes/static/documentation/wireframes/Home-tablet.png)
- [Contact Page wireframe: ](./myonlinerecipes/static/documentation/wireframes/contactpage-tablet.png)
- [Login page wireframe: ](./myonlinerecipes/static/documentation/wireframes/loginpage-tablet.png)
- [Add Recipes form wireframe: ](./myonlinerecipes/static/documentation/wireframes/Addrecipeform-tablet.png)
- [My Recipes page wireframe: ](./myonlinerecipes/static/documentation/wireframes/myrecipespage-tablet.png)
- [Register account page wireframe: ](./myonlinerecipes/static/documentation/wireframes/Registeraccountpage-tablet.png)


##### Mobile
- [Home Page wireframe: ](./myonlinerecipes/static/documentation/wireframes/Home-mobile.png)
- [Contact Page wireframe: ](./myonlinerecipes/static/documentation/wireframes/contactpage-mobile.png)
- [Login page wireframe: ](./myonlinerecipes/static/documentation/wireframes/loginpage-mobile.png)
- [Add Recipes form wireframe: ](./myonlinerecipes/static/documentation/wireframes/Addrecipeform-mobile.png)
- [My Recipes page wireframe: ](./myonlinerecipes/static/documentation/wireframes/myrecipespage-mobile.png)
- [Register account page wireframe: ](./myonlinerecipes/static/documentation/wireframes/Registeraccountpage-mobile.png)

<br>

### Database

**MyOnlineRecipes** utilises a relational Database via PostgreSQL for storing **User**, **Recipes** and **Comments** data.

- The **User** model is composed of 7 columns: username, email, password, date created, the last login of the user and an image of the user. The only field that are quired are title, Ingridients and method and they all have a * at the top. The User model has one to many relationships with the **Recipes** model and **Comments** model which help to access that data and filter it by the user id. by setting one to many relationships we were able to have multiple recipes and comments that belong to just one user.

- The **Recipes** model is composed of 15 columns, the main id which is set to Primary Key. Furthermore is connected by its id to the **Comments** model. The **Recipes** model has a one to many relationships with the **Comments** which means that a recipe can have many comments.

- The **Comments** model is composed of 7 columns including the id as well. this model does not have one to many relationships with other models but it can easily access to the **User** and **Recipes** model because of its **backref relationship** that points from **User** and **Recipes** to **Comments**

- Database schema design was created using [DrawSql](https://drawsql.app/), see below.
![Database Design](./myonlinerecipes/static/documentation/Database_schama.png)

### Surface

##### Design
The Project Design is a combination of my own design implemented with the bootstrap framework. The colour helps the website to stand out and give a clear meaning of what the website is about as the colour is usually found in food and nature. Its aim is to be engaging, alluring, and cohesive.

##### Logo design 
The logo of the site is located on the left side of the navbar as the bootstrap standard logo, and it is bigger than the others links in order to stand out. and make it recognised by the users.

##### Colour Scheme
The colour scheme for the game was chosen in order to convey excitement, clean and visually appealing site.

![alt text](./myonlinerecipes/static/documentation/readme-images/colour-palette.png "myonlinerecipes' Reviewed colour palette.")

<br>

<sub>*Colour palette created at* [coolors.co](https://coolors.co/ffbe0b-fb5607-ff006e-8338ec-3a86ff).</sub>

- #004b49, Deep jungle green,Psychologically, when humans think of this color, Deep jungle green, they might associate it with being clean, glamorous, elegant, the home, and accessibility.
     - Used in the navbar and in the footer as it makes a beautiful combination.

- #f2f2f2, Culture color, which is a light grey represent neutrality and balance. 
   - Used in the background of the website in order to the main content stand out.

- #ffffff, White represents purity or innocence and stands for everything good and right.
- Use in all the links of the text
- Used in the Card
- As main color text

- #626567, Granite Grey, used in the card for the text as it is darker than the Culture colour and makes the text to be more visible.

- #000000, Black color represents evil, darkness, night, and despair. It’s the color used to convey certainty and authority.
- Used in all header title so the users knows at glance where they are located


#### Icons
Icons were used within the site in order to help the user to understand the content easier. 
They were taken from [Font Awesome](https://fontawesome.com/) and chosen to be self explanatory.

#### Typography
After an intensive search for the right font, I encountered Montserrat, the most used font for recipes websites, this font I have used to be a company with Georgia and serif in case Montserrat does not load. I have used this font for the body of the website.

## Existing Features

The project consists of three main pages, and has a 404.html and 500.html error page, login and logout functionality, a response page page for for the contact, myrecipes that is where all the recipes for the user is stored, and the home page. The main pages can be accessed through the navbar.

**Fabicon**

Myonlinerecipes favicon, displayed on the web Brower’s tab, allows the user to identify the website by sight.
 
**More Features**

- **myonlinerecipe Logo**: It is the default logo style for boostrap but recognizable across all website.

- **The recipe form Page** and **The edif form Page**: allow the user to craete beatiful recipes, I added a rich ckeditor which help to tape the ingridients and method easier and more beatiful.

- **The Search functionality**: allow the user to search for any recipe in the database except for the recipe that are privat. they are allow to search by method, title and ingridients.

- **Commet section**: allow the user comment on any recipe and even ask questions about the recipe. All users can interact with each other this way and share their experiend with the recipe.


**Footer**
Each page has a fixed footer at the bottom. This provides Facebook, Instagram, Twitter and Tik Tok links as well as a copyright with my name on it.

#### (home) features
  - In home we can see the all the beatiful recipes, a big heading title so the user understand where it is located and a navbar and footer.
  - in Navbar we can vizualize the all links in color white and background green. all links contains icons to make the user understand at glance.
  - Footer contains copyright and links with the same color schema of the navbar.

#### Myrecipe page feature
  - The same as the home page except that it has:
  - A edit button, 
  - Delete button,
  - Add recipe button bellow the heading title

#### contact.html features
  - Title encoraging user to send a mesage.
  - A well structured contact form with 5 fields: name, subject, email, and message with a submit btn at the end.

#### contact-response.html features
  - Has a positive message comfirming to the user that their message has been sent.
  - A botton that redirect the user back home if desired.


  #### 404.html features
  - Has a message informing the user that the page they are loking for does not exist.
  - A botton that redirect the user back home if desired.
  - A footer with icons and links and navbar


  #### 500.html features
  - Has a message informing the user that something went wrong.
  - A botton that redirect the user back home if desired.
  - A footer with icons and links and navbar


### Future Feature Considerations
  - For adding future features I would like to add pagination and a password reset function that send an email to the user and logged them back in where they can set a new password.


## Technologies Used

- Languages: 

  * [HTML5](http://en.wikipedia.org/wiki/HTML5). Used to create the structure of the myonlinerecipe website and the custom 404 and 500 pages.
  * [CSS3](http://en.wikipedia.org/wiki/CSS). Used to add style to the website. 
  * [JavaScript](https://en.wikipedia.org/wiki/JavaScript). Used to create the dynamic, interactive elements of the website such as the carousel and to call the Google Books API.
  * [Python](https://en.wikipedia.org/wiki/Python_(programming_language)). Used to create and run the web application.
  * [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)). Used to simplify displaying data from the backend of this project smoothly and effectively in html.

- Websites:
* The project was debugged using [Google Chrome](https://www.google.com/intl/en_uk/chrome/) [Dev Tools](https://developers.google.com/web/tools/chrome-devtools).
* The project uses [GitHub](https://GitHub.com/) for hosting source code, for utilising git version control, and for hosting the site on GitHub pages.  
* The project uses [FontAwesome](https://fontawesome.com/) v5.15.1, a free icon-set/toolkit for web development.
* The project's accessibility was assesed via WebAim's [W.A.V.E](https://wave.webaim.org/) and Google Chrome's [Lighthouse](https://developers.google.com/web/tools/lighthouse).
* The project's screen-reader accessibility was tested using [Screen Reader for Google Chrome](https://chrome.google.com/webstore/detail/screen-reader-for-google/nddfhonnmhcldcbmhbdldfpkbfpgjoeh/related?hl=en).
* The project used Toptal's [Colorfilter](https://www.toptal.com/designers/colorfilter/) to assess how colour-blind-friendly the site was.
* The project's colour contrast ratio was assessed using [Contract-Ratio](https://webaim.org/resources/contrastchecker/)
* The project's HTML was validated using [W3C HTML Markup Validator](https://validator.w3.org/).
* The project's CSS was validated using [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/).
* The project's wireframes were designed in [Balsamiq](https://balsamiq.com/wireframes/).
* [Slack](code-institute-room.slack.com). Used during all phases of development and testing to find the answers to questions and the solutions to problems enountered.
* [Coolors](https://coolors.co/ffbe0b-fb5607-ff006e-8338ec-3a86ff). Used to choose a colour scheme.
* [pixabay.com](https://pixabay.com/vectors/recipe-label-icon-symbol-spoon-575434/). Used for the icons detail page.
* [www.freepik.com](https://www.freepik.com/free-vector/404-error-with-person-looking-concept-/). Used image for the 404 error page.
* [www.freepik.com](https://www.freepik.com/free-vector/404-error-with-person-looking-concept-/). Used image for the 404 error page and 500 internal error.
* [express.adobe.com](https://express.adobe.com/express-apps/logo-maker/preview). this site it was suposed to be for logo only for a created a imaga that was use for the recipes that does not contain image.
* [flask-sqlalchemy.palletsprojects.com](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/). This site was used for following instruction on how to extract with sqlalchemy queries.
* [Favicon.io](https://favicon.io/favicon-converter/). used to convert the logo to favicon.
- Frameworks
* [Bootstrap Framework](https://getbootstrap.com/). Used to structure the website layout and ensure that it was responsive on all devices.
* [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)).  Python web framework used to create the web app.

* [designs.ai](https://designs.ai/colors/color-meanings/midnight-blue). used to check colors combinations to achieve beautiful results.
- Database
  * [Postgresql](https://www.postgresql.org/), the relational database. Used to store the users' information, recipe comments and recipe data.

## Testing

[Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) were used extensively throughout the development process in order to test whether elements were responsive when viewed on mobile and tablet devices. When problems were encountered the Device Selector was used to target the element.  Using the Elements Panel in Developer Tools the code in question was altered in order to achieve the desired result. 
Working code snippets were then replicated in the style.css file in vs code. Other solutions for errors were found in the Code Institute [Slack](code-institute-room.slack.com) channels, on [Stack Overflow](https://stackoverflow.com/), on [W3Schools](https://www.w3schools.com) and on [heroku website](https://dashboard.heroku.com/).

The website was regularly tested using the ***Google Chrome Developer Tools Lighthouse test**. During the testing I highlighted errors across the site which have since been recitified:

## Home page

 ***Error 1 Best Practice error** - "Browser errors logged to the console":
![alt text](./myonlinerecipes/static/documentation/testing/best_practice_problem_in_home.png "Screenshot of Best Practice error.")
<br>

And it was showing in the **console** as:
![alt text](./myonlinerecipes/static/documentation//testing/script_console_error.png "Screenshot of Best Practice error.")
<br>

The reason why the error occur is because javascript could not get the id unless we are at the page, so what I did was to add an extra measure. and said basicaly if the id is in the page then request the toggle btn.
Image error fixed
![alt text](./myonlinerecipes/static/documentation//testing/succesful_test_home.png "error fixed.")
<br>

## Myrecipe page

***Error 2 Accessibility error**  - "buttons do not have dicernible name"
![alt text](./myonlinerecipes/static/documentation//testing/myrecipes-accessability_problem.png "error fixed.")
<br>

To fixed the problem above, I  to add aria-label and and rel to the button in my recipe page.

**Problem 2 solved**
![alt text](./myonlinerecipes/static/documentation//testing/succcesful_test_myrecipes.png "error fixed.")
<br>


### HTML Validation

[W3C HTML Validation Service](https://validator.w3.org/#validate_by_uri) was used to validate the HTML documents. It highlighted 3 errors across the site which have since been recitified: 

## Contact page 

***Error 1**  - "Attribute is obsolete"
<br>
***Error 2**  - "section lack of heading error"
![alt text](./myonlinerecipes/static/documentation//testing/contact_test_html_fail.png "error fixed.")
<br>
To fixed ***Error 1** issue I eliminated the link that was not been used.
To fixed ***Error 2**  I added a heading element in the title.

Both error Fixed
![alt text](./myonlinerecipes/static/documentation//testing/contact_html_test_pass.png "error fixed.")
<br>

## Home page 

***Error 3**  - "Error tag i"
![alt text](./myonlinerecipes/static/documentation//testing/home_html_fail.png "error fixed.")

By Mistake I added double closing i tag when i was adding the icons. so I just deleted the exta tag.

![alt text](./myonlinerecipes/static/documentation//testing/home_html_pass_test.png "error fixed.")
<br>

The rest of the pages passed the test with no problem.

**login html test**
![alt text](./myonlinerecipes/static/documentation//testing/login_html_test_pass.png "error fixed.")

**sign Up html test**
![alt text](./myonlinerecipes/static/documentation//testing/signup_html_test_pass.png "error fixed.")

**myrecipe html pages test**
![alt text](./myonlinerecipes/static/documentation//testing/myrecipes-html-test-pass.png "error fixed.")


### CSS Validation

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator) was used to validate the style.css file.

There were no errors to show so I did not have to fix anything:

![alt text](./myonlinerecipes/static/documentation//testing/css_validation.png "error fixed.")
<br>

### **Python File**
[pep8online.com](http://pep8online.com/) was used to check whether the app.py Python file was PEP8 compliant.

There were **4 errors** saying that the lines were too long.

![alt text](./myonlinerecipes/static/documentation/testing/fail_PP8.png "Screenshot of pep8online.com's results showing 4 errors.")
<br>

So I close the if statement in extra () and shorten it and that **Fixed the errors**

![alt text](./myonlinerecipes/static/documentation/testing/pass_PP8.png "Screenshot of pep8online.com's results showing 4 errors.")
<br>

### **Check Python error**

I also test the website with [infoheap](https://infoheap.com/python-lint-online/) Python linter and it showed the following error:

![alt text](./myonlinerecipes/static/documentation/testing/fail_error_test.png "Screenshot of infoheap Python linter results.")
<br>
In reality f-strings is not an error it is just a new way for formatting a string in python but probably the website have not been updated. so I just deleted it and add + signs to format the strings with variables, after that, the ** error was fixed **.

![alt text](./myonlinerecipes/static/documentation/testing/pass_error_test.png "Screenshot of infoheap Python linter results.")
<br>

### Manual Testing
The recipe website has been tested in the following browsers:
- Chrome Version 85.0.4183.121 
- Samsung Internet Version 12.0.1.47	
- Microsoft Edge Version 85.0.564.63 
- Opera 70
- Mozilla Firefox 81.0.1

The recipe website and functions as expected on Samsung Internet, Google Chrome, Microsoft Edge, Opera and Firefox.
<br>

### Responsiveness
The game was tested for responsive design using [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools).  
It was tested, and found to respond appropriately with regard to each of the following:

**Mobile devices:**
- Moto G4
- Galaxy S5
- Pixel 2
- Pixel 2 XL
- iPhone 5/SE
- iPhone 6/7/8
- iPhone 6/7/8 Plus
- iPhone X

**Tablet devices:**
- iPad
- iPad Pro
- Surface Duo
- Galaxy Fold

**Laptop dimensions:**
- 15" Laptop (1024 x 800)
- 13" Laptop (1024 x 800)

**Desktop dimensions:**
- 24" Desktop (1920 x 1200)
- 22" Desktop (1680 x 1050)
- 20" Desktop (1600 x 900)

<br>
## Navigation bar (Navbar)

## Navigation in (footer)

All functionality for the footer was manualy tested on every page.

* Visit all links within the navbar in every possible order to ensure they are functional and route correctly.

## Enquire Form
*Ensure all placeholders has its appropriate name.
*Ensure Full Name field accepts any value, but requires at least one character to be deemed valid.
*Ensure Subject field accepts any value, but requires at least one character to be deemed valid.
*Ensure Message field accepts any value, but requires at least one character to be deemed valid.
*Ensure Email field only accept values in appropriate email format and cannot leave it in blank.
*Ensure all input request are met before submitting the form.
*Ensure users received the nice and tidy message after submitting the form.

<br>
<br>

## Error during Development and Fixes

I encounter the following error during **developemt**:

![alt text](./myonlinerecipes/static/documentation/testing/error_duplicate.png "Screenshot of error_duplicate.")
<br>

This error appear because I had the value unique=true in my models so when I added even empty values more than 1 the error was apearing. so I deleted and **there were no error anymore**.

## Error during **Deployment**
I encounter the following error during ployment:

![alt text](./myonlinerecipes/static/documentation/testing/sqlalchemy_dialects_postgres_error.png "sqlalchemy dialects postgres error.")
<br>

 Looking fo solution for this problem on [Stack Overflow](https://stackoverflow.com/), and in other websites. but I finally I manged to find it in the actual [heroku website](https://dashboard.heroku.com/).

![alt text](./myonlinerecipes/static/documentation/testing/heroku_recomendation.png "sqlalchemy dialects postgres error.")
<br>
Basically SQLAlchemy 1.4.x has removed support for the postgres URI scheme, and as defaul heroku has that url scheme. so to fix the problem I follow heroku recomendation and added the following code.

![alt text](./myonlinerecipes/static/documentation/testing/my_fixes_from_heroku.png "sqlalchemy dialects postgres error.")
<br>

After that the **Problem was fixed**

####  Testing user story

As a potential MyOnlineRecipes site user I want to be able to:

&#9745; mmediately comprehend the purpose behind the MyOnlineRecipes site and view some of the recipes.

![alt text](./myonlinerecipes/static/documentation/testing/home_page.png "home page.")
<br>

&#9745; Navigate throughout the site with eases.

![alt text](./myonlinerecipes/static/documentation/testing/navbar.png "navbar.")
<br>

&#9745; Easily create an account and sign in to it..

![alt text](./myonlinerecipes/static/documentation/testing/signUp.png "signUp.")
<br>

![alt text](./myonlinerecipes/static/documentation/testing/login.png "login.")
<br>

&#9745; Log out of my account once finished on the website.

![alt text](./myonlinerecipes/static/documentation/testing/logout.png "logout.")
<br>

&#9745; Contact admin with queries or feedback.

![alt text](./myonlinerecipes/static/documentation/testing/contact.png "contact.")
<br>


*** As a returning or registered user**

As a registered user of MyOnlineRecipes site I want to be able to:

&#9745; Save private recipes that only I can see..

![alt text](./myonlinerecipes/static/documentation/testing/private.png "private.")
<br>

&#9745; Have the option to share my recipes with other users.

![alt text](./myonlinerecipes/static/documentation/testing/public.png "public.")
<br>

&#9745; Create my own recipes.

![alt text](./myonlinerecipes/static/documentation/testing/add_recipe.png "add_recipe screenshoot.")
<br>

&#9745; Edit the recipes I have added..

![alt text](./myonlinerecipes/static/documentation/testing/edit_recipe.png "edit_recipe screenshoot.")
<br>

&#9745; Delete the recipes I have added..

![alt text](./myonlinerecipes/static/documentation/testing/delete.png " delete.")
<br>

&#9745; Have a rich text editor which enable me to writing beatiful content.

![alt text](./myonlinerecipes/static/documentation/testing/rich_text_editor.png "screenshoot of text editor.")
<br>

&#9745; Comments on recipes, so I can share my opinion with other users.

![alt text](./myonlinerecipes/static/documentation/testing/social_media.png "social_media screenshoot.")
<br>


***Site Owner**

&#9745; Provide the user with a beatiful image cover in case they decide not put add an image to the recipes..

![alt text](./myonlinerecipes/static/documentation/testing/image-cover.png "image-cover screenshoot.")
<br>

&#9745; Provide site members with the ability to search the site for a specific recipes by entering the title or Ingridients into a search box within the site.

![alt text](./myonlinerecipes/static/documentation/testing/search-box.png "search-box screenshoot.")
<br>

![alt text](./myonlinerecipes/static/documentation/testing/search-functionality.png "search-box screenshoot.")
<br>


## Deployment
### How to run this project locally

To run this project on your own Integrated Development Environment ensure that the 
following are installed on your machine:

- PIP
- Python 3
- Git

- Download postgresq (Refer to the [postgresq](https://www.postgresql.org/download) for more help.)

<br>

### To clone the repository:
1. Log in to Github.

2. Navigate to the main page of the repository.

3. Select the Code button from the navigation bar below the repository title.

![alt text](./myonlinerecipes/static/documentation/testing/github-clone-repo.png "Clone or Download Menu in GitHub.")

<br>

4. Under the heading Clone select 'HTTPS'

5. Click the image of a clipboard to the right of the URL in order to copy the address.

6. Open a terminal window in your selected IDE.

7. Navigate to the desired directory in which you wish to place the cloned directory.

8. Type git clone, space, and then paste the copied URL.

```
git clone https://github.com/Gersondelacruzdeveloper/myBookOfRecipes.git
```
9. Press 'Enter' to create the clone.

(Alternative you can select "Download ZIP" from the dropdown menu, extract the zip file to your chosen folder and use your IDE of choice to access it.)

<br>
11. Within your terminal window install the required dependencines needed to run the application using the following command:

```
$ pip3 install -r requirements.txt
```
12. Initialize virtual environment by typing the following command into the terminal:
```python
py -m venv virtual
```
14. Within your IDE create a file to hold your environment variables and call it env.py.


import os
os.environ.setdefault("IP", "0.0.0.0" )
os.environ.setdefault("PORT", "5000" )
os.environ.setdefault("SECRET_KEY", "SECRET_KEY" )
os.environ.setdefault("DEBUG", "True" )
os.environ.setdefault("DATABASE_URL", "YOUR_DATABASE_NAME")
os.environ.setdefault("DEVELOPMENT", "True" )
os.environ.setdefault("MAIL_PORT", "587")
os.environ.setdefault("MAIL_USERNAME", "YOUR_EMAIL" )
os.environ.setdefault("MAIL_PASSWORD", "YOUR_MAIL_PASSWORD")

15. Add your .env file to your .gitignore file.

16. You will then be able to run the app locally by typing 
```python
python run.py

```
## Heroku Deployment

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

<br>

### Deployment procedure followed:
1. Navigated to the [Heroku](https://www.heroku.com/) site.
2. Logged in to the site.
3. Created a new app on the Heroku website by clicking the "New" button on the dashboard. 
![alt text](documentation/readme-images/heroku-new-app-button.png "New App button in Heroku.")

<br>

4. Named the Heroku App and set the region to Europe.

5. 'Deploy' was selected from the dashboard of the newly created application.  In the 'Deployment method' section GitHub was selected.
![alt text](documentation/readme-images/heroku-deploy-to-github.png "Deploy to GitHub in Heroku.")

 Making sure that the correct GitHub profile was displayed, myBookOfRecipes repository was entered into the search box.

 7. When found, the button 'Connect' was clicked.

|Key            |Value                  |
|:--------------|:----------------------|
|IP	            |0.0.0.0                |
|PORT           |5000                   |
|DATABASE_URL	  |Heroku will generate one for you|
|SECRET_KEY	    |<secret_key>      |
|MAIL_PASSWORD  |<your_password>   |
|MAIL_PORT       |587           |
|MAIL_USERNAME   |<your_email>  |
|debug           |False

<br>


9. In the Heroku dashboard within the 'Deploy' tab, the 'Master' branch was selected in the 'Manual Deployment' section.

10. Clicking on the 'Deploy Branch' button successfully deployed the site.

---
## Credits

### Content

* All text used throughout the site was written by me.
* All general development concepts were devised by me.

### Media

* All images for the site were taken from  [jamieoliver](https://www.jamieoliver.com/recipes/)

## Code

* HTML/CSS: Implementation and utilisation of Grid CSS layout was assisted by [CSS-Tricks](https://css-tricks.com/snippets/css/complete-guide-grid/).
]
* HTML/CSS: Implementation and utilisation of Grid CSS layout was assisted by [W3school](https://www.w3schools.com/css/css_grid.asp).

---

## Acknowledgements

- [Code Institue](https://codeinstitute.net/) and the very helpful tutors.
- My project mentor [Gurjot Singh](https://www.linkedin.com/in/gurjot-singh-64466b199/) for his help and guidance during the design and build process. 
- The [Code Institue](https://codeinstitute.net/) community on [Slack](code-institute-room.slack.com) for their support.

<br>

# Disclaimer

This Portfolio is for educational purposes only.

---