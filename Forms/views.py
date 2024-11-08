from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from .forms import Contactform2
from .forms import contactForm3
from .forms import ContactForm

# Create your views here.
def controlerform1(request):
    if request.method == 'POST':
        f = request.POST['firstname']  # 'firstname' is the name attribute in the HTML page
        l = request.POST['lastname']
        e = request.POST['email']
        m = request.POST['message']
        
        # Create and save the Contact object
        contact = Contact.objects.create(firstname=f, lastname=l, Email=e, msg=m)
        contact.save()
        
        return HttpResponse('<h2> Data has been submitted </h2>')
    
    return render(request, "myform1.html")

def controleform2(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = Contactform2(request.POST)  # Nous reprenons les données

        if form.is_valid():  # Nous vérifions que les données envoyées sont valides
            # Ici nous pouvons traiter les données du formulaire
            f = form.cleaned_data['firstname']
            l = form.cleaned_data['lastname']
            e = form.cleaned_data['Email']
            m = form.cleaned_data['msg']

            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
            contact = Contact.objects.create(firstname=f, lastname=l, Email=e, msg=m)
            return HttpResponse('<h2> Data has been submitted </h2>')

    else:  # Si ce n'est pas du POST, c'est probablement une requête GET
        form = Contactform2()  # Nous créons un formulaire vide

    return render(request, 'myform2.html', {'mycontactform2': form})

def controleform3(request):
    if request.method == 'POST':
        form = ContactForm3(request.POST)
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the form data to the database
            return HttpResponse('<h2>Data has been submitted</h2>')  # Success message
    else:
        form = contactForm3()  # Create an empty form
    return render(request, "myform3.html", {'mycontactform3': form})  # Render the form

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email_list = []
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            to_email = form.cleaned_data['to_email']
            email_list.append(to_email)

            try:
                send_mail(subject, message, from_email, email_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "mail.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')