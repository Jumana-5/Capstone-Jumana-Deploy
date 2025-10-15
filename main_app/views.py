from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, CreateView
from .models import item, category, User
from .forms import itemForm
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')

def item_list(request):
    all_items = item.objects.all()
    return render(request,'items/all-items.html',{'all_items':all_items})

def category_list(request):
    all_categories = category.objects.all()
    return render(request,'categories/all-categories.html',{'all_categories':all_categories})

def item_list_categories(request):
    all_items_by_category = item.objects.filter(categories= category.category_id)
    return render(request,'categories/category-details.html',{'all_items_by_category':all_items_by_category})

# Only items I created
@login_required

def item_list_personal(request):
    my_items = item.objects.filter(creator=request.user)
    return render(request,'items/my-items.html',{'my_items':my_items})


@login_required
def item_details(request,id):
    found_item = item.objects.get(item_id = id)
    return render(request,'items/item-details.html',{'item':found_item})

#does not prevent editing other users items
@login_required
def my_item_details(request,id):
    #found_item = item.objects.get(creator=request.user)
    found_item = item.objects.get(item_id = id)
    #found_item = item.objects.filter(creator=request.user)
    return render(request,'items/my-item-details.html',{'item':found_item})

def category_details(request,id):
    found_category = category.objects.get(category_id = id)
    #found_item = item.objects.filter(categories= category.category_id)
    return render(request,'categories/category-details.html',{'category':found_category})


@login_required
def create_item(request):
    if request.method == 'POST':
      form = itemForm(request.POST)
      if form.is_valid(): 
          item = form.save(commit = False)
          item.creator = request.user
          item.save()
          form.save_m2m()
          return redirect(reverse('item_list'))
      else:
          return render(request,'items/item-form.html',{'form': form})
    elif request.method == 'GET':
        form = itemForm()
        return render(request,'items/item-form.html',{'form': form})
    

# Update

@login_required 
def update_item(request,id):
    item_changed = item.objects.get(pk = id)
#   if item_changed.creator == User.username:
    if request.method == 'POST':
        form = itemForm(request.POST, instance=item_changed)
        if form.is_valid():
            item_changed = form.save()
            return redirect(f'/items/{item_changed.item_id}')
        #    return redirect(reverse('item_details',id= item.item_id))
        else:
            return render(request, 'items/item-form.html',{'form':form})        
    elif request.method == 'GET':

        form = itemForm(instance=item_changed) #fills my form with the item that was fetched from the db
        return render(request, 'items/item-form.html',{'form':form})
#    else:
#        return redirect(f'/items/{item_changed.item_id}')
# Delete

@login_required 
def delete_item(request,id):
    item_changed = item.objects.get(pk = id)
    item_changed.delete()
    return redirect(reverse('item_list'))



class SignUpView(CreateView):
    model = User
    form_class= UserCreationForm
    success_url = '/auth/login'
    template_name = 'registration/sign-up.html'