from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from blog.models import Entry

def index(request):
    latest_entries = Entry.objects.all().order_by('-created_at')
    t = loader.get_template('blog/index.html')
    for entry in latest_entries:
        entry.url = entry.title.replace(' ', '_')

    return render(request, 'blog/index.html' , {'latest_entries': latest_entries })

def entry(request, entry_url):
    single_entry = get_object_or_404(Entry, title=entry_url.replace('_', ' '))
    single_entry.views += 1
    single_entry.save()
    template = loader.get_template('blog/entry.html')
    context = { 'single_entry': single_entry, }
    return HttpResponse(template.render(context))
