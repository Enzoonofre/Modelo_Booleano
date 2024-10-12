Ideia do trabalho:
Utilizar apenas a biblioteca Spacy para fazer a criação de um índice invertido e um modelo booleano, que tenha consultas e gere arquivos de texto com a respota das consultas e com o índice invertido

O arquivo do trabalho foi separado em 3 partes no código, referenciadas com o comentário e traços "----",sendo essas partes: índice invertido, modelo booleano e main, cada uma da parte armazena as funções e linhas de códigos necessárias para compor o script.

Para o script rodar ele precisar estar na mesma pasta que as pastas "base1" e "base_samba", se ele estiver dentro das pastas não rodorá como o esperado, mas é possível ajustar o código para conseguir rodar dentro das pastas.

Lógica do programa:
Recebe a base.txt, entra nas pastas e procura essa base, quando acha, le todos os documentos que estão referenciados na base, após isso, armazena os tokens referentes a esses documentos e cria objetos da classe "termo", que tem o atributo "palavra" e "ocorrência", palavra seria propriamente o termo e ocorrência é um dicionário falando em qual documento ele aparece e quantas vezes, por exemplo --> amor:0:4,4:2,etc

Após isso a parte do modelo booleano se concentra em ler a consulta e analisar os operadores lógicos que há na consulta e a partir dai buscar no índice quais documentos que satisfazem essa consulta.

Para conseguir rodar os corretores automáticos disponibilizados, é necessário utilizar os corretores dentro da pasta que quer fazer a verificação, abrir o CMD dentro dessa pasta e chamar da seguinte forma:

python3 waxm_corretor_modelo_booleano.pyc base.txt consulta.txt ../modelo_booleano.py

lembrando que o script não deve estar dentro da pasta da base que se for fazer a verificação


Para rodar:

Para rodar o programa é necessário abrir o CMD na pasta em que estiver o arquivo "modelo_booleano.py" e utilizar o seguinte código:
python modelo booleano.py base.txt consulta.txt

no qual a base poderá escolher entre "base samba" e "base" e a consulta vai variar da base que escolher.

Com o entendimento desses passos, será possível rodar o script e analisa-lo
