import os
from . forms import SubscribeForm
from django.db.models import F
from django.http import JsonResponse
from publishapp.models import Posts
from django.shortcuts import(render, redirect, get_object_or_404) 
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.urls import reverse
from django.conf import settings
from contactus.forms import ContactUsForm
from testimonials.models import (CustomerStories, BlockQuote)
from .models import (
    NadiaClients, 
    LizzyClients,
    ZaaloloClients,
    KingpindrakoClients, 
    DownloadPageArticle, 
    Application, 
    PrivacyPolicy, 
    TermsOfUse
)
from contactus.models import (PreVisitInquires, SalesQuestions, BillingQuestions, OfficeAddressDetail)
from about.models import ( FirstSection, SecSection, FourthSection, FifthSection, AboutUsIcons)
from pricing.models import (
    PricingComparePlan,
    PricingFAQ,
    PricingHeading,
    ProfessionalPlan,
    TeamsPlan,
    HighLightSection
)
from homepage.models import (
    FifthColumn, SecondColumn,
    ThirdColumn, FourthColumn,
    SixthColumn
)
from careers.models import (
    FirstRow, SecondRow,
    ThirdRow, FourthRow,
    FifthRow, SixthRow
)


def index(request):
    object_list = Posts.published.all()[0:3]    
    second_column = SecondColumn.objects.all()[0]
    third_column = ThirdColumn.objects.all()[0]
    fourth_column = FourthColumn.objects.all()[0]
    fifth_column = FifthColumn.objects.all()[0]
    sixth_column = SixthColumn.objects.all()[0]

    return render(request, 'core/index.html', {
    
        'seo_title' : 'Novavideocall | AI Powered Video Conferencing, Video Calls, Online Meetings',
        'seo_description' : 'Novavideocall is a cloud-based video conferencing platform that offers a range of AI-powered features to make virtual meetings more efficient and engaging. With Vidicu, you can host high-quality video and audio meetings, share screens, and collaborate with team members in real-time',
        'og_description' : 'Novavideocall is a cloud-based video conferencing platform that offers a range of AI-powered features to make virtual meetings more efficient and engaging. With Vidicu, you can host high-quality video and audio meetings, share screens, and collaborate with team members in real-time',
        "og_title" : 'Novavideocall | AI Powered Video Conferencing, Video Calls, Online Meetings', 
        'og_url': 'https://novavideocall.live/',
        'og_type' : 'website',
        "og_image" : 'https://novavideocall.live/static/vidicu.png',
        "og_site_name" : 'Novavideocall',
        'tw_card' : 'summary',
        'tw_site' : '@novaviddeocall',
        'tw_title' : 'Novavideocall | AI Powered Video Conferencing, Video Calls, Online Meetings',
        'tw_description' : 'Novavideocall is a cloud-based video conferencing platform that offers a range of AI-powered features to make virtual meetings more efficient and engaging. With Vidicu, you can host high-quality video and audio meetings, share screens, and collaborate with team members in real-time',
        'tw_image' : 'https://novavideocall.live/static/vidicu.png',
        'posts' : object_list,
        'second_column' : second_column,
        'third_column' : third_column,
        'fourth_column' : fourth_column,
        'fifth_column' : fifth_column,
        'sixth_column' : sixth_column
    })



