class Link_produto:
  def __init__(self, link, nome_produto, categoria, descricao_produto, preco_produto):
      self.link = link
      self.nome_produto = nome_produto
      self.categoria = categoria
      self.descricao_produto = descricao_produto
      self.preco_produto = preco_produto   
      
  
  def __str__(self):
      return(f"Nome do produto: {self.nome_produto} \nCategoria:{self.categoria} \nDescrição: {self.descricao_produto} \nPreço: {self.preco_produto} \n \nLink: {self.link} \n")


    
  @property
  def links(self):
      return self.nome_produto if self.links != None else "Não há link"

  def detalhes_produto(self):
      print(f"{self.nome_produto} ({self.categoria}): {self.descricao_produto}")

  def preco_produto(self):
      """Returns the product price."""
      return f"Price: {self.preco_produto}"
  