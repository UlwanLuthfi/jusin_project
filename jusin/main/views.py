from django.shortcuts import render


def home(request):
    return render(request, "main/home.html")


def about(request):
    return render(request, "main/about.html")


def gallery(request):
    return render(request, "main/gallery.html")


def order(request):
    if request.method == "POST":
        context = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "juice": request.POST.get("juice"),
            "notes": request.POST.get("notes"),
            "submitted": True,
        }
        return render(request, "main/order.html", context)

    return render(request, "main/order.html")