def about_us(request):
    aboutus_icons = AboutUsIcons.objects.all()[0]
    first_section = FirstSection.objects.all()[0]
    second_section = SecSection.objects.all()[0]
    fourth_section = FourthSection.objects.all()[0]
    fifth_section = FifthSection.objects.all()[0]


    return render(request, 'core/about_us.html', {  
        'seo_title' : 'About Us | Novavideocall',
        'seo_description' : "Novavideocall is an AI-powered video conferencing platform based in Poland. Our platform is designed to provide seamless video calls and online meetings for individuals and businesses alike. Our mission is to bring people closer together, no matter where they are in the world, and enable them to connect and collaborate with ease. we use AI technology to ensure that your video calls are crystal clear and easy to use. Vidicu includes real-time language translation to help bridge the language barrier and make it easy for people to communicate, no matter what language they speak.",
        'og_description' : "Novavideocall is an AI-powered video conferencing platform based in Poland. Our platform is designed to provide seamless video calls and online meetings for individuals and businesses alike. Our mission is to bring people closer together, no matter where they are in the world, and enable them to connect and collaborate with ease. we use AI technology to ensure that your video calls are crystal clear and easy to use. Vidicu includes real-time language translation to help bridge the language barrier and make it easy for people to communicate, no matter what language they speak.",
        "og_title" : 'About Us | Novavideocall', 
        'og_url': 'https://novavideocall.live/about-us/',
        'og_type' : 'website',
        "og_image" : 'https://novavideocall.live/static/vidicu.png',
        "og_site_name" : 'Novavideocall',
        'tw_card' : 'summary',
        'tw_site' : '@novaviddeocall',
        'tw_title' : 'About Us | Novavideocall',
        'tw_description' : "Novavideocall is an AI-powered video conferencing platform based in Poland. Our platform is designed to provide seamless video calls and online meetings for individuals and businesses alike. Our mission is to bring people closer together, no matter where they are in the world, and enable them to connect and collaborate with ease. we use AI technology to ensure that your video calls are crystal clear and easy to use. Vidicu includes real-time language translation to help bridge the language barrier and make it easy for people to communicate, no matter what language they speak.",
        'tw_image' : 'https://novavideocall.live/static/vidicu.png',
        'aboutus_icons' :  aboutus_icons,
        'first_section' : first_section, 
        'second_section' : second_section,
        'fourth_section' : fourth_section,
        'fifth_section' : fifth_section
    })


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def contact_us(request):
    previsitinquires = PreVisitInquires.objects.all()[0]
    salesquestions = SalesQuestions.objects.all()[0]
    billling_question = BillingQuestions.objects.all()[0]
    office_address = OfficeAddressDetail.objects.all()[0]
    contactus_form = ContactUsForm()

    if request.method == "POST" and is_ajax(request=request):
        contactus_form = ContactUsForm(request.POST)
        if contactus_form.is_valid():
            name = contactus_form.cleaned_data['first_name']
            contactus_form.save()
            return JsonResponse({"name": name}, status=200)

        else:
            errors = contactus_form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


    return render(request, 'core/contact_us.html', {
        'seo_title' : 'Contact Us | Novavideocall',
        'seo_description' : 'Find answers to your questions and how to contact our support team on novavideocall or send us your feedback by contacting us through our various channels.',
        'og_description' : 'Find answers to your questions and how to contact our support team on novavideocall or send us your feedback by contacting us through our various channels.',
        'og_title' : 'Contact Us | Novavideocall', 
        'og_url': 'https://novavideocall.live/contact-us/',
        'og_type' : 'website',
        'og_image' : 'https://novavideocall.live/static/vidicu.png',
        'og_site_name' : 'novavideocall',
        'tw_card' : 'summary',
        'tw_site' : '@novaviddeocall',
        'tw_title' : 'Contact Us | Novavideocall',
        'tw_description' : 'Find answers to your questions and how to contact our support team on novavideocall or send us your feedback by contacting us through our various channels.',
        'tw_image' : 'https://novavideocall.live/static/vidicu.png',
        'previsitinquires' : previsitinquires,
        'salesquestions' :  salesquestions,
        'office_address' : office_address,
        'billing_question' : billling_question,
        'contactform'   : contactus_form
    })


def subscribe(request):
    if request.method == "POST" and is_ajax(request=request):
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            email = subscribe_form.cleaned_data['email']
            subscribe_form.save()
            return JsonResponse({"email": email}, status=200)

        else:
            errors = subscribe_form.errors.as_json()
            return JsonResponse({'errors' : errors}, status=400)

    else:
        return JsonResponse({'errors' : 'Not Found'}, status=404)




