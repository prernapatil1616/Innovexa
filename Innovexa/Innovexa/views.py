from django.shortcuts import redirect, render
from app.models import Categories, Level,Challenge,SubmitForm
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib import messages



def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    challenge = Challenge.objects.filter().order_by('-id')

    context = {
        'category': category,
        'challenge': challenge,
    }
    return render(request, 'main/home.html', context)


def SINGLE_CHALLENGE(request):
    category = Categories.objects.all().order_by('id')
    challenge = Challenge.objects.filter().order_by('-id')

    level = Level.objects.all()
    context = {
        'category': category,
        'level': level,
        'challenge': challenge,
    }

    return render(request, 'main/single_challenge.html', context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    level = request.GET.getlist('level[]')

    if categories == ['BEGINNER']:
        challenge = Challenge.objects.filter(category__id__in=categories).order_by('-id')
    elif level:
        challenge = Challenge.objects.filter(level__id__in=level).order_by('-id')
    else:
        challenge = Challenge.objects.all().order_by('-id')

    t = render_to_string('ajax/challenge.html', {'challenge': challenge})
    return JsonResponse({'data': t})


def CONTACT_US(request):
    category = Categories.get_all_category(Categories)
    context = {
        'category': category,
    }
    return render(request, 'main/contact_us.html', context)


def ABOUT_US(request):
    return render(request, 'main/about_us.html')


def CHALLENGE_DETAILS(request, slug):
    challenge = Challenge.objects.filter(slug=slug)
    if challenge.exists():
        challenge = challenge.first()
    else:
        return redirect('404')

    context = {
        'challenge': challenge,

    }

    return render(request, 'challenge/challenge_details.html', context)


def PAGE_NOT_FOUND(request):
    return render(request, 'error/404.html')


def MY_CHALLENGES(request):
    challenge = Challenge.objects.filter(user = request.user)
    return render(request, 'challenge/my-challenges.html')


def CHALLENGE_START(request):
    challenge = Challenge.objects.filter()
    if challenge.exists():
        challenge = challenge.first()
    else:
        return redirect('404')

    context = {
        'challenge': challenge,
    }

    return render(request, 'challenge/start_challenge.html', context)

def CHALLENGE_SUBMIT(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        repoUrl = request.POST.get('repoUrl')
        liveUrl = request.POST.get('liveUrl')
        feedback = request.POST.get('feedback')

        data = SubmitForm(
            title=title,
            repoUrl=repoUrl,
            liveUrl=liveUrl,
            feedback=feedback
        )
        data.save()
        messages.success(request, 'Challenge is successfully added!')

        return redirect('submit')

    return render(request, 'challenge/submit.html')


def RESOURCES(request):
    return render(request, 'challenge/resources.html')


