# Projeto de Índice Invertido e Modelo Booleano com SpaCy

## Ideia do Trabalho
O objetivo deste projeto é implementar um índice invertido e um modelo booleano utilizando apenas a biblioteca **SpaCy**. O sistema processa consultas e gera arquivos de texto contendo as respostas, assim como um índice invertido, que facilita a busca em documentos.

## Estrutura do Código
O código do projeto está organizado em três partes principais, cada uma referenciada com um comentário e traços "----":
1. **Índice Invertido**: Responsável por criar e armazenar o índice invertido, onde cada termo é mapeado para os documentos em que aparece e a quantidade de vezes que aparece.
2. **Modelo Booleano**: Lida com as consultas feitas pelo usuário e utiliza o índice invertido para determinar quais documentos satisfazem as condições da consulta.
3. **Main**: Onde as funções são chamadas, controlando o fluxo do programa e gerenciando a interação com o usuário.

## Lógica do Programa
O programa opera da seguinte maneira:
1. **Recepção da Base de Dados**: O script começa recebendo um arquivo `base.txt`, que contém referências a documentos em duas pastas (`base1` e `base_samba`).
2. **Leitura de Documentos**: Ao encontrar o arquivo de base, o programa lê todos os documentos listados e armazena os tokens (palavras) referentes a esses documentos.
3. **Criação de Objetos da Classe `termo`**: Cada termo é armazenado em objetos da classe `termo`, que possui os atributos:
   - `palavra`: o termo em si.
   - `ocorrência`: um dicionário que indica em quais documentos o termo aparece e quantas vezes (ex: `"amor:0:4,4:2"`).

4. **Execução de Consultas**: A parte do modelo booleano lê a consulta do usuário, analisa os operadores lógicos e busca no índice para identificar quais documentos correspondem à consulta.

## Instruções para Execução

### Pré-requisitos
Certifique-se de ter o **SpaCy** instalado. Você pode instalar usando o seguinte comando:

```bash
pip install spacy
