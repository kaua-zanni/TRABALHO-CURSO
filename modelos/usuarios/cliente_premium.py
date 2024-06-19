from modelos.usuarios.usuario import usuario

class Cliente_premium(usuario):
  def __init__(self, vantagens, preco_premium,nome,idade,email,telefone):
    super().__init__(nome,idade,email,telefone)
    self.vantagens = vantagens
    self.preco_premium = preco_premium

  def obter_beceficios_premium(self):
     print(f"Beneficios premium:{','.join(self.vantagens)}")
  
  def preco_premium(self):
    print(self.preco_premium)

  
  def __str__(self) :
    return f"Vantagens: {self.vantagens} \nPreço: {self.preco_premium}"
    
    