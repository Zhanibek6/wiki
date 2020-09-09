from django.shortcuts import render

from . import util
from .forms import NewEntryForm
from django.shortcuts import redirect
import markdown
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def entry(request, title):
	md = markdown.Markdown()
	ent = util.get_entry(title)
	return render(request, "encyclopedia/entry.html", {
		"title": title,
		"content": md.convert(ent)
	})



def search(request):
	title = request.GET.get('q').capitalize()
	#results = util.search_entries(title)
	results = util.list_entries()
	results = [x for x in results if title in x] 
	return render(request, "encyclopedia/search.html", {
		"results": results
	})



def new_page(request):
	if request.method == 'POST':
		form = NewEntryForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			title = cd['title']
			content = cd['text']
			util.save_entry(title, content)
			return redirect('index')

	else:
		return render(request, "encyclopedia/new_page.html", {
			"form": NewEntryForm()
		})



def edit(request, title):
	if request.method == 'POST':
		form = NewEntryForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			title = cd['title']
			content = cd['text']
			util.save_entry(title, content)
			return redirect('index')

	entry = util.get_entry(title)
	form = NewEntryForm(initial={
		"title": title,
		"text": entry
	})
	return render(request, "encyclopedia/new_page.html", {
		"form": form
	})



def random_page(request):
	entries = util.list_entries()
	ent = random.choice(entries)
	return redirect(entry, ent)


