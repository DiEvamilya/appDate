from django.shortcuts import render, redirect
from .models import Profile
from .forms import Profileform
from django.shortcuts import render, get_object_or_404


def profile_list_view(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})


def create_profile_view(request,):
    if request.method == 'POST':
        form = Profileform(request.POST)
        if form.is_valid():
            profile = Profile.objects.create(
                login=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                age=form.cleaned_data['age'],
                hobbies=form.cleaned_data['hobbies'],
                favorite_music=form.cleaned_data['favorite_music'],
            )
            return redirect('profile_detail', profile.slug)
    else:
        form = Profileform()

    return render(request, 'create_profile.html', {'form': form})


def profile_detail_view(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {'profile': profile}

    # Отображаем шаблон с переданным контекстом
    return render(request, 'profile_detail.html', context)