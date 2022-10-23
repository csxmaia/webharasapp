from django.db import models
from django.contrib.auth.models import User

class Estado(models.Model):
    sigla = models.CharField(max_length=2, verbose_name="Sigla")
    nome = models.CharField(max_length=50, verbose_name="Nome")

    def __str__(self):
        return self.nome + " - " + self.sigla

class Cidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, verbose_name="Estado")

    def __str__(self):
        return self.nome + " - " + self.estado.sigla

class Raca(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")

    def __str__(self):
        return self.nome

class Pelagem(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    descricao = models.CharField(max_length=200, verbose_name="Descrição")

    def __str__(self):
        return self.nome

class Habilidade(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo")

    def __str__(self):
        return self.tipo

class Genero(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo")

    def __str__(self):
        return self.tipo

class Cavalo(models.Model):
    nome = models.CharField(max_length=70, verbose_name="Nome")
    preco = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Preço")
    data_nascimento = models.DateTimeField(verbose_name="Data de nascimento")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT, verbose_name="Raça")
    pelagem = models.ForeignKey(Pelagem, on_delete=models.PROTECT, verbose_name="Pelagem")
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, verbose_name="Genero")
    habilidade = models.ForeignKey(Habilidade, on_delete=models.PROTECT, verbose_name="Habilidade")
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, verbose_name="Cidade")
    status = models.CharField(max_length=20, verbose_name="Status")
    proprietario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="cavalo_proprietario")
    registro = models.CharField(max_length=50, verbose_name="Registro", null=True, blank=True)
    #TODO treinamento

    criado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name="cavalo_criado_por")
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name="cavalo_atualizado_por")
    modificado_em = models.DateTimeField(auto_now=True)

class Imagem(models.Model):
    cavalo = models.ForeignKey(Cavalo, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to="imagens")