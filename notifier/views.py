from django.shortcuts import render
from notifier.services import send_notifications


def dashboard(request):
    result = None

    if request.method == "POST":
        environment = request.POST.get("environment")
        result = send_notifications(environment)

    return render(request, "notifier/dashboard.html", {"result": result})