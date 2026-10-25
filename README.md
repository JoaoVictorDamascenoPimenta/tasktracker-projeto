# TaskTracker

## Sobre o projeto

o TaskTracker é um sistema simples de gerenciamento de tarefas desenvolvido em Python. ele permite cadastrar tarefas e visualizar as tarefas cadastradas, incluindo título, descrição, prioridade, data limite e status.

## Funcionalidades

- cadastro de novas tarefas;
- validação do título para impedir campos vazios;
- validação da prioridade, aceitando Alta, Média ou Baixa;
- visualização das tarefas cadastradas;
- execução por meio de um menu interativo no terminal.

## Tecnologias utilizadas

- Python 3.11
- Docker
- Docker Compose
- Git e GitHub

## Estrutura do projeto

```text
tasktracker-projeto/
├── docs/
│   └── planejamento_logico.pdf
├── src/
│   └── main.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Como executar o projeto

### 1. Pré-requisitos

para executar o projeto utilizando contêineres, é necessário ter o Docker Desktop instalado e em execução.

### 2. Construir a imagem Docker

na pasta raiz do projeto, execute:

```bash
docker build -t tasktracker .
```

### 3. Executar o contêiner

para iniciar o sistema de forma interativa, execute:

```bash
docker run -it --rm tasktracker
```

### 4. Executar com Docker Compose

outra forma de iniciar o sistema é utilizando o Docker Compose:

```bash
docker compose run --rm tasktracker
```

o uso de `stdin_open: true` e `tty: true` no arquivo `docker-compose.yml` permite a interação com o menu do programa pelo terminal.

## Como utilizar

ao iniciar o sistema, será apresentado um menu com as seguintes opções:

1. cadastrar nova tarefa;
2. visualizar tarefas cadastradas;
3. sair.

escolha a opção desejada e siga as instruções exibidas no terminal.

## Conteinerização

o projeto utiliza um `Dockerfile` para definir a imagem da aplicação e um arquivo `docker-compose.yml` para facilitar sua execução em um contêiner interativo.

essa estrutura ajuda a manter o ambiente de execução padronizado e facilita a execução do sistema em diferentes computadores.

## Repositório

acesse o código-fonte e o histórico de alterações no GitHub:

https://github.com/JoaoVictorDamascenoPimenta/tasktracker-projeto