from django.contrib import admin
from .models import Author, ArticleType, Journal, Article, Citation

################################################################
################################################################
## Name: admin.py
## Author: Bradley Dowling, 2021
## Description: admin.py controls the layout and functionality
##              of the admin site.
##
##

# Model registrations:
admin.site.register(Author)
admin.site.register(ArticleType)
admin.site.register(Journal)

# Site customization:
admin.site.site_header = "Conversations with a Neuron | Admin"
admin.site.site_title = "Conversations with a Neuron"

# Set up of tabular inline view of citations (used when editing an article):
class CitationInline(admin.TabularInline):
    model = Citation
    fields = ('citation_number', 'citation_text')
    extra = 0

# Set up of the Article app's admin page:
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'journal', 'type')
    list_filter = ['journal']
    inlines = [CitationInline]
    
    # Additional functionality/styling:
    class Media:
        js=('articles/js/inline_incrementer.js',)

# Registration of Article admin page:
admin.site.register(Article, ArticleAdmin)