def pricing(request):
    pricing_compare_plan = PricingComparePlan.objects.all()
    pricingfaq = PricingFAQ.objects.all()[0]
    pricingheading = PricingHeading.objects.all()[0]
    professionalplan = ProfessionalPlan.objects.all()[0]
    teamsplan = TeamsPlan.objects.all()[0]
    highlightsection = HighLightSection.objects.all()[0]
    
    return render(request, 'core/page-pricing.html', {
        'seo_title' : 'Pricing & Plans | Novavideocall',
        'seo_description' : "Check novavideocall flexible plans and pricing, Novavideocall offers pricing plans tailored to your unique needs, Try Novavideocall for free or explore our Professional and Teams Ready plans to see which one is right for you.",
        'og_description' :  "Check novavideocall flexible plans and pricing, Novavideocall offers pricing plans tailored to your unique needs, Try Novavideocall for free or explore our Professional and Teams Ready plans to see which one is right for you.",
        "og_title" : 'Pricing & Plans | Novavideocall', 
        'og_url': 'https://novavideocall.live/pricing/',
        'og_type' : 'website',
        "og_image" : 'https://novavideocall.live/static/vidicu.png',
        "og_site_name" : 'novavideocall',
        'tw_card' : 'summary',
        'tw_site' : '@novavideocall',
        'tw_title' : 'Pricing & Plans | Novavideocall',
        'tw_image' : 'https://novavideocall.live/static/vidicu.png',
        'tw_description' : "Check novavideocall flexible plans and pricing, Novavideocall offers pricing plans tailored to your unique needs, Try novavideocall for free or explore our Professional and Teams Ready plans to see which one is right for you.",
        'pricing_compare_plan' : pricing_compare_plan,
        'pricingfaq' : pricingfaq, 
        'pricingheading' : pricingheading,
        'professionalplan' : professionalplan,
        'teamsplan' : teamsplan,
        'highlightsection' : highlightsection
    })


def terms_of_use(request):
    terms_of_use = TermsOfUse.objects.all()[0]
    return render(request, 'core/page-terms.html', { 
        'terms_of_use' : terms_of_use
    })


def privacy_policy(request):
    privacy_policy = PrivacyPolicy.objects.all()[0]
    return render(request, 'core/page-privacy.html', {
        'privacy_policy' : privacy_policy
    })


def download_app(request):

    download_article = DownloadPageArticle.objects.all()[0]
    download_token = request.session.get('download_token') or None 
        
    return render(request, 'core/download_app.html', {
        'code': download_token,
        'seo_title' : 'Download Novavideocall App | Novavideocall',
        'seo_description' : 'Download Novavideocall for Windows and Linux, And Find out why users trust novavideocall as their collaboration solution.',
        'og_description' : 'Download Novavideocall for Windows and Linux, And Find out why users trust novavideocall as their collaboration solution.',
        "og_title" : 'Download Novavideocall App | Novavideocall', 
        'og_url': "https://novavideocall.live/download",
        'og_type' : 'website',
        "og_image" : 'https://novavideocall.live/static/vidicu.png',
        "og_site_name" : 'novavideocall',
        'tw_card' : 'summary',
        'tw_site' : '@novavideocall',
        'tw_title' : 'Download the novavideocall desktop app | Novavideocall',
        'tw_description' : 'Download Vidicu for Windows and Linux, And Find out why users trust Novavideocall as their collaboration solution.',
        'tw_image' : 'https://novavideocall.live/static/vidicu.png',
        'download_article' : download_article
    })


def installer(request, platform):
    response = None 
    app = Application.objects.all()[0]

    if platform == "windows":
        filepath = app.windows_exe_file.path
        response = modify_download_headers(filepath, "setup.exe") 

    if platform == "linux":
        filepath = app.linux_exe_file.path
        response = modify_download_headers(filepath, "setup") 


    return response


