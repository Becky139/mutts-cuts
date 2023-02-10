# Mutts-Cuts

![mockup images](docs/readme/responsive.PNG "Website preview at different resolutions"))

[View The Live Project Here](https://muttscuts-grooming.herokuapp.com/)

## Table Of Contents
1. [Introduction](#Introduction)
    1. [Scenario](#Scenario)
2. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Design Thinking](#Design-Thinking)
3. [Features](#Features)
    1. [Design Features](#Design-Features)
    2. [Existing Features](#Existing-Features)
    3. [Future Adaptations](#Future-Adaptations)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
    1. [Main Languages Used](#Main-Languages-Used)
    2. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
    1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
    1. [Deployment.md](DEPLOYMENT.md)
8. [Credits](#Credits)
    1. [Content](#Content)
    2. [People](#People)
9. [Acknowledgements](#Acknowledgements)


***

## Introduction
# Mutts Cuts

Welcome to Mutts Cuts!  A booking site for a small dog grooming business.

## Scenario

A business tends to perform better with a steady stream of customers. It can accept walk ins and/or utilise some sort of appointment booking system.  At its simplest, this could be using a phone with a handwritten diary to record client names and their booking times.

Consider *Mutts Cuts Grooming*, a hypothetical startup business whose only employee is its sole trader/owner.
Phone calls to book appointments can occur at anytime during business hours. Such calls can be inconvenient when lathering shampoo into someone's pet.

It could help the business if customers book an appointment using a webform. This method has the advantage that appointments can also be made outside standard working hours.  In theory, this increases accessibility to business thus improving productivity and turnover.

Another valid concern is that some people prefer to book a service passively using the web as opposed to making a phonecall, especially those of a shy disposition or from a younger generation as they are accustomed to this way of working.

A business with a well developed website tends to do better than its peers.  Customers can gain a better insight of its ethos, facilities and services on offer.  In theory this fosters confidence and leads to greater engagement.

With the above in mind, let's help Mutts Cuts!

## UX

### User-Stories

Following an *Agile* paradigm, *user stories* will target customer needs and reduce embelishments on the part of the developer.  These non technical statements will aid with the incremental changes needed to build the application.

Site user needs can broadly be split into 4 categories or epics:

- navigation
- account management
- bookings management
- other

NAVIGATION

- **As an** unregistered user, **I can** navigate to a page **so that** I can view the services offered by the business

- **As an** unregistered user, **I can** follow a link **so that** I can view the Kennel's social media content

- **As an** unregistered user, **I can** use a sidenav **so that** I can navigate the site on all views

- **As a** user, **I can** select a link **so that** I can register/ log in to my account

ACCOUNT MANAGEMENT

- **As an** unregistered user, **I can** provide details **so that** I can create a unique account

- **As a** registered user, **I can** provide details **so that** I can login to my account

- **As an** unregistered user, **I can** create a unique password **so that** I can protect my personal account

- *As a* logged in user, **I can** view a page **so that** I can see my personal account details by individual field 

- *As a* logged in user, **I can** click a button **so that** I can change my personal account details by individual field 

- *As a* logged in user, **I can** click a button **so that** I can delete my account

- *As a* logged in user, **I can** request an email **so that** I can reset my account password if I have forgotten it

BOOKINGS MANAGEMENT

- *As a* logged in user, **I can** provide booking details **so that** I can set up appointment

- *As a* logged in user, **I can** update details **so that** I can reschedule an appointment with the Mutts cuts

- *As a* logged in user, **I can** cancel an appointment **so that** I can cancel an appointment with the Mutts cuts


- *As a* logged in user, **I can** request an email **so that** be reminded of an appointment

- *As an** employee, **I can** view a page **so that** I can see my daily bookings or the current day

OTHER

- *As a* user, **I can** view the site on a small screen **so that** I can use it when traveling with a mobile device

- **As a** unregistered user, **I can** view the landing page **so that** I understand the site's purpose

[Agile](AGILE.md) use has been documented in a separate file.

It became something of learning aid/development tracker for this project. 

### Design Thinking

Applying a *Design Thinking* approach, what *features* would users find most useful on the developed site?  How feasible is it for an inexperienced student developer to deliver prioritised features given the time constraints of a hard deadline?
As per assessment criteria, this project must utilise CRUD functionality.  This provides a broad outline of what is needed.  A brief though shower offered the following:


| Feature                                 | Importance | Feasability |
|:----------------------------------------|:----------:|:-----------:|
| View available services                 | 4          | 5           |
| Create personal account                 | 5          | 5           |
| Update account information              | 5          | 5           |
| Able to cancel account                  | 5          | 5           |
| Make an appoinment                      | 5          | 5           |
| Review latest appointment date/time     | 3          | 4           |
| Able to change/cancel an appointment    | 3          | 4           |
| Send client booking detail via email    | 2          | 4           |
| View history of all appointments made   | 2          | 3           |
| View costs of previous appointments     | 2          | 1           |
| Owner has calendar view of daily clients| 4          | 3           |
| **Overall Score**                       | **40**     | **44**      |
    
The above exercise indicates that overall importance/feasability scores were similar.  Therefore the project should be deliverable.

## Colour Schema
The colour schema was selected from [Adobe Color](https://color.adobe.com/search?q=dog) and the accessibility was checked using the [contrast grid](https://contrast-grid.eightshapes.com) tool from [Eightshapes](https://contrast-grid.eightshapes.com).

The developed site should appear bright to contrast with the negative space.

In keeping with the dog theme, colours are based of the *Mystery Machine* as seen in [Scooby-Doo](https://en.wikipedia.org/wiki/Scooby-Doo).

![colour-schema](docs/readme/colour-schema.png "colour schema")

![colour-accessibility](docs/readme/colour-accessibility.png "colour accessibility")

## Database Design

Entity Relationship Diagrams help to visualise database architecture before creating models in Django.  Understanding the relationships between different tables can save time recoding later in the project.  Fortunately this system is quite simple so only 4 tables are [required](docs/readme/mutts-cuts-erd.png.png "mutts-cuts-erd").

Update - mid project it was discovered there was no need for a calendar table.  This can be omitted from the ERD.

![Mutts Cuts ERD](docs/readme/mutts-cuts-erd-v1.png)

#### Scope

#### Skeleton
Wireframes were made to showcase the appearance of the site pages while keeping a positive user experience in mind. The wireframes were created using a desktop version of [Balsamiq](https://balsamiq.com/).

<details>
<summary>Balsamiq Wireframes</summary>
    
![Site Wireframes](docs/readme/wireframes/00-index-page.png)

![Site Wireframes](docs/readme/wireframes/01-our-services.png)

![Site Wireframes](docs/readme/wireframes/02-join-us.png)

![Site Wireframes](docs/readme/wireframes/03-my-account.png)

![Site Wireframes](docs/readme/wireframes/04-book-now.png)

![Site Wireframes](docs/readme/wireframes/05-my-appointments.png)

![Site Wireframes](docs/readme/wireframes/06-daily-calender.png)

</details>   


[Back to top](#Mutts-Cuts)

## Features

**SCREENSHOOTS AND BRIEF SYNOPSIS OF MAIN SITE FEATURES TO GO HERE**
**Useful Hint**
In *DevTools*, in the Elements tab, right click on the target element and select `Capture node screenshot`.
Useful for creating image files for readme.

### Design Features

### Existing Features

Landing Page

The user understands the site's purpose on arrival.

![landing](docs/readme/features/00-features-landing.PNG "landing")

Minimised Navigation 

The whole site uses a collapsable menu to save screen real estate on all resolutions.

It occupies the whole screen to encourage the user to make a decision where to navigate to.

Menu options also change depending on whether or not the user is logged in.

![dynamic-menu-options-1](docs/readme/features/01-features-dynamic-menu-options-1.PNG "dynamic-menu-options-1")

![dynamic-menu-options-2](docs/readme/features/02-features-dynamic-menu-options-2.PNG "dynamic-menu-options-2")

Fixed Footer

Links are always available at the bottom of the page for all viewscreen sizes.

It has been intentionally omitted from the landing page for styling purposes.

To assist user, link elements change style when hovering.

![fixed-footer](docs/readme/features/03-features-fixed-footer.PNG "fixed-footer")

CTA Buttons on Landing Page

If user is logged in, an additional `Book Now` button becomes available.  This is a short cut to the *view booking* template.

To enhance user experience, buttons change style when hovering.

![cta-not-logged-in](docs/readme/features/04-features-cta-not-logged-in.PNG "cta-not-logged-in")

Additionally the registration and logon CTA buttons are hidden when a user is authenticated.  They aren't required in this context.

To enhance user experience, buttons change style when hovering.

![cta-logged-in](docs/readme/features/05-features-cta-logged-in.PNG "cta-logged-in")

Services Page

Contains a brief synopsis of the services offered, drawn from the backend Services table.

A carousel element with 3 images has been included to make the site feel more dynamic.

![services](docs/readme/features/06-features-services.PNG "services")

Registration Page

Standard allauth signup page adapted to the site's theme.

![registration](docs/readme/features/07-features-registration.PNG "registration")

Login Page

Standard allauth signup page adapted to the site's theme.

![login](docs/readme/features/08-features-login.PNG "login")

View bookings page
This shows the user all existing bookings.  It is intended that that they use this information to book an appointment that doesn't overlap with an existing one.

All accounts can:
- view a page personalised with their username
- view bookings from the current date to one year in the future
- filter the table using a jquery support datepicker. This has been setup to allow selections from current date to one year in the future.
- `Show all` button removes filtering and restores table to default.
- create a booking by selecting `Book Now`
- the table itself utilizes a hover effect for a whole row to emphasis the record the user is actively viewing/selecting.

![jquery-datepicker](docs/readme/features/09-features-jquery-datepicker.PNG "jquery-datepicker")

![view-booking-table](docs/readme/features/10-features-view-booking-table.PNG "view-booking-table")

Superuser and staff accounts have:
- full CRUD access to all bookings made.
- can view all booking information including user names

![view-booking-full-crud-access](docs/readme/features/11-features-view-booking-full-crud-access.PNG "view-booking-full-crud-access")

Standard user accounts have:
- CRUD functionality limited to their own records. This is to counter malicious or accidental tampering with the database.
- To protect identities of clients, a `*****` placeholder is used to anonymize the user field for records created by others.

![view-booking-anonymize-other-users](docs/readme/features/12-features-view-booking-anonymize-other-users.PNG "view-booking-anonymize-other-users")

Create booking page
There is no need to ask the user for their name when they are signed into their account.
To simplify data entry, the form contains an `html` datepicker and dropdown menus whose options are based on the booking model.

![create-booking](docs/readme/features/13-features-create-booking.PNG "create-booking")

Edit booking page
The edit booking follows the same conventions as the create booking page and is prepopulated with the record the user chose to edit.

![edit-booking](docs/readme/features/14-features-edit-booking.PNG "edit-booking")

Cancel booking modal
This serves as a defensive programming feature for the user asking if they really wish to cancel their booking.

The title and message body are personalised and the buttons have the same hover effects in keeping with the rest of the site.

![cancel-booking-modal](docs/readme/features/15-features-cancel-booking-modal.PNG "cancel-booking-modal")

#### Help using our site

![help-modal](docs/readme/features/20-features-help-modal.PNG "help-modal")

Customised alerts
The Django framework has been used to apply messages throughout the site to give the user useful feedback.
To do this a `messages.html` template was included in the base.html,
`Alerts` can be seen at the top of the page for:

- Post Registration / logging in

![sign-in-msg](docs/readme/features/16-features-sign-in-msg.PNG "sign-in-msg")

- logging out

![sign-out-msg](docs/readme/features/17-features-sign-out-msg.PNG "sign-out-msg")

- creating/editing a valid booking

![confirm-booking-msg](docs/readme/features/18-features-confirm-booking-msg.PNG "confirm-booking-msg")

- preventing a booking clash (with time formatting)

![prevent-booking-clash-msg](docs/readme/features/19-features-prevent-booking-clash-msg.PNG "prevent-booking-clash-msg")
prevent-booking-clash
  

### Future adaptations

This was the first occasion using allauth which more than met most of the project needs. 

Only by addressing this can the user account edit/update/delete functionality be realised in the front-end. (Bookings were the highest priority for this project).It is possible to extend allauth forms to include the Profile model though this will have to be an item for the future due to time constraints.

The Profile model has(with address and phone number fields) a 1-1 relationship with the user table.  They are not crucial for the process of logging in/out but can serve other business needs such as marketing.

CRUD functionality for the full user account including address and phone number fields cannot be realised in the front-end without the above.

A good source to aid with this expansion is by [Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone).


It would be preferable to give a user their own page to view appointments to replace the filter workaround solution in `view bookings`.

Within that area, discrete option buttons representing a time could to work in conjunction with a datepicker.

Javascript would be needed to manipulate the DOM dependent on the result of a queryset of existing Booking table records.

The state of these buttons may be changed by adding a class to give a muted style or even hide.

[Back to top](#Mutts-Cuts)

## Issues and Bugs
The developer ran into several issues during the development of the website, with the noteworthy ones listed below, along with solutions or ideas to implement in the future.

Bug 1

Testing Issue Checking static folder is working on deployed site #28

this is in Sprint 2 of my projects. Any images stored in static/img/ folder should display when deployed. Remember to delete the DISABLE_COLLECTSTATIC config var in Heroku Settings by clicking on the X.
When I deleted this config var and tried to redeploy, the build log stated python manage.py collectstatic --noinput.
This prompted a different approach to handling static files by installing the dotenv python package. From there i updated the requirements.txt file and settings.py and env.py files in the project before pushing them to GitHub again.
https://github.com/Becky139/mutts-cuts/issues/28

Bug 2

Carousel images change dimensions when transitioning #52

Found in Sprint 4. Carousel image resizes when transitioning despite being of similar/size dimension to other images.
It produces an unwanted jumping effect.
Resolved by setting height of parent element (class="carousel-inner height-640px") to match height of carousel items.
https://github.com/Becky139/mutts-cuts/issues/52

Bug 3

Write view logic in booking view to prevent created and updated bookings from clashing an existing booking #56

This can be found in Sprint 8. The answer to this conundrum lay within Django documentation.
Querysets. It's abstracted so there is no need to open the database connection, perform actions, or close the connection.
Applied logic within the bookings/views.py function.
Essentially, if a record exists for a specific date AND specific time, the program can branch to tell the user their attempt to create or edit an appointment to the same time cannot be done. The business can only perform one appointment at a time as there is 1 member of staff.
(https://github.com/Becky139/mutts-cuts/issues/56)

Bug 4

Content cut off when viewing on a small mobile device #58

This can be found in Sprint 8 Issues found on two pages Services and View Bookings This can be found in Sprint 8.
In MDN docs i found the following to test
1. Remove the following properties from the viewport in the head.html file
2. user-scalable=no, maximum-scale=1.0, minimum-scale=1.0
But then found the solution below to fix the issue
Services page x-overflow solved. Container fluid was applied to multiple sections and a number of stray divs. Resolved.
Table in view bookings cannot be viewed properly below 768px. Research suggests if was a poor choice to use table elements with so many fields when responsive design was a feature. This can be resolved by using a combination of display: block and flexbox to stack td elements. This could compact information to less than 500px and still be effective.
https://github.com/Becky139/mutts-cuts/issues/58

Bug 5

Appointment now available message when editing an appointment and not changing any details #57

This can be found in Sprint 8. In this scenario, if no details at changed, a separate 'info' message should be displayed stating no details were changed. Additional code will need to be added to the edit_booking function in bookings/views.py.
Changed message and status from error to warning in bookings/views.py.
Now displaying a yellow bootstrap message stating No appointment available or this is your booking.
https://github.com/Becky139/mutts-cuts/issues/57

Bug 6

Cannot dismiss the alert element which displays the messages from views.py #54

This can be found in Sprint 8. Reviewed the header structure passed from base.html.
The navbar element spans the width of the page.
Technically the btn-close element is visible but it is actually behind #navbar element.
To resolve and restrict to the behavior to the alert button:
It was given an id of #alert-button
In style.css a z-index: 1031 was set to ensure it sat on top of the navbar element.
https://github.com/Becky139/mutts-cuts/issues/54

[Back to top](#Mutts-Cuts)

## Technologies Used

### Main Lanuages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")

### Frameworks, Libraries & Programs Used

- [Balsamiq](https://balsamiq.com/) for wireframing
- [Lucidchart](https://lucid.co/) to produce ERD's
- [Adobe Color](https://color.adobe.com/) to research colour schemas.
- [Eightshapes](https://contrast-grid.eightshapes.com) to review colour schema accessibility.
- [GitHub](https://github.com/) for repo storage and Agile project management using kanban boards/issue tracking.
- [Heroku](https://id.heroku.com/) for project deployment to the world wide web.
- [Python3 ](https://docs.python.org/3/) with the following modules
    - asgiref==3.5.0
    - dj-database-url==0.5.0
    - Django==3.2
    - django-allauth==0.50.0
    - gunicorn==20.1.0
    - oauthlib==3.2.0
    - psycopg2==2.9.3
    - PyJWT==2.3.0
    - python3-openid==3.2.0
    - pytz==2022.1
    - requests-oauthlib==1.3.1
    - sqlparse==0.4.2
    - whitenoise==6.0.0
- [Bootstrap](https://getbootstrap.com/)
- [JQuery](https://jquery.com/) 
- [Django](https://www.djangoproject.com/)
- [Django Templating](https://docs.djangoproject.com/en/4.0/ref/templates/language/)
- [PostgreSQL](https://www.postgresql.org/)
- [Favicon-Icons8](https://icons8.com/)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [W3C Markup Validator](https://validator.w3.org/) HTML linter
- [Jigsaw](https://jigsaw.w3.org/css-validator/) CSS linter
- [JSHint](https://jshint.com/) JS linter
- [PEP8](https://www.pythonchecker.com/) Python linter


[Back to top](#Mutts-Cuts)

## Testing

Refer to [TESTING.md](TESTING.md) for details on manual and automated testing.
- manual testing
- automated testing
- Lighthouse site performance checks
- linter checks on html, css, js and python code

### Deployment

The site was deployed early closely following Code Institute guides.

This process has been documented separately in [DEPLOYMENT.md](DEPLOYMENT.md)

Update - More dependancies were added after deployment.
[WhiteNoise](http://whitenoise.evans.io/en/stable/) was used instead of [Cloudinary](https://cloudinary.com/).

For a small site, it's better for the web app to serve its own static files rather than rely on a 3rd party API.
It was also much easier to setup.

Update - there was an unforseen deployment issue with [Heroku](https://status.heroku.com/incidents/2413).  As described by the link this was to prevent unauthorised access to gitHub repositories.

This was resolved by deploying to Heroku via the CLI in Gitpod.

1. Login to heroku and enter your details.
command: heroku login -i
2. Get your app name from heroku.
command: heroku apps
3. Set the heroku remote. (Replace <app_name> with your actual app name)
command: heroku git:remote -a <app_name>
4. Add, commit and push to github
command: git add . && git commit -m "Deploy to Heroku via CLI"
5. Push to both github and heroku
command: git push origin main
command: git push heroku main

MFA/2FA enabled?
1. Click on Account Settings (under the avatar menu)
2. Scroll down to the API Key section and click Reveal. Copy the key.
3. Enter the command: heroku_config , and enter your api key you copied when prompted
4. Complete the steps above, if you see an input box at the top middle of the editor...
 a. enter your heroku username
 b. enter the api key you just copied

## Credits

### Content

- - Favicon in pagetab by [Icons8](https://icons8.com/icons/set/favicon-dog)
- Paw favicons from [Font Awesome](https://fontawesome.com/search?q=paw&c=animals&s=solid%2Cbrands)
- Facebook and LinkedIn icons by [Font Awesome](https://fontawesome.com/search?s=solid%2Cbrands)
- Inspiration for navbar design from [Vandelay Design](https://www.vandelaydesign.com/inspirationalnavigation-menus/)
- Landing page image from [Google Images](https://images.google.co.uk/)
- For dog breed [images](https://www.purina.co.nz/find-a-pet/dog-breeds) used in the carousel element.
- Datepicker customisation from [Jquery](https://jqueryui.com/datepicker/)
- [Will McCutchen](https://strftime.org/) for his useful string from time cheatsheet.


### People

My thanks to:
- [Tutorials Point](https://www.tutorialspoint.com/python_data_access/python_postgresql_drop_table.htm) for guidance working directly with Postgres tables.
- Youtube tutorial *58 - Django urls, includes, and app name - Python & Django 3.2 Tutorial Series* by [
CodingEntrepreneurs](https://www.youtube.com/watch?v=icVke1tJ6aI)
- [AJ Welch](https://chartio.com/resources/tutorials/how-to-filter-for-empty-or-null-values-in-a-django-queryset/) for a bolstering my understanding of Django lookups.
- [LearnerAndLearn](https://stackoverflow.com/a/65065813) for there explanation on the difference between multiple arguments and chain filtering and how that affects SQL queries.
- For his useful Bootstrap revision sheet, [Alexander Rechsteiner](https://hackerthemes.com/bootstrap-cheatsheet/)
- [Guillermo Brachetta](https://code-institute-room.slack.com/files/UQG5DAG7K/F01RH23KDV4/django-env.pdf) for his Environment Variable setup guide.  In the end I choose an alternative method but it could be useful for future development.
- Fellow students, David Bowers and Helena Johansson for their moral support.  They kept me going during periods of self doubt.
- [Jaysha](https://ordinarycoders.com/blog/article/django-messages-framework) at ordinarycoders for her breakdown of django messaging with Bootstrap.
- [W3schools](https://www.w3schools.com/bootstrap/bootstrap_alerts.asp) for working with bootstrap.

[Back to top](#Mutts-Cuts)

## Acknowledgements

- I would like to thank my family for their valued opinions and critic during the process of design and development.
- I would like to thank my tutor Seun, for their invaluable help and guidance throughout the process.
- Lastly, I would like to extend my deepest gratitude to the amazing people in Slack who helped me rigorously test every aspect of my site.

[Back to top](#Mutts-Cuts)

***
