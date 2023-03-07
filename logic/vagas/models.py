from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=30)
    cnpj = models.CharField(max_length=14)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)

class Vaga(models.Model):
    NIVEL = [
        ('ESTAGIO', 'Estagio'),
        ('TRAINEE', 'Trainee'),
        ('JUNIOR', 'Junior'),
        ('ANALISTA', 'Analista')
    ]
    
    CONTRATO = [
        ('CLT', 'clt'),
        ('PJ', 'pj')
    ]
    
    MODALIDADE = [
        ('REMOTO', 'remoto'),
        ('HIBRIDO', 'hibrido'),
        ('PRESENCIAL', 'presencial')
    ]
    
    DURACAO = [
        ('-6m', 'até 6 meses'),
        ('6m-1a', '6 meses - 1 ano'),
        ('1a-2a', '1 ano - 2 anos'),
        ('indeterm', 'indeterminado')
    ]
    
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=3000)
    requisitos = models.CharField(max_length=3000)
    beneficios = models.CharField(max_length=3000)
    nivel = models.CharField(max_length=8, choices=NIVEL)
    contrato = models.CharField(max_length=3, choices=CONTRATO)
    duracao = models.CharField(max_length=8, choices=DURACAO)
    salario = models.CharField(max_length=5)
    modalidade = models.CharField(max_length=10, choices=MODALIDADE)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)
    data_postagem = models.DateField('data de publicação')
    link = models.CharField(max_length=3000)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)