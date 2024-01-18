from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

menu = [
        {'title': 'Посты', 'url_name': 'main:post_list'},
        {'title': 'Добавить пост', 'url_name': 'main:post_add'},
        {'title': 'О сайте', 'url_name': 'main:about'},
        {'title': 'Контакты', 'url_name': 'main:contacts'},
        ]
        

# главная страница сайта
def index_root(request):
    return render(request, 'main/index_root.html')

# главная страница приложения main
def index(request):
    return render(request, 'main/index.html', context={'menu':menu})

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def post_add(request):
    pass

# Отображение списка постов
def post_list(request):
    # Получаем все объекты таблицы (модели) Post
    posts = Post.objects.all()
    # Заносим их в объект контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name='main/post_list.html', context=context)

def post_add(request):
    title = "Создать пост"
    if request.method == "GET":
        form = PostForm()
        context = {"title": title, "menu": menu, "form": form}
        return render(request, "main/post_add.html", context)

    if request.method == "POST":
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = Post()
            post.author = post_form.cleaned_data['author']
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']

            post.publish()
            # возвращаем список всех постов
            return post_list(request)
