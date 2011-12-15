from django import forms

class TweetForm(forms.Form):
	tweet = forms.CharField(widget=forms.Textarea, max_length=140)
