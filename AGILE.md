# Agile

## Sprint 1
- Setup repo
- Create Django project
- Install basic dependencies and add to requirements
- Create procfile to deploy to Heroku
- Create app on Heroku
- Link GitHub repo to Heroku app
- Test to deploy working project ASAP

- Document project creation and deployment
- Perform design thinking exercise for features to include in project
- Add user stories to readme
- Add wireframes to readme
- Identify a colour schema to use in the site
- Mock up initial database design and document in readme
- List and link technologies used in readme

- Learn to use GitHub projects. Create user stories and drop onto Kanban board

### Reflections

Several false starts.
Got more comfortable using an Agile tool to plan functionality.  Applied retrospectively to 1st week objectives to practice how it works.

This was effectively the first iteration for the project before any real coding took place.

In a way I'll already started categorising user stories by area such as navigation or account management.  This gives an idea to the separate apps what will need to be created.

I found I was jumping from one task to the next with no real direction.  Best to plan each future iteration to make it easier to track what still needs to be done.

![01](docs/readme/agile/sprint-1-kanban-use-01.PNG)

## Sprint 2
- Setup base.html
- create separate components for site such as head, navbar, scripts and footer in a subfolder to inject into base.html
- Setup index page in home app
- Build navigation

### Reflections

This week I focused on building out part of the frontend.  The `home` app will contain the index page for the site.
The templates folder in the root directory contains the base.html *et al* templates.  From what I've learned so far different webpage components should be injected into each template.  Follow a modular/reusable/extension approach.  

In the background I continued researching models as I want to try to get these right 1st time.

Also it's useful to have some templates to link to models via views when the time comes.

TWIL (This week I learned) after creating a new project, cards can be dragged across from the add card area.  Also helps to use checkboxes to tick off smaller tasks relating to a larger one.

![01](docs/readme/agile/sprint-2-subtasks-01.png)

![02](docs/readme/agile/sprint-2-kanban-use-02.PNG)

