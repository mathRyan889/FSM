# 💰 FSM — Financial System Manager

> API REST completa para gestão financeira pessoal — controle de contas, cartões, transações e orçamentos com alertas automáticos e integração com dados do Banco Central do Brasil.

<br>

## 📋 Sobre o Projeto

O FSM é um sistema backend de gestão financeira pessoal que permite ao usuário controlar suas contas bancárias, cartões de crédito, transações e metas de orçamento. O sistema atualiza o saldo das contas automaticamente via Django Signals, categoriza gastos e disponibiliza relatórios por período.

Desenvolvido como projeto de portfólio com foco em boas práticas de desenvolvimento backend: arquitetura em apps separados por domínio, autenticação JWT, permissões por objeto, documentação Swagger e código padronizado com PEP8.

<br>

## 🚀 Tecnologias

| Tecnologia | Uso |
|---|---|
| Python | Linguagem principal |
| Django | Framework web |
| Django REST Framework | API REST |
| Simple JWT | Autenticação stateless |
| PostgreSQL | Banco de dados relacional |
| Django Jazzmin | Interface administrativa |
| dj-rql | Filtros avançados na API |
| drf-spectacular | Documentação Swagger/OpenAPI |
| Celery + RabbitMQ | Tasks assíncronas e alertas |
| Docker + Docker Compose | Containerização |
| flake8 + autopep8 | Linter e formatação PEP8 |

<br>

## 🗂️ Estrutura de Apps

```
FSM/
├── accounts/        # Perfil de usuário (UserProfile)
├── authentication/  # Autenticação JWT
├── finance/         # Contas bancárias e cartões
├── transactions/    # Transações, categorias e signals de saldo
├── budgets/         # Metas de orçamento por categoria
├── core/            # Settings, urls raiz e permissões globais
├── manage.py
├── .flake8
└── .gitignore
```

<br>

## ⚙️ Funcionalidades

- ✅ Cadastro e gestão de **contas bancárias** (corrente, poupança, investimento)
- ✅ Cadastro de **cartões de crédito** vinculados a contas
- ✅ Registro de **transações** (receitas e despesas) com categorização
- ✅ **Saldo atualizado automaticamente** via Django Signals a cada transação criada ou deletada
- ✅ **Metas de orçamento** por categoria e período
- ✅ **Resumo financeiro por período** — total de receitas, despesas e saldo líquido
- ✅ **Permissões por objeto** — usuário acessa apenas seus próprios dados
- ✅ Autenticação com **JWT** (access + refresh token)
- ✅ **Filtros avançados** com RQL
- ✅ **Documentação interativa** via Swagger

<br>

## 🔐 Níveis de Acesso

| Nível | Quem | Acesso |
|---|---|---|
| Admin | `is_staff=True` | Acesso total a todos os dados |
| Autenticado | Token JWT válido | Acesso apenas aos próprios dados |
| Público | Sem token | Sem acesso à API |

<br>

## 📡 Principais Endpoints

### Autenticação
```
POST   /api/auth/token/           → Login (retorna access + refresh token)
POST   /api/auth/token/refresh/   → Renovar access token
POST   /api/auth/register/        → Cadastro de novo usuário
```

### Contas
```
GET    /api/accounts/             → Listar contas do usuário
POST   /api/accounts/             → Criar conta
GET    /api/accounts/{id}/        → Detalhar conta
PATCH  /api/accounts/{id}/        → Atualizar conta
DELETE /api/accounts/{id}/        → Desativar conta
```

### Transações
```
GET    /api/transactions/          → Listar transações (suporta filtros RQL)
POST   /api/transactions/          → Criar transação (Signal atualiza saldo)
GET    /api/transactions/{id}/     → Detalhar transação
PATCH  /api/transactions/{id}/     → Atualizar transação
DELETE /api/transactions/{id}/     → Deletar (Signal reverte saldo)
GET    /api/transactions/summary/  → Resumo do período (receitas, despesas, saldo)
```

### Orçamentos
```
GET    /api/budgets/              → Listar orçamentos
POST   /api/budgets/              → Criar orçamento por categoria
PATCH  /api/budgets/{id}/         → Atualizar orçamento
DELETE /api/budgets/{id}/         → Deletar orçamento
```

<br>

## 🧠 Django Signals

O saldo das contas é gerenciado automaticamente via Signals — sem necessidade de atualização manual.

```python
# Criação de transação → Signal atualiza saldo
Transaction.objects.create(account=conta, amount=200, type='EXPENSE', ...)
# conta.balance: 1000.00 → 800.00 ✅

# Deleção de transação → Signal reverte o saldo
transaction.delete()
# conta.balance: 800.00 → 1000.00 ✅
```

<br>

## 🛠️ Como rodar localmente

### Pré-requisitos

- Python 3.12+
- pip
- Git

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/mathRyan889/FSM.git
cd FSM
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente**

Crie um arquivo `.env` na raiz do projeto:
```env
SECRET_KEY=sua-secret-key-aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=fsm_db
DB_USER=postgres
DB_PASSWORD=sua-senha
DB_HOST=localhost
DB_PORT=5432
```

**5. Rode as migrations**
```bash
python manage.py migrate
```

**6. Crie o superusuário**
```bash
python manage.py createsuperuser
```

**7. Inicie o servidor**
```bash
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000`

<br>

## 📚 Documentação

| Interface | URL |
|---|---|
| Swagger UI | `http://127.0.0.1:8000/api/schema/swagger-ui/` |
| Redoc | `http://127.0.0.1:8000/api/schema/redoc/` |
| Django Admin | `http://127.0.0.1:8000/admin/` |

<br>

## 🔍 Filtros com RQL

A API suporta filtros avançados via RQL nos endpoints de transações:

```
# Filtrar por tipo
GET /api/transactions/?type=EXPENSE

# Filtrar por período
GET /api/transactions/?date__gte=2026-01-01&date__lte=2026-01-31

# Resumo do período
GET /api/transactions/summary/?date_from=2026-01-01&date_to=2026-01-31
```

<br>

## 📁 Padrões de código

O projeto utiliza **flake8** para análise estática e **autopep8** para formatação automática seguindo PEP8.

```bash
# Verificar erros
flake8 .

# Formatar automaticamente
autopep8 --in-place --recursive .
```

<br>

## 👤 Autor

**Matheus Ryan**
- GitHub: [@mathRyan889](https://github.com/mathRyan889)
- LinkedIn: [matheus-ryan-74110521b](https://linkedin.com/in/matheus-ryan-74110521b)
- Website: [stolus.pythonanywhere.com](https://stolus.pythonanywhere.com)