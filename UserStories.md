UserStories
---

User Stories are driven by Three main user profiles: user(visitor), Content Manager and Developer(maintainer).

### A User

* Wants to navigate the site and explore its content, his main goal is to learn through video classes and articles
  available in the platform.
* For this profile the navigation has to be intuitive content easy to find aligning with simple tools to save favorite
  videos and take notes, and later access on his own Personal space. A personal space is available to every registered User. 

### A Content Manager

* For User profile the private area has to be responsive and easy to upload content.
* When writing a new article it should be easy and intuitive to write it on the page, ideally saving the draft in case
  the page reloads
* when publishing new video classes, Form needs to be intuitive and clear, allowing an uninterrupted flow of work.

### Developer/Maintainer

* His goal is to produce tested, clean-code, respecting DRY and other best practices of development.
* Whenever possible I want to re-use frameworks and apps available to speed development and provide a secure solution to
  end-users
* When writing an article I want the page the content responsive and free of Errors and Bugs.
* Test often and release frequently to maintain the flow of feature Releases.

## UserStories by User Profile

### As a user,

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
- **[Done]** I want to have the pricing model available for review
  - Added a link to NavBar on page header to Pricing Page. 
    - The Pricing Page can be edited by the Content Manager at anytime to reflect the Stripe Subscriptions created on Stripe Dashboard.
    - [Pricing Page](https://the-learning-hub-prod.herokuapp.com/pricing)
- **[Done]** I want to be able to pay for a subscription
  - Added a `Call to Action` button, that redirects the registered User to the subscription Page.
  - The Premium Button is only available to registered Users.
  - Page to Pay for [Subscription](https://the-learning-hub-prod.herokuapp.com/products/subscriptions)
- **[Done]** I want to cancel My subscription
  - Once user is set as a Premium User the [Manage Subscription](https://the-learning-hub-prod.herokuapp.com/personal_space/) is available to him on the Personal Space.
  - If user navigates to the Sign-up page again, the page will render the `manage subscription` button, instead of allowing a new subscription.
    
- **[Done]** I want to bookmark my favorite VideoClasses same way I can do for articles.
  - I added Bookmark button to video_class Page;
  - The Personal space `Bookmarks` tab also shows video classes in the table now. The table render each content type in different colors(also adding an Icon) to help users to quickly identify the content type of each item on the list. 

### As a content manager(Staff)

- **[DONE]** I want access to the restricted action to publish/edit/delete content
  - A few options are available to Content Manager: 
  - In the browse content page, each object has a `manage content` button which allow editing or delete this object. that is **only visible for content-managers**.
  - On each Page if user is authenticated as a content manager a side menu is list the actions available to him ex: `Edit Page`.
  - If user clicks on Profile on the dropdown Menu there's a content Management Area, With Actions to Edit the Main Pages(Home, About, privacy_policy). 
  - On the Management Area there's also links to create Articles and Videos.
  
- **[DONE]** I want a textarea to comfortably write and enrich the article content, with headings, paragraphs
  - Support for TinyMCE is added to each form that supports a page or article. With that Field user has rich text Editor features available to enrich text and Add Media.
  - A File Upload form is also available on each edit Page and Articles.

- **[Done]** I want to upload images and videos to My article body.
  - File Upload form included on each Edit Page. 
  - Once file is uploaded, it shows on the page with a link and a copy to clipboard button, that link can be used to add images to the TinyMCE content Body.
  - A Toggle Info button is also available on the list of files, explaining how the user can add files to the page.
- **[Done]** I want to submit an article, but keep it as a Draft for further review before publish.
  - If the User submits the Article form with the draft flag clicked, the article is hidden from users on the search result and content browse page.
- **[Done]** I want to flag some content as restricted, for access only to premium(paying) users.
  - If `premium content` flag is set to true only Premium Users and staff members can see the content on search results.
- **[Done]** I want to have a `Call to Action` to redirect user to Pricing and subscription button on site Landing page.
  - If user is registered and authenticated then the button to sign-up for premium is added.
- **[Done]** Home, About and Pricing and Site title be managed by content-Manager. 
  - The Idea is to extract the content of these pages into a Model to then convert the block content on each page with a template variable on the view context
  - Create a Form only visible to Content Manager Allowing This User to edit content directly through the Site interface, note that this will use the TinyMCE just at the [articles form](articles/forms.py) does to allow user to Edit and Preview changes.

- **[Done]** I want to have a Control Panel Page with quick links to edit all Site Pages, content and create New Content.
  - For authenticated content-managers a link to the management area is added to the dropdown under the user section on the Navbar. From there `Content Managers` can edit main pages, update the Stripe Subscription Plans, and create new content. 

### As a Developer

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

- **[DONE]** On Files uploaded menu: add a feature to Copy text to clipboard:
  - Simple `copy to clipboard` feature example on file_upload form
    from [w3school](https://www.w3schools.com/howto/howto_js_copy_clipboard.asp)
    - Also added toggle with instructions to use the feature to make it easier to add local files to form. 

- **[DONE]** I want to Implement payment structure integration with [Stripe](https://stripe.com/) to support monthly subscriptions and paid access to individual classes
  - Using the [Products](/products) App and the [UserSubscription](products/models.py) model. There's added support to add and manage Stripe subscription and hold that information on the application Database. 
  - A new integration is available to the Product application [stripe.py](src/integrations/stripe.py), In that file are TheLearningHub Related functions to handle the webhook call from Stripe to fulfill subscription, cancel subscription, and get user_subscription status.     
  - A New View [stripe_webhook](products/views.py#L54), handles callbacks from the Stripe Api to keep the Application database consistent with the Stripe Customer_id (application user identifier on Stripe) status.
  - A New view to redirect user to Stripe [Manage Subscription Portal](products/views.py#L81)
  - View to [create a checkout session](products/views.py#L24) - redirects user to stripe portal to pay for subscription
  - A Site [Manager page to manage Stripe subscription](products/views.py#L92) products on the LearningHub Control Panel.   [Delete subscription](products/views.py#L114)
  - A [subscriptions view](products/views.py#L123), handling the `pricing.html` page and redirects to the checkout session.
- **[Done]** I want to Add forms for Content manager to Allow Home/About/Pricing pages to be edited without a need for a change in code.
  - Completed as part of the Stripe integration works. A new entry on the Control Panel allows site manage to add/remove new subscriptions. 
    
- **[Done]** I want to Store static content and Media on AWs S3 to improve user experience and avoid issues managing content
  - On Production environments Added all the proper credentials, these are handled by Environment variables in the [settings.py](TheLearningHub/settings.py#L176), If environment is not DEVELOPMENT integration is enabled. 
  - A new S3 Bucket is available to Staging and Production environment on an AWS account. 
  - [Storages_backend](TheLearningHub/storages.py) has a new Class called MediaStorage that handles S3 operations through the `S3Botostorage`.
  - All forms that handle files and videos were refactored to support both the regular filesystem and S3 backends
  - one point to note is that the files are no longer removed from the filesystem, on the S3 Bucket, a new lifecycle policy is now on set on the bucket to remove files not used for over 6 months. for More information: [object-lifecycle-mgmt](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
  
- **[DONE]** I want to add a Call to Action (join our premium area now) button on index page.
  - Added a `Sign-up for premium today` on Header page, This button will only show to registered users. 
  - If a Premium user click on the Button, The upgrade to Premium button is replaced by `Manage your Subscription`.
  
- **[DONE]** I want to the Search to support all content-types, at this point site has only Articles available and Query is directed at that Db table, when courses and Video classes are added to the system, that needs to be supported by the search.
  - That was achieved by refactoring the search view to load Both video_classes and Articles objects to the template. 
  - The Search template body is now split into three files: The [learning_area.html](home/templates/learning_area.html) and the includes [articles](htome/templates/includes/learning_area_article_cards.html), and [video_class](/home/templates/includes/learning_area_video_class_cards.html). The included templates are loading different css and Icons for each card(css class from bootswatch theme), to provide visual input for the user to identify quickly the content type he is looking for.
  - The NavNar now has a Learning area dropdown, with a search filter for Articles or videos, both leveraging the same backend view (learning_area).
  - Latest update the whole `search` view is now refactored to support the `learning_area` view. With that done the `learning_area` view is now removed and the `/learning_area/` urls points to `search`. From the user perspective the same behaviour is observed. Review tests in [test_view.py](home/test_views.py#L167) for more information. 
 
 
- **[DONE]** File upload form and Video_class form, limiting File Size on Client Size.
    - [How to upload files and images](https://www.ordinarycoders.com/blog/article/django-file-image-uploads)
    - [django file uploads](https://docs.djangoproject.com/en/3.1/topics/http/file-uploads/)
    - After some review, I've decided to run the file size validation on the client Side. Adding the file limit on the field label and a javaScript function validation on form submission, to alert user of file size. This is to improve the feedback loop for the user, it's faster to check on the client-side.
    
- **[DONE]** Dynamic, Button only shows if there's at least one stripe subscription Application, `Call to Action Button` on NavBar Redirecting user to Pricing Page, selecting subscription from List.
    
- **[DONE]** Button redirects to a `subscription Page` that render the Free features and lists a subscription if there's any added to Application.
  - Added a template and view with the Subscription Page. Table will always show the Free features and if there's a Stripe subscription on the Application database, then a second table row is added to the page showing the features(hardcoded), A `upgrade now` button is also shown on this Row. In case user is already subscribed, Button is replaced with `Manage subscription` to let user navigate to his Stripe Customer Portal.
  

### Discovered while testing

- `allauth` templates forms weren't all aligned to center form fields
  - **[Fix]** Updated templates including forms within a div with `col` and centralized content.
  - Verify your e-mail Address page, could use a re-send verification button in case user didn't received first e-mail (spam, mailserver issue). User gets a new email on every login.  
  - Application emails were still with example.com domain
    - **[Fix]** Updated Model to use heroku live production domain

- File Upload form returns 500 error trying to delete file, same action is working on local tests, the difference being Production application is using S3 buckets as a backend to store files.
  - **[Fix-1]** Removing delete file from SystemStorage, as it is not supported by S3 backend. Will use S3 Lifecycle policies to clean-up bucket from files not accessed for long periods.
  - **[Fix-2]** Another source of a 500 Error was that the [parser_http_referer](src/http_helper/http_meta.py#L1), needed to support an extra scenario for the `articles/edit`, returning the proper url['path'] to edit_article. 
  - **Note:** the file upload form is in use by multiple views(write and edit articles, edit home,about, etc.), hence the redirect has to support multiple redirects. By Using the `http_referer` embedded on the request, the view can send the user back to the form he is editing.  
  - An edge case where happens when a User start the subscription process and stop halfway through. App Creates a new entry in “UserSubscription” without the stripe product ID. In this scenario, every operation to manage a subscription  will fail.
    - **[Fix]** On Personal space subscription Status Added extra validation to only show `Manage subscription` button If user subscription is active and has the stripe ids.   
