from django.contrib import admin
from .models import menus,hmenus,CustomUser,Reservation,tables
# Register your models here.
admin.site.register(menus)
admin.site.register(hmenus)
admin.site.register(CustomUser)
admin.site.register(Reservation)
admin.site.register(tables)

class menusAdmin(admin.ModelAdmin):
    list_display=('name','desc','price')
    
