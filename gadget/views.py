from django.shortcuts import render


def view_gadget(request):
    context = {}
    return render(request, 'gadget_view.html', context)
