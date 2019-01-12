# travis [![Build Status](https://travis-ci.org/damianism/rate-my-rig.svg?branch=master)](https://travis-ci.org/damianism/rate-my-rig)

BUILD ME A RIG 
==================

\<\<\< gif \>\>\>

Real world application
----------------------

There are many <a href="https://damianism.github.io/custom_pc/benefits.html" target="_blank">benefits</a>
of building your own computer. However, the whole process can be cumbersome,
frustrating and nerve-wrecking.

Here are a few problems associated with building your own computer.

##### Research

The amount of time spent on research to get the right build for yourself can be
quite off putting, it’s definitely not for the impatient, as I personally spent
over two months researching different configurations and component in the hopes
of getting the exact performance that I wanted. You may even find yourself
having to wait even longer in some circumstances such as waiting for a driver of
a component you’re interested in to be updated or waiting for new component to
be released. I personally had to wait two weeks for the new Ryzen cpu line-up to
be released.

##### Put it together

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

##### Aim

Wouldn’t it be great if somebody else had gone through EVERYTHING stated above
in order to get a specific build fully functional, so you wouldn’t have to? This
is exactly what this web app aims to achieve by allowing its users to share
their complete builds with other users wishing to build their own systems.

As a user you may

-   Use an existing build as a blueprint for your own build.
-   Get ideas from an existing build for your own build.
-   Gain assurance on components compatibility before system assembly.
-   Contact the owner/author of a build to seek advice via comments.
-   Gain assurance of the system performance before system assembly.
-   Purchase the exact posted build.
-   Purchase a build posted yourself.

This web will ultimately save its users days if not months spent on research and
running diagnostics to get their ideal configurations since everything will be
available to them from the start, even the actual performance of the system
they’re trying to build.

###### Purchasing builds:

Users not wishing to assemble their own units may purchase a pre-existing or
their own posted build on the website through us for a flat fee of £100. After
placing your order, we will assess your selected configuration and contact you
via phone or email within 24 hours to discuss your configuration. At this point
if your selected configuration passes our compatibility tests, and you are happy
with your selected configuration, you will then be charged for the full cost of
the selected components (RAM, GPU, CPU etc). Upon completion of the order, we
will ship your new and fully tested assembled unit to you.



Pre-registered testing accounts
-------------------------------

