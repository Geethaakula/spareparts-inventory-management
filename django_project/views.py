from django.views import View
from django_project.models import Stuff
from django.shortcuts import render

things = list(Stuff.objects.all())
l = []


class Home(View):
    def get(self, request):
        return render(request, 'index.html', {"stuff": things})


class item(View):
    def get(self, request):
        return render(
            request,
            "item.html",
            {
                "name": request.GET["name"],
                "stuff": things
            },
        )


class new(View):
    def get(self, request):
        return render(request, "new.html")

    def post(self, request):
        message = "Succesful"
        temp = 1
        name = request.POST["name"]
        for i in l:
            if name == i:
                temp = 0
        if (temp == 0):
            message = "invalid Name Please Enter a Different Name"
        else:
            message = "Sucessful . Mission Accomplished!"
            l.append(name)
        return render(request, "new.html", {"message": message})
