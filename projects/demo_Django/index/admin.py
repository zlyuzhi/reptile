from django.contrib import admin
from index.models import BookInfo, HerroInfo


# Register your models here.
class HerroInfoStackInlin(admin.TabularInline):
    model = HerroInfo
    extra = 1

class HerroInfoAdmin(admin.ModelAdmin):
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True


#定义管理样式
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    list_display =['id','btitle','image']
    list_filter = ['btitle']
    search_fields = ['bread']
    fieldsets = (  # 分组显示
        # (组名称,{'fields':[属性,...]})
        ('基本', {'fields': ['btitle', 'bpub_date','image']}),
        ('可选', {'fields': ['bread', 'bcomment']})
    )

    inlines = [HerroInfoStackInlin]

admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HerroInfo,HerroInfoAdmin)
