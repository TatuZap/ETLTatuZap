# TatuZap

O TatuZap é um bot de WhatsApp, que tem como objetivo auxiliar os estudantes da UFABC à acessar dados cruciais para o cotidiano da faculdade, como dados da matrícula atual do aluno, salas, professores, matérias, entre outros.

O MVP do TatuZap consiste de dois repositórios, o ETLTatuZap, reponsável por carregar os dados da UFABC periodicamente e popular o banco de dados, e o BotTatuZap, que consiste na IA que será responsável por se comunicar com o usuário e recuperar os dados solicitados no banco já populado.

<hr />

## ETLTatuZap

Os códigos presentes nesse repositório são relativos ao processo de Extração, Transformação e Carregamento (LOAD), também conhecido como *ETL*, toda essa etapa tem como objetivo alimentar o banco de dados a ser utilizado em nosso chatbot (https://github.com/TatuZap/BotTatuZap) para responder queries de usuários.

Dentro do ETLTatuZap, pretendemos utilizar as seguintes tecnologias:

* Python(3.9)

* Pandas

* MongoDB

* FastAPI

## Instruções
Passo a passo para rodar o projeto.


### Pré-requisitos
- Clone o repositório do Tatuzap ETL
```sh
git clone git@github.com:TatuZap/ETLTatuZap.git
```

- Instale a biblioteca Pandas para auxiliar na manipulação de dados
```sh
# PyPI
pip install pandas
```

- Instale esta biblioteca para que seja possível ler e escrever arquivos Excel usando um código fácil
```sh
# PyPI
pip install openpyxl
```

- Instale a biblioteca unidecode
```sh
# PyPI
pip install unidecode
```

### Execução

- Para testar a primeira query, rode o comando a seguir no diretório raiz do projeto:
```sh
python3 src/extract/classes_by_ra_query.py
```

OBS: Query ainda não implementada, tarefa bloqueada pelo ajuste no tratamento dos dataframes, que está com bugs