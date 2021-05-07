# Kanvas
> Nessa semana você vai desenvolver uma API em Django semelhante ao Canvas. Porém ela será bem mais simples. Vamos chamá-la de Kanvas.
<br>
<h2>Instalação</h2>
<br>

<h2>Linux:</h2>
<h4>Faça o clone do projeto com o comando :</h4>
<br>

```sh
git clone git@gitlab.com:programadorpires/kenzie-pet.git
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
POST /animals/ - cadastrar animal
<br>
<br>
GET /animals/ - listar animais
<br>
<br>
GET /animals/<int: animal_id> - filtrar animal
<br>
<br>
DELETE /animals/<int: animal_id> - deletar animal
<br>
<br>
<br>
<br>
Cadastrando de animal:
<br>
<br>
POST /animals/
<br>
<br>

```sh
// REQUEST
{
  "name": "Bidu",
	"age": 1,
	"weight": 30,
	"sex": "macho",
  "group": {
	"name": "cao",
	"scientific_name": "canis familiaris"
	},
  "characteristic_set": [
    {
	"characteristic": "peludo"
    },
    {
	"characteristic": "medio porte"
    }
  ]
}
```

<br>
<br>
Fazendo a leitura dos animais cadastrados:
<br>
GET /animals/
<br>
<br>

```sh
// RESPONSE STATUS -> HTTP 200
[
  {
    "id": 1,
    "name": "Bidu",
    "age": 1,
    "weight": 30,
    "sex": "macho",
    "group": {
      "id": 1,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristic_set": [
      {
        "id": 1,
        "characteristic": "peludo"
      },
      {
        "id": 2,
        "characteristic": "medio porte"
      }
    ]
  },
  {
    "id": 2,
    "name": "Hanna",
    "age": 1,
    "weight": 20, 
    "sex": "femea",
    "group": {
      "id": 2,
      "name": "gato",
      "scientific_name": "felis catus"
    },
    "characteristic_set": [
      {
        "id": 1,
        "characteristic": "peludo"
      },
      {
        "id": 3,
        "characteristic": "felino"
      }
    ]
  }
]
```

<br>
<br>
Filtrando animais:
<br>
GET /animals/< int:animal_id >/
<br>
<br>

```sh
// RESPONSE STATUS -> HTTP 200
  {
  "id": 1,
  "name": "Bidu",
  "age": 1,
  "weight": 30,
  "sex": "macho",
  "group": {
    "id": 1,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristic_set": [
    {
      "id": 1,
      "characteristic": "peludo"
    },
    {
      "id": 2,
      "characteristic": "medio porte"
    }
  ]
}
```
<br>
<br>
Deletando animais:
<br>
DELETE /animals/< int:animal_id >/
<br>
<br>

```sh
// RESPONSE STATUS -> HTTP 204 (no content)
```
<br>


