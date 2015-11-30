# What is it? #

This is a fork of well-known <a href='http://code.google.com/p/couchdb-python/'>couchdb-python</a> project.


# Goals #
Main goal - drop away buggy unneeded httplib2 and replace it with mature robust curl library (via <a href='http://pycurl.sourceforge.net/'>pycurl</a> wrapper).


# Status #
  * Server - works
  * Database - works
  * Document (with attachments) - works
  * Views - work

Actually, everything is working pretty well, and is capable to face much more load, than httplib-based implementation.

And, we are not dead! Couchdb-python-curl is working in a number of our company internal projects, so it's production-ready (at least, for us). Patches, fixes, bugs are welcome!

# Documentation #

http://packages.python.org/couchdb-python-curl/

# Installation #

easy\_install couchdb-python-curl

# Downloads #

http://packages.python.org/couchdb-python-curl/