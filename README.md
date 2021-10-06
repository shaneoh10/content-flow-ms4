# Website for Content Flow

![Content Flow Mockup](assets/images/content-flow-mockup.png)

## Code Institute Milestone Project 4 : Full Stack Frameworks with Django

Content Flow is an online community where users can view and share content in a variety of different categories. Registered users will be able to follow categories and other users of their choice and they will also be able to reward each other with tokens, via their posts. The website will allow users to purchase tokens using the Stripe Authentication Software and users will also be able to convert and withdraw their tokens as cash for financial gain.

The website will feature a landing page with information about the community and how it works, encouraging users to sign up. Users will be able to view the main website and content without signing up, however, they will need a registered account to access the full experience. (post content, comment, likes, send/receive rewards etc.) The website will make use of HTML, CSS and JavaScript for the front end and Python with the Django Framework for the backend. It will also incorporate a PostgreSQL relational database system with full CRUD functionality.

A link to the live website can be found [here.](https://content-flow-ms4.herokuapp.com/)

## Table of Contents

- [User Experience (UX)](#ux)

## UX

### Strategy

The website for Content Flow is not going to be designed with a specific set of users in mind. As the website will be a place for anyone to view and share content, I want it to appeal to anyone who uses the internet to view content and users will then be able to customise their own experience on the site by filtering content based on their own interests. Upon visiting the website for the first time, users should immediately recognise the purpose of the website and it should not take them long to decide if it is of interest to them or not.

Users will be able to intuitively navigate around the website and view content in categories of their choice. For convenience, users will be able to search for specific categories and posts and they will be able to sort content by date or by most popular. Logged in users will have access to more features such as creating posts, commenting on posts, liking posts, sending/receiving rewards and they will also be able to customise their own content feed by following their favourite categories and users. Admin users will have the ability to edit and delete any post on the website and they will have full CRUD power over the site.

As there is no specific demographic of users - a user is anyone who wants to view or post content online - the user stories are split into first time user, general user, logged-in user and administrator.

User Story No. | As a User | I want to be able to | So that I can | Complete
--------------|-----------|----------------------|---------------|--------------
1|First Time User|immediately recognise the purpose of the site|decide if I am interested in using the site or not| :heavy_check_mark:
2|General User|easily navigate the website on various devices|browse the website without feeling lost or confused| :heavy_check_mark:
3|General User|view a list of post categories|choose which categories I am interested in| :heavy_check_mark:
4|General User|view all posts in a specific category|view the posts I am interested in| :heavy_check_mark:
5|General User|view individual posts|see all post details (comments, author, likes and date posted)| :heavy_check_mark:
6|General User|sort posts by date / popularity|view most recent or most popular posts| :heavy_check_mark:
7|General User|search the website|find and view specific posts, categories and users| :heavy_check_mark:
8|General User|easily register a new account|have the full website experience and contribute to the community| :heavy_check_mark:
9|Logged In User|easily log in / log out|access my own personal account| :heavy_check_mark:
10|Logged In User|create a new post|share content with other users and receive rewards| :heavy_check_mark:
11|Logged In User|comment on a post|personally respond to a post| :heavy_check_mark:
12|Logged In User|like a post|express that I like the content of the post| :heavy_check_mark:
13|Logged In User|follow users/categories|view content that I am interested in on my own personal feed| :heavy_check_mark:
14|Logged In User|send rewards to users for their posts|reward a user for posting good quality content| :heavy_check_mark:
15|Logged In User|receive rewards from users for my posts|be rewarded by other users for posting good quality content| :heavy_check_mark:
16|Logged In User|buy tokens with credit/debit card|add tokens to my account balance| :heavy_check_mark:
17|Logged In User|withdraw tokens as cash|convert my tokens to cash and withdraw to my bank account| :heavy_check_mark:
18|Logged In User|view order details when buying or withdrawing tokens|review my purchase/withdrawal| :heavy_check_mark:
19|Logged In User|receive email confirmation for purchases/withdrawals|keep record of successful transactions| :heavy_check_mark:
20|Logged In User|have a personal profile|view and customise my personal profile and account details| :heavy_check_mark:
21|Logged In User|edit/delete my own posts|edit any errors or remove my post completely| :heavy_check_mark:
22|Logged In User|reset password|access my account if I forget my password| :heavy_check_mark:
23|Logged In User|delete my account|delete my account if I no longer wish to use the website| :heavy_check_mark:
24|Administrator|edit/delete any posts|moderate the website / remove inappropriate content| :heavy_check_mark:

### Scope

After analysing the user stories, I have decided on the following features as my intitial minimum scope.
- Responsive design
- Landing page with information about the website
- User account registration & login/logout functionality
- All users able to view posts with ability to view by category and filter by date/popularity
- Registered users able to create, edit and delete posts of their own
- Registered users able to like and comment on posts an follow specific users/categories
- Registered users able to purchase tokens to reward other users for their posts
- Search functionality to search for posts, categories and users
- Administrators will have full CRUD control to moderate the entire website

### Structure

I did some research on various blogs, social media sites and content sharing sites to get an idea of what kind of designs users are familiar with. Most of these websites shared a similar pattern of a navbar containing a user icon and a search bar at the top of the page and a content feed below it. Some sites also have a text field above the content feed to allow users to create a post instantly and some had some extra content or links to the side of the content feed. On most of the sites that I visited, the purpose of the website is immediately evident, so I decided to base my design around these websites so that users will have a sense of familiarity when visiting. This familiarity will also prevent any steep learning curve that may throw users off using the website.

Another thing I noticed while doing research is that there are a lot of advertisements and promoted content on most of the websites I visited, which I found quite annoying and distracting. I feel the exclusion of this content in my own website will provide users with a friendlier and more enjoyable experience for them while they are browsing through the website content.

The entire website is designed to be easy to navigate with all information presented in a clean manner so that users will have a familiar and enjoyable experience.

I have structured the website with:
- A navbar at the top of the page with a brand logo on the left and nav-items to the right which is common to most websites. The navbar will contain a searchbar for users to search the website
- A collapsible navbar for smaller screens
- Navbar common to all pages - items displayed in navbar depending on user status (log in will not be available for a user already logged in etc.)
- Main content will have a simple layout written with Bootstrap for structure and responsive design
- Landing page, register, login and content pages accessible by all users of the website
- User account settings, user profile, create post, purchase token pages only accessible to logged in users. Unauthorized users trying to access will be prompted to log in.

### Skeleton 

I designed wireframes for desktop, tablet and mobile using Balsamiq. These wireframes can be viewed [here.](https://github.com/shaneoh10/content-flow-ms4/tree/main/assets/wireframes)

### Surface

#### Colours

I decided to use a neutral colour palette for the website so as not to distract users from the main content and to keep the user interface clean. For the user interaction buttons, I decided to use the blue bootstrap primary colour for positive interactions (add post, sign in, follow etc.) and the red bootstrap danger colour for negative interactions (delete etc.). This makes it easier for users to distinguish between which type of action they are trying to take and it provides a good contrast from the neutral colour palette so the buttons stand out well.

- #FAFAFA - Cultured (Off-white)
- #DBDFF0 - Lavendar Web
- #E6F2FF - Alice Blue
- #007BFF - Azure (Bootstrap primary)
- #DC3546 - Rusty Red (Bootstrap danger)

#### Typography

I chose 'Arial' as the main font for the project as it is clean and easy to read, making it a good choice for a website where users will be spending a great deal of time reading through content.

## Database Schema

The project uses a PostgreSQL relational database consisting of the django allauth User model and 7 models created by myself.

### Database Structure

#### Category

Name              |Field Type                                                
------------------|---------------
category_name     |SlugField                                              
description       |CharField                                    
image             |ImageField                                    
followers         |ManyToManyField(User)

#### Post

Name              |Field Type                                                
------------------|---------------
title             |SlugField                                              
image             |ImageField                                    
author            |ForegnKey(User)                                    
body              |RichTextField
category          |ForeignKey(Category)
post_date         |DateTimeField
likes             |ManyToManyField(User)

#### Comment

Name              |Field Type                                                
------------------|---------------
post              |ForeignKey(User)                                              
author            |ForeignKey(User)                                    
body              |TextField(User)                                    
comment_date      |DateTimeField
likes             |ManyToManyField(User)


#### UserProfile

Name              |Field Type                                                
------------------|---------------
user              |AutoOneToOneField(User)                                              
bio               |TextField                                   
image             |ImageField                                    
followers         |ManyToManyField(User)
tokens_score      |IntegerField
tokens_balance    |IntegerField

#### Product

Name              |Field Type                                                
------------------|---------------
name              |CharField                                             
icon_url          |CharField                                   
tokens            |IntegerField                                    
price             |IntegerField
display_price     |FloatField

#### Order

Name              |Field Type                                                
------------------|---------------
order_number      |CharField                                             
card_name         |CharField                                   
username          |CharField                                    
email             |EmailField
date              |DateTimeField
tokens            |IntegerField
order_total       |DecimalField

#### Withdrawal

Name              |Field Type                                                
------------------|---------------
order_number      |CharField                                             
account_name      |CharField                                   
iban              |CharField                                   
username          |CharField                                    
email             |EmailField
date              |DateTimeField
tokens            |IntegerField
withdrawal_total  |DecimalField

### Database Relationships

The image below represents all the database models and the relationships they share.

![DB relationships](assets/images/content-flow-db-schema.jpg)

## Features

The website features a landing page which provides a description of the website and its features, prompting users to sign up. Users also have the option to view the content without signing up but they are limited to only viewing posts and profiles. After users have signed up to the website, they will have full access to the features of Content Flow (add posts/comments, like posts/comment, follow users/categories, send/receive rewards, buy tokens, custom profile). All new accounts will be set up with standard level access which limits the users to only editing or deleting posts or comments created by their own account. This is to ensure that users do not interfere with content that they do not own. Superuser accounts have the ability to edit or delete all posts/comments on the website to ensure the any inappropriate content or misinformation can be edited or deleted by website moderators/admins. User accounts can be upgraded to superuser via the django admin dashboard.

### Across all pages:
- The navbar is visible at the top of the page across all pages of the website. The navbar has the Content Flow logo on the left and there are navigation items on the left and right hand side of the navbar. The navigation items displayed can change and are dependant on whether the user is logged in or not. The navbar collapses into a hamburger icon on smaller screens.
- There is also a search bar in the navbar which allows users to enter a search query and returns results based on the query.

### Home Page:

#### Header
- There is a high quality image of people sitting at a table using laptops and phones, which makes it apparent to users that the website has a social aspect to it.
- A main heading and logo quickly draws the user's attention to the center of the page and provides them with a brief description of the website
- There are two buttons below the heading, Sign up and Learn More. These buttons encourage users to either sign up immediatedly or read more about the website before choosing to sign up.
- There is a smaller link for to log in below these buttons if the user already has an account. This is smaller in size so as not to distract potential new users from the main content.

#### About Section
- This section contains colourful icons and a description of how the website works to encourage users to sign up. The descriptions are brief but contain sufficient information to allow users to understand how the website works.
- Below the descriptions there are buttons that allow users to either sign up or view the content posted to Content Flow.

#### Footer
- Located at the bottom of the page, this contains links to sign up, view all posts, log in and go back to the top. It also contains a copyright notice.
- The footer is only displayed on the home page as it could be distracting to users while browsing content and there are enough links available to users in the navbar so they should not feel lost while browsing.

### Sign Up:
- This page contains a sign up form for new users to create an account. The user registration is handled by the django allauth app, which checks all the user inputs from the form and either creates a new account if the information is valid or alerts the user to any errors they have made in the form (username already exists, password does not meet criteria etc.). Upon successful registration users will be redirected to an email verification page, prompting the user to check their email for a verification link. When the user succesfully verifies their email, their account is then activated and they are redirected to a log in page.
- Below the sign up form is a link to log in for users that already have an account and may have accidentally clicked on the sign up page.

### Log In:
- The log in links around the website will bring up a log in modal for users to enter their credentials to log in. The log in credentials are handled by django allauth, and if the credentials are correct the user will be redirected to the All Posts page and notified with a toast that they are logged in. If the credentials are incorrect, the user will be redirected to another log in page which will notify the user of the log in error (username/password incorrect etc.). The user can now attempt to log in again from this login page.
- On both the log in page and log in modal, there are links for a password reset page if the user has forgot their password and there is a link to the sign up page if the user does not have an account and wants to create one.

### Log Out:
- When users click the log out button, a modal will open prompting the user to confirm the log out. When the log out is confirmed, the form is handled by django allauth which will redirect the user back to the home page and notify them with a toast that they have been logged out.

### Account Settings:
- The account settings page can be accessed by users with a verified account. This page shows the user's current profile image, token balance, and contains a form for users to update their proifile image and their user bio. Users can select a new image to upload and change the text in their bio and these changes will be updated when the update account button is pressed, providing the form is valid.
- Below the update account form there are three buttons: withdraw tokens, change password, delete account. The withdraw tokens button redirects users to the withdraw tokens page. The change password button redirects to a change password page which is handled by django allauth. The delete account button opens a modal, which asks users to verify that they want to delete their account and if this is confirmed their account will be deleted from the database.

### User Profile:
- Each verified user will have thier own user profile page and this page can be viewed by users with or without an account. This page displays any posts created by the user who's profile you are viewing and it also displays their profile image and user bio on a card to the side. Logged in users will have access to a follow button if the profile is not their own, and that follow button is replaced with a settings button if it is the user's own profile.
- The follow button allows users to 'follow' another user which will add any posts created by that user to the current user's custom feed page. If the current user is already following the user the button is replaced by an unfollow button which performs the reverse of the follow button.

### All Posts:
- This page displays all the posts that have been uploaded to the database and can be viewed by users with or without an account. Each posts is displayed on a card displaying the posts title, body, author, category, number of likes and the time since posted. The body of the post is sliced to a max of 150 characters to save screen space and if the post contains an image that is also dispyed on the card.
- At the top of the page there are buttons to filter the posts by New(most recently posted) and Top(highest number of likes). Logged in users will also have access to the Add Post button which redirects them to the Add Post page.

### Categories:
- Each category on the website has its own page which has the same layout as the all posts page but only posts within that category are displayed. For example, if a user adds a new post with News selected as the category, that post will appear on the News category page. All users with or without an account can view the category pages. Logged in users will have access to a follow button which will add any posts in the selected category to their custom feed.
- Logged in users can add a new category to the website via the Add Category page. This page contains a form which requires a unique category name, an optional image, and a description. If the form is valid the new category will be uploaded to the database and it will be automatically added to the list of categories to choose from when adding a post or choosing a category page to view.

### Add Post:
- This page contains a form to upload a new post to the website and is only accessible by logged in users. The user must choose a title, select a category, and add text to the textfield. The user also has the option to upload an image with the post but that is not a requirement for the form to be valid. Their is a text editor built in to the textfield so that the user can add some basic editing and formatting to their post to make it more legible to other users.
- When a new post is added, the post appears on the all posts page, the category page for the specified category of the post and on the profile page of the user who created the post.

### Edit Post:
- This page contains a form to edit an existing post and is only accessible by logged in users. The form is pre filled with the existing post data and the user has the option to edit the title, category and body of the post.
- If a user tries to edit a post that they did not create, they will be notified with an error message that they can only edit their own posts and the changes will not be saved to the database. This does not apply to superusers as they have the authority to edit and delete any post on the website.

### Post Detail:
- This page contains a full detail view of an individual post and can be viewed by users with or without an account. It displays the post title at the top of the page and on a card below it displays the author, category, body, and post likes. Logged in users will have access to a like button and if it is their own post or they are a superuser they will have access to edit and delete buttons. If the post was created by a user other than themselves a send reward button will be abailable.
- There is a comment section below the post card which displays any comments and the user who posted the comment. Logged in users will have access to the add comment button and a like button for each comment. Users can delete their own comments and superusers can delete any comment.
- When a user clicks the add comment button they are redirected to the add comment page. This page contains a form with a single textfield input for the body of the comment. When the form is submitted the commented is added to the comments section on the post detail page of the post they chose to comment on.

### My Feed:
- Logged in users will have access to the custom feed page. This page displays posts to users based on the categories and users they are following. All posts from the categories and users that the current user is following will be displayed on this page for a customised experience. If the user decides to unfollow a category/user, the relevant posts will be removed from the feed and vice versa if they choose to follow more categories/users.

### Send Reward:
- Logged in users will have access to this feature. When viewing a post created by another user, the current user can send a token reward to that user. The send reward button opens up a modal where the user can decide how many tokens they want to send to the author of the post. If the current user has a sufficient balance they can submit the form and the tokens will be deducted from their own balance and added to the post authors balance. If the user does not have any tokens available in their account balance, they will be prompted to redirect to the Buy Tokens page.

### Buy Tokens:
- Logged in users will have access to this feature. There are three available options for the amount of tokens a user can purchase and when an option is chosen, the user is redirected to the checkout page. The checkout page displays the order details to the user and has a form requesting the user's card name, email and card number for payment. The payment is handled by Stripe and if successful the user is redirected to an order confirmation page containing their order details and an email with the same order details is sent to the email provided by the user. Any form or card errors will be displayed on screen to the user.
- When Stripe sends a webhook to confirm succesful payment, the tokens are then added to the users token balance on their user profile.

### Withdraw Tokens:
- Logged in users will have access to this feature. This allows users to withdraw any tokens they have in their tokens balance to their bank account as cash, provided they have the minimum withdrawal amount of 1000 Tokens. The withdrawal form asks users for the amount of tokens they want to withdraw, their bank IBAN, the account name and an email. For the purpose of the project the IBAN field of the form is set to a sample IBAN and set to readonly. When the user enters the amount of tokens they want to withdraw, the cash amount of the withdrawal is displayed at the bottom of the form so users can see the value of their withdrawal before submitting.
- When the withdrawal form is submitted, the user is redirected to a withdrawal success page which displays the withdrawal details to the user and an email with the same withdrawal details is sent to the email provided by the user. The token amount from the withdrawal is then deducted from the user's token balance.


## Technologies Used

- HTML5 - This is the main language of the website templates and content
- CSS3 - This is used to style the web pages
- Python 3 - The main applications to run the website and use CRUD functionality are written in python
- JavaScript, jQuery - Used for visual effects, interactivity, DOM manipulation, Stripe Payments
- [Bootstrap 5.0](https://getbootstrap.com/docs/5.0/getting-started/introduction/) - Bootstrap elements used for structure, design and responsive layout
- [Django](https://www.djangoproject.com/) - Web framework used to provide tools, libraries and technologies for rapid deployment and clean, pragmatic design
- [PostgreSQL](https://www.postgresql.org/) - Relational database used for deployed site
- [Stripe](https://stripe.com/docs) - Used to process payments in the project
- [CKEditor](https://ckeditor.com/) - Used for the RichTextField text editor input fields
- [django-annoying](https://pypi.org/project/django-annoying/) - Used for AutoOneToOne field and HTTPResponseReload
- GitHub - Used to store the code, linked to Heroku for automatic deployment
- Heroku - Platform used to deploy the web application
- Amazon Web Services (AWS) - Used to store static and media files for deployed site
- Gitpod - This is the IDE I used for the project
- Git - Used within Gitpod as the version control system
- Chrome Developer Tools - Used within Google Chrome to inspect the web pages. This is helpful when designing responsive features and troubleshooting bugs.
- Balsamiq - I created the project wireframes with this software
- Google Fonts - Used to import the fonts for the project
- [Font Awesome](https://fontawesome.com/) - Used to import icons
- [Techsini](https://techsini.com/) - Used this website to generate the multi-device website mockup
- [dbdiagram.io](https://dbdiagram.io/home)- Used to generate the database schema and relationships drawing