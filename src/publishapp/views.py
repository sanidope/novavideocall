from taggit.models import Tag
from django.db.models import Count
from .forms import SearchForm
from django.db.models import Q
from .models import Posts, AboutAuthor
from django.shortcuts import (render, get_object_or_404) 
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)


def is_valid_queryparam(param):
    return param != '' and param is not None



def post_list(request, tag_slug=None):
    tag = None
    search_form =  SearchForm(request.GET)
    keyword = request.GET.get('keyword') 
    posts = Posts.published.all()
    tags = Tag.objects.all().distinct()

    if is_valid_queryparam(keyword):
        posts = Posts.published.filter(
            Q(title__icontains=keyword)|
            Q(body__icontains=keyword) |
            Q(tags__name__icontains=keyword)
        ).distinct()

    if tag_slug:
        tag  = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
        

    paginator = Paginator(posts, 6)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1) 

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
 
    return render(request, 'publishapp/post_list.html', {
        'seo_title' :'Blog | AI Assisted Video Conferencing | Vidicu',
        'seo_description' : 'Insights, news, and articles about ai assisted video conferencing solutions from vidicu.',
        'og_description' : 'Insights, news, and articles about ai assisted video conferencing solutions from vidicu.',
        "og_title" : 'Blog | AI Assisted Video Conferencing | Vidicu', 
        'og_url': 'https://vidicu.live/blog/posts/',
        'og_type' : 'website',
        "og_image" : 'https://vidicu.live/static/vidicu.png',
        "og_site_name" : 'Vidicu',
        'tw_card' : 'summary_large_image',
        'tw_site' : '@vidiculive',
        'tw_title' : 'Blog | AI Assisted Video Conferencing | Vidicu',
        'tw_description' : 'Insights, news, and articles about ai assisted video conferencing solutions from vidicu.',
        'tw_creator' : '',
        'tw_image' : 'https://vidicu.live/static/vidicu.png',
        'posts': posts,
        'page': page,
        'tags' : tags,
        'search_form': search_form,  
    })


def post_detail(request, post):
    about_author = AboutAuthor.objects.all()[0]
    post = get_object_or_404(
        Posts,
        slug = post, 
    )
    
    post_meta_description = post.convert_in_meta
    post_meta_title = post.title
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Posts.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    
    return render(request, 'publishapp/detail.html', {
        'seo_title' : post_meta_title,
        'seo_description' : post_meta_description,
        'og_description' :  post_meta_description,
        "og_title" :  post_meta_title, 
        'og_url': 'https://vidicu.live/blog/posts/detail/',
        'og_type' : 'website',
        "og_image" : 'https://vidicu.live/static/vidicu.png',
        "og_site_name" : 'Vidicu',
        'tw_card' : 'summary_large_image',
        'tw_site' : '@vidiculive',
        'tw_title' : 'Vidicu | AI Powered Video Conferencing, Video Calls, Online Meetings',
        'tw_description' : 'Vidicu is a cloud-based video conferencing platform that offers a range of AI-powered features to make virtual meetings more efficient and engaging. With Vidicu, you can host high-quality video and audio meetings, share screens, and collaborate with team members in real-time',
        'tw_creator' : '',
        'tw_image' : 'https://vidicu.live/static/vidicu.png',
        'post':post,
        'similar_posts': similar_posts,
        'about_author' : about_author
    })