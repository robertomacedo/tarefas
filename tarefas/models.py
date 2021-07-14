from django.db import models


class Tarefa(models.Model):
    OP_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )
    OP_STATUS = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )

    descricao = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OP_CATEGORIA, default='importante')
    status = models.CharField(max_length=25, choices=OP_STATUS, default='pendente')
