# Kanvas
> Nessa semana você vai desenvolver uma API em Django semelhante ao Canvas. Porém ela será bem mais simples. Vamos chamá-la de Kanvas.
<br>
<h2>Instalação</h2>
<br>

<h2>Linux:</h2>
<h4>Faça o clone do projeto com o comando :</h4>
<br>

```sh
git clone git@gitlab.com:programadorpires/kanvas.git
```
<h4>Navegue pelo terminal até a pasta do projeto para instalação do virtual venv e rode o comando abaixo :</h4>
<br>

Primeiro comando:
```sh
python3 -m venv venv
```
Segundo comando:
```sh
source venv/bin/activate
```
<h4 style='color:#EE82EE'>Observe o (env)na frente do prompt. Isso indica que esta sessão de terminal opera em um ambiente virtual configurado por virtualenv<h4>
<br>

<h4>Agora podemos instalar as dependencias do projeto :</h4>
<br>

```sh
pip install -r requirements.txt
```
<br>
<h4>Com as dependências instaladas podemos rodar o comando de migração no terminal dentro da pasta do projeto :<h4>
<br>

```sh
python manage.py migrate
```

<h4>Parte final rodar o comando para inicializar o server :</h4>

```sh
python manage.py runserver
```
<h3>Endpoints:<h3>
<br>
<br>
Requests e URLs:
<br>
<br>
<h4>POST /api/accounts/ - cria usuários</h4>
<br>
<h4></h4>
<h4>POST /api/login/ -  faz autenticação</h4>
<br>
<h4>PUT /api/courses/registrations/  - matricula estudantes num determinado curso (user: instrutor apenas)</h4>
<br>
<br>
<h4>GET /api/courses/ - lista cursos e alunos matriculados (sem autenticação)</h4>
<br>
<h4>POST /api/activities/ -  cria atividade do estudante (sem nota, user: estudante apenas)</h4>
<br>
<h4>PUT /api/activities/ - edita atividade - atribui nota - (user: facilitador e instrutor)</h4>
<br>
<h4>GET /api/activities/ -  lista atividades do estudante (user: estudante)</h4>
<br>
<h4>GET /api/activities/ - lista todas as atividades de todos os estudantes (user: facilitador e instrutor)</h4>
<br>
<h4>GET /api/activities/<int:user_id>/ - filtra as atividades por user_id (user: facilitador e instrutor)</h4>
<br>
<br>
Criando um estudante:
<br>
<br>
POST /api/accounts/
<br>
<br>

```sh
// REQUEST
{
  "username": "student",
  "password": "1234",
  "is_superuser": false,
  "is_staff": false
}
```
```sh
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "username": "student",
  "is_superuser": false,
  "is_staff": false
}
```
<br>
<br>
Criando um facilitador:
<br>
<br>
POST /api/accounts/
<br>
<br>

```sh
// REQUEST
{
  "username": "facilitator",
  "password": "1234",
  "is_superuser": false,
  "is_staff": true
}
```
```sh
// RESPONSE STATUS -> HTTP 201
{
  "id": 2,
  "username": "facilitator",
  "is_superuser": false,
  "is_staff": true
}
```
<br>
<br>
Criando um instrutor:
<br>
<br>
POST /api/accounts/
<br>
<br>

```sh
// REQUEST
{
  "username": "instructor",
  "password": "1234",
  "is_superuser": true,
  "is_staff": true
}
```
```sh
// RESPONSE STATUS -> HTTP 201
{
  "id": 3,
  "username": "instructor",
  "is_superuser": true,
  "is_staff": true
}
```
<br>
Caso haja a tentativa de criação de um usuário que já está cadastrado o sistema deverá responder com HTTP 409 - Conflict.
<br>
<br>
Sobre Autenticação:
<br>
A API funcionará com autenticação baseada em token:
<br>
<br>
POST /api/login/
<br>
<br>

```sh
// REQUEST
{
  "username": "student",
  "password": "1234"
}
```
```sh
// RESPONSE STATUS -> HTTP 200
{
  "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```
