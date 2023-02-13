from django.http import HttpRequest


def seo_attr(request:HttpRequest):

    return {
        'seo_title' : '',
        'seo_description': '',
        'keywords' : '',
    }



def twitter_seo_attr(request:HttpRequest):
    return {
        "tw_card" : '',
        "tw_site" : '',
        "tw_title" : '',
        "tw_description" : '',
        "tw_creator" : '',
        "tw_image" : '',
    }



def og_seo_attr(request:HttpRequest):

    return {
        "og_title" : '',
        "og_type" : '',
        "og_url" : '',
        "og_image" : '',
        "og_description" : '',
        "og_site_name" : '',
        "og_locale" : "pl_PL",
        "og_locale_alt" : "en_US"
    }