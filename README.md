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
Flask
PyXB
requests
flask-cors
```
