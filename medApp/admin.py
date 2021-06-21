from django.contrib import admin
from .models import UserInfo, content, tagMdl

# Register your models here.
admin.site.register(UserInfo)

admin.site.register(tagMdl)


class contents(admin.ModelAdmin):
    # def has_add_permission(self, request):
    #     return False

    list_display = ('no', 'doc_id', 'title', 'authors',
                    'keywords', 'date')
    list_filter = ('date', 'doc_id')


admin.site.register(content, contents)
