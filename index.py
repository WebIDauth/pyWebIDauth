import bottle
import WebIDauth
import M2Crypto
import os, wsgiref
from bottle import route, get, request


@get('/')
def hello():
    return "Hello World!"


@get('/auth')
def auth():

    cert=request.environ['SSL_CLIENT_CERT']
    # this works
    c=M2Crypto.X509.load_cert_string(cert)

    alt=c.get_ext('subjectAltName').get_value()
    alt=alt.split(',')
    for uri in alt:
        if uri.find('URI:') != -1:
            webid=str(uri)[4:len(uri)] # remove the URI: part
    webid=webid.strip()

    modulus=c.get_pubkey().get_modulus()

    verified=WebIDauth.verify(webid, modulus)
    if verified == True:
        return 'True'
    else:
        return 'False'
