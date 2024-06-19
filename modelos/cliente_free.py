from modelos.usuario import clie
class ClienteFree (nome, idade, email, telefone):
    def __init__(self) -> None:
        self.is_premium = False

    def __str__(self):
        return "Você é um cliente normal"

    def informacao_plano_free(self):
        return "Você está no plano gratuito, aproveite os recursos básicos!"

    def upgrade_premium(self):
        self.premium = True
        return "Parabéns, você agora é um cliente premium!"



