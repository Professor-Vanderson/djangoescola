from django.db import models

class categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    data_acesso = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.nome

class professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    data_acesso = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "professores"

    def __str__(self):
        return self.nome

class aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    dtNascimento = models.DateField(blank=True, null=True, verbose_name='Data de nascimento')
    nrTelCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    curso = models.CharField(max_length=100)
    mensalidade = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    data_acesso = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "alunos"

    def __str__(self):
        return self.nome