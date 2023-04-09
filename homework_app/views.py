from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    per = 100
    return render(request, 'index.html', {'name': per})

def binary_sum(request):
    request_data_dict = dict(request.GET.items())
    print(request_data_dict)
    first = int(request_data_dict['first'])
    twice = int(request_data_dict['twice'])

    result = 0
    for i in range(first, twice + 1):
        if i % 2 == 0:
            result += i
    return render(request, 'binary_sum.html', {'result': result})

def sentence_case(request):
    if request.method == 'POST':
        request_data_dict = dict(request.POST.items())
        result = request_data_dict['input_string'].capitalize()
    else:
        result = '-'
    print(result)
    return render(request, 'change_case.html', {'result': result})

def lower_case(request):
    if request.method == 'POST':
        request_data_dict = dict(request.POST.items())
        result = request_data_dict['input_string'].lower()
    else:
        result = '-'
    print(result)
    return render(request, 'change_case.html', {'result': result})

def upper_case(request):
    if request.method == 'POST':
        request_data_dict = dict(request.POST.items())
        result = request_data_dict['input_string'].upper()
    else:
        result = '-'
    print(result)
    return render(request, 'change_case.html', {'result': result})

def capitalize_each_word(request):
    if request.method == 'POST':
        request_data_dict = dict(request.POST.items())
        result = request_data_dict['input_string'].title()
    else:
        result = '-'
    print(result)
    return render(request, 'change_case.html', {'result': result})

def toggle_case(request):
    if request.method == 'POST':
        request_data_dict = dict(request.POST.items())
        result = request_data_dict['input_string'].swapcase()
    else:
        result = '-'
    print(result)
    return render(request, 'change_case.html', {'result': result})

def swap_words(request):
    if request.method == 'POST':
        request_data_dict = dict(request.POST.items())
        result = request_data_dict['input_string'].replace(request_data_dict['find_word'], request_data_dict['replace_to'])
        print(request_data_dict)
    else:
        result = '-'
    print(result)
    return render(request, 'swap_words.html', {'result': result})