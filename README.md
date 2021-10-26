# About

This document explains how to use the resources available in the REST API for Reservation and Comparison of Hotels.

## Install

Create a directorie to the project:

```
mkdir hoteis-project
```

Inside 'hoteis-project', install a virtual environment and initialize it:

Lunix or Mac
```
python3 -m venv env
source env/bin/activate
```
Windows
```
py -m venv env
.\env\Scripts\activate
```

Download repositorie:

```
git clone https://github.com/vpdiogo/hoteis.git
```

Install dependencies:

```
cd hoteis
make install
```

Create the a JSON file for SECRET KEY and credentials:

```
touch credentials.json
```

Inside the created file, write:

```
{
    "DATABASE": "base",
    "JWT_SECRET_KEY": "DontTellAnyone"
}
```

## Execute 
For initialize the application, inside directory from app.py:

```
python3 app.py
```

## Testing

### 1. Consult Hotels

|Method   | URL
|---------|----------------------------------
|GET      | [/hoteis]
|GET      | [/hoteis/bravo]
|GET      | [/hoteis?estrelas_min=4.5&limit=10&offset=0&diaria_max=600]

### 2. Register User

|Method   | URL
|---------|----------------------------------
|POST     | [/cadastro]

|Header
|---------------------------------------------
|Content-Type | [application/json]

|Request Body
|---------------------------------------------
|{
|   "login": "ana",
|   "senha": "asdf" 
|}

### 3. Login

|Method   | URL
|---------|----------------------------------
|POST     | [/login]

|Header
|---------------------------------------------
|Content-Type | [application/json]

|Request Body
|---------------------------------------------
|{
|   "login": "ana",
|   "senha": "asdf" 
|}

Copy access token.

### 4. Create Hotel

|Method   | URL
|---------|----------------------------------
|POST     | [/hoteis/teste]

|Header
|---------------------------------------------
|Content-Type  | [application/json]
|Authorization | [Bearer {access_token}]

|Request Body
|---------------------------------------------
|{
|   "nome": "Teste Hotel",
|   "estrelas": 4.4,
|   "diaria": 520.2,
|   "cidade": "Rio de Janeiro"
|}

### 5. Update Hotel

|Method   | URL
|---------|----------------------------------
|PUT      | [/hoteis/teste]

|Header
|---------------------------------------------
|Content-Type  | [application/json]
|Authorization | [Bearer {access_token}]

|Request Body
|---------------------------------------------
|{
|   "nome": "Teste Hotel Alterado",
|   "estrelas": 4.9,
|   "diaria": 720.2,
|   "cidade": "Rio de Janeiro"
|}

### 6. Delete Hotel

|Method   | URL
|---------|----------------------------------
|DELETE   | [/hoteis/teste]

|Header
|---------------------------------------------
|Authorization | [Bearer {access_token}]

### 7. Logout

|Method   | URL
|---------|----------------------------------
|POST     | [/logout]

|Header
|---------------------------------------------
|Authorization | [Bearer {access_token}]

### 8. Consult User Data

|Method   | URL
|---------|----------------------------------
|GET      | [/usuarios/1]

|Header
|---------------------------------------------
|Content-Type  | [application/json]

### 9. Delete User

|Method   | URL
|---------|----------------------------------
|DELETE   | [/usuarios/1]

|Header
|---------------------------------------------
|Authorization | [Bearer {access_token}]

## Suggestions

If you haven't Git and Python 3 installed, folow the ULR to download them:
- https://www.python.org/
- https://git-scm.com/

If you use Windows, install Windows Subsystem for Linux in:
- https://docs.microsoft.com/en-us/windows/wsl/install 