=====================
PDF Repository Viewer
=====================

A Flask app that will serve pdf files from a repository.


A demo can be viewed here:  https://pdf-repo-viewer.herokuapp.com/


What it does
------------

Lets a user navigate through your directory to view pdf files.  It is really simple and is supposed to be.


What it doesn't
---------------

Add files.  Delete files.  Prevent anyone from viewing files.  Search for files.  It's really basic.


Motivation
----------

I needed a central location for pdf reports that are accessible by anyone.  The good thing about pdf files is
that they are viewable in a browser, so you really don't need adobe acrobat or anything special installed on your computer.
You can view pdfs from your phone or computer, and as long as your folder structure makes sense,
users will easily find your pdf reports.


Roadmap
-------

This app really needs control of who can access the pdf files.  When I say "anyone" can access your reports, I mean it.
You don't really want that do you?

I am thinking of something like this:

* POST /api/login -> login & get some type of response containing a user_profile

* GET /api/user/<user_profile>/files/ -> list files for a user_profile
* POST /api/user/<user_profile>/files/ -> create files for a user_profile

* GET /api/user/<user_profile>/files/<file_id> -> get specific file for user_profile
* PUT /api/user/<user_profile>/files/<file_id> -> update specific file for user_profile
* DELETE /api/user/<user_profile>/files/<file_id> -> delete specific file for user_profile