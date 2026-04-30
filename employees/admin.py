from django.contrib import admin
from .models import Abakozi, Umushahara


# Register your models here.
class UmushaharaAdmin(admin.ModelAdmin):
    list_display = ('id','umukozi','get_akazi', 'umushahara')
    def get_akazi(self, obj):
        return obj.umukozi.akazi
    get_akazi.short_description = 'akazi'

admin.site.register(Umushahara, UmushaharaAdmin)

class AbakoziAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'akazi', 'arakora', 'itariki')
    list_filter = ('arakora', 'akazi')
    search_fields = ('first_name', 'last_name', 'akazi')
    list_editable = ('arakora',)

admin.site.register(Abakozi, AbakoziAdmin)