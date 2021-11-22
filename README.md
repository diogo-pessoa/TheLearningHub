<h1 align="center">The Learning Hub</h1>

[![Build Status](https://app.travis-ci.com/diogo-pessoa/TheLearningHub.svg?branch=main)](https://app.travis-ci.com/diogo-pessoa/TheLearningHub)

[View the live project here.](https://the-learning-hub-prod.herokuapp.com)

## Description

The goal of this project is to provide a platform for content creators to share and connect with their readers. The web page provides a mix of free and premium. It gives the user a taste of what the writer has to offer.

#### For the content manager, the platform provides:

* **A blog section** — Content creator can regularly release articles, control the accessibility (free, registered or premium). Add a topic and extra tags, correlate articles with other site content. 
* **A virtual classroom** — Content creator can publish recorded video classes or as part of the full course, limiting access to the public.
* **Course path** — As a content manager, the site provides the ability to group the content (articles, classes) into a single course path, to help guide users to mastering the content. 


#### There are three options for the users to explore the content:

* **Anonymous access**, user can read all free articles and related discussion 
* **Registered user**, provides access to all free content. The user has its personal space with a list of favorite content and saved notes; Once registered, the user can also Subscribe to the premium plan for extra content. 
* **Premium access**, monthly subscription model. Unlock access to all the site content for as long as the subscription is active.

#### The pricing model and Value to the Content Owner:

While selling his premium content, a site owner can connect to his public, understanding their needs and doubt and ever evolving this content. Provides different access to content, by selling single courses for more advanced users and also more guided course paths to beginners. All that while creating a distinct brand for content.

#### The value for the user:

By providing different levels of access to content, the Learning Hub platform has something for every user. As a registered user, she enjoys a whole set of features that will allow her to develop new skills. Taking her time to select the premium content that has most value to her.

## User Experience (UX)
-   ### User stories
    [UserStories.md](UserStories.md)
-   ### Design
    -   #### Colour Scheme
            - From Bootswatch (sandstone)[https://bootswatch.com/sandstone/]
    -   #### Typography
        -   The Montserrat font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Montserrat is a clean font used frequently in programming, so it is both attractive and appropriate.
    -   #### Imagery
        -   Imagery is important. The large, background hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.

*   ### Wireframes

    -   Home Page Wireframe - [Desktop](readme_resources/wireframes/Desktop)
        - [Home](readme_resources/wireframes/Desktop/Home.png)
        - [Article](readme_resources/wireframes/Desktop/Article.png)
        - [Profile_landing](readme_resources/wireframes/Desktop/Profile_landing.png)
        - [Search](readme_resources/wireframes/Desktop/Search.png)
        - [Video_class](readme_resources/wireframes/Desktop/Video_class.png)
    
    -   Mobile Wireframe - [Mobile](readme_resources/wireframes/Mobile)
        - [Home](readme_resources/wireframes/Mobile/Home.png)
        - [Article](readme_resources/wireframes/Mobile/Article.png)
        - [Profile_landing](readme_resources/wireframes/Mobile/Profile_landing.png)
        - [Search](readme_resources/wireframes/Mobile/Search.png)
        - [Video_class](readme_resources/wireframes/Mobile/Video_class.png)
    
## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [PyCharm:](https://www.jetbrains.com/pycharm/)
    - A fully featured Python IDE, with great support for code syntax, test frameworks and version control integration
    
2. [Bootstrap4:](https://getbootstrap.com/)
    - To leverage the grid system and build a responsive interface.  
    
3. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](readme_resources/wireframes) during the design process.
    
4. [Draw.io:](https://app.diagrams.net/)
    - Draw.io was used to create the Entity Relationship [diagram](readme_resources/TheLearningHub_ER.jpg) during the design process.
    
5. [Google Fonts:](https://fonts.google.com/)
    
6. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
7. [jQuery:](https://jquery.com/)
    - jQuery to support advanced feature on Bootstrap   

8. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
    
9. [django](https://www.djangoproject.com/)
    - [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) to manage forms on this project.
10. [heroku](https://heroku.com/) 
     - Is used to host application in the cloud providing scalability and availability. 

11. [postgres](https://www.postgresql.org/)
     - Relational database used to store application content.

12. [gunicorn](https://gunicorn.org/)
     - Web server used to host Django web framework 

13. [TinyMCE](https://www.tiny.cloud/get-tiny/self-hosted/)
     - Used to provide content manager with better experience when writing content for Articles 

14. [travis.com](https://app.travis-ci.com/) - Run automated tests from codebase.
    1. Test information on [Testing.md](Testing.md#8)

15. [Stripe](https://stripe.com/) - A fully integrated suite of payments products
    1. Deployment details on [Deployment.md](Deployment.md#L66)
16. [AWS S3](https://aws.amazon.com/s3/pricing/) - A powerful Object storage for distributed content Delivery 
    1. Deployment details on [Deployment.md](Deployment.mdL85)
    

## Testing

[Testing](Testing.md)

## Deployment

[Deploy](Deployment.md)

## Credits

### Code

- Using `whitenoise` to setup local server static content on Heroku based on [Heroku-devcenter](https://devcenter.heroku.com/articles/django-assets)
  - only in use on Development Mode. 
  - Staging and Production are new Using AWS S3 Bucket as backend

- quick way to generate random keys for Django's `SECRET_KEY`. [Source Blog Post](https://tech.serhatteker.com/post/2020-01/django-create-secret-key/).
  - Used to generate random keys on each travis build

- Setting up the subscription integration with Stripe following this process [here](https://stripe.com/docs/billing/integration-builder)

### Content

-
-

### Media

-

### Acknowledgements


### Future features (These won't be available on Project submission due to time constraints)

- Create Stripe Product integration through the LearningHub Content Manager interface
  - Stripe provides an API to create products and prices, This provides a nice to have feature where Site owner can do it through the Learning hub interface. Not needing to navigate to Stripe to create new Products, more information [here](https://stripe.com/docs/api/products)

- Cancel subscription at the end of billing period
  - Stripe provides support to  `cancel at end of Billing Period` description: After canceling, customers can still renew subscriptions until the billing period ends.
  - For that the toggle on theLearningHub database needs to happen at end of subscription period. 
    - such thing can be achieved with a background scheduler, doing some research there are some schedulers for [django](https://django-background-tasks.readthedocs.io/en/latest/) 
 
