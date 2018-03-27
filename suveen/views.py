from django.shortcuts import render


# Return to index.html on loading home page
def index(request):
    return render(request, "suveen/index.html", {});