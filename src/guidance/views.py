from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from django.db.models import Q
from . models import (
    Payment, MyAccounts,
    Purchasing, ProfilePlan,
    Support, More
)


def is_valid_queryparam(param):
    return param != '' and param is not None


def help_list(request):

    payments = Payment.objects.all()
    myaccounts = MyAccounts.objects.all()
    purchasing = Purchasing.objects.all()
    profileplan = ProfilePlan.objects.all()
    support = Support.objects.all()
    more = More.objects.all()
    return render(request, 'core/page-help-center.html', {
        'seo_title' : 'Support | Novavideocall',
        'seo_description' : '',
        'og_description' : 'Novavideocall Support provides a dynamic platform for real-time technical support',
        "og_title" : 'Support | Novavideocall', 
        'og_url': 'https://novavideocall.live/help-center/',
        'og_type' : 'website',
        "og_image" : 'https://novavideocall.live/static/vidicu.png',
        "og_site_name" : 'Novavideocall',
        'tw_card' : 'summary',
        'tw_site' : '@novaviddeocall',
        'tw_title' : 'Support | Novavideocall',
        'tw_description' : 'Novavideocall Support provides a dynamic platform for real-time technical support',
        'tw_creator' : '@novaviddeocall',
        'tw_image' : 'https://novavideocall.live/static/vidicu.png',
        'payments' : payments,
        'myaccounts' : myaccounts,
        'purchasing' : purchasing,
        'profileplan' : profileplan,
        'support' : support,
        'more' : more,
    })


def help_detail(request, classname, post): 
    MODEL_MAPPING = {
        "payment": Payment,
        "myaccounts": MyAccounts,
        "purchasing": Purchasing,
        "profileplan": ProfilePlan,
        "support" :  Support,
        "more" : More

    }
    user_input =  classname
    ModelClass = MODEL_MAPPING.get(user_input)
    object_list =  ModelClass.objects.exclude(slug=post)
    post = get_object_or_404(
        ModelClass,
        slug = post
    )

    
    
    return render(request, 'core/page-help-center-article.html', {
        'seo_title' : '',
        'seo_description' : '',
        'og_description' : '',
        "og_title" : '', 
        'og_url': 'https://vidicu.live/pricing/',
        'og_type' : 'website',
        "og_image" : '',
        "og_site_name" : '',
        'tw_card' : '',
        'tw_site' : '',
        'tw_title' : '',
        'tw_description' : '',
        'tw_creator' : '',
        'tw_image' : '',
        'post': post,
        'objects': object_list,
    })