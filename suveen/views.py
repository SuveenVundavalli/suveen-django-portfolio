from .models import Contact

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import get_template


# Return to index.html on loading home page
def index(request):
    return render(request, "newDesign.html", {})

# def index(request):
#     context = {"navbar": "profile"}
#     return render(request, "suveen/index.html", context)


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
        context['messageHeader'] = "Thank you!"
        context['message'] = "Thank you %s for reaching me. Your response is noted! I will get back to you ASAP!" % (
            contact_me.name)
        mail_context = {'name': contact_me.name, 'email': contact_me.email, 'mobile': contact_me.mobile,
                        'subject': contact_me.subject, 'message': contact_me.message, 'site_url': settings.SITE_URL,
                        'contact_id': contact_me.pk}
        subject = "New entry in Contact me from @ suveen.me"
        mail_text = get_template("mail/contact.txt")
        mail_html = get_template("mail/contact.html")
        send_email(mail_context, mail_html, mail_text, subject)

    return render(request, "suveen/contact.html", context)


def send_email(mail_context, mail_html, mail_text, subject):
    subject = subject
    from_email = "contact@suveen.me"
    to = "suveenkumar.vundavalli@gmail.com"
    text_content = mail_text.render(mail_context)
    html_content = mail_html.render(mail_context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)


def mark_contact_read(request, pk):
    context = {"navbar": "profile"}
    contact = Contact.objects.get(pk=pk)
    contact.read = True
    contact.save()
    context['messageHeader'] = "Message marked read!"
    context['message'] = "You marked %s as read" % contact
    return render(request, "suveen/index.html", context)


def experience(request):
    context = {"navbar": "experience"}
    return render(request, "suveen/experience.html", context)


def education(request):
    context = {"navbar": "education"}
    return render(request, "suveen/education.html", context)


def skills(request):
    context = {"navbar": "skills"}
    return render(request, "suveen/skills.html", context)


def training(request):
    context = {"navbar": "training"}
    return render(request, "suveen/training.html", context)


def internships(request):
    context = {"navbar": "internships"}
    return render(request, "suveen/internships.html", context)


def voluntary(request):
    context = {"navbar": "voluntary"}
    return render(request, "suveen/voluntary.html", context)


def academic(request):
    context = {"navbar": "academic"}
    return render(request, "suveen/academic.html", context)


def publications(request):
    context = {"navbar": "publications"}
    return render(request, "suveen/publications.html", context)


def github(request):
    return redirect("https://github.com/suveenkumarchowdary")


def linkedin(request):
    return redirect("https://www.linkedin.com/in/svundavalli/")
