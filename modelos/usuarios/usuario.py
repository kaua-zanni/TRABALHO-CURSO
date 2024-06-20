from abc import ABC, abstractmethod

class usuario:
  def __init__(self,nome,idade,email,telefone):
    self.nome = nome
    self.idade = idade
    self.email = email
    self.telefone = telefone

  def __str__(self) :
    return f'Nome: {self.nome} \nIdade: {self.idade} \nEmail:{self.email} \nTelefone: {self.telefone}'

  def email_usuario(self):
    return f"Email: {self.email}"
    
  @abstractmethod
  def login_bem_sucedido(self):
    print('login efetuado com sucesso')
    
  @abstractmethod
  def login_falhou(self):
    print('Login falhou!')

