from django.views import View
from django_project.models import Stuff
from django.shortcuts import render

things = list(Stuff.objects.all())
l = []


class Home(View):
    def get(self, request):
        
        return render(request, 'index.html', {"stuff": things})


class item(View):
    def get(self, request, **kwargs):
        #extracting name url paramter from the url
        name = kwargs["name"]
        #retrieve objects from model
        item = list(Stuff.objects.filter(name=name).values())
        print(item)
        return render(request,"item.html", context = {"item":item[0]})
         
        
class new(View):
    def get(self, request):
        return render(request, "new.html")

    def post(self, request):
        
        name = request.POST["name"]
        message = {}
        
        #Save to DB
        #Error Handling 
        try:
            # Check for existing products with the same name
            products = list(Stuff.objects.filter(name=name).values())
            
            if len(products) > 0:
                message["type"] = "danger"
                message["message"] = "Item already exists!"
                raise Exception("Item already exists!")
            else:
                newItem = Stuff(
                    name=request.POST["name"],
                    manufacturer=request.POST["manufacturer"],
                    cost=request.POST["cost"],
                    weight=request.POST["weight"],
                    image=request.POST["image"]
                )
                newItem.save()
                message["type"] = "success"
                message["message"] = "Item saved!"
        except Exception as e:
            message["type"] = "danger"
            message["message"] = "Item saving failed!"
            print(e)

        return render(request, "new.html", {"message": message})
