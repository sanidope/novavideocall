

try:
    from . local import *

except:
    pass


try:
    from .production import *

except:
    pass

try:
    from .pythonanywhere import *

except:
    pass