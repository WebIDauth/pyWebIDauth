pyWebIDauth
===========

A quick python implementation of WebID authentication. More details about WebID [here](http://webid.info/).

Installation
------------

You can install the server into /var/www/pyWebIDauth. If you want to change the location, then you need to remember to modify the wsgi script (webid.wsgi) to reflect the new path.

Once the server is up and running, you can go to `https://localhost/auth` to test the authentication script.

Dependencies
------------

 * mod_wsgi (Apache)
 * bottle.py (the REST server)
 * rdflib (RDF parsing)
 * rdfextras (RDF utilities)

rdflib and rdfextras may be installed with setuptools (easy_install) or pip:

    $ easy_install rdflib
or

    $ pip install rdflib

The reason why Apache is required is to expose the certificate contents to the Web application. Here is a typical Apache configuration:

```
<VirtualHost *>
    ServerName py.example.com 
    # ssl.conf contains your server's SSL certificates
    Include /var/www/conf/ssl.conf

    WSGIDaemonProcess test user=www-data group=www-data processes=1 threads=5
    WSGIScriptAlias / /var/www/pyWebIDauth/webid.wsgi
    
    <Directory /var/www/pyWebIDauth>
        WSGIProcessGroup test
        WSGIApplicationGroup %{GLOBAL}
        WSGIPassApacheRequest On
        SSLOptions +StdEnvVars
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
```


License
-------

MIT


