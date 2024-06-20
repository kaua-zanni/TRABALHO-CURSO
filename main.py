from modelos.usuarios.cliente_free import ClienteFree
from modelos.usuarios.cliente_premium import Cliente_premium
from modelos.link_produto import Link_produto
from modelos.suporte import Suporte
from modelos.usuarios.usuario import usuario
def main():
    
    free_customer = ClienteFree('𝖓𝖔𝖒𝖊','15','email','99564826583')
    premium_customer = Cliente_premium(["Desconto", "Entrega rápida"], 50.00,'nome','15','email','99564826583')
    produto_link = Link_produto(
        "https://www.kabum.com.br/produto/238671/console-playstation-5-sony-ssd-825gb-controle-sem-fio-dualsense-com-midia-fisica-branco-1214a", "Produto A", 
        "Eletrônicos",  
        "Console Playstation 5 Sony, SSD 825GB, Controle sem fio DualSense, Com Mídia Física, Branco - 1214A",
     '3.440,99'
    )

    support = Suporte("example@email.com", "1234567890", "Suporte ao cliente")
    login = usuario('𝖓𝖔𝖒𝖊','𝖎𝖉𝖆𝖉𝖊',"user@example.com",'telefone')

    
    print("-" * 30)
    print("Free Customer:")
    print(free_customer)
    free_customer.informacao_plano_free()
    free_customer.login_bem_sucedido()
    print("-" * 30)
    print("Premium Customer:")
    print(premium_customer)
    premium_customer.obter_beceficios_premium()
    premium_customer.login_bem_sucedido()
    print("-" * 30)
    print("Product Link:")
    print(produto_link)
    produto_link.detalhes_produto()
    print("-" * 30)
    print("Support:")
    print(support)
    print("-" * 30)
    print("usuario:")
    print(login)
    login.login_bem_sucedido()
    print("-" * 30)
    

if __name__ == "__main__":
    main()