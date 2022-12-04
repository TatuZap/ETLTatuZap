# TatuZap

O TatuZap é um bot de WhatsApp, que tem como objetivo auxiliar os estudantes da UFABC à acessar dados cruciais para o cotidiano da faculdade, como dados da matrícula atual do aluno, salas, professores, matérias, entre outros.

O MVP do TatuZap consiste de dois repositórios, o ETLTatuZap, reponsável por carregar os dados da UFABC periodicamente e popular o banco de dados, e o BotTatuZap, que consiste na IA que será responsável por se comunicar com o usuário e recuperar os dados solicitados no banco já populado.

<hr />

## ETLTatuZap

Os códigos presentes nesse repositório são relativos ao processo de Extração, Transformação e Carregamento (LOAD), também conhecido como _ETL_, toda essa etapa tem como objetivo alimentar o banco de dados a ser utilizado em nosso chatbot (https://github.com/TatuZap/BotTatuZap) para responder queries de usuários.

Dentro do ETLTatuZap, pretendemos utilizar as seguintes tecnologias:

- Python(3.9)

- Pandas

- MongoDB

- FastAPI

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

## Executando localmente

### Instalando python:

- Windows: download do [Instalador](https://www.python.org/downloads/)

- Linux: sudo apt-get install python3

### Instalando PIP

- Windows: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
- Linux: sudo apt install python3-pip
  Conferindo a instalação: pip3 --version

### Instalando virtualenv

- pip install virtualenv

#### Criando Ambiente Virtual

- python3 -m venv venv

#### Ativando ambiente virtual

- Windows: No CMD venv\Scripts\Activate

- Linux: source venv/bin/activate

### Instalando Dependencias

- pip install -r requirements.txt

### Executando

- python src/main.py

# TODO Refazer README
