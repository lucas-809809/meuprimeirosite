from django import forms
from django.core.mail.message import EmailMessage


class FormContato(forms.Form):
    nome = forms.CharField(label="Nome", max_length=150)
    email = forms.EmailField(label="E-mail", max_length=150)
    telefone = forms.CharField(label='Telefone', max_length=20)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        telefone = self.cleaned_data['telefone']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'de: {nome} \n ' \
                   f'{mensagem} \n {telefone}'
        mail = EmailMessage(
            subject='Formulário do site',
            body=conteudo,
            from_email='contato@site.com',
            to=['contato@site.com'],
            headers={'reply_to': email}
        )
        mail.send()
