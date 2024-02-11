
# Regras de Usuário 

### Login

```http
  POST /login/
```

| Parâmentro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | Nome do usuário para o login. |
| `password` | `int` | Senha do usuário para o login. |

### Criar Usuário

```http
  POST /users/register/
```

| Parâmentro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username` | `string` | Nome do usuário para o criação da conta. |
| `password` | `int` | Senha do usuário para a criação da conta. |
| `first_name` | `string` | Primeiro nome. |
| `last_name` | `string` | Segundo nome. |
| `email` | `string` | Email. |
| `bio` | `string` | Biografia ou descrição. |
| `location` | `string` | Localização do usuário. |
| `birth_date` | `string` | Data de aniversário. |


### Pegar Usuário

```http
  GET /users/home/<username>/
```

| Cabeçalho   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Authorization`      | `string` | Token de autenticação JWT |

### Atualizar dados de Usuário

```http
  PATCH /users/change-user/<username>/
```

| Cabeçalho   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Authorization`      | `string` | Token de autenticação JWT |

| Parâmentro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `first_name` | `string` | (Opcional) Primeiro nome. |
| `last_name` | `string` | (Opcional) Segundo nome. |
| `email` | `string` | (Opcional) Email. |
| `bio` | `string` | (Opcional) Biografia ou descrição. |
| `location` | `string` | (Opcional) Localização do usuário. |
| `birth_date` | `string` | (Opcional) Data de aniversário. |


### Deletar Usuário

```http
  DELETE /users/delete/<username>/
```

| Cabeçalho   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Authorization`      | `string` | Token de autenticação JWT |



# Regras de Eventos 


### Criar Eventos

```http
  POST /users/register/
```

| Cabeçalho   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Authorization`      | `string` | Token de autenticação JWT |

| Corpo   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user_id`      | `string` | ID do usuário que está criando o evento. |
| `nome`      | `string` | Nome do evento. |
| `data`      | `string` | Data do evento. |
| `tipo`      | `string` | Tipo do evento. |
| `presenca`      | `string` | Presença confirmada no evento. |
| `comentarios`      | `string` | Cometarios adicionados sobre o evento. |



### Pegar Evento

```http
  GET /users/events/<event_id>/
```


### Pegar todos os Eventos

```http
  GET /users/events/
```

### Atualizar dados de Eventos

```http
  PATCH /users/events/update/<id>/
```

| Cabeçalho   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Authorization`      | `string` | Token de autenticação JWT |

| Corpo   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user_id`      | `string` | ID do usuário que está criando o evento. |
| `nome`      | `string` | (Opcional) Nome do evento. |
| `data`      | `string` | (Opcional) Data do evento. |
| `tipo`      | `string` | (Opcional) Tipo do evento. |
| `presenca`      | `string` | (Opcional) Presença confirmada no evento. |
| `comentarios`      | `string` | (Opcional) Cometarios adicionados sobre o evento. |

### Deletar Usuário

```http
  DELETE users/events/delete/<event_id>/
```

| Cabeçalho   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `Authorization`      | `string` | Token de autenticação JWT |
