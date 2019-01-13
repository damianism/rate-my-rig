
BUILD ME A RIG [![Build Status](https://travis-ci.org/damianism/rate-my-rig.svg?branch=master)](https://travis-ci.org/damianism/rate-my-rig)
==============


Real world application
----------------------

There are many <a href="https://damianism.github.io/custom_pc/benefits.html" target="_blank">benefits</a>
of building your own computer. However, the whole process can be cumbersome,
frustrating and nerve-wrecking.

Here are a few problems associated with building your own computer.

#### Time spent on research

The amount of time spent on research to get the right build for yourself can be
quite off putting, it’s definitely not for the impatient, as I personally spent
over two months researching different configurations and component in the hopes
of getting the exact performance that I wanted. You may even find yourself
having to wait even longer in some circumstances such as waiting for a driver of
a component you’re interested in to be updated or waiting for new component to
be released. I personally had to wait two weeks for the new Ryzen cpu line-up to
be released.

#### Putting it together

Picking the right parts for your build is only half the battle. After receiving
your parts, you still have to put it all together, and that’s where things
usually go wrong. Often, after spending an hour or so (depending on how fast you
are) putting your system together, you will find that the system doesn’t boot
up, which simply means that one of the parts was dead on arrival or not
compatible at all, so you have to spend hours if not days running diagnostics to
identify the part that needs replacing, but doing so is not that easy, for
example you many need another mainboard just to be able to test your CPU or RAM,
so not everyone is capable of running these diagnostics. Furthermore, even if
you do manage to identify the culprit, more time will be wasted on taking out
the part again, repackaging, and sending it back to the retailer. The retailer
will waste even more time processing your return, issuing the replacement and
you still have to wait for it to be delivered.

Even if your system boots up successfully on the first attempt, like my latest
system did, it doesn’t mean that everything is running as they should. In my
case, I realised that my RAM wasn’t fully compatible with my motherboard, even
though it was listed as “fully compatible” on the mainboard manufacturer’s
website. So I’m not able get the most out of those RAM units until they are
fully supported by the mainboard, which is a huge blow to me personally since I
paid extra for faster RAMs.

Finally, having gone through all of that, there is no guarantee that system will
give you the performance you were hoping for, forcing you to make further
tweaks by replacing some of the parts and ultimately spending even more time and 
money on it.

#### Aim

Wouldn’t it be great if somebody else had gone through **everything** stated above
in order to get a specific build fully functional, so you wouldn’t have to? This
is exactly what this web app aims to achieve by allowing its users to share
their complete builds with other users wishing to build their own systems.

As a user you may

-   Use an existing build as a blueprint for your own build.
-   Gain assurance on components compatibility before system assembly.
-   Contact the owner/author of a build to seek advice via comments.
-   Gain assurance of the system performance before system assembly.
-   Get ideas from an existing build for your own build.
-   Purchase the exact posted build.
-   Purchase a build posted yourself.

This web app will ultimately save its users days if not months spent on research and
running diagnostics to get their ideal configurations since everything will be
available to them from the start, even the actual performance of the system
they’re trying to build.

#### Purchasing builds:

Users not wishing to assemble their own units may purchase a pre-existing or
their own posted build on the website through us for a flat fee of £100. After
placing your order, we will assess your selected configuration and contact you
via phone or email within 24 hours to discuss your configuration. At this point
if your selected configuration passes our compatibility tests, and you are happy
with your selected configuration, you will then be charged for the full cost of
the selected components (RAM, GPU, CPU etc). Upon completion of the order, we
will ship your new and fully tested assembled unit to you.


Wireframes
==========

Wireframes created using [mockingbird](https://gomockingbird.com/home).

Only list links to wireframes

Features
========

The list below shows all the added features that needed to be in place for the
project to be fully functional. The features planned to be added in the future
are listed in the [Future Features](#future-features) section of this
documentation.

#### User authentication

-   Register an account
-   Login into an account
-   Login using an email address
    -   Existing email address detection
-   Automatic user profile creation using Django signals
    -   Default user profile image
-   Change details of an account
    -   First name
    -   Last name
    -   Username
    -   Profile pic
-   Password reset of an account

#### Dynamic navbar links

All users have access to the following navbar links
-   Home
-   Builds
-   Contact
-   Search
-   About
-   Cart

ONLY the logged in user have access to the following navbar links
-   New post
-   Profile
-   Logout

Users not logged in will have access to
-   Login
-   Register

#### Contact us
-   Users can contact admin(superuser) via email

#### Blog/Builds
-   View all posted builds
-   Post a new build
    -   Default build image
-   Change/update an existing build
-   Delete an existing build
-   View user details
    -   Name
    -   Username
    -   Email
    -   Posted builds
-   Filter posted builds by
    -   CPU
    -   GPU
    -   RAM
    -   PSU
-   Order posted builds
    -   Ascending
    -   Descending

#### Search categorically
-   Search by title
-   Search by ram
-   Search by cpu
-   Search by gpu
-   Search by psu
-   Search by mainboard

#### Pagination

Pagination is available on the following pages:
-   Search results view
-   Builds/Blog view

#### Comments
-   Leave comments on posted builds

#### E-commerce
-   Cart
    -   Add items to cart
    -   Update number of items in cart
    -   Calculate Total cost
-   Checkout (forces login)
    -   Ability to take payments through the [STRIPE](https://stripe.com/gb) API

#### Compartmentalised base template

Consists of 9 sections all together
-   Base
    -   Base template used for all views
-   Comments
    -   Comments section at the end of each posted build
-   Filter
    -   Filter section of the Builds view
-   Footer
-   Messages
    -   Flash messages from Django
-   Navigation
-   Class based pagination
    -   Pagination used with class-based views
-   Function based pagination
    -   Pagination used with function-based views
-   Search_form

#### Flat UI
-   Attempted to mimic Google’s material design
-   Collapsible build pictures in search results and builds views.
-   Responsive design.


Future Features
===============

All the features listed within this section WILL be added upon completion of the
course. The following features were shelved solely due to lack of time and my
unfortunate sudden change of circumstances.

#### Discussion board
Users may open threads in regards to
- Technical issues and troubleshooting.
- Seeking further advice on a build.

#### Advanced comments
Users may
- Delete their own comments
- Like/Dislike comments left by other users
- Reply to comments

#### Add user address to the registration process
- Could automatically fill in the user's address into the checkout form
- Collect data about the user's location to be used with a graphical dashboard
    
#### A more sophisticated modelling system
- Individual components model
    - Example; (component: storage, type: SSD, interface: M.2,
            manufacturer: Samsung, capacity: 500Gb, price: £150)
- A complete build model consisting of all the added components
    - Will be able to get the exact price of the build
    - List the individual components in detail
    - Link component purchasing links


Technologies Used
=================

The list of technologies used for this project in no specific order.

#### Core Technologies

-   [Could9](https://aws.amazon.com/cloud9/?origin=c9io) – used as main editor
-   [Python](https://www.python.org/downloads/) v3.4.3
-   Pip3 - used to install various libraries within Cloud9
-   [Django](https://docs.djangoproject.com/en/2.1/releases/2.0/) v2.0
    -   [Jinja2](http://jinja.pocoo.org/docs/2.10/) - used to apply logic to
        Django templates
    -   Django specific libraries installed via pip3
        -   [crispy_forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
            – module for styling forms
        -   [django-resized](https://github.com/un1t/django-resized) – used to
            resize the uploaded images
        -   [django-filters](https://django-filter.readthedocs.io/en/latest/guide/install.html)
            – to filter posted builds
        -   [Pillow](https://pypi.org/project/Pillow/) – required for uploading
            photos
    -   [django-secret-key-generator](https://www.miniwebtool.com/django-secret-key-generator/) – used to 
        generate a more secure secret key
-   JavaScript
-   [jQuery](https://jquery.com/) v3.3.1
-   HTML5

#### Styling technologies

-   [SASS](https://sass-lang.com/) - Main method of styling. Used with a variety
    of SASS variables, colors, mixins and functions.
-   CSS
-   [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    v4.0
    -   Responsive design
    -   Styling
        -   Cards, Buttons, accordions, animations.
        -   Text alignment.
        -   Colouring.
-   Flexbox – used for centring items
    -   Primary tool for centring item.
    -   Primary layout tool for cart and checkout templates.
-   [Google fonts](https://fonts.google.com/)
    -   [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono) – applied
        to the buttons (small and large)
    -   [Roboto](https://fonts.google.com/specimen/Roboto) – used as the main
        font for the project
-   [FontAwesome](https://fontawesome.com/)
-   [MycolorSpace](https://mycolor.space/) – used to apply gradient to the
    background
-   [Favicongenerator](http://www.favicongenerator.co.uk/) – used to generate a
    custom favicon
-   [Cssmatic.com](https://www.cssmatic.com/box-shadow) – used to create shadows
    for the cards
-   [Gimp](https://www.gimp.org/) – used for image format conversions, rescaling
    and touch ups.

#### Database technologies

-   [SqLite3](https://docs.python.org/2/library/sqlite3.html) – Default database
    initially used with Django v2 in development mode
-   [Heroku Postgres](https://www.heroku.com/postgres) – replaced sqlite3 after
    the very first deployment to Heroku for both development and deployment.
-   [Psycopg2](https://pypi.org/project/psycopg2/) – pip3 installed library
    required to establish connection to Postgres databases.
-   [dj-database-url](https://pypi.org/project/dj-database-url/) – pip3
    installed library which establishes connection to the Heroku Postgres
    database URL.

#### Deployment Technologies

-   [Heroku](https://www.heroku.com/) – Used to as the primary deployment
    platform.
-   [Gunicorn](https://gunicorn.org/) – pip3 installed library used for running
    the deployed Django project on Heroku.

#### Cloud Storage

-   [Amazon web services](https://aws.amazon.com/cloud9/?origin=c9io)
    -   S3 – used to store static and media files
-   Boto3 – pip3 installed library to connect to AWS S3
-   [Django-Storage](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
    – pip3 installed library to control Django storage

#### Version control

-   [Git/Github](https://github.com/damianism)
    -   Kept track of the project’s evolution with frequent commits and
        informative messages.
    -   GitHub was also used to access bootstrap’s source code.

#### Testing

-   Chrome and Firefox developer tools
    -   Used extensively for live-testing and running numerous different tasks.
        To name a few:
        -   Testing JavaScript functions.
        -   Individual elements loading times.
        -   Website/grid responsiveness.
        -   Element Colours, style, opacity and etc.
        -   Aligning and centring.
        -   Attribute value search.
        -   Fluidity and core functionality of the website.
-   [Travis](https://travis-ci.org/) – continuous integration service used to
    build and test software projects hosted at
    [GitHub](https://en.wikipedia.org/wiki/GitHub)


Testing
=======

Here is the list of the tests carried out for this project in no particular
order.

#### STRIPE API

The API was tested using the four sets of “4242” card number.

#### Sendemail – dedicated email for 

Created a dedicated gmail to be used with this project only. Carried out tests
on both [mobile and desktop platforms](#responsiveness-and-aesthetics).

#### Account password reset

Carried out tests with both admin and normal accounts on [mobile and desktop
platforms](#responsiveness-and-aesthetics).

#### Travis

Fully automatic testing set up after pushing to Github.

#### Amazon S3 static and media files

Both Media and static files were tested manually by checking the S3 panel and
the links of the files uploaded via the network section of the Firefox and
chrome browser’s developer tools. Checking the static files were especially easy
since without them the website would have loaded without any styling.

### Responsiveness and Aesthetics

The responsiveness, functionality, fluidity of each page was extensively and
virtually tested on all the Chrome/Firefox responsive tool’s available devices,
ranging from Amazon fire tablets to iPhone XS. Additionally, every page was
numerously loaded on the following devices by various users in order to identify
possible malfunctions and misbehaving elements.

-   Galaxy S5 (width less than 370px)
-   iPhone X
-   Google Pixel 2 XL
-   iPhone 7 Plus
-   Nexus 6P
-   Nexus 7 2013
-   LG G4
-   Huawei P9 Lite
-   22inch Full HD 1080p monitor
-   24inch Full HD LCD 1080p monitor
-   27inch Full HD 1080p monitor
-   25inch Quad HD 1440p monitor
-   13inch Full HD screen of a Dell XPS Ultrabook
-   15inch HD screen of a DELL Precision M4600
-   15inch Full HD screen of a DELL Precision M4800

#### Browsers

The following browsers were used to test the deployed version of the website
with.

-   Opera Version 57.0.3098.116
-   Firefox Version 64.0.2 (64-bit)
-   Chrome Mobile on Android Pie
-   Chrome Mobile on Android Oreo
-   Chrome Mobile on Android Kitkat
-   Firefox Mobile on Android Pie
-   Safari Mobile iOS 12

#### Operating systems

The browsers listed above were used to test the deployed version of the website
with the following mobile and desktop operating systems.

-   Android Pie
-   Android Oreo
-   Android Kitkat
-   Windows 10 pro
-   Window 7 pro
-   iOS 12

Known Issues
============

#### Search

Searching in RAM category for “8” will bring up posts with both “128GB” and
“8GB” ram posts. Furthermore, searching for empty spaces (“ “) in the TITLE
category will return the posts with empty spaces in them such as “Pink Hornet”.
I’m not entirely sure if that’s going to cause any problems, I certainly
couldn’t get it go wrong after testing it. But, technically speaking, it is
returning exactly what the user has searched for.

#### Stripe API failing

Stripe payment was repeatedly failing without issuing any errors. After seeking
help from “Neil Mc Ewen” we realised that the jQuery was listed after the stripe
script on the base template and without jQuery, stripe couldn’t have functioned.

#### Calc() function wasn’t working in SASS

```
min-height: calc(100% - 70.4px);
```
Calc() function was added to expand the pages with no or only a few elements on
there. However, the function was being ignored by all of the browsers I tested.
I could hard code a value for min-height but that didn’t resolve the issue as it
broke the responsiveness of the website. Upon further research I figured out
that the html tag also has to have its height set to 100% and not just the body
tag.


#### Responsive design of blog_home -filter

One of the choices for the CPU select box (Ryzen Threadripper gen-1) within the
filter panel of the Builds/Blog view turned out to be quite long since I could
not find a way to abbreviate or shorten it, doing so would have caused
confusion in regards to the CPU model and its brand. The select box is still
fully responsive as long as it’s not open. Consequently, if the select box has
been triggered open, the choices will expand out of the frames of the select
box. This could not be properly tested since it only happens on Ipad resolution,
and as I don’t currently own an Ipad, naturally I resorted to using
chrome/Firefox responsive design tools, which didn’t really help since both
tools render the choices of the select box as if it is being loaded on a desktop
platform while the select box is open.

#### Name change

I initially intended to create a rating system, which would have been the core
feature of this project, all the other features would have been built around 
this particular feature. But unfortunately, due to lack of time and my sudden
change of circumstances, the rating system was axed, forcing me to change the
name of the project from “ratemyrig” to “buildmearig”.

Since changing the name of the git repository was not possible. Only the name of
the deployed Heroku app was changed via Heroku’s settings. I had to change the
hostname within the Django’s settings.py and Heroku’s Config Vars accordingly.

#### Unit testing with Heroku Postgres

Unfortunately, due to my sudden change of circumstance, I couldn’t carry out
unit testing on any of my apps with the exception of the blog app. However, when
I did make the time to finally go through with it, I immediately started having
issues with Django being denied access to the Heroku Postgres database. Upon
doing some research I realised that Django’s unit testing relies entirely on its
default local database (Sqlite3). I then temporarily switched back to SQLite3
for the sole purpose of unit testing my project’s apps. However, it only made
things worse but causing Travis continuous testing to fail. I eventually managed
to rectify the issue with Travis which turned out to be a data migration issue
and inability of Travis to switch between the two databases. Evidently to avoid
any further issues with Travis, I decided not add any more unit testing to this
project.

Note: even though I haven’t included any unit testing with this project, I can
confirm that no corners have been cut when it comes to testing this project. All
the apps and logic within this project have been manually tested numerous times
on various platforms and devices.

#### Firefox 

Every now and then when I try to load the deployed version of the website on
Firefox, I’m greeted by the following error message and then it locks me out of
the website.

```
Not Found
The requested URL / was not found on this server.
```

I haven’t been able to replicate this particular issue on any the browsers I’m
currently using. However, I believe it is caused by inactivity and the way the
session is managed in Firefox, since logging out manually using the url
(/user/logout/) would resolve the issue.



Deployment
==========

[Heroku](https://id.heroku.com/login) was used as the PRIMARY deployment
platform for this project. 


The following aliases were defined in the **.base_aliases** file for ease of use. 
```
alias run = "python3 manage.py runserver $IP:$C9_PORT"
alias makemigrations = "python3 manage.py makemigrations"
alias migrate = "python3 manage.py migrate"
```

## Development version with SQlite3 database

**env.py** file was created for the sole purpose of setting up environment variables 
for this project’s sensitive information. The file was then added to .gitignore.

#### Setting up environment variables

The condition below was then added to **settings.py**, which imports the
**env.py** and automates Django’s **DEBUG** value.

```
if os.path.exists("env.py"):
    development = True
    import env
else:
    development = False
    
DEBUG = development
```

At this level the following environment variables were set in **env.py**
and used in **settings.py**.

```
os.environ.get('C9_HOSTNAME')   # set automatically by cloud9
os.environ.get('SECRET_KEY')    # flask secret key
```

#### Setting up local database

Initially when the project was first started and deployed locally using Django’s
very own default SQLite3 database.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

#### Setting up static and media files

Required libraries installed:
-   [Pillow](https://pypi.org/project/Pillow/) – caters for the “ImageFields” allowing images to be uploaded via the
    admin page
-   [Whitenoise](http://whitenoise.evans.io/en/stable/) - Allows us to host our staticfiles such as css and javascript

**settings.py**:
```
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```


## Development version with PostgreSQL database

After familiarising myself with the local SQLite3 database, I decided to make
the jump to the PstgresSQL database.

Required libraries:
-   [Psycopg2](https://pypi.org/project/psycopg2/)
-   [dj-database-url](https://pypi.org/project/dj-database-url/)

#### Setting up Heroku's PostgreSQL database

-   Create Heroku app on EU region
    ```
    heroku create "unique-app-name" --region eu
    ```
    
-   Setup [Heroku Postgres](https://www.heroku.com/postgres) database addon for Heroku
    ```
    heroku addons:create heroku-postgresql:hobby-dev --app "unique-app-name"
    ```

-   **DATABASE_URL** added to Heroku’s Config Vars
    ```
    heroku config:set DATABASE_URL ="postgres://dummy-postgres-url"
    ```

4.  **DATABASE_URL** set as an environment variable in **env.py** and make changes to 
    **settings.py** file accordingly



```
import dj_database_url     # installed library

if 'DATABASE_URL' in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    print("Postgres URL not found, using sqlite3 instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

## Production version on Heroku

qq

## Production version on Heroku with AWS

qq

Throughout the project, git was used to seamlessly
and safely back up the code locally and pushed to Github frequently.

For testing purposes, the project was first deployed locally on the Cloud9
environment and most of the testing was done through Cloud9. However, later on I
realised that it is not fully reliable and it can’t be trusted as the actual
deployment platform might not behave the same way as mentioned above in the
“Heroku Deployment issue” section of the “[Testing and
challenges](#_Defensive_design_and)”.

The project was pushed to Heroku at its early stages and was repeatedly done so
with the addition or alteration of any feature, incremental or major. However,
on the previous project, the Heroku app was created using bash within the cloud9
environment, unfortunately doing so would create the app on the American serves,
since causing the website to take a lot longer than it needs to once deployed.
This time I took the precaution of creating the app within the Heroku’s very own
control panel and made sure that the app is indeed sitting on the European
servers for faster response time.

\<p align="center"\>\<img src="static/img/extras/heroku.png"/\>\</p\>

In addition to the usual IP, PORT and FLASK environment variables, I also had to
include other credentials for the Oxford dictionary API into the config vars.

\<p align="center"\>\<img src="static/img/extras/heroku2.png"/\>\</p\>

There are no differences between the deployed version of the project found
[here](http://vocabulary-journal.herokuapp.com/) and its development version.
Since the project was deployed at such an early stage, no major problems were
encountered. The whole process was completely hassle free.

Cedits
=======

#### Django-filters

-   [Django filtering system with Django-filters](https://www.youtube.com/watch?v=nle3u6Ww6Xk)
-   [stackoverflow](https://stackoverflow.com/questions/21840365/set-initial-value-with-django-filters)
-   [stackoverflow](https://stackoverflow.com/questions/46491786/best-way-to-filter-listview-with-drop-down-form-in-django/46492378#46492378)

#### Filter and paginations conflicting issues

-   [Filtering and Pagination with Django](https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/)
    by Dan Poirier
-   [stackoverflow](https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278)
-   [Creating custom template tags in Django](https://www.codementor.io/hiteshgarg14/creating-custom-template-tags-in-django-application-58wvmqm5f)
    by Hitesh Garg
-   [Djano-filter – Filterset Options](https://django-filter.readthedocs.io/en/master/ref/filterset.html)

#### Sendmail

-   [Django contact form tutorial](https://wsvincent.com/django-contact-form/)
    by William S. Vincent

#### Django tutorials

-   [Python Django tutorial](https://www.youtube.com/watch?v=UmljXZIypDc) by
    Corey Schafer

Acknowledgements
================

-   Yoni Lavi
-   Neil Mc Ewen
-   Nakita McCool
-   Robin Zigmond
