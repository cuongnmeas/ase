'''
Created on Apr 3, 2014

@author: ducdienpt
'''
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from mongoengine.django.auth import User
from mongoengine.queryset.visitor import Q

from myapp.models import UserProfile, Curriculumn, Material
from myapp.util import context_processors


def index(request):
	lisUserProfile = {}
# 	print('begin')
# 	for user in lisUserProfile:
# 		print(user.company)
# 	print('finish')
	c = {'lisUserProfile':lisUserProfile,}
	if request.method == 'GET':
		return render(request, 'myapp/search-mentor.html', c)
	elif request.method == 'POST':
		try:
			keyword = request.POST['search']
			users = User.objects(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
			#search data
# 			lisUserProfile = UserProfile.objects(user_id__in=users,is_mentor=True)
			lisUserProfile = UserProfile.objects(user_id__in=users)
			
			listAllCurriculumn = Curriculumn.objects()
			listCurriculumn =Curriculumn.objects(name__icontains=keyword)
			c = {'lisUserProfile':lisUserProfile,'listCurriculumn':listCurriculumn,'listAllCurriculumn':listAllCurriculumn,'search':keyword}
			#get data from mongodb
			c.update(csrf(request))
			c.update(context_processors.user(request))
			return render_to_response("myapp/search-mentor.html", c)
		except Exception:
			c.update(csrf(request))
			c.update(context_processors.user(request))
			return render_to_response("myapp/search-mentor.html", c)
	return render(request, 'myapp/search-mentor.html', c)