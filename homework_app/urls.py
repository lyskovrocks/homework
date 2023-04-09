from homework_app.views import index, binary_sum, sentence_case, lower_case, upper_case, capitalize_each_word, \
    toggle_case, swap_words
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', index),
    path('binary_sum/', binary_sum),
    path('change_case/sentence_case', sentence_case),
    path('change_case/lower_case', lower_case),
    path('change_case/upper_case', upper_case),
    path('change_case/capitalize_each_word', capitalize_each_word),
    path('change_case/toggle_case', toggle_case),
    path('swap_words/', swap_words),
]
