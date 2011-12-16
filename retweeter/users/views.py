from django.http import HttpResponse
from django.http import HttpResponseRedirect
from retweeter.utils.helpers import render_page
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.http import urlencode

@login_required
def users(request):
	if not request.user.is_superuser:
		params = urlencode({'error': 'You are not permitted to access the admin features.'})
		return HttpResponseRedirect('/?' + params)

	data = {}

	u = User.objects.filter(is_superuser=0)
	data['users'] = u

	return render_page('users.html', data, request)

@login_required
def add_staff(request, user_id):
	if not request.user.is_superuser:
		params = urlencode({'error': 'You are not permitted to access the admin features.'})
		return HttpResponseRedirect('/?' + params)

	u = User.objects.get(id=user_id)
	u.is_staff = True
	u.save()

	params = urlencode({'msg': 'User ' + u.username + ' was added as a staff.'})
	return HttpResponseRedirect('/users/?' + params)

@login_required
def remove_staff(request, user_id):
	if not request.user.is_superuser:
		params = urlencode({'error': 'You are not permitted to access the admin features.'})
		return HttpResponseRedirect('/?' + params)

	u = User.objects.get(id=user_id)
	u.is_staff = False
	u.save()

	params = urlencode({'msg': 'User ' + u.username + ' is not a staff anymore.'})
	return HttpResponseRedirect('/users/?' + params)
