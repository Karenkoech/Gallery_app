from multiprocessing import context
from django.shortcuts import render,redirect
from .models import Image,Category,Location

# Create your views here.
def home(request):
    category = Category.objects.all()
    locations = Location.objects.all()
    images = Image.objects.all()
    context = {'category':category, 'locations':locations, 'images':images}
    return render(request, 'images/home.html',context)
   



def gallery(request):
    category =request.GET.get('category')
    if category == None:
        images=Image.objects.all()
    else:
        images = Image.objects.filter(category__category_name=category)

    categories = Category.objects.all()

    context = { 'categories': categories, 'images': images, }

    return render(request, 'images/gallery.html',context)

def viewPhoto(request,pk):
    
    image=Image.objects.get(id=pk)
    context = {  'image': image,}


    return render(request, 'images/images.html',context)

def addPhoto(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        data=request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category,created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        image=Image.objects.create(image=image,category=category)

        return redirect('gallery')

    context = {'categories':categories}
    return render(request, 'images/add-image.html',context)

def search_category(request):
    title = 'Search'
    categories = Category.objects.all()
    locations = Location.objects.all()
    if 'image_category' in request.GET and request.GET['image_category']:
        search_term = request.GET.get('image_category')
        found_results = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(search_term)
        print(found_results)

        return render(request, 'images/search.html',{'title':title,'images': found_results, 'message': message, 'categories': categories, "locations":locations})
    else:
        message = 'You havent searched yet'
        return render(request, 'images/search.html',{"message": message})

def search_location(request):
    location = request.GET.get('location')
    
    if request.method == 'POST':
        location=request.POST.get('location')
        
    
    return render(request, 'images/search.html',{'location':location},)
    

