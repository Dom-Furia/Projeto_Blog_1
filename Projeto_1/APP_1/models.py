from django.db import models

#Estrutra do post no banco de dados 
class Post (models.Model):
    titulo = models.CharField(max_length = 200)
    conteudo = models.TextField()
    publicacao_em = models.DateTimeField(auto_now_add = True)
    autor = models.CharField(max_length = 100)
    resumo = models.TextField()
    slug = models.SlugField(unique = True )
    img = models.CharField(max_length = 200)
    class meta:
        ordering = ['-publicado_em']

#Estrutura de Comentarios no banco de dados 
class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name = 'comentarios', on_delete = models.CASCADE)
    nome = models.CharField(max_length = 150)
    email = models.EmailField()
    conteudo = models.CharField(max_length = 500)
    publicado_em = models.DateTimeField(auto_now_add = True)
    class meta:
        ordering = ['publicado_em']