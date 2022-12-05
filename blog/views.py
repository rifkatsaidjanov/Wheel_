from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from django.contrib import messages
from .models import Article, Category
from .forms import ArticleForm, LoginForm, RegistrationForm


# Bu glavniy saxifa uchun def
# def index(request):
#     articles = Article.objects.all()
#
#     context = {
#         'articles': articles
#     }
#     return render(request, 'blog/article_list.html', context)


# Bu glavniy saxifa uchun class
class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'

    paginate_by = 3

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category')




# Qaysidir kategoriya bosilganda unga tegishli maqolalar qolsin qogani ketishi uchun def
# def category_list(request, pk):
#     articles = Article.objects.filter(category_id=pk)
#
#     context = {
#         'articles': articles
#     }
#     return render(request, 'blog/article_list.html', context)

# Qaysidir kategoriya bosilganda unga tegishli maqolalar qolsin qogani ketishi uchun class
class ArticleListByCategory(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(
            category_id=self.kwargs['pk'], is_published=True
        ).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context




# Batafsil knopkasi bosilganda ochiladigan saxifa uchun def
# def article_detail(request, pk):
#     article = Article.objects.get(pk=pk)
#
#     context = {
#         'title': article.title,
#         'article': article
#     }
#     return render(request, 'blog/article_detail.html', context)


# Batafsil knopkasi bosilganda ochiladigan saxifa uchun class
class ArticleDetails(DetailView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['title'] = f"Maqola {article.title}"
        return context



# Maqola qo'shish saxifasi uchun'
# def add_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article = Article.objects.create(**form.cleaned_data)
#             article.save()
#             return redirect('index')
#     else:
#         form = ArticleForm
#
#     context = {
#         'form': form,
#         'title': 'Maqola qoshish'
#     }
#     return render(request, 'blog/add_article.html', context)



# Maqola qo'shish saxifasi uchun'
class NewArticle(CreateView):
    form_class = ArticleForm
    template_name = 'blog/add_article.html'
    extra_context = {
        'title': 'Maqola qoshish'
    }
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# search uchun kodlar
class SearchResults(ArticleList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        article = Article.objects.filter(title__icontains=word)
        return article


# Maqolani o'zgartirish knopkasi uchun'
class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add_article.html'


# Maqolani o'chirish uchun kodlar'
class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('index')
    context_object_name = 'article'


# Bu profil saxifasi uchun
@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'title': 'Ваш профиль'})



# Bu kirish saxifasi uchun
def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, "Вы успешно авторизовались")
                return redirect('index')
            else:
                messages.error(request, "Что то не так")
                return redirect('login')
        else:
            messages.error(request, "Что то не так")
            return redirect('login')
    else:
        form = LoginForm()

    context = {
        'title': 'Авторизация пользователя',
        'form': form
    }
    return render(request, 'blog/user_login.html', context)


# Bu vixod knopkasi uchun
def user_logout(request):
    logout(request)
    messages.warning(request, 'Вы вышли из аккаунта')
    return redirect('index')



# Bu yog'i registratsiya knopkasi uchun'
def registration(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Аккаунт успешно создан')
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'title': 'Регистрация пользователя',
        'form': form
    }

    return render(request, 'blog/register.html', context)









