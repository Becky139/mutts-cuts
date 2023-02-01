# Mutts-Cuts

![mockup images](docs/readme/responsive.PNG "Website preview at different resolutions"))

[View The Live Project Here]()

## Table Of Contents
1. [Introduction](#Introduction)
    1. [Scenario](#Scenario)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Design Thinking](#Design-Thinking)
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

Welcome to Mutts Cuts!  A  booking site for a small dog grooming business.

## Scenario

A business tends to perform better with a steady stream of customers. It can accept walk ins and/or utilise some sort of appointment booking system.  At its simplest, this could be using a phone with a handwritten diary to record client names and their booking times.

Consider *Mutts Cuts Grooming*, a hypothetical startup business whose only employee is its sole trader/owner.
Phone calls to book appointments can occur at anytime during business hours. Such calls can be inconvenient when lathering shampoo into someone's pet.

It could help the business if customers book an appointment using a webform. This method has the advantage that appointments can also be made outside standard working hours.  In theory, this increases accessibility to business thus improving productivity and turnover.

Another valid concern is that some people prefer to book a service passively using the web as opposed to making a phonecall, especially those of a shy disposition or from a younger generation as they are accustomed to this way of working.

A business with a well developed website tends to do better than its peers.  Customers can gain a better insight of its ethos, facilities and services on offer.  In theory this fosters confidence and leads to greater engagement.

With the above in mind, let's help Mutts Cuts!



## UX
### Ideal User Demographic


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
The colour schema was selected from [Adobe Color](https://color.adobe.com/search?q=dog) and the accessibility was checked usin the [contrast grid](https://contrast-grid.eightshapes.com) tool by eightshapes.

The developed site should appear bright to contrast with the negative space.

In keeping with the dog theme, colours are based of the *Mystery Machine* as seen in [Scooby-Doo](https://en.wikipedia.org/wiki/Scooby-Doo).

![colour-schema](docs/readme/colour-schema.png "colour schema")

![colour-accessibility](docs/readme/colour-accessibility.png "colour accessibility")

## Database Design

Entity Relationship Diagrams help to visualise database architecture before creating models in Django.  Understanding the relationships between different tables can save time recoding later in the project.  Fortunately this system is quite simple so only 4 tables are [required](docs/readme/mutts-cuts-erd.png.png "mutts-cuts-erd").

Update - mid project it was discovered there was no need for a calendar table.  This can be omitted from the ERD.

![Mutts Cuts ERD](docs/readme/mutts-cuts-erd-v1.png)



#### Scope


#### Structure
The information above was then organized in a hierarchical tree structure, a site map, showing how users can navigate through the site with ease and efficiency, with the following results:


<details>
<summary>Site Map</summary>

![Site Map]()

</details>


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
Menu options change depending on whether or not the user is logged in.

![dynamic-menu-options-1](docs/readme/features/01-features-dynamic-menu-options-1.PNG "dynamic-menu-options-1")

![dynamic-menu-options-2](docs/readme/features/02-features-dynamic-menu-options-2.PNG "dynamic-menu-options-2")

Fixed Footer

Links are always available at the bottom of the page for all viewscreen sizes.

To assist user, link elements change style when hovering.

![fixed-footer](docs/readme/features/03-features-fixed-footer.PNG "fixed-footer")

CTA Buttons on Landing Page

If user is logged in, an additional `Book Now` button becomes available.  This is a short cut to the *view booking* template.

To enhance user experience, buttons change style when hovering.

![cta-not-logged-in](docs/readme/features/04-features-cta-not-logged-in.PNG "cta-not-logged-in")

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
  

### Future adaptations

- Extending allauth [Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone) **STILL TO WORK OUT one to one to add address and phone number fields**


[Back to top](#Mutts-Cuts)

## Issues and Bugs
The developer ran into several issues during the development of the website, with the noteworthy ones listed below, along with solutions or ideas to implement in the future.



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
- [Bootstrap](https://getbootstrap.com/)
- [JQuery](https://jquery.com/) 
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Favicon-Icons8](https://icons8.com/)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/)


[Back to top](#Mutts-Cuts)

## Testing

Refer to [TESTING.md](TESTING.md) for details on manual and automated testing.
**DONT FORGET TO ADD HTML AND CSS VALIDATOR CHECKS, LIGHTOUSE AND JSHINT use proper ci tool!**

### Deployment

The site was deployed early closely following Code Institute guides.

This process has been documented separately in [DEPLOYMENT.md](DEPLOYMENT.md)

Update - More dependancies were added after deployment.
[WhiteNoise](http://whitenoise.evans.io/en/stable/) was used instead of [Cloudinary](https://cloudinary.com/).

For a small site, it's better for the web app to serve its own static files rather than rely on a 3rd part API.
It was also much easier to setup.

## Credits

### Content

- Favicon by [Icons8](https://icons8.com/icons/set/favicon-dog-paw)
- Facebook and LinkedIn icons by [Font Awesome](https://fontawesome.com/search?s=solid%2Cbrands)
- Inspiration for navbar design from [Vandelay Design](https://www.vandelaydesign.com/inspirationalnavigation-menus/)
- Landing page image from [Google Images](https://images.google.co.uk/)
- For dog breed [images](https://www.purina.co.nz/find-a-pet/dog-breeds) used in the carousel element.
- Datepicker customisation from [Jquery](https://jqueryui.com/datepicker/)


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

[Back to top](#Mutts-Cuts)

## Acknowledgements



[Back to top](#Mutts-Cuts)

***
