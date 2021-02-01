from django.shortcuts import render


def app_base_home(request):
    context = dict(path=request.path, user_agent=request.META['HTTP_USER_AGENT'])
    return render(request=request, template_name='app_base/home.html', context=context)