def download_installer(request, code, platform):
    response = None
    user_token_obj = None
    download_token = request.session.get('download_token') or None
    app = Application.objects.all()[0]
    
    try:
        user_token_obj = NadiaClients.objects.get(id_token=download_token)
       
    except NadiaClients.DoesNotExist:
        pass

    try:
        user_token_obj = LizzyClients.objects.get(id_token=download_token)
        
    except LizzyClients.DoesNotExist:
        pass

    try:
        user_token_obj = ZaaloloClients.objects.get(id_token=download_token)
        
    except ZaaloloClients.DoesNotExist:
        pass
    
    try:
        user_token_obj = KingpindrakoClients.objects.get(id_token=download_token)
        
    except KingpindrakoClients.DoesNotExist:
        pass
 

    if platform == "linux":
        filepath = app.linux_exe_file.path
        response = modify_download_headers(filepath, "setup") 


    if platform == "windows":
        filepath = app.windows_exe_file.path
        response = modify_download_headers(filepath, "setup.exe")

    if download_token:
        user_token_obj.__class__.objects.select_for_update().filter(id_token=user_token_obj.id_token).update(app_downloaded=True)
        
    return response



def modify_download_headers(filepath, download_file_name):
    filename = download_file_name
    path = open(filepath, 'rb')

    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type='application/force-download')
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % smart_str(filename)
    response['Content-Length'] = os.path.getsize(filepath)
    response['X-Sendfile'] = smart_str(filepath)
    # Return the response value
    return response


def coming_soon(request):
    
    return render(request, 'core/page-coming-soon-simple.html', {
        'seo_title' : '',
        'seo_description' : '',
        'og_description' : '',
        "og_title" : '', 
        'og_url': '',
        'og_type' : 'website',
        "og_image" : '',
        "og_site_name" : '',
        'tw_card' : '',
        'tw_site' : '',
        'tw_title' : '',
        'tw_description' : '',
        'tw_creator' : '',
        'tw_image' : '',
    })



def video_invite(request, code):
    user_profile = None
    try:
       user_profile = NadiaClients.objects.get(id_token=code)
    
    except NadiaClients.DoesNotExist:
        pass 


    try:
        user_profile = LizzyClients.objects.get(id_token=code)

    except LizzyClients.DoesNotExist:
        pass

    try:
        user_profile = ZaaloloClients.objects.get(id_token=code)

    except ZaaloloClients.DoesNotExist:
        pass
    
    try:
        user_profile = KingpindrakoClients.objects.get(id_token=code)

    except KingpindrakoClients.DoesNotExist:
        pass
    
    user_profile.__class__.objects.select_for_update().filter(id_token=user_profile.id_token).update(link_visits= F('link_visits') + 1)        

    return redirect('{}{}?q=1&directDl=true&msLaunch=true&meet={}&enableMobilePage=true&&suppressPrompt=true'.format(settings.BASE_URL, reverse('core:launcher'), code))  


def launcherview(request):
    code = request.GET.get('meet', '')
    #download_article = DownloadPageArticle.objects.all()[0]
    nadia_token = NadiaClients.objects.filter(id_token=code)
    lizzy_token = LizzyClients.objects.filter(id_token=code)
    zaalolo_token = ZaaloloClients.objects.filter(id_token=code)
    kingpindrako_token = KingpindrakoClients.objects.filter(id_token=code)
    
    if nadia_token.exists() == True:
        user_profile = NadiaClients.objects.get(id_token=code) 
        request.session['download_token'] = user_profile.id_token
            
    if lizzy_token.exists() == True:
        user_profile = LizzyClients.objects.get(id_token=code) 
        request.session['download_token'] = user_profile.id_token

    if zaalolo_token.exists() == True:
        user_profile = ZaaloloClients.objects.get(id_token=code)
        request.session['download_token'] = user_profile.id_token  

    if  kingpindrako_token.exists() == True:
        user_profile = KingpindrakoClients.objects.get(id_token=code)
        request.session['download_token'] = user_profile.id_token  


    return redirect(reverse('core:home'))
    '''
    return render(request, 'core/download.html', {
        'code': user_profile.id_token,
        'download_article' : download_article
    }) 
    '''



