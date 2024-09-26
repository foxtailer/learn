from django.shortcuts import render


def main(request):
    context = {'goods': True}
    return render(request, 'base.html', context=context)


def news(request):
    return render(request, 'main/news.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def social_plug(request):
    return render(request, 'social_plug.html')
