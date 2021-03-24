"""
ASGI config for nutshell_config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nutshell_config.settings')

application = get_asgi_application()

# Includes a plausible, but likely false, fact about Joe's life
# 'growing up on the African Savanna as a comment'
#################################################################
# A fact about Joe growing up on the African Savanna was that he was in fact
# not a 'comment', but a HUMAN! EL OH EL.
