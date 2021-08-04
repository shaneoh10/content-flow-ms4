# Website for Content Flow

## Code Institute Milestone Project 4 : Full Stack Frameworks with Django

Content Flow is an online community where users can view and share content in a variety of different categories. Registered users will be able to follow categories and other users of their choice and they will also be able to reward each other with tokens, via their posts. The website will allow users to purchase tokens using the Stripe Authentication Software and users will also be able to convert and withdraw their tokens as cash for financial gain.

The website will feature a landing page with information about the community and how it works, encouraging users to sign up. Users will be able to view the main website and content without signing up, however, they will need a registered account to access the full experience. (post content, comment, likes, send/receive rewards etc.) The website will make use of HTML, CSS and JavaScript for the front end and Python with the Django Framework for the backend. It will also incorporate a PostgreSQL relational database system with full CRUD functionality.

A link to the live website can be found [here.](#)

## Table of Contents

- [User Experience (UX)](#ux)

## UX

### Strategy

The website for Content Flow is not going to be designed with a specific set of users in mind. As the website will be a place for anyone to view and share content, I want it to appeal to anyone who uses the internet to view content and users will then be able to customise their own experience on the site by filtering content based on their own interests. Upon visiting the website for the first time, users should immediately recognise the purpose of the website and it should not take them long to decide if it is of interest to them or not.

Users will be able to intuitively navigate around the website and view content in categories of their choice. For convenience, users will be able to search for specific categories and posts and they will be able to sort content by date or by most popular. Logged in users will have access to more features such as creating posts, commenting on posts, liking posts, sending/receiving rewards and they will also be able to customise their own content feed by following their favourite categories and users. Admin users will have the ability to edit and delete any post on the website and they will have full CRUD power over the site.

As there is no specific demographic of users - a user is anyone who wants to view or post content online - the user stories are split into first time user, general user, logged-in user and administrator.

User Story No. | As a User | I want to be able to | So that I can | Complete
--------------|-----------|----------------------|---------------|--------------
1|First Time User|immediately recognise the purpose of the site|decide if I am interested in using the site or not|
2|General User|easily navigate the website on various devices|browse the website without feeling lost or confused|
3|General User|view a list of post categories|choose which categories I am interested in|
4|General User|view all posts in a specific category|view the posts I am interested in|
5|General User|view individual posts|see all post details (comments, author, likes and date posted)|
6|General User|sort posts by date / popularity|view most recent or most popular posts|
7|General User|search the website|find and view specific posts, categories and users|
8|General User|easily register a new account|have the full website experience and contribute to the community|
9|Logged In User|easily log in / log out|access my own personal account|
10|Logged In User|create a new post|share content with other users and receive rewards|
11|Logged In User|comment on a post|personally respond to a post|
12|Logged In User|like a post|express that I like the content of the post|
13|Logged In User|follow users/categories|view content that I am interested in on my own personal feed|
14|Logged In User|send rewards to users for their posts|reward a user for posting good quality content|
15|Logged In User|receive rewards from users for my posts|be rewarded by other users for posting good quality content|
16|Logged In User|buy tokens with credit/debit card|add tokens to my account balance|
17|Logged In User|withdraw tokens with credit/debit card|convert my tokens to cash and withdraw to my bank account|
18|Logged In User|view order details when buying or withdrawing tokens|review my purchase/withdrawal|
19|Logged In User|receive email confirmation for purchases/withdrawals|keep record of successful transactions|
20|Logged In User|have a personal profile|view and customise my personal profile and account details|
21|Logged In User|edit/delete my own posts|edit any errors or remove my post completely|
22|Logged In User|reset password|access my account if I forget my password|
23|Logged In User|delete my account|delete my account if I no longer wish to use the website|
24|Administrator|edit/delete any posts|moderate the website / remove inappropriate content|
