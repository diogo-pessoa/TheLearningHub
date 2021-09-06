UserStories
---

User Stories are driven by Three main user profiles: user(visitor), Content Manager and Developer(maintainer).

### A User

* Wants to navigate the site and explore its content, his main goal is to learn through video classes and articles available in the platform.
* For this profile the navigation has to be intuitive content easy to find aligning with simple tools to save favorite videos and take notes, later accessible on the private profile page. 

###A Content Manager 

* For User profile the private area has to be responsive and easy to upload content.
* When writing a new article it should be easy and intuitive to write it on the page, ideally saving the draft in case the page reloads
* when publishing new video classes, instructions have to be clear on how to add a video and organize it as part of a course
        
###Developer/Maintainer
    
* His goal is to produce tested, clean-code, respecting DRY  and other best practices of development. 
* Whenever possible I want to re-use frameworks and apps available to speed development and provide a secure solution to end-users 
* When writing an article I want the page the content to be saved local at least until I create the article, in case of accidental page reloads.


## UserStories by User Profile

- ### As a user, 
  
    - **[DONE]** I want to register and login with a personal e-mail
       - Leveraging all-auth to enable personal e-mail registration
    - I want to reset my password to reset my password from my profile page
    
- #### As a Developer

    - **[DONE]** I want to create to customize the login/signup pages from allauth based on the site base.html
        - Added `account` & `socialaccount` directories on root `templates` folder, extending base.html file
        - Created hew base.html file
        - loaded fonts awesome and Materialize Css on base.html to improve responsiveness and look of the page. 
    - I want to customize The login/Signup/Sign-out page form and buttons wil the site theme and Typography
    - I want some padding/margin on the User Profile Icon on top-right, it's too close to edge of screen

- I noticed the html from the article content wasn't being formmated as HTML.
  - disabling autoscape on the template did the trick, 
    - Reference: [stackoverflow](https://stackoverflow.com/questions/19357462/django-passing-html-string-to-template)
      

- ### As a content manager(Superuser)
  
  - I want access to the restricted area to publish content 
