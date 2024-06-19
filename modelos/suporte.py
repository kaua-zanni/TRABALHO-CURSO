class Suporte:
  def __init__(self, email, telefone, problema):
    self.email = email
    self.telefone = telefone
    self.problema = problema

  def __str__(self):
     return f'Email: {self.email} \nTelefone: {self.telefone} \nProblema ?: {self.problema}'
