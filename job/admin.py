from django.contrib import admin
from .models import Carousel,Top_content,Client_review,products,catagory,Specification,Project,Service,Blogpost,Phone_number
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# class CarouselAdmin(admin.ModelAdmin):
#     search_fields = ('title',"heading2",'text' )
#     list_filter   = ('enable', )
#     list_display  = ('title','position', )

# admin.site.register(Carousel,CarouselAdmin)

# client
class Client_reviewAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display  = ('title', )
admin.site.register(Client_review,Client_reviewAdmin)

class TabularSpec(admin.TabularInline):
    model = Specification

class catagoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class productADI(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('title', 'catagory__title', )
    list_display  = ('title','position', )
    list_filter   = ('Enable','index', 'catagory__title',  )
    inlines = [TabularSpec]

    class Meta:
        model=products

admin.site.register(catagory,catagoryAdmin)
admin.site.register(products,productADI)
admin.site.register(Specification)
admin.site.register(Service)
admin.site.register(Blogpost)
admin.site.register(Phone_number)
admin.site.register(Top_content)



class ProjectADI(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ('title', )
    list_display  = ('title','position', )
    list_filter   = ('Enable','index',  )

admin.site.register(Project,ProjectADI)
