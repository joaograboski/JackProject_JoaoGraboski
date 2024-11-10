1.0. Diário de Bordo do Projeto:

DIA 1:
Na primeira etapa foram realizadas pesquisas a respeito da linguagem Python e suas sintaxes, já que eu não havia desenvolvido nenhum projeto com tal linguagem. Ainda foram relembradas algumas funções NoSQL a serem utilizadas posteriormente.

DIA 2:
No segundo dia foi criada toda a estrutura a ser utilizada no projeto, como o Cluster do MongoDB para o banco de dados e o repositório git para código e readme. Além disso, foi iniciado o desenvolvimento do código a partir da escolha das bibliotecas.

DIA 3:
A terceira etapa foi focada no desenvolvimento do código, além de diversas tentativas de execução até chegar ao resultado final. Também foram realizadas as conexões ao meu próprio banco de dados e pesquisas adicionais também relacionadas a Python.


1.1. Análise do Código:

Foram escolhidas algumas bibliotecas/framework/classes a serem utilizada, tais como pymongo para conexão com o MongoDB, o framework FastAPI requisitado, bson para identificar o ObjectID do MongoDB, além de outro(a)s para criar a lista de pessoas, para exceções, para o tipo data e validação dos dados.

Foi feita a conexão com o MongoDB através da string de conexão e dos nomes da database e da coleção.

Criação da classe de pessoa contendo os tipo requisitados: nome e data de nascimento.

Transformação do ObjectID do MondoDB em string pra ser compatível com o código.

Foi feita uma função para passar o tipo datetime para date para ser aceito no MongoDB. O MongoDB não lê o tipo date (sem o horário), assim foi convertido o tipo date para datetime (data com hora) de modo que as horas ficam no mínimo (zeradas).

Criação das funções CRUD (com seus respectivos parâmetros):

Funções que modificam o banco através de comandos NoSQL como insert_one, update_one, delete_one e .find().

Atualizações no dicionário de acordo com cada função através de .dict().

Criação de exceções usando 'HTTPException' e exibindo mensagens de erro.


2.0. Tutorial de como rodar na sua máquina:

- Instalar Python (caso não esteja instalado na máquina);

- Baixar os arquivos do repositório;
  
- Extrair arquivos da pasta;

1.Abrir o Prompt de Comando do computador (terminal);

-Comandos a serem executados dentro do terminal-

2.Navegar até o diretório da pasta (adquirida do repositório):

cd -caminho até o repositório-

3.Criar um ambiente virtual para rodar a API na sua máquina:

python -m venv venv

E depois ativar esse ambiente virtual:

.\venv\Scripts\activate

4.Instalar as dependências para rodar a API:

pip install fastapi pymongo uvicorn 

5.Rodar a FastAPI usando o Uvicorn:

uvicorn fapi:app --reload

//"fapi" já é o nome do arquivo (.py) em python a ser executado 

Após todos os passos anteriores, abrir esse endereço no navegador:
http://127.0.0.1:8000/docs

Tudo pronto para usar as funções nesse endereço!



