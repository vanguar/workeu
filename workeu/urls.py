from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.landing, name='landing'), # Переадресация для вывода Лендинга
    url(r'^post_list/$', views.post_list, name='post_list'), # ... для вывода страницы постов по Польше
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), # ... для более детального вывода поста по Польше
	url(r'^contactView/$', views.contactView, name='contactView'), # ... для контактной формы
	url(r'^thanks/$', views.thanks, name='thanks'), # ... для страницы подтверждения отправки сообщения
	url(r'^postp_list_pribaltik/$', views.postp_list_pribaltik, name='postp_list_pribaltik'), # ... для вывода страницы постов по Польше
	url(r'^postp_detail_pribaltik/(?P<pk>[0-9]+)/$', views.postp_detail_pribaltik, name='postp_detail_pribaltik'), # ... для более детального вывода поста по Прибалтике
	url(r'^postf_list_finland/$', views.postf_list_finland, name='postf_list_finland'), # ... для вывода страницы постов по Польше
	url(r'^postf_detail_finland/(?P<pk>[0-9]+)/$', views.postf_detail_finland, name='postf_detail_finland'), # ... для более детального вывода поста по Прибалтике
	url(r'^alljobs/$', views.alljobs, name='alljobs'), # страница со всеми вакансиями 
    url(r'^resume/$', views.resume, name='resume'), # страница с резюме	
	url(r'^HelpInVisa/$', views.HelpInVisa, name='HelpInVisa'), # страница с визой
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #прибавим функцию static() для вывода фото