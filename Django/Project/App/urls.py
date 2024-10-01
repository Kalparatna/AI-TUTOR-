# App/urls.py
from django.urls import path
from .views import index, modules
from . import views

urlpatterns = [
    path('', index, name='index'),  # Main page
    path('modules/<str:topic>/', modules, name='modules'),  # Updated Modules page with topic as a parameter




    path('get_gemini_response/', views.character_selection, name='get_gemini_response'),  # This will show the character selection
    path('chat/<str:character>/', views.chat_with_tutor, name='chat_with_tutor'),  # Chat with selected tutor


]