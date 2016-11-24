beetsonic
=========

Subsonic server interface for [beets](http://beets.io/). 
Work in progress version.
Right now, server API is fixed at 1.14.0.

Development
-----------

In order to generate Python binding class from Subsonic XSD:
```
pyxbgen -u xsd/subsonic-rest-api-version.xsd -m beetsplug.subsonic.bindings
```

Dependencies
------------

```
beets
Flask (for Web framework)
PyXB (for binding Subsonic model)
requests (for lyrics fetching)
flask-cors (for CORS)
unittest2 (for testing)
mock (for testing)
```
