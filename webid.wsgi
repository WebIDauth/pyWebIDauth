import sys, os, bottle

sys.path = ['/var/www/py/'] + sys.path
os.chdir(os.path.dirname(__file__))

import index # This loads the application

application = bottle.default_app()
