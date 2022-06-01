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
    if request.method == 'POST':
        image_category = request.POST['image_category']
        images=Image.objects.filter(image_category__category_name__icontains=image_category)

        return render(request, 'images/search.html',{'image_category':image_category,'images':images})
    else:
        return render(request, 'images/search.html',{},)

def search_location(request):
    
    if request.method == 'POST':
        location_name=request.POST['location']
        images=Image.objects.filter(image_location__location_name__icontains=location_name)
        
    return render(request, 'images/search.html',{'location_name':location_name,'images':images})
    

