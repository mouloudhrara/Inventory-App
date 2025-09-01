from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProductForm
from .models import Product

# CRUD = Create, Read, Update, Delete
# Home View
def home_view(request):
    return render(request, 'invApp/home.html')



# Create View 
def product_create_view(request):
    # intiantiate the form object
    form = ProductForm()
    if request.method== "POST":
        # pass to the form info coming from the 
        form = ProductForm(request.POST)
        # checking the form is valid
        if form.is_valid():
            # save it to the database
            form.save()
            # redirect the user to the products list view
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})

# Read View
# query all the products from the db and render the product list html template with the products
def product_list_view(request):
    #  selecting all the products in db
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html',{'products': products})

# Update View
# get the product using its product id 
def product_update_view(request, product_id):
    product = Product.objects.get(product_id= product_id)
    form = ProductForm()
    if request.method == 'POST':
        # by the form data from the request 
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form': form})

# Delete View
# target a certain product with its id and delete it 
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})