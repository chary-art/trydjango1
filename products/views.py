from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, ProductFormSecond, RawProductForm
from .models import Product


# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     # print(request.GET)     #http://127.0.0.1:8000/create/?title=men%20barder shuny yazmaly backend da hem gorunyar
#     # print(request.POST)
#     # if request.method == "POST":
#     if request.method == "POST":
#         my_new_title = request.POST.get('name')     #<input type="text" name="title" placeholder="your search"/> name deng bolmaly
#
#         print(my_new_title)
#     # Product .objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)  # post edyar
    if form.is_valid():
        form.save()  # sohranit edyar
        form = ProductForm()  # sahypany obnovit edyar

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


def product_experiment_view(request):
    form = ProductFormSecond(request.POST or None)  # post edyar
    if form.is_valid():
        form.save()  # sohranit edyar
        form = ProductFormSecond()  # sahypany obnovit edyar

    context = {
        'form': form
    }

    return render(request, "products/product_experiment.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=19)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'salgysy': obj.salgysy,
    #     'surat': obj.surat,
    #     'maglumat': obj.maglumat,
    #     'city': obj.city,
    #     'etraby': obj.etraby,
    #
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

    # shu yerde baza dannyda yazylan zatlary iputda gorkezyar....


# shung usti bilen admin paneldakyny uytgedip bolyar browsering yuzunden (inpudyng usti bilen)
def render_initial_data(request):
    initial_data = {'title': "My this awesome title"}  # bu yerde yazan zadyng browserda inputda yazylgy duryar..
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, "products/product_create.html", context)


# shu yuzune chykaryar browsering
def dynamic_lookup_view(request, id):        #ine id goysang hem bolyar yone urls dada yazmaly id diyip
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:            # does not exist diyip chykarmaly yone chykarmady browserda
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


                     #View of a List of Database Objects
def product_list_view(request):
    queryset = Product.objects.all()        #list of objects
    context = {
        'object_list': queryset

    }
    return render(request, 'products/product_list.html', context)


