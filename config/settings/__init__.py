from decouple import config

if config('DEBUG') == 'True':
    from .dev import *
else:
    from .prod import *