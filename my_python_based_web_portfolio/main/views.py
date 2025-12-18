import os
import shutil
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WorkImageForm
from .models import WorkImage


def index(request):
    # Ensure profile image is available in media/profile/ib_p.jpg
    profile_dest_dir = settings.MEDIA_ROOT / 'profile'
    profile_dest_dir.mkdir(parents=True, exist_ok=True)
    src = settings.BASE_DIR / 'ib_p.jpg'
    dest = profile_dest_dir / 'ib_p.jpg'
    if src.exists() and not dest.exists():
        try:
            shutil.copy(src, dest)
        except Exception:
            pass

    if request.method == 'POST':
        form = WorkImageForm(request.POST, request.FILES)
        if form.is_valid() and form.cleaned_data['password'] == 'chopchopninja#123':
            work_image = form.save(commit=False)
            work_image.save()
            return redirect('index')
        elif form.is_valid() and form.cleaned_data['password'] != 'chopchopninja#123':
            form.add_error('password', 'Wrong password, try again.')
        upload_error = bool(form.errors)
    else:
        form = WorkImageForm()
        upload_error = False

    images = WorkImage.objects.order_by('-uploaded_at')

    return render(request, 'index.html', {
        'form': form,
        'images': images,
        'upload_error': upload_error,
    })


def delete_work(request, pk):
    if request.method == 'POST' and request.POST.get('password') == 'chopchopninja#123':
        img = get_object_or_404(WorkImage, pk=pk)
        img.delete()
        return redirect('index')
    return redirect('index')
