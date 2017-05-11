from .production import *

try:
    from .local import *
except:
    pass

"""
If local settings file is added to .gitignore file
only production settings will be available
"""
