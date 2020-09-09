from django import forms


class SearchForm(forms.Form):
	searching = forms.CharField(label='Search Encyclopedia')


class NewEntryForm(forms.Form):
	title = forms.CharField(label="Title", max_length=64)
	text = forms.CharField(widget=forms.Textarea)