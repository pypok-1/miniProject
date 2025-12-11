from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/list.html', {'page_obj': page_obj})


@login_required
def article_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')
    else:
        form = ArticleForm()

    return render(request, 'articles/create.html', {'form': form})


@login_required
def article_detail(request: HttpRequest, article_id: int) -> HttpResponse:
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {'article': article})
