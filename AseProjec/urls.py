import os

from django.conf import settings
from django.conf.urls import patterns, url , include

from myapp.views import Home, AccountSetting, PostDetail, SignIn, MentorPost, \
	Profile, SignUp, SignOut, PeopleDirectory, Chat, PersonalHome , AuthenFail


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
						url(r'^error-authenticate$', AuthenFail.index),
						url('', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^$', Home.index),
                       url(r'^home$', Home.index),
                       url(r'^index$', Home.index),
                       url(r'^account-setting$', AccountSetting.index),
                        url(r'^blog-single$', PostDetail.index, name='blog-single'),
                        url(r'^mentorpost$', MentorPost.index),
						url(r'^mentorview$', Home.index,name='mentorview'),
						url(r'^studentview$', Home.index,name='studentview'),
						url(r'^personalhome$', PersonalHome.index,name='personalhome'),
                        url(r'^mentorpost$', MentorPost.index),
                        url(r'^mentorview$', Home.index,name='mentorview'),
                        url(r'^studentview$', Home.index,name='studentview'),
                        url(r'^personalhome$', PersonalHome.index,name='personalhome'),
                       url(r'^signin$', SignIn.index, name='signin'),
                       url(r'^profile$', Profile.index, name='profile'),
                       url(r'^signup$', SignUp.index, name='signup'),
                       url(r'^signout$', SignOut.index, name='signout'),
                       url(r'^create-profile$', Profile.createProfile),
                       url(r'^update-profile$', Profile.updateProfile),
                       url(r'^people-directory$',PeopleDirectory.index),
                       url(r'^chat$',Chat.index),
                       url(r'^post-detail$', PostDetail.index, name='post-detail'),
                       url(r'^lecture-detail$', PostDetail.index, name='lecture-detail'),
                       url(regex  = r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 
    view   = 'django.views.static.serve', 
    kwargs = {'document_root': os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))+"/common",
              'show_indexes' : True})
    # Examples:
    # url(r'^$', 'AseProjec.views.home', name='home'),
    # url(r'^AseProjec/', include('AseProjec.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
