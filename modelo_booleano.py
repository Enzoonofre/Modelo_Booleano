import spacy
import os
import sys


# Carregar o modelo de linguagem portuguesa
nlp = spacy.load("pt_core_news_lg")

# Listando todos os arquivos da pasta base
caminho_principal = '.'

#----------------Construção do Indice Invertido---
class Termo:
    def __init__(self, palavra):
        self.palavra = palavra
        self.ocorrencias = {}  # Um dicionário simples

    def adicionar_ocorrencia(self, doc_id):
        if doc_id in self.ocorrencias:
            self.ocorrencias[doc_id] += 1
        else:
            self.ocorrencias[doc_id] = 1

    def __str__(self):
        return f"{self.palavra}: {self.ocorrencias}"


def processar_textos(textos):
    termos = {}
    for i, texto in enumerate(textos, start=1):  # Enumerar a partir de 1 para identificar o documento
        doc = nlp(texto)
        for token in doc:
            # Remover stopwords, verificar se é alfabético e fazer lematização
            if not token.is_stop and token.is_alpha:
                palavra_lema = token.lemma_.lower()
                if palavra_lema not in termos:
                    termos[palavra_lema] = Termo(palavra_lema)
                # Atualizar a quantidade de vezes que a palavra aparece no documento atual
                termos[palavra_lema].adicionar_ocorrencia(i)
    return termos

def gerarIndiceInvertido(termos, caminho_pasta):
    termos_ordenados = sorted(termos, key=lambda termo: termo.palavra)
    with open(os.path.join(caminho_pasta, "indice.txt"), "w", encoding="utf-8") as f:
        for termo in termos_ordenados:
            if termo.ocorrencias:
                f.write(f"{termo.palavra}: ")
                for doc_id, count in termo.ocorrencias.items():
                    f.write(f"{doc_id}: {count}; ")
                f.write("\n")



#-----------------Modelo booleano

# Função para verificar se um termo está em um texto
def contem_termo(texto, termo):
    return termo in texto

# Função para processar uma consulta booleana
def processar_consulta(consulta, textos):
    termos = consulta.split()
    resultados = []

    resultados_atuais = set()
    operador_atual = None

    for termo in termos:
        if termo == '&':
            operador_atual = '&'
        elif termo == '|':
            operador_atual = '|'
        elif termo.startswith('!'):
            termo = termo[1:]
            textos_filtrados = {i for i, texto in enumerate(textos) if not contem_termo(texto, termo)}
            if operador_atual == '&':
                resultados_atuais &= textos_filtrados
            elif operador_atual == '|':
                resultados_atuais |= textos_filtrados
            else:
                resultados_atuais = textos_filtrados
            operador_atual = None
        else:
            textos_filtrados = {i for i, texto in enumerate(textos) if contem_termo(texto, termo)}
            if operador_atual == '&':
                resultados_atuais &= textos_filtrados
            elif operador_atual == '|':
                resultados_atuais |= textos_filtrados
            else:
                resultados_atuais = textos_filtrados
            operador_atual = None

    return resultados_atuais

def gerar_resposta(caminho_base, consulta, resultados):
    with open(os.path.join(caminho_base, "resposta.txt"), "w", encoding="utf-8") as f:
        if resultados:
            documentos = ", ".join(str(indice) for indice in sorted(resultados))
            f.write(f"Consulta: {consulta}\n")
            f.write(f"Documentos: {documentos}\n")
        else:
            f.write(f"Consulta: {consulta}\n")
            f.write("Nenhum documento satisfaz a consulta.\n")




#----------Main---------

if __name__ == "__main__":
    # Verifica se o número de argumentos é o esperado
    if len(sys.argv) != 3:
        print("Uso: python modelo_booleano.py <base.txt> <consulta.txt>")
        sys.exit(1)

    caminho_base = sys.argv[1]  # Caminho para a base de documentos
    consulta_nome = sys.argv[2]  # Nome do arquivo de consulta
    # Listar apenas pastas dentro do caminho principal
    pastas = [nome for nome in os.listdir(caminho_principal) if os.path.isdir(os.path.join(caminho_principal, nome))]

    #Procura do arquivo da base dentro das pastas
    x = []
    encontrou_arquivo = False
    for pasta in pastas:
        if pasta.startswith("base"):
            caminho_pasta = os.path.join('.', pasta)
            arquivos2 = os.listdir(caminho_pasta)

            for arquivo in arquivos2:
                arquivo = arquivo.strip()  # Remove quebras de linha e espaços
                if arquivo == caminho_base.split(os.path.sep)[-1]:  # Verifique apenas o nome do arquivo
                    encontrou_arquivo = True
                    caminho_arquivo = os.path.join(caminho_pasta, arquivo)

                # Verificar se o arquivo existe antes de tentar abrir
                    if os.path.exists(caminho_arquivo):
                        with open(caminho_arquivo, "r", encoding="utf-8") as linhas:
                            for linha in linhas:
                                x.append(linha)
                    else:
                        print(f"Arquivo {caminho_arquivo} não encontrado!")
        if encontrou_arquivo:
            break



    textos = []

    x = [arquivo_nome.strip() for arquivo_nome in x]

    #Leitura do conteúdo de cada arquivo e salvando na lista "textos"
    for arquivo_nome in x:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo_nome)  # Use o caminho base

        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                textos.append(conteudo)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {caminho_arquivo}")



    # Processar os textos
    tokens_lemmatizados = processar_textos(textos)

    # Transformar o dicionário em uma lista de objetos da classe Termo
    lista_termos = list(tokens_lemmatizados.values())

    gerarIndiceInvertido(lista_termos, caminho_pasta)

    # Exibir os objetos Termo
    for termo in lista_termos:
        print(termo)  # Isso irá chamar o método __str__ da classe Termo


    consulta_path = os.path.join(caminho_pasta, consulta_nome)

    with open(consulta_path, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read().strip()
        print(f"Consulta: {conteudo}")

    resultado = processar_consulta(conteudo, textos)
    gerar_resposta(caminho_pasta, conteudo, resultado)
