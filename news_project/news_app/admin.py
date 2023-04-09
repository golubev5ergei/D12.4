from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'date_published')
    search_fields = ('title',)
    list_editable = ('cat',)
    list_filter = ('cat', 'date_published')

admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subscribers')

    def get_subscribers(self, obj):
        return "\n".join([user.username for user in obj.subscribers.all()])

    get_subscribers.short_description = 'Подписчики'

admin.site.register(Category, CategoryAdmin)

