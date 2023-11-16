from django import forms

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("thanks"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "signup/authenticate.html", {"form": form})


def thanks(request):
    return HttpResponse("thanks!")
