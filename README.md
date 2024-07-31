# marin
The Marin cosplay contest manager, originally written for AnimeFest/GameFest/World Fandom.  (Yes, I did read My Dress Up Darling.)

I wrote this using Python and Django because I was sick of the sheer amount of paperwork needed to run a cosplay contest, and I wanted something that I can very cheaply implement with extremely low-end Linux hardware.

You will need these additional Python libraries on top of the version of Django I used (>=5.0.0) and Python 3.12:

- django2-tables
- django2-bootstrap3
- brother_ql-inventree (this is required for the Brother QL-600 label printer we used for printing badge labels for the contest)

These libraries will pull additional required libraries (such as Pillow).

THIS IS DEFINITELY DEVELOPMENT CODE.  DO NOT DEPLOY UNLESS IF YOU KNOW WHAT YOU ARE DOING! (When I was writing this, the whole CrowdStrike incident was happening.)  This is outside of what I would normally program, and I had to learn a lot of concepts in a couple of days.

I put this up here in the hopes that others will take this and improve it for their own contests.

We ran this on a Raspberry Pi 4 on Apache, using the SQLite database.
