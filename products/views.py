from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """ A view to return all products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'all_deals' in request.GET:
            products = products.filter(
                Q(is_multipack=True) | Q(is_clearance=True))

        if 'clearance' in request.GET:
            products = products.filter(is_clearance=True)

        if 'multipack' in request.GET:
            products = products.filter(is_multipack=True)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You haven't entered any search details!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    template = 'products/products.html'
    context = {
        'products': products,
        'search': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


def product_item(request, product_id):
    """ A view to return one particular product item """

    product = get_object_or_404(Product, pk=product_id)

    template = 'products/product_item.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


@login_required
def add_products(request):
    # Allow admin to add products
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you do not have admin rights')
        return redirect(reverse('products'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'New product added!')
            return redirect(reverse('product_item', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product!')
    else:
        form = ProductForm()

    template = 'products/add_products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def update_products(request, product_id):
    # Allow admin to edit products
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you do not have admin rights')
        return redirect(reverse('products'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully Updated!')
            return redirect(reverse('product_item', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Currently editing {product.name}')

    template = 'products/update_products.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    # Allow admin to delete products
    product = get_object_or_404(Product, pk=product_id)
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you do not have admin rights')
        return redirect(reverse('products'))
    else:
        if request.method == 'POST':
            product = get_object_or_404(Product, pk=product_id)
            product.delete()
            messages.success(
                request, 'Product has been deleted from the database!')
            return redirect(reverse('products'))

    template = 'products/delete_product.html'
    context = {
        'product': product,
    }
    return render(request, template, context)
