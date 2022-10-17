# TatuZap

O TatuZap é um bot de WhatsApp, que tem como objetivo auxiliar os estudantes da UFABC à acessar dados cruciais para o cotidiano da faculdade, como dados da matrícula atual do aluno, salas, professores, matérias, entre outros.

O MVP do TatuZap consiste de dois repositórios, o ETLTatuZap, reponsável por carregar os dados da UFABC periodicamente e popular o banco de dados, e o BotTatuZap, que consiste na IA que será responsável por se comunicar com o usuário e recuperar os dados solicitados no banco já populado.

<hr />

## ETLTatuZap

Os códigos presentes nesse repositório são relativos ao processo de Extração, Transformação e Carregamento (LOAD), também conhecido como *ETL*, toda essa etapa tem como objetivo alimentar o banco de dados a ser utilizado em nosso chatbot (https://github.com/TatuZap/BotTatuZap) para responder queries de usuários.

Dentro do ETLTatuZap, pretendemos utilizar as seguintes tecnologias:

* Python(3.9)

* Pandas

* Tabula

* MongoDB

* FastAPI



