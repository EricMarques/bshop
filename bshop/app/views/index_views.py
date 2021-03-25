from django.shortcuts import render


def show_index(request):
    return render(request, 'base.html')


def show_dashboard(request):
    return render(request, 'pages/dashboard/dashboard.html')
