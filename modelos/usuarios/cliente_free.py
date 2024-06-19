from modelos.usuarios.usuario import usuario

class ClienteFree (usuario):
    def __init__(self,nome,idade,email,telefone) -> None:
        super().__init__(nome, idade, email, telefone)

    def __str__(self):
        return "Você é um cliente Free"

    def informacao_plano_free(self):
        return "Você está no plano gratuito, aproveite os recursos básicos!"

    def upgrade_premium(self):
        self.premium = True
        return "Parabéns, você agora é um cliente premium!"

