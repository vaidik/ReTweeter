from django import forms

class SubmitTweet(forms.Form):
	status = forms.CharField(widget=forms.Textarea, max_length=140)
