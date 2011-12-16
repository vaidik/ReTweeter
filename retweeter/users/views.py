from django.http import HttpResponse
from django.http import HttpResponseRedirect
from retweeter.utils.helpers import render_page
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def users(request):
	if not request.user.is_superuser:
		return HttpResponseRedirect('/')

	data = {}

	u = User.objects.filter(is_superuser=0)
	data['users'] = u

	return render_page('users.html', data, request)

@login_required
def add_staff(request, user_id):
	if not request.user.is_superuser:
		return HttpResponseRedirect('/')

	u = User.objects.get(id=user_id)
	u.is_staff = True
	u.save()

	return HttpResponseRedirect('/users/')

@login_required
def remove_staff(request, user_id):
	if not request.user.is_superuser:
		return HttpResponseRedirect('/')

	u = User.objects.get(id=user_id)
	u.is_staff = False
	u.save()

	return HttpResponseRedirect('/users/')