Please feel free to use the following accounts for testing purposes. For more
information about the differences between normal and admin accounts please refer
to “[Admin privileges](#future-features)” of the features section.

-   Admin account:
    -   skullphish
    -   admin

-   Normal accounts:
    -   beny1976
    -   user

Wireframes
==========

Wireframes created using [mockingbird](https://gomockingbird.com/home).

Only list links to wireframes

Features
========

The list below shows all the added features that needed to be in place for the
project to be fully functional. The features planned to be added in the future
are listed in the “[Future Features](#future-features)” section of this
documentation.

-   registration – allows users to register
    ([register.html](https://github.com/damianism/vocab_journal/blob/master/templates/register.html)).

-   Login – registered users can log in
    ([index.html](https://github.com/damianism/vocab_journal/blob/master/templates/index.html)).

-   Cart - …

Just list the items no need to go in depth

Future Features
===============

All the features listed within this section WILL be added upon completion of the
course in the exact order listed below. The following features were shelved only
due to lack of time and my hectic work schedule but will be perused once the
course is completed to be presented as a portfolio.

1.  Paginations

2.  User-specific lookup details

3.  Enhanced administration tools
    1.  delete users
    2.  edit user info

4.  Global search box to search keywords in
    1.  vocabs
    2.  tags
    3.  reference text
    4.  miscellaneous text
    5.  context text

5.  Adding vocab pronunciations (audio)

6.  More languages – API supports multiple languages

7.  Users to be able to download all their entered data (all user vocabs and
    their stats)

8.  Vocab of the day

9.  Vocab memory test game

    1.  One of the vocabs entered by the user will be presented to the user to
        define with a very basic scoring system e.g. “you managed to get 7/10
        definitions right”

Technologies Used
=================

The list of technologies used for this project in no specific order.

1.  [Python](https://www.python.org/downloads/) v3.4.3

    -   Unittest module for Test Driven Development.

2.  [FLASK](http://flask.pocoo.org/) v1.0.2

3.  [Jinja2](http://jinja.pocoo.org/docs/2.10/)

    -   Used to apply logic to flask templates

4.  Markdown

5.  Pip3
    -   Used to install various python modules.

6.  Django

7.  [PostgresSQL](https://www.postgresql.org/)

8.  [Bootstrap v4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
    -   Responsive design
    -   Styling
        -   Cards, Buttons, accordions, animations.
        -   Text alignment.
        -   Colouring.

9.  JavaScript and [jQuery](https://jquery.com/) v3.3.1
    -   Debugging
    -   Stripe


10. [SASS](https://sass-lang.com/)
    -   Adopted main method of styling. Used with combination of SASS variables,
        mixins and functions in total of 8 scss files.

11. HTML5

12. CSS
    -   Used with SASS.

13. Flexbox
    -   Primary tool for centring item.
    -   Primary layout tool.

14. [Google fonts](https://fonts.google.com/)
    -   [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono) – applied
        to the buttons (small and large)
    -   [Roboto](https://fonts.google.com/specimen/Roboto) – used as the main
        font for the project

15. [Gimp](https://www.gimp.org/)
    -   Applied a filter to the selected background to better suit the theme of
        the project.
    -   Image format conversion, rescaling and touch ups.

16. Microsoft Word
    -   To write up the content of the README.md file before deployment.

17. Chrome and Firefox developer tools
    - Used extensively for live-testing and running numerous different tasks.
        To name a few:
        -   Testing JavaScript functions.
        -   Individual elements loading times.
        -   Website/grid responsiveness.
        -   Element Colours, style, opacity and etc.
        -   Aligning and centring.
        -   Attribute value search.
        -   Fluidity and core functionality of the website.

18. [Git/Github](https://github.com/damianism)
    -   Kept track of the project’s evolution with frequent commits and
        informative messages.
    -   Secondary platform for deployment.
    -   GitHub was also used to access bootstrap’s source code.

19. [Heroku](https://www.heroku.com/)
    -   Used to as the primary deployment platform.

20. Cloud9
    -   Used as the main editor.

Testing and challenges
======================

Logic Debugging
---------------

STRIPE API testing

Email sendmail

Email reset

Travis

Responsiveness/Aesthetics/Functionality Testing
-----------------------------------------------

The responsiveness, functionality, fluidity of each page was extensively and
virtually tested on all the Chrome/Firefox responsive tool’s available devices,
ranging from Amazon fire tablets to iPhone x. Additionally, every page was
numerously loaded on the following devices by various users in order to identify
possible malfunctions and misbehaving elements.

-   Galaxy S5 (width less than 370px)
-   iPhone x
-   Google Pixel 2
-   iPhone 7 Plus
-   Nexus 6P
-   22inch Full HD 1080p monitor
-   25inch Quad HD 1440p screen
-   13inch Full HD screen of a Dell XPS Ultrabook
-   15inch HD screen of a Dell Precision M4600

Browsers
--------

The following browsers were used to test the final version of the website with.

-   Opera Version 56.0.3051.104
-   Firefox Version 63.0.3 (64-bit)
-   Version 70.0.3538.110 (Official Build) (64-bit)
-   Chrome Mobile on Android Pie
-   Chrome Mobile on Android Oreo
-   Firefox Mobile on Android Pie
-   Safari Mobile iOS 12

Deployment
==========

[Heroku](https://id.heroku.com/login) was used as the PRIMARY deployment
platform for this project. Throughout the project, git was used to seamlessly
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
