UserStories
---

User Stories are driven by Three main user profiles: user(visitor), Content Manager and Developer(maintainer).

### A User

* Wants to navigate the site and explore its content, his main goal is to learn through video classes and articles
  available in the platform.
* For this profile the navigation has to be intuitive content easy to find aligning with simple tools to save favorite
  videos and take notes, later accessible on the private profile page.

### A Content Manager

* For User profile the private area has to be responsive and easy to upload content.
* When writing a new article it should be easy and intuitive to write it on the page, ideally saving the draft in case
  the page reloads
* when publishing new video classes, instructions have to be clear on how to add a video and organize it as part of a
  course

### Developer/Maintainer

* His goal is to produce tested, clean-code, respecting DRY and other best practices of development.
* Whenever possible I want to re-use frameworks and apps available to speed development and provide a secure solution to
  end-users
* When writing an article I want the page the content to be saved local at least until I create the article, in case of
  accidental page reloads.

## UserStories by User Profile

- ### As a user,

    - **[DONE]** I want to register and login with a personal e-mail
        - Leveraging all-auth to enable personal e-mail registration
    - **[DONE]** I want to update my password to reset my password from my profile page
      - Added Button on Profile page under User Details tab, that allows user to reach the change password page
    - **[DONE]** I want to update my update or change emails in my account from my profile page
      - Profile page, on personal details tab there's a button to redirect him to manage accounts form
    - **[DONE]** I want to have my favorites content(articles, classes, video classes ) saved to a bookmark space
      - Added Bookmarks tab under User profile, with table mapping user saved content, table has a button allowing user to navigate to content. 
        - Table has column for content type and is color-coded(each content has its own row color)
    - **[DONE]** I want to search articles by name or content.
      - On the Navigation bar on top of the page, user can at any point query content based on a words. He'll then, be redirected to browse for content page showing the results.
    - **[In-Progress]** Added Button to allow user to navigate to form to edit his profile details(first name, last_name, and bio).  
    - I want to have access to my class notes
    - I want to filter articles by topic or date(latest).
    - I want access to public articles as an anonymous user.
    - I want to update my profile information



- ### As a content manager(Superuser)

    - I want access to the restricted action to publish/edit/delete content 
      - each content in browse content page the content, has a `manage content` button which allow editing or delete this object. that is only visible for content-managers
    - I want a confirmation after clicking on delete button, to avoid accidental removals.
    - I want a textarea to comfortably write and enrich the article content, with headings, paragraphs
    - I want the article content to be saved temporarily to avoid losing content if I accidentaly refresh my page.
    - I want to upload images and videos to My article body.
    - I want to submit an article, but keep it as a Draft for further review before publish.
    - I want to flag some content as restricted, for access only to premium(paying) users.
    

- #### As a Developer

  - **[DONE]** I want to create to customize the login/signup pages from allauth based on the site base.html
      - Added `account` & `socialaccount` directories on root `templates` folder, extending base.html file
      - Created hew base.html file
      - loaded fonts awesome and Materialize Css on base.html to improve responsiveness and look of the page.

  - **[DONE]** I want to review the css and formatting of all allauth forms (login,sign-in ,sign-out , etc.) and apply site default styling.
  - **[DONE]** I want to customize The login/Signup/Sign-out page form and buttons wil the site theme and Typography
    - Pulled templates from `allauth` module, added styling and classes to it.
  - **[DONE]** I noticed the html from the article content wasn't being formatted as HTML.
      - disabling `autoescape` on the template did the trick,
          - Reference: [stackoverflow](https://stackoverflow.com/questions/19357462/django-passing-html-string-to-template)

  - **[DONE]** I want to give the user some insight on result of an action. ex: delete action without being superuser (should be
    possible as button is not rendered). User will get a warning saying why he was redirect back to /Home, letting him
    know he is not allowed to use that action.
      - Added a basic message structure on the `base.html` and views are using
        the [django message framework](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/) to add a message to
        the response.
  - **[DONE]** css and Styling centralizing title and increasing heading
    - move heading to a `col-sm` and added css class to centralize html element. 
  - I want to explore the idea of extracting the Back button and page title header into template block with request path as condition, to reduce repetition
  - I want to add a Call to Action (join our premium area now) button on index page. 
  - I want to the Search to support all content-types, at this point site has only Articles available and Query is directed at that Db table, when courses and Video classes are added to the system, that needs to be supported by the search.
  - I want to have a button on each content to allow user to bookmark content (button needs to be updated(Js) once user bookmark content)