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
    - **[Done]** I want to update my profile information
      - Added Button to allow user to navigate to form to edit his profile details(first name, last_name, and bio).
      - New Form to update user details added to Profile page.
    
    - **[Done]** I want to have access to my class notes
      - In the Video class page User has access to responsive form to save and view his class notes;
      - User will later be able to see his saved notes on his Profile Page
    - **[Done]** I want access to public articles as an anonymous user.
      - any site visitor can Read Articles, to user extra features user will have to create his own profile
    - I want to have the pricing model available for review 
    - I want to be able to pay for a subscription
    - I want to cancel My subscription
    
    - I want to filter articles by topic or date(latest).
    - I want to bookmark my favorite VideoClasses same way I can do for articles.
    - I want to see the Author Page and list content by the author.
    
    
- ### As a content manager(Superuser)

    - I want access to the restricted action to publish/edit/delete content 
      - each content in browse content page the content, has a `manage content` button which allow editing or delete this object. that is only visible for content-managers
    - I want a confirmation after clicking on delete button, to avoid accidental removals.
    - I want a textarea to comfortably write and enrich the article content, with headings, paragraphs
    - I want the article content to be saved temporarily to avoid losing content if I accidentally refresh my page.
    - I want to upload images and videos to My article body.
    - I want to submit an article, but keep it as a Draft for further review before publish.
    - I want to flag some content as restricted, for access only to premium(paying) users.
    - I want to have a `Call to Action` to redirect user to Pricing and subscription button on site Landing page.
    - **[Done]** Home, About and Pricing and Site title be managed by content-Manager. 
      - The Idea is to extract the content of these pages into a Model to then convert the block content on each page with a template variable on the view context
      - Create a Form only visible to Content Manager Allowing This User to edit content directly through the Site interface, note that this will use the TinyMCE just at the [articles form](articles/forms.py) does to allow user to Edit and Preview changes.
    - I want to have a Control Panel Page with quick links to edit all Site Pages, content and create New Content.

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
  - **[DONE]** I want to have a button on Articles to allow user to bookmark content
    - Added a view on personal space to add/remove bookmarks.
    - Updated article.html template to call views. User gets a message to confirm an article was saved as bookmark
  - **[Bug - Resolved]** Removing FileBrowser from TinyMCE as implementation didn't work well on Django 3.2
    - Media Handling on Forms was an issue using TinyMCE + FileBrowser and grappeli. 
      - [Solution] Implemented a file upload form, Model and delete view to handle files uploads for Articles, home, About, etc. that will provide an option to upload custom content to site and reference it on TinyMCE Content field.

  - I want to Implement payment structure integration with [Stripe](https://stripe.com/) to support monthly subscriptions and paid access to individual classes and courses
  - I want to Store static content and Media on AWs S3/cloudfront to improve user experience and avoid issues managing content
  - I want to Add forms for Content manager to Allow Home/About/Pricing pages to be edited without a need for a change in code.
  - I want to add a Call to Action (join our premium area now) button on index page.
  - I want to the Search to support all content-types, at this point site has only Articles available and Query is directed at that Db table, when courses and Video classes are added to the system, that needs to be supported by the search.
  - I want to explore the idea of extracting the Back button and page title header into template block with request path as condition, to reduce repetition


- TODO handle Invoice paid to keep subscription active
- TODO handle Invoice unpaid to disable subscription and email user
- Dynamic, Button only shows if there's at least one strip subscription Application, `Call to Action Button` on NavBar Redirecting user to Pricing Page, selecting subscription from List.