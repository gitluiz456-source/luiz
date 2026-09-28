def salvarPessoa():
    nome = input("Digite seu nome: ")
    numero = input("Digite o seu número: ")
    cidade = input("Digite a sua cidade: ")
    idade = input("Digite sua idade: ")

    arquivo = open("pessoa.txt", "w", encoding="utf-8")
    arquivo.write("Nome: " + nome + "\n")
    arquivo.write("Número: " + numero + "\n")
    arquivo.write("Cidade: " + cidade + "\n")
    arquivo.write("Idade: " + idade + "\n")
    arquivo.close()


def salvarProfissional():
    profissao = input("Digite sua profissão: ")
    empresa = input("Digite o nome da empresa: ")
    experiencia = input("Digite seu tempo de experiência profissional: ")

    arquivo = open("profissional.txt", "w", encoding="utf-8")
    arquivo.write("Profissão: " + profissao + "\n")
    arquivo.write("Empresa: " + empresa + "\n")
    arquivo.write("Tempo de Experiência: " + experiencia + "\n")
    arquivo.close()


def salvarIdiomas():
    arquivo = open("idiomas.txt", "w", encoding="utf-8")

    idioma = input("Digite um idioma ou 'fim' para terminar: ")

    while idioma.lower() != "fim":
        arquivo.write(idioma + "\n")
        idioma = input("Digite outro idioma ou 'fim' para terminar: ")

    arquivo.close()


def salvarHabilidades():
    arquivo = open("habilidades.txt", "w", encoding="utf-8")

    habilidade = input("Digite uma habilidade ou 'fim' para terminar: ")

    while habilidade.lower() != "fim":
        arquivo.write(habilidade + "\n")
        habilidade = input("Digite outra habilidade ou 'fim' para terminar: ")

    arquivo.close()
    
##############################################################################################################################

def gerarHTML():
    arquivo = open("curriculo.html", "w", encoding="utf-8")

    arquivo.write("<html>\n")
    arquivo.write("<head>\n")
    arquivo.write("<title>Meu Currículo</title>\n")

    arquivo.write("<style>\n")

    arquivo.write("body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #dbeafe, #eef2ff); margin: 0; padding: 40px; color: #333; }\n")

    arquivo.write(".curriculo { max-width: 850px; margin: auto; background: white; padding: 35px; border-radius: 18px; box-shadow: 0 8px 25px #999; }\n")

    arquivo.write(".cabecalho { background: linear-gradient(135deg, #123c69, #2563a6); color: white; padding: 30px; border-radius: 15px; text-align: center; }\n")

    arquivo.write(".foto { width: 150px; height: 150px; object-fit: cover; border-radius: 50%; border: 5px solid white; }\n")

    arquivo.write("h1 { margin: 15px 0 5px; font-size: 34px; }\n")

    arquivo.write("h2 { color: #123c69; border-bottom: 2px solid #2563a6; padding-bottom: 8px; margin-top: 30px; }\n")

    arquivo.write(".dados { background: #f8fafc; padding: 15px; border-radius: 10px; line-height: 1.9; }\n")
    arquivo.write("ul { background: #f8fafc; padding: 20px 40px; border-radius: 10px; }\n")

    arquivo.write("li { margin: 8px; }\n")

    arquivo.write("</style>\n")
    arquivo.write("</head>\n")
    arquivo.write("<body>\n")

    arquivo.write("<div class='curriculo'>\n")
    arquivo.write("<div class='cabecalho'>\n")
    arquivo.write("<img src='fotoluiz.png' class='foto'>\n")
    arquivo.write("<h1>Meu Currículo</h1>\n")
    arquivo.write("</div>\n")

    pessoa = open("pessoa.txt", "r", encoding="utf-8")
    profissional = open("profissional.txt", "r", encoding="utf-8")
    idiomas = open("idiomas.txt", "r", encoding="utf-8")
    habilidades = open("habilidades.txt", "r", encoding="utf-8")

    dadosPessoa = pessoa.read()
    dadosProfissional = profissional.read()

    arquivo.write("<h2>Informações Pessoais</h2>\n")
    arquivo.write("<div class='dados'>" + dadosPessoa.replace("\n", "<br>") + "</div>\n")
    arquivo.write("<h2>Informações Profissionais</h2>\n")
    arquivo.write("<div class='dados'>" + dadosProfissional.replace("\n", "<br>") + "</div>\n")
    arquivo.write("<h2>Idiomas</h2>\n")
    arquivo.write("<ul>\n")

    linha = idiomas.readline()

    while linha != "":
        arquivo.write("<li>" + linha.strip() + "</li>\n")
        linha = idiomas.readline()

    arquivo.write("</ul>\n")

    arquivo.write("<h2>Habilidades</h2>\n")
    arquivo.write("<ul>\n")

    linha = habilidades.readline()

    while linha != "":
        arquivo.write("<li>" + linha.strip() + "</li>\n")
        linha = habilidades.readline()

    arquivo.write("</ul>\n")

    arquivo.write("</div>\n")
    arquivo.write("</body>\n")
    arquivo.write("</html>\n")

    pessoa.close()
    profissional.close()
    idiomas.close()
    habilidades.close()
    arquivo.close()


salvarPessoa()
salvarProfissional()
salvarIdiomas()
salvarHabilidades()
gerarHTML()