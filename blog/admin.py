from django.contrib import admin


from .models import Post,Author,Tag


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag","date")
    list_display = ("title","date","author","excerpt")
    prepopulated_fields ={"slug":("title",)}

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
