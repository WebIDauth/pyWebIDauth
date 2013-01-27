import os, rdflib
from rdflib import plugin
from rdflib.namespace import Namespace

plugin.register(
    'sparql', rdflib.query.Processor,
    'rdfextras.sparql.processor', 'Processor')
plugin.register(
    'sparql', rdflib.query.Result,
    'rdfextras.sparql.query', 'SPARQLQueryResult')


""" Verify if modulus matches """
def verify(webid, modulus):

    g = rdflib.Graph();
    r = g.parse(webid)

    qres = g.query(
        """SELECT ?m ?e WHERE { 
            <https://my-profile.eu/people/deiu/card#me> cert:key 
                [ cert:modulus ?m ] .
        }""",
        initNs=dict(cert=Namespace("http://www.w3.org/ns/auth/cert#")))

    for row in qres.result:
        if (row[0].replace('\n','').replace('\r','') == modulus):
            return True

    return False
