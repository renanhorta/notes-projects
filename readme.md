# Projeto de Lembretes

## Tecnologias Utilizadas
- **Backend**: Django (Django Rest Framework)
- **Frontend**: React
- **Banco de Dados**: Postgres
- **Autenticação**: JWT

## Descrição do Projeto
O projeto consiste em um aplicativo web para a criação, edição e gerenciamento de lembretes. O objetivo principal é demonstrar conhecimentos em:

- Construção de uma API RESTful com Django Rest Framework (DRF)
- Integração entre frontend (React) e backend (Django)
- Implementação de autenticação segura com JWT
- Deployment da aplicação, feita no site Choreo
- Conceitos básicos e boas práticas de programação

## Funcionalidades
- **Cadastro/Login de usuários**
- **Criação, edição e exclusão de lembretes**
- **Listagem de lembretes do usuário logado**
- **Autenticação e autorização com JWT**
- **Armazenamento de lembretes no banco de dados**

## Estrutura do Projeto
```
notes-projects/
│── backend/       # Código do backend em Django
│── frontend/      # Código do frontend em React
│── README.md      # Arquivo com informações sobre o projeto
```

## Deployment
A aplicação está rodando em um deploy na **Choreo**. No entanto, o serviço utilizado possui uma limitação onde o banco de dados desliga a cada hora. O objetivo deste projeto não é manter um ambiente de produção estável, mas sim aprender a configurar e executar um deploy completo, rodando a aplicação sem depender do localhost.

