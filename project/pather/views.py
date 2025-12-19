from django.shortcuts import render
from project.settings import INSTALLED_APPS
# Create your views here.


def handler(request):
    apps_all = [app for app in INSTALLED_APPS if "apps" in app]
    apps = list()
    for app in apps_all:
        ls = list(app.split("."))
        apps.append(ls[0])

    context = {
        "apps":apps
    }
    return render(request, "pather/index.html", context=context)