# Create your views here.
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.template import Context
from django.template.loader import get_template

def main_page(request):
	# Because we have already set TEMPLATE_DIR in settings, so
	# the system will know the location of the main_page.html
	template = get_template('main_page.html')

	variables = Context({
		'head_title': 'Django Bookmarks',
		'page_title': 'Welcome to Django Bookmarks',
		'page_body':  'Where you can store and share Bookmarks!',
		'user': 	request.user

		})
	output = template.render(variables)
	return HttpResponse(output)


def user_page(request, username):
	try:
		user = User.objects.get(username = username)
	except:
		raise Http404('Requested user not found ~~~~lalalala')
	Bookmarks = user.bookmark_set.all()
	template = get_template('user_page.html')
	variables = Context({
		'username': username,
		'bookmarks': Bookmarks
		})
	output = template.render(variables)
	return HttpResponse(output)

