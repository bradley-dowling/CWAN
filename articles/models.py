from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

################################################################
################################################################
## Name: models.py
## Author: Bradley Dowling, 2021
## Description: models.py defines all of the fields and methods
##              of the data stored in the article database.
##
##

# Author represents the author of an article
class Author(models.Model):
    # Fields:
    first_name = models.CharField(max_length=70, help_text='Enter first name of author')
    last_name = models.CharField(max_length=70, help_text='Enter last name of author')

    # Metadata:
    class Meta:
        ordering = ['last_name', 'first_name']

    # Methods:
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# ArticlyType represents the type of article (anatomy, physiology, review, etc.)
class ArticleType(models.Model):
    # Fields:
    type = models.CharField(max_length=70, help_text='Enter type of article here')

    # Metadata:
    class Meta:
        ordering = ['type']

    # Methods:
    def __str__(self):
        # String for representing the ArticleType object
        return self.type

# Journal represents a single edition/publication of Conversations with a Neuron
class Journal(models.Model):
    # Fields:
    editor_first_name = models.CharField(max_length=70, help_text='Enter Editor\'s first name')
    editor_last_name = models.CharField(max_length=70, help_text='Enter Editor\'s last name')
    publication_date = models.DateField(null=True, blank=True)
    volume_number = models.SmallIntegerField(unique=True)
    cover = models.ImageField(upload_to='images/journal_images', blank=True, null=True)
    banner = models.ImageField(default='', upload_to='images/journal_images', blank=True, null=True)
    preface = RichTextUploadingField(config_name='article_editor', blank=True, null=True)
    downloadable_file = models.FileField(upload_to='volumes/', blank=True, null=True)

    # Metadata:
    class Meta:
        ordering = ['publication_date']

    # Methods:
    def __str__(self):
        return f'{self.editor_last_name} {self.publication_date.year}'

# Citation represents the full citation/reference within an article
class Citation(models.Model):
    # Fields:
    article = models.ForeignKey('Article', on_delete=models.SET_NULL, null=True, help_text='Select article associated with this citation')
    citation_number = models.SmallIntegerField(default=1, help_text='Add reference number')
    citation_text = RichTextField(config_name='citation_editor', blank=True, null=True)

    # Metadata:
    class Meta:
        ordering = ['citation_number', 'citation_text']

    # Methods:
    def __str__(self):
        return f'{self.citation_number}. {self.citation_text}'

# Article represents the full text and all other components of an article
class Article(models.Model):
    # Fields:
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, help_text='Select an author for this article')
    title = models.TextField(default='', help_text='Enter the title for this article')
    journal = models.ForeignKey('Journal', on_delete=models.SET_NULL, null=True, help_text='Select which journal this article belongs to')
    summary = models.TextField(default='', null=True, blank="True", help_text='Enter the summary for this article')
    contents = RichTextUploadingField(config_name='article_editor', blank=True, null=True)
    type = models.ForeignKey('ArticleType', on_delete=models.SET_NULL, null=True, help_text='Select this article\'s type')

    # NOTE: pg numbers are set so that individual articles can be downloaded from a single PDF stored
    #       in an issue/publication of the journal
    first_page = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Enter the volume's page number for the first page of this article")
    last_page = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Enter the volume's page number for the last page of this article")

    # Metadata:
    class Meta:
        ordering = ['journal', 'title']

    # Methods:
    def __str__(self):
        return self.title