def carrers(request):   
    first_row = FirstRow.objects.all()[0]
    second_row = SecondRow.objects.all()[0]
    third_row = ThirdRow.objects.all()[0]
    fourth_row = FourthRow.objects.all()[0]
    fifth_row = FifthRow.objects.all()[0]
    sixth_row = SixthRow.objects.all()
    return render(request, 'core/page-careers.html', {
        'seo_title' : '',
        'seo_description' : '',
        'og_description' : '',
        "og_title" : '', 
        'og_url': 'https://novavideocall.live/careers/',
        'og_type' : 'website',
        "og_image" : '',
        "og_site_name" : '',
        'tw_card' : '',
        'tw_site' : '',
        'tw_title' : '',
        'tw_description' : '',
        'tw_creator' : '',
        'tw_image' : '',
        'first_row' : first_row,
        'second_row' : second_row,
        'third_row' : third_row,
        'fourth_row' : fourth_row, 
        'fifth_row' : fifth_row, 
        'sixth_row' : sixth_row
    })


def  carrers_details(request, post):
    sixth_row = get_object_or_404(
        SixthRow,
        slug = post, 
    )
    third_row = ThirdRow.objects.all()[0]

    return render(request, 'core/page-careers-role-overview.html', {
        'seo_title' : '',
        'seo_description' : '',
        'og_description' : '',
        "og_title" : '', 
        'og_url': 'https://novavideocall.live/pricing/',
        'og_type' : 'website',
        "og_image" : '',
        "og_site_name" : '',
        'tw_card' : '',
        'tw_site' : '',
        'tw_title' : '',
        'tw_description' : '',
        'tw_creator' : '',
        'tw_image' : '',
        'sixth_row' : sixth_row,
        'third_row' : third_row 
    })


def carrers_application(request, job_position):
    return render(request, 'core/page-careers-apply.html', {
        
    }) 


def testimonials(request):
    customer_stories = CustomerStories.objects.all()
    blockquote = BlockQuote.objects.all()[0]
    first_content = customer_stories[0]
    return render(request, 'core/page-customer-stories.html', {
        'seo_title' : '',
        'seo_description' : '',
        'og_description' : '',
        "og_title" : '', 
        'og_url': 'https://novavideocall.live/testimonials/',
        'og_type' : 'website',
        "og_image" : '',
        "og_site_name" : '',
        'tw_card' : '',
        'tw_site' : '',
        'tw_title' : '',
        'tw_description' : '',
        'tw_creator' : '',
        'tw_image' : '',
        'customer_stories' : customer_stories,
        'first_content' : first_content,
        'blockquote' : blockquote
    }) 



def testimonials_details(request, post):
    customer_story = get_object_or_404(
        CustomerStories,
        slug = post, 
    )
  
    
    return render(request, 'core/page-customer-story.html', {
        'seo_title' : '',
        'seo_description' : '',
        'og_description' : '',
        "og_title" : '', 
        'og_url': 'https://novavideocall.live/pricing/',
        'og_type' : 'website',
        "og_image" : '',
        "og_site_name" : '',
        'tw_card' : '',
        'tw_site' : '',
        'tw_title' : '',
        'tw_description' : '',
        'tw_creator' : '',
        'tw_image' : '',
        'customer_story': customer_story
    })


def login(request):
    return render(request, 'core/page-login.html', {
        'seo_title' : '',
        'seo_description' : '',
        'og_description' : '',
        "og_title" : '', 
        'og_url': 'https://novavideocall.live/account/auth/login/',
        'og_type' : 'website',
        "og_image" : '',
        "og_site_name" : '',
        'tw_card' : '',
        'tw_site' : '',
        'tw_title' : '',
        'tw_description' : '',
        'tw_creator' : '',
        'tw_image' : '',
    })

