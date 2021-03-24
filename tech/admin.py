from django.contrib import admin
from tech.models import Contact, Service, Blog

admin.site.register((Contact, Service))
admin.site.register(Blog)

# Dataclass # Changing Admin header
admin.site.site_header = "BtEch"
admin.site.site_title = "Welcome to BTech Admin Site"
admin.site.index_title = "Welcome back"
