class Evento:
    def __init__(self):
        self.__nome = None
        self.__quantidade = None
        self.__artista = []
        self.__setor = []

    def getNome(self):
        return self.__nome

    def setNome(self, nom):
        self.__nome = nom

    def getQuantidade(self):
        return self.__quantidade

    def setQuantidade(self, qua):
        self.__quantidade = qua

    def getArtista(self):
        return self.__artista

    def setArtista(self, art):
        self.__artista.append(art)

    def getSetor(self):
        return self.__setor

    def setSetor(self, seto):
        self.__setor.append(seto)

class Artista:
    def __init__(self):
        self.__nome = None
        self.__cpf = None
        self.__cache  = None
        self.__pagamento = None
        self.__classificacao = None

    def getClassificacaoA(self):
        return self.__classificacao

    def setClassificacaoA(self, cla):
        self.__classificacao = cla

    def getPagamentoA(self):
        return self.__pagamento

    def setPagamentoA(self, pag):
        self.__pagamento = pag

    def getNomeA(self):
        return self.__nome

    def setNomeA(self, nom):
        self.__nome = nom

    def getCpfA(self):
        return self.__cpf

    def setCpfA(self, cpf):
        self.__cpf = cpf

    def getCacheA(self):
        return self.__cache

    def setCacheA(self, cache):
        self.__cache = cache

class Usuario:
    def __init__(self):
        self.__nome = None
        self.__email = None
        self.__senha = None
        self.__evento = None

    def getEventoU(self):
        return self.__evento

    def setEventoU(self, event):
        self.__evento = event

    def getNomeU(self):
        return self.__nome

    def setNomeU(self, nome):
        self.__nome = nome

    def getEmailU(self):
        return self.__email

    def setEmailU(self, email):
        self.__email = email

    def getSenhaU(self):
        return self.__senha

    def setSenhaU(self, senha):
        self.__senha = senha


class Categoria:
    def __init__(self):
        self.__nome = None
        self.__descricao = None
        self.__evento = None

    def getNomeC(self):
        return self.__nome

    def setNomeC(self, nom):
        self.__nome = nom

    def getDescricaoC(self):
        return self.__descricao

    def setDescricaoC(self, desc):
        self.__descricao = desc

    def getEventoC(self):
        return self.__evento

    def setEventoC(self, even):
        self.__evento = even

class Setor:
    def __init__(self):
        self.__nome = None
        self.__evento = []

    def getNomeS(self):
        return self.__nome

    def setNomeS(self, nom):
        self.__nome = nom

    def getEvento(self):
        return self.__evento

    def setEvento(self, evento):
        self.__evento.append(evento)

class Ambiente:
    def __init__(self):
        self.__nome = None
        self.__descricao = None
        self.__classificacao = None

    def getNomeA(self):
        return self.__nome

    def setNomeA(self, nom):
        self.__nome = nom

    def getDescricaoA(self):
        return self.__descricao

    def setDescricaoA(self, des):
        self.__descricao = des

    def getClassificacaoA(self):
        return self.__classificacao

    def setClassificacaoA(self, clas):
        self.__classificacao = clas

class Pagamento:
    def __init__(self):
        self.__usuario = []
        self.__evento = []
        self.__tipoPagamento = None
        self.__total = None

    def getUsuario(self):
        return self.__usuario

    def setUsuario(self, usu):
        self.__usuario.append(usu)

    def getEvento(self):
        return self.__evento

    def setEvento(self, eve):
        self.__evento.append(eve)

    def getTipoPagamento(self):
        return self.__tipoPagamento

    def setTipoPagamento(self, tip):
        self.__tipoPagamento = tip

    def getTotal(self):
        return self.__total

    def setTotal(self, tot):
        self.__total = tot


evento1 = Evento()

evento1.setNome("Show do BTS")
evento1.setQuantidade(1000)

artista1 = Artista()

artista1.setNomeA("Jungkook ")
artista1.setCpfA("000.000.000-00")
artista1.setCacheA(5000.00)
artista1.setClassificacaoA("Cantor")

evento1.setArtista(artista1)

usuario1 = Usuario()

usuario1.setNomeU("Step")
usuario1.setEmailU("step@email.com")
usuario1.setSenhaU("senha123")

usuario1.setEventoU(evento1)

categoria1 = Categoria()

categoria1.setNomeC("Música")
categoria1.setDescricaoC("Eventos com apresentações musicais")

categoria1.setEventoC(evento1)

setor1 = Setor()

setor1.setNomeS("VIP")

setor1.setEvento(evento1)

ambiente1 = Ambiente()

ambiente1.setNomeA("Teatro")
ambiente1.setDescricaoA("Espaço para apresentações teatrais ")
ambiente1.setClassificacaoA("Livre")

pagamento1 = Pagamento()

pagamento1.setTipoPagamento("Cartão de crédito")
pagamento1.setTotal(2000.00)

pagamento1.setUsuario(usuario1)
pagamento1.setEvento(evento1)


print("Nome do evento: ", evento1.getNome())
print("Quantidade de ingressos disponíveis: ", evento1.getQuantidade())

print("Nome do artista: ", evento1.getArtista()[0].getNomeA())
print("CPF do artista: ", evento1.getArtista()[0].getCpfA())
print("Cache do artista: ", evento1.getArtista()[0].getCacheA())
print("Classificação do artista: ", evento1.getArtista()[0].getClassificacaoA())

print("Nome do usuário: ", usuario1.getNomeU())
print("Email do usuário: ", usuario1.getEmailU())
print("Senha do usuário: ", usuario1.getSenhaU())

print("Nome da categoria: ", categoria1.getNomeC())
print("Descrição da categoria: ", categoria1.getDescricaoC())

print("Nome do setor: ", setor1.getNomeS())

print("Nome do ambiente: ", ambiente1.getNomeA())
print("Descrição do ambiente: ", ambiente1.getDescricaoA())
print("Classificação do ambiente: ", ambiente1.getClassificacaoA())

print("Tipo de pagamento: ", pagamento1.getTipoPagamento())
print("Total a pagar: ", pagamento1.getTotal())