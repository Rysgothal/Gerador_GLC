#  Software que gera textos aleatórios em um subconjunto da língua Portuguesa especificado através de uma gramática livre de contexto.

#   Autor 1: Lucas Souza Frade (ra181370@ucdb.br)
#   Autor 2: Gabriela Villani Moreira (ra181884@ucdb.br)

# Funcionalidade do programa:
## Software que gera textos aleatórios em um subconjunto da língua Portuguesa (como principal) especificado através de uma gramática livre de contexto. O software basicamente gera frases aleatórias.
## Permite que o usuário insira sua gramática, mostra a sequência de produções usadas para gerar a cadeia, mostra a árvore e suas possíveis ramificações.

# ------------------------------------------------------
#             Criando e Ativando o Ambiente. 
# ------------------------------------------------------

## 1° - Criando o Ambiente:

```sh
    $ conda create -n glc
```

## 2° - Verifique se o Ambiente foi criado:

```sh
    $ conda env list
```

## 3° - Ative o Ambiente:

```sh
    $ conda activate glc
```

# ------------------------------------------------------
#       Preparar e instalar dependências. 
# ------------------------------------------------------

## Para maior agilidade
## O "requirements.txt" é um arquivo com todas as dependências, de esse comando para instalar todas (verifique antes, se esta na pasta correta): 

```sh
    $ pip install -r requirements.txt
``` 

# Comando úteis:

## Caso ao criar o Ambiente ele falar que:
### "O comando 'pip' não foi encontrado" então para evitar, de o comando abaixo: 

```sh
    $ sudo apt install python3-pip
```

## Ou se estiver com dúvidas e querer instalar uma por uma:

```sh
    $ pip install networkx
    $ pip install pandas
    $ pip install matplotlib
    $ pip install tk
    $ pip install Pillow
``` 

## Até aqui ja da para rodar o programa:
```sh
    $ python3 PrincipalGLC.py
```
# Caso existir alguma falha:
## Entretanto há uma pequena chance do Python não reconhecer o tkinter, caso isso ocorra, escreva esse comando:  

```sh
    $ sudo apt-get install python3-tk
```

## Em seguida para evitar conflitos de versão, atualize:

```sh
    $ sudo apt-get update
    $ python3 -m pip install --upgrade pip
```
# Gabriela Villani Moreira:
* Criou a base os arquivos de funçoes e a árvore (funcoes_glc, arvore_glc)
* Auxiliou na construção da janela principal
* Implementou a GUI para a nova gramática (frase)
* Implementou o Botão Resetar
* Distribuiu melhor os componentes da tela principal
* Criou a base das funções dos eventos dos botões 
* Corrigiu bugs da classe e da arvore

# Lucas Souza Frade:
* Criou o Arquivo Principal, e a Classe (principal_glc, classe_glc)
* Auxiliou na construção das funçoes e da Arvore 
* Auxiliou nas funções da GUI da nova gramática (frase)
* Criou outro estilo de inserção de gramática
* Auxiliou na criação dos eventos dos botões
* Corrigiu Bugs do arquivo principal e funções


# Memorial do projeto:
* [Generating random sentences from a context free grammar](https://eli.thegreenplace.net/2010/01/28/generating-random-sentences-from-a-context-free-grammar),este link foi utilizado ccomo referência principal para o desenvolvimento da classe principal do projeto, uma base sólida para sua implementação.

* [CFG Developer](https://web.stanford.edu/class/archive/cs/cs103/cs103.1156/tools/cfg/), esse link foi utilizado mais como testes para maior certeza do software

* [Chat](https://openai.com/blog/chatgpt), um suporte significativo, especialmente na identificação e resolução de bugs. A parte de verificar campos vazios, onde possui a variavel vEdits, foi ideia dele, muito boa, nunca ia imaginar que isso ia dar certo :)

* [Arquivo do Professor](https://classroom.google.com/u/4/c/NDkyMzIxNDQ0NDAy/a/NDkyMzIxNDQ0NDMy/details), serviu mais de orientação para o projeto

* O projeto possui 2 imagens desde o inicio do projeto (Sem GUI), para ver somente as frases

* A estimativa de tempo gasto neste projeto foi em torno de 4/5 meses de desenvolvimento, contendo pausas, e refatorações (e muitos, mas muitos bugs com dor de cabeça). 

### Para mais informações abrir código fonte. Não comentamos dentro do código o que cada um fez para não ficar muito extenso.
