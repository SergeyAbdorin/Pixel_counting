import re
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ImageForm, ColorForm
from .models import ImageModel, PixelCount
from .utils import pixel_count_add


def index(request):
    """Index page for upload images"""
    form = ImageForm(request.POST or None, files=request.FILES or None)
    context = {
        "form": form
    }
    if not form.is_valid():
        return render(request, "index.html", context)
    image = form.save()
    pixel_count_add(image.id)
    return redirect('result', image_id=image.id)


def result(request, image_id):
    """image processing result and check with custom color"""
    image = get_object_or_404(
        ImageModel,
        id=image_id
        )
    pixel = get_object_or_404(
            PixelCount,
            image_id=image_id
        )
    context = {
            "compare": pixel.black_or_white,
            "image": image
        }
    if 'button' in request.GET:
        form = ColorForm(request.GET)
        context["form"] = form
        if form.is_valid():
            color = form.cleaned_data['hex_color']
            colors = pixel.hex_colors.keys()
            context["color"] = color.lower()
            context["count"] = 0
            if color.lower() in colors:
                context["count"] = pixel.hex_colors[color]
            return render(request, "result.html", context)
        return render(request, "result.html", context)
    form = ColorForm()
    context["form"] = form
    return render(request, "result.html", context)


def server_error(request):
    return render(request, "misc/500.html", status=500)


def page_not_found(request, exception):
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )
