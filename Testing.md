Testing
---

Section to describe How to run tests on local development environment and describe testing running
in [travis.com](https://app.travis-ci.com/)

- [Staging Environment](https://the-learning-hub-staging.herokuapp.com/)

### Automated Tests

For the automated testing this project leverages [travis.com](https://app.travis-ci.com/)

- [.travis.yml](/.travis.yml)
    - this file content describe steps executed during build

### Local tests

- make sure to apply migrations:

---

      $ python3 manage.py makemigrations
      $ python3 manage.py showmigrations 
      $ python3 manage.py migrate

- run tests

---

    # Run whole test suite
      $ python3 manage.py test 
    # Run test for a single app
      $ python3 manage.py test articles
    # For a single Class
      $ python3 manage.py test articles.test_views.TestArticlesViews

- Show Test coverage

---

    # make sure coverage is installed
      $ pip3 install coverage #is in app requirements should be installed already
    # Run run test to generate coverage report
      $ coverage run  --source=TheLearningHub manage.py test
    # get report 
      $ coverage report

### Stripe Webhook manual tests

As a developer if I need to test the Stripe webhook integration here are the
steps [StripeWebhooks](https://stripe.com/docs/webhooks/test)

    brew install stripe/stripe-cli/stripe # For IOS
    stripe login (use stripe credentials)
    stripe listen --forward-to localhost:8000/products/webhook

### Manual Testing

This Section outlines manual checks, i.e. link redirects to correct destination, application is sending email as
expected.

#### [Personal Space](https://the-learning-hub-prod.herokuapp.com/personal_space/)

##### User Details

All links listed below need an authenticated session.

| Action | Manual Test | Is Back Button working |
|---|---|---|
| [Update Personal Details](https://the-learning-hub-prod.herokuapp.com/personal_space/update_personal_details) | Add information form works | yes |
| [Change Password](https://the-learning-hub-prod.herokuapp.com/accounts/password/change/) | update Password is working | yes |
| [Manage account emails](https://the-learning-hub-prod.herokuapp.com/accounts/email/) | Add new Email works | yes |
| [Manage account emails](https://the-learning-hub-prod.herokuapp.com/accounts/email/) | Remove email works | yes |
| [Resend Verification works](https://the-learning-hub-prod.herokuapp.com/accounts/email/) | Add new Email works | yes |

##### Bookmarks

##### My Notes

##### Subscription status

#### Login/sign-up actions (allauth)

| Action | Manual Test | Passing | Is Back Button working |
|---|---|---| ---|
| [Anonymous user sign-up](https://the-learning-hub-prod.herokuapp.com/accounts/signup/) | Using Sign-up button from navbar | yes | N/A |
| [User Login](https://the-learning-hub-prod.herokuapp.com/accounts/login/) | Once email is verified user is able to login | yes | N/A |
| [email Verification](https://the-learning-hub-prod.herokuapp.com/accounts/confirm-email/) |Once profile is created, at first login user receives verification email | yes | N/A |
|[email Verification](https://the-learning-hub-prod.herokuapp.com/accounts/confirm-email/) | if for some reason first email fails, User receives email on later login | yes | N/A |
| [User Logout](https://the-learning-hub-prod.herokuapp.com/accounts/logout/) | from Navbar, click user dropdown, then logout  | yes | N/A |
| [Password Reset](https://the-learning-hub-prod.herokuapp.com/accounts/password/reset/) | fill email form and receive link to reset password | yes | N/A|

#### [Control Panel](https://the-learning-hub-prod.herokuapp.com/content_management)

| Action | Manual Test | Passing |
|---|---|---| 
| Only available is user is (Content_manager/superuser) | Logging without privilege, does not show content management area | yes |
| Write New article | clicking on `write new article` form opens. | yes |
| Create new video class | clicking on `create Video class` correct form opens. | yes |
| Edit page `home` | clicking on opens Edit form for `Home` Page. | yes |
| Edit page `about` | clicking on opens Edit form for `about` Page. | yes |
| Edit page `pricing` | clicking on opens Edit form for `pricing` Page. | yes |
| Edit page `terms_of_service` | clicking on opens Edit form for  `terms_of_service` Page.| yes |
| Edit page `privacy_policy` | clicking on opens Edit form for  `privacy_policy` Page.| yes |
| Manage Stripe subscription | Creating new subscription information | yes |
| Manage Stripe subscription | once create existing subscription shows on page bottom | yes |
| Show existing Stripe subscription | once create existing subscription shows on page bottom | yes |
| Remove Stripe subscription | Remove button on stripe subscription table, removes subscription| yes |


### Subscription

| Action | Manual Test | Passing |
|---|---|---| 
| Sign-up for Premium (call to Action Button) | Redirects to subscription Page, only show for registered users.  | yes |
| Subscriptions page | Upgrade button is replaced by `Manage Subscription` for premium Users | yes |

