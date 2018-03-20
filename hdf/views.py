from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'hdf/index.html')


def about(request):
    return render(request, 'hdf/about.html')


def services(request):
    return render(request, 'hdf/services.html')


def agents(request):
    return render(request, 'hdf/agents.html')


def for_sale(request):
    return render(request, 'hdf/forsale.html')


def for_rent(request):
    return render(request, 'hdf/forrent.html')


def pricing(request):
    return render(request, 'hdf/pricing.html')


def faqs(request):
    return render(request, 'hdf/faqs.html')


def idx_press(request):
    return render(request, 'hdf/idxpress.html')


def terms_of_use(request):
    return render(request, 'hdf/terms.html')


def privacy_policy(request):
    return render(request, 'hdf/privacy.html')
