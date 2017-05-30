from django.utils import timezone
from .models import Post
from .models import Postp
from .models import Postf
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django import forms



# ПОЛЬША
# Лендинговая страница по краткому выводу постов по Польше
def landing(request):
    postsp = Postp.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:10] #Ограничиваем вывод постов в Таллинне на главной странице
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:10] #Ограничиваем вывод постов в Польше на главной странице
    postsf = Postf.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:10] #Ограничиваем вывод постов в Финляндии на главной странице
    return render(request, 'workeu/landing.html', {'posts': posts, 'postsp': postsp, 'postsf': postsf})
	

def post_list(request): # Страница вывода постов по Польше
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'workeu/post_list.html', {'posts': posts})
	
	
def post_detail(request, pk): # Страница вывода поста по Польше более детально
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'workeu/post_detail.html', {'post': post})

def techwork(request): # Страница вывода сообщения о выполнении технических работ
            return render(request, 'workeu/techwork.html')		

#Контактная форма для отправки сообщения		
class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))#Заполняем в скобках, чтобы тема работала в бутрстраповских стилях
	sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))#Заполняем в скобках, чтобы тема работала в бутрстраповских стилях
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))#Заполняем в скобках, чтобы тема работала в бутрстраповских стилях
	copy = forms.BooleanField(required = False)

	
def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']
            
			recipients = ['tzvanguardia@gmail.com']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			if copy:
				recipients.append(sender)
			try:
				send_mail(subject, message, 'tzvanguardia@gmail.com', recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'workeu/thanks.html')
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
	return render(request, 'workeu/contactView.html', {'form': form})
	
def thanks(reguest): # Страница вывода сообщения об отправке сообщения
    thanks = 'thanks'
    return render(reguest, 'workeu/thanks.html', {'thanks': thanks})	
	
# ПРИБАЛТИКА
def postp_list_pribaltik(request): # Страница вывода постов по Таллинну
    postsp = Postp.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'workeu/postp_list_pribaltik.html', {'postsp': postsp})
	
	
def postp_detail_pribaltik(request, pk): # Страница вывода поста по Таллинну более детально
        post = get_object_or_404(Postp, pk=pk)
        return render(request, 'workeu/postp_detail_pribaltik.html', {'post': post})

# ФИНЛЯНДИЯ
def postf_list_finland(request): # Страница вывода постов по Финляндии
    postsf = Postf.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'workeu/postf_list_finland.html', {'postsf': postsf})
	
	
def postf_detail_finland(request, pk): # Страница вывода поста по Финляндии более детально
        post = get_object_or_404(Postf, pk=pk)
        return render(request, 'workeu/postf_detail_finland.html', {'post': post})	

def alljobs(request):
    postsp = Postp.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #Вывод списка вакансий в Таллине
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #Вывод списка вакансий в Польше
    postsf = Postf.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #Вывод списка вакансий в Финляндии
    return render(request, 'workeu/alljobs.html', {'posts': posts, 'postsp': postsp, 'postsf': postsf})		
	
def resume(reguest): # Страница вывода сообщения об отправке сообщения
    return render(reguest, 'workeu/resume.html')

def HelpInVisa(reguest): # Страница с визой
    return render(reguest, 'workeu/HelpInVisa.html')		