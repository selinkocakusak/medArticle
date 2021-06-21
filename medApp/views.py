
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import UserForm
from .models import content, tagMdl
from django.urls import reverse
import requests
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "medApp/index.html")


@ login_required
def search_results(request):
    if request.method == 'POST':
        term = request.POST.get('term')
        author = request.POST.get('author')
        year = request.POST.get('year')
        keyword = request.POST.get('keywords')
        abstrt = request.POST.get('abstract')
        articles = content.objects.filter(
            title__icontains=term, authors__icontains=author, date__icontains=year, keywords__icontains=keyword, abstract__icontains=abstrt).values(
                'title', 'authors', 'date', 'keywords', 'doc_id', 'no').order_by('no')

        # paginator = Paginator(context, 10)
        # page_num = request.GET.get('page', 10)
        # context = paginator(page_num)
        # page = paginator.get_page(page_num)
        items = {
            # 'count': paginator.count,
            'term': term,
            'articles': articles
        }
        # page_num = request.POST.get('page', 10)
        # context = paginator(page_num)
        return render(request, 'medApp/search_results.html', items)
        # return render(request, 'medApp/search_results.html', {'term': term, 'context': context})
    else:
        return render(request, 'medApp/search_results.html', {})


@ login_required
@csrf_exempt
def get_wikidata(request):
    url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=en&type=item&continue=0&search="
    query = request.GET['query']
    data = requests.get(url+query)
    data = data.json()['search']
    descriptions = []
    for entity in data:
        description = entity['description']
        descriptions.append(description)
    return JsonResponse({"descriptions": descriptions})


@ login_required
def tag(request):
    if request.method == 'POST':
        tagged = request.POST.get('tag')
        autocomplete = request.POST['query']
        try:
            docid = request.POST.get('idlabel')
            description = request.POST['chosen']
            url = "https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=en&type=item&continue=0&search=" + \
                autocomplete
            data = requests.get(url)
            data = data.json()['search']
            for item in data:
                if description == item.get('description'):
                    link = item.get('concepturi')
                    if tagMdl.objects.filter(docId=docid, tag=tagged, link=link).exists():
                        failure = "The tag and link you are trying to save already exist!."
                        return render(request, 'medApp/tag.html', {'failure': failure})
                    else:
                        db = tagMdl(docId=docid,
                                    tag=tagged, link=link)
                        db.save()
                        success = "The tag successfully stored!."
                        tagDB = tagMdl.objects.filter(
                            docId=docid).values('tag', 'link', 'docId')
                        return render(request, 'medApp/tag.html', {'success': success, 'tagDB': tagDB})
        except:
            value = "The tag you are trying to save does not exist."
            return render(request, 'medApp/tag.html', {'value': value})
    else:
        return render(request, 'medApp/tag.html')


@ login_required
def article(request, doc_id):
    article = content.objects.filter(doc_id__exact=doc_id).values(
        'title', 'authors', 'date', 'keywords', 'doc_id', 'no', 'abstract')
    docid = tagMdl.objects.filter(
        docId=doc_id).values('docId', 'tag', 'link')
    return render(request, 'medApp/article.html', {'article': article, 'docid': docid})


@ login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('medApp:home'))


def register(request):
    registered = False
    if request.method == 'POST':
        # Get info from the form
        user_form = UserForm(data=request.POST)
        # Check if form is valid
        if user_form.is_valid():
            # Save User Form to Database
            user = user_form.save()
            # Hash the password
            user.set_password(user.password)
            # Store with Hashed password
            user.save()
            # Registration success
            registered = True
        else:
            # Form is invalid
            print(user_form.errors)
    else:
        # is not an HTTP post so give forms as blank
        user_form = UserForm()
    return render(request, 'medApp/registration.html',
                  {'user_form': user_form,
                           'registered': registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
        # If we have a user
        if user:
            # Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # redirect the user back to some page.
                return HttpResponseRedirect(reverse('medApp:home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        # If nothing is provided for username or password.
        return render(request, 'medApp/login.html', {})


def search(request):
    return render(request, 'medApp/search.html', {})