Use bootstrap for speed.  Copy their [code](https://getbootstrap.com/docs/5.0/components/navs-tabs/) rather than start from scratch.

![03](docs/readme/agile/03-sprint-2-bootstrap-use.png)

Start to tailor the bootstrap code to something more site specific.

![basic-menu-setup](docs/readme/agile/sprint-2-basic-menu-setup.png "basic-menu-setup")

With a basic navbar in place, this will have to be updated as new views/respective templates are created to deliver user story functionality.

*Register*, *Login* and *Appointments* in the menu have been purposefully disabled for now.

Update - change navbar to an off canvas type.  Closer to wireframe design.  

Update - use 5 list items in menu, home, our services, register, login, Book Appointment.

Focus on finishing the landing page and creating an *Our Services* page. Link up as necessary.

Update - change navbar to an off canvas type.  Closer to wireframe design.  

Update - use 5 list items in menu, home, our services, register, login, Book Appointment.

Update - leave homepage bare bones. Can change the aesthetics toward the tail end of the project.

Removed User Story #17 from sprint 2 project - As a site user I can view the site on a small screen so that I can use it when traveling with a mobile

Removed User Story #18 from sprint 2 project - As a unregistered user I can view the landing page so that I understand the site's purpose

Technically services are a different function.  Time for a new *services* app!  #18 can drop into a future project week.  I feel it's best to get authentication working next as this affects the navbar.  Next logical step to complete that.

I want to fix [issue #5](https://github.com/Becky139/mutts-cuts/issues/28) to wrap up this week.

## Sprint 3
- Install `allauth` package
- Add allauth to installed applications in settings.py
- Add login/logout redirects back to index page
- Perform migrations
- Adapt navigation bar using Django Templates to to give registered/unregistered site users different menu options

- develop the landing page a little more using bootstrap. Aim to get the hero image to display correctly. Use its FSF approach to develop the frontend faster.

### Reflections
This week it wanted to focus on user accounts and authentication as that alters the navbar options through use of Django templates.
Also, I realised I had to revise my use of Bootstrap as much of this knowledge hasn't been used in a few months.  By developing a generic landing page using Bootstrap I can speed up the creation of future templates.  Bespoke css/js/jquery can be added at a later time for a less derivative site.

Seven user stories satisfied this week.

![01](docs/readme/agile/sprint-3-kanban-use.png)

## Sprint 4
- Copy & modify Allauth templates
- Extend Allauth user model
- Build Services page

### Reflections
This week I wanted to take the allauth package and style it to suit my website.  Much of the instructed can from the relevant CI unit presented by Matt Rudge.  Towards the later part of the week I want to extend the alluth user class to suit my project.
A second outcome was getting comfortable wiring up a new page/template with Django.  The template must be set up correctly in a directory which must then be rendered by the view.  That view must then be referenced in the app url which in turn is referenced in the main project folder urls file.  In future I must remember to add the app to the installed apps list in main/settings.py!

1 unfixed [bug](https://github.com/Becky139/mutts-cuts/issues/52) were the carousel image resizes when transitioning despite being of similar/size dimension to other images.  It produces an unwanted jumping effect.  Come back to this as I really need to make a start on models.

Allauth sped up development of an authentication system for the site.  However a few extra custom fields were desired for the project including user `address` and `contact number`.  As I already performed migrations I choose not to extend the Abstract User model.  Rather I created a new model with a one-to-one relationship to the existing User Model through a OneToOneField.  This was suitable as the extra information was desirable but not related to the authentication process.  Note, a bit of extra work will likely be needed to display the custom model but its a safer overall option. Still to resolve [bug](https://github.com/Becky139/mutts-cuts/issues/53).

![01](docs/readme/agile/sprint-4-kanban-use.png)

## Sprint 5
- Create bookings app, view and templates
- Link booking template to nav menu and homepage link buttons
- Show `Book Now` button only if user is logged in
- Create services model
- Create calendar model
- Become familiarised with creating records in Django admin. 

### Reflections
I went into a bit less detail this week on template creation and links for bookings.  No need as the process is becoming more familiar.

There's not much in the way of crossing off user stories this week.  We are very much in the architecture stage or just getting things to work.

When naming classes to create models, use a singular name.  For example I created a `Services` model which shows up on the Django as `Servicess`.
Minor but annoying.  I redid my migrations as I can be pedantic with naming.
Take future care, be careful to synonymously reference my code for easier reading and debugging.

When re-reading the assignment brief, I started to think how my models affected site features.  The original `booking` model was too simple. To make business sense:

Appointments were to be restricted to 8am-5pm business hours, not in the middle of the night!
Appointment times should be standardised to specific time and duration.  Ie. 45 minutes each hour starting from 8am to 4pm. A 9 hour day with 15 minute downtime between appointments (This will prevent appointment overlaps and the logic to do this must be supplied to the view)

Considering the above, the booking model **will** have to be updated.  First thoughts are to separate the booking time (date/time) to date and hour fields where the hour field can only be selected from a subclassed appointment list.

This has a downside. It isn't possible to use the `timedelta` method on the booking model to add an end time for an appointment.  It only works on `datetime` and not `time` datatype.

The calendar model in the ERD isn't required.  It's a pointless replication with hindsight so keep it simple.  A calendar is a way to display database objects so I can create one using a library such as `calendar.py` or take a premade one from a useful site such as [Colorlib](https://colorlib.com/wp/template/calendar-20/).  Event logic is still required.  A bit of jQuery on individual calendar elements can trigger events as needed...

Or do I simply display daily appointments as a list in a Django template.  This would be simpler.

Final thought of the week.  You can follow instructions to the letter.  Things you assume will work because you are told don't always.  To be a better developer, assume nothing.

![01](docs/readme/agile/sprint-5-kanban-use.png)

## Sprint 6
- build view bookings page
- build create bookings page and add form from BookingForm model
- Create view and functionality for basic CRUD operations.

### Reflections
Keeping it simple, when the user selects `Book Appointment` they are directed to the `view_booking` template.  Here they can see the bookings already made.  In theory, they can work out what appointments are available. (Not perfect but a starting point. I'd like to show them available appointments only).  Will require a bit of logic with Django templates... Continue to research....

![01](docs/readme/agile/sprint-6-kanban-use.png)

## Sprint 7
- Develop a means to display only appointments for a given day using a method like a date picker...
- All logged in users are able to create, view, edit and delete other users appointments.  Restrict this to view only.  We only want them to see were slots are taken on a given time/day.
- When performing a CRUD operation, give the user a chance to confirm if they want to proceed.
- At this stage Django template language is used to differentiate between superuser & staff access and standard user access.

### Reflections
This is were the project goes from closely following generic tutorials to becoming more unique.

Table row elements were filtered using JavaScript to achieve filtering by user.

Learn how to use query sets within Django.  Powerful and usable.

Defensive programming.  Effectively best to make someone confirm an action.  Modals can be useful for this.

![01](docs/readme/agile/sprint-7-kanban-use.PNG "01")

## Sprint 8 - Take-off & Punchlist
- Prevent booking clashes
- give user feedback when logging in / out
- give user feedback when successfully/unsuccessfully creating and editing bookings
- review responsiveness on multiple resolutions/browsers
- include a help modal to advise the user how to use the site

### Reflections

More consideration should have been given to responsiveness *earlier* in the project.  It was developed optimally for 768px/tablet use.  Start small!
Making the table in view booking was a challenge. Not rendered perfect but stacked appearance displays all data without the need for horizontal scrolling.

![01](docs/readme/agile/sprint-8-kanban-use.PNG "01")
