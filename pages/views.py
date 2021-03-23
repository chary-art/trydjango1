from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")

    my_content = {
        "my_text": 'this is my first text',
        "my_number": 123456,
    }
    return render(request, "base.html", my_content)


def first_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    my_content2 = {
        "my_text2": 'this is second text ',
        "my_number2": 234343
    }
    return render(request, "first.html", my_content2)


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})


def about_view(request, *args, **kwargs):
    my_content3 = {
        "my_text3": 'this is third text',
        "my_number3": 322,
        'my_list': [223, 4, 5, "ABC"],
        'my_html': '<h1>Hello oooo dfdfjn kdjfkd</h1>'

    }
    return render(request, "about.html", my_content3)


def home_view2(request, *args, **kwargs):
    return render(request, "home.html", {})
