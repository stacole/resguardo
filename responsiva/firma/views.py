from django.shortcuts import render
from .forms import SignatureForm
from jsignature.utils import draw_signature

# Create your views here.
def home(request):
    form = SignatureForm(request.POST or None)
    if form.is_valid():
        signature = form.cleaned_data.get('signature')
        if signature:
            # as an image
            signature_picture = draw_signature(signature)
            # or as a file
            signature_file_path = draw_signature(signature, as_file=True)
    else:
        form = SignatureForm()
    context = {
        'form': form,
    }
    return render(request, "responsiva/home.html", context)

def responsivas(request):
    return render(request, "responsiva/responsivas.html")