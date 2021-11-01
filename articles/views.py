from django.shortcuts import render
from django.views import generic
from .models import *
# Create your views here.
from django.http import HttpResponse
import datetime
import io
import PyPDF2
from django.http import FileResponse

def home(request):
    """View function for the home page (currently under construction...)"""
    context = {
        'isHome': True,
    }

    return render(request, 'articles/index.html', context=context)

def article_list(request, volume_number):
    """View function to display articles in a specific volume"""
    article_list = Article.objects.filter(journal__volume_number=volume_number)
    journal = Journal.objects.get(volume_number=volume_number)
    publication_month = journal.publication_date.strftime("%b")
    publication_year = journal.publication_date.year
    neuroanatomy_list = article_list.filter(type__type='Neuroanatomy')
    neurophysiology_list = article_list.filter(type__type='Neurophysiology')
    neuroreview_list = article_list.filter(type__type='Neuroscience In Review')
    context = {
        'volume_number': volume_number,
        'article_list': article_list,
        'journal': journal,
        'neuroanatomy_list': neuroanatomy_list,
        'neurophysiology_list': neurophysiology_list,
        'neuroreview_list': neuroreview_list,
        'publication_month': publication_month,
        'publication_year': publication_year,
    }
    return render(request, 'articles/article_list.html', context=context)

def article_view(request, article_id):
    """View function to display article details"""
    article = Article.objects.get(id=article_id)
    author = article.author.id
    journal = article.journal
    citation_list = Citation.objects.filter(article_id=article_id).order_by('citation_number')
    other_articles = Article.objects.filter(author_id=author).exclude(id=article_id)
    context = {
        'article': article,
        'citation_list': citation_list,
        'other_articles': other_articles,
        'journal': journal,
    }
    return render(request, 'articles/article_view.html', context=context)

def article_download(request, article_id):
    """View function for returning a PDF of an article"""
    article = Article.objects.get(id=article_id)
    first_page = article.first_page
    last_page = article.last_page
    
    # Try to open the volume
    pdfFile = open(article.journal.downloadable_file.path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile, strict=False)
    pdfWriter = PyPDF2.PdfFileWriter()
    
    for page in range(first_page - 1, last_page):
        pdfWriter.addPage(pdfReader.getPage(page))
    
    # Create the buffer and write to it
    buffer = io.BytesIO()
    pdfWriter.write(buffer)
    buffer.seek(0)
    
    # Set up filename
    file_name = "CWAN_{last_name}_{article_type}_{year}.pdf".format(last_name = article.author.last_name, article_type = article.type, year = article.journal.publication_date.year)
    
    return FileResponse(buffer, as_attachment=True, filename=file_name)