<br>
<br>
Para criação do Curso:
<br>
Para criar um curso é necessario um token de Intrutor:
<br>
<br>
POST /api/courses/
<br>
<br>

```sh
// REQUEST
// Header -> Authorization: Token <token-do-instrutor>
{
  "name": "Javascript 101"
}
```
```sh
// RESPONSE STATUS -> HTTP 201
{
  "id": 1,
  "name": "Javascript 101",
  "user_set": []
}

```
<br>
<br>
Atualizando a lista de estudantes matriculados em um curso:
<br>
<br>
Para atualizar o curso somente token de instrutor
<br>
<br>
PUT /api/courses/registrations/
<br>
<br>

```sh
// REQUEST
// Header -> Authorization: Token <token-do-instrutor>
{
  "course_id": 1,
  "user_ids": [1, 2, 7]
}
```
```sh
// RESPONSE STATUS -> HTTP 200
{
  "id": 1,
  "name": "Javascript 101",
  "user_set": [
    {
      "id": 1,
      "is_superuser": false,
      "is_staff": false,
      "username": "luiz"
    },
    {
      "id": 7,
      "is_superuser": false,
      "is_staff": false,
      "username": "isabela"
    },
    {
      "id": 2,
      "is_superuser": false,
      "is_staff": false,
      "username": "raphael"
    }
  ]
}

```
<br>
<br>
Obtendo a lista de cursos e alunos:
<br>
<br>
GET /api/courses/
<br>
<br>

```sh
// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "name": "Javascript 101",
    "user_set": [
      {
        "id": 1,
        "is_superuser": false,
        "is_staff": false,
        "username": "luiz"
      }
    ]
  },
  {
    "id": 2,
    "name": "Python 101",
    "user_set": []
  }
]

```
<br>
<br>
Criando uma atividade (estudante):
<br>
Somente o estudante pode criar ativiades mais não pode mandar a nota e mesmo que mande vai ser setada como NULL:
<br>
<br>
POST /api/activities/
<br>
<br>

```sh
// REQUEST
// Header -> Authorization: Token <token-do-estudante>
{
  "repo": "gitlab.com/cantina-kenzie",
  "grade": 10 // Esse campo é opcional
}
```
```sh
// RESPONSE STATUS -> HTTP 201
// Repare que o campo grade foi ignorado
{
  "id": 6,
  "user_id": 7,
  "repo": "gitlab.com/cantina-kenzie",
  "grade": null
}

```
<br>
<br>
Listando de  atividades com token de facilitador ou instrutor
<br>
GET /api/activities/
<br>
<br>

```sh
//REQUEST
//Header -> Authorization: Token <token-do-facilitador ou token-do-instrutor>

```
```sh
[
  {
    "id": 1,
    "user_id": 1,
    "repo": "github.com/luiz/cantina",
    "grade": null
  },
  {
    "id": 6,
    "user_id": 1,
    "repo": "github.com/hanoi",
    "grade": null
  },
  {
    "id": 10,
    "user_id": 2,
    "repo": "github.com/foodlabs",
    "grade": null
  },
  {
    "id": 35,
    "user_id": 3,
    "repo": "github.com/kanvas",
    "grade": null
  },
]
```
<br>
<br>
Filtrando atividades fornecendo um user_id opcional com token de facilitador ou instrutor
<br>
GET /api/activities/
<br>
<br>

```sh
//REQUEST (/api/activities/1/)
//Header -> Authorization: Token <token-do-facilitador ou token-do-instrutor>

```
```sh
[
  {
    "id": 1,
    "user_id": 1,
    "repo": "github.com/luiz/cantina",
    "grade": null
  },
  {
    "id": 6,
    "user_id": 1,
    "repo": "github.com/hanoi",
    "grade": null
  },
  {
    "id": 15,
    "user_id": 1,
    "repo": "github.com/foodlabs",
    "grade": null
  },
]
```
<br>
<br>

