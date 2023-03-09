from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    criado = models.DateTimeField('Criado', auto_now_add=True)
    modificao = models.DateTimeField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=500)
    imagem = StdImageField('Imagem', upload_to='servico',
                           variations={
                               'thumb': {
                                   'width': 480,
                                   'height': 480,
                                   'crop': True
                               }
                           }
                           )

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome

