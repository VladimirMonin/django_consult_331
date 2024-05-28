from django.shortcuts import render
# Импортируем TemplateView
# На основе ее создаем простую вьюшку для главной страницы шаблон main.html

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'main.html'

    
