import coloredlogs
import logging

# Set up colored logging
log_format = '%(asctime)s - %(levelname)s - \n\n\
----------------------------------------------------------------------\n\n\
%(message)s\n\n\
----------------------------------------------------------------------\n\n'

coloredlogs.install(level='DEBUG', fmt=log_format)


