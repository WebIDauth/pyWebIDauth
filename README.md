pyWebIDauth
===========

A quick python implementation of WebID authentication. More details about WebID [here](http://webid.info/).

Dependencies
------------

 * mod_wsgi (Apache)
 * bottle.py (the REST server)
 * rdflib (RDF utilities)

RDFLib may be installed with setuptools (easy_install) or pip:

    $ easy_install rdflib
or

    $ pip install rdflib

The reason why Apache is required is to expose the certificate contents to the Web application.

License
-------

MIT
