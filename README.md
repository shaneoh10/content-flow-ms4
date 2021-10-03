# Website for Content Flow

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
