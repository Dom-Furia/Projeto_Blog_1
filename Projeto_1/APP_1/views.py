from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comentario
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm

# Create your views here.
def home(request):
 posts = Post.objects.all()
 return render(request,'home.html', {'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        comentario = Comentario(nome=nome, email=email, conteudo=conteudo, post=post)
        comentario.save()
        return redirect('post_detail', slug=post.slug)
    
    return render(request, 'post_details.html', {'post': post})
def index(request):
 return render(request, 'index.html')

####### signup page ###############
def user_signup(request):
 if request.method == 'POST':
   form = UserCreationForm(request.POST)
   if form.is_valid():
     form.save()
     return redirect('login')
 else:
     form = UserCreationForm()
 return render(request, 'signup.html', {'form': form})
 
########## Pagina de Login/Entrar ########
def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user:
        login(request, user)
        return redirect('home')
  else:
    form = LoginForm()
  return render(request, 'login.html', {'form': form})
    
######## Pagina de logout/Sair ##########
def user_logout(request):
 logout(request)
 return redirect('login')
 
 
