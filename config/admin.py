from django.contrib import admin

from .settings.base import ADMIN_INDEX_TITLE, ADMIN_SITE_HEADER, ADMIN_SITE_TITLE


admin.site.site_header = ADMIN_SITE_HEADER
admin.site.site_title = ADMIN_SITE_TITLE
admin.site.index_title = ADMIN_INDEX_TITLE