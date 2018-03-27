from django.shortcuts import render
from .models import Contact


# Return to index.html on loading home page
def index(request):
    return render(request, "suveen/index.html", {"navbar": "profile"})


def contact(request):
    context = {"navbar": "contact"}
    if request.method == "POST":
        contact_me = Contact()
        contact_me.name = request.POST.get("name")
        contact_me.email = request.POST.get("email")
        contact_me.mobile = request.POST.get("mobile")
        contact_me.subject = request.POST.get("subject")
        contact_me.message = request.POST.get("message")
        contact_me.save()
        context['messageHeader'] = "Thank you! "
        context['message'] = "Thank you %s for reaching me. Your response is noted! I will get back to you ASAP!" % (contact_me.name)

    return render(request, "suveen/contact.html", context)
