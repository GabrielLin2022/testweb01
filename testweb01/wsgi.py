"""
WSGI config for testweb01 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testweb01.settings')#environ.setdefault設定為初始環境，'testweb01的資料夾，下的settings檔案'，架到伺服器上時，用自動帶入這個路徑

application = get_wsgi_application()
