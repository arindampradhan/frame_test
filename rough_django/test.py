import os

BASE_DIR = os.path.dirname(os.path.dirname('__file__'))
print BASE_DIR


TEMPLATE_DIRS = (
            os.path.join(os.path.dirname(BASE_DIR), "static", 'templates'),
            )
print TEMPLATE_DIRS
