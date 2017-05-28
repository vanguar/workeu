from django.contrib import admin
from .models import Post # Импортирование поста по Польше
from .models import Postp # Импортирование поста по Прибалтике
from .models import Postf # Импортирование поста по Финляндии

admin.site.register(Post) # Регистрация в админке постов по Польше
admin.site.register(Postp) # Регистрация в админке постов по Прибалтике
admin.site.register(Postf) # Регистрация в админке постов по Финляндии

