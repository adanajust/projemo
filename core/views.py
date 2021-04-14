from django.shortcuts import render, get_object_or_404
from .models import Item, OrderItem, Order, Writer
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from templates.forms import OrderForm, CreateUserForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from . models import Item
from templates.forms import OrderForm, CreateUserForm

def item_list(request):
    context={
        'items': Item.objects.all()
    }
    return render(request, "order-page.html", context)

def check_out(request):
    return render(request, "checkout-page.html", {})

class Homeview(ListView):
    model=Item
    template_name = "home-page.html"

class ItemDetailView(DetailView):
    model = Item
    template_name = "order-page.html"

def add_to_inprogress(request, slug):
    item=get_object_or_404(Item, slug=slug)
    order_item=OrderItem.objects.create(item=item)
    order_qs=Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs(0)
def LoginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login/dashboard/')


    #form=CreateUserForm()
    context={}
    return render(request, 'Accounts/login.html', context)
def RegisterPage(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'Accounts/register.html', context)


@login_required(login_url='login')
def dashboard(request):

	orders = Order.objects.all()
	writers = Writer.objects.all()

	#total_customers = Writer.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()



	context = {'orders':orders, 'writers':writers,'total_orders':total_orders,'delivered':delivered,'pending':pending }


	return render(request, 'Accounts/dashboard.html', context)


def writer(request, pk_test):
	writer = Writer.objects.get(id=pk_test)

	orders = writer.order_set.all()
	order_count = orders.count()

	#myFilter = OrderFilter(request.GET, queryset=orders)
	#orders = myFilter.qs

	context = {'customer':writer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/customer.html',context)



@login_required(login_url='login')
def home(request):
	orders = Order.objects.all()
	customers = writer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'Accounts/dashboard.html', context)






