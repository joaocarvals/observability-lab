# Observability Lab

Laboratório de estudos de **SRE e Observabilidade**: uma API em FastAPI instrumentada com métricas Prometheus e logging estruturado, acompanhada de um stack de monitoramento via Docker Compose.

## Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — API web
- **[prometheus-fastapi-instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)** — exposição automática de métricas em `/metrics`
- **[Prometheus](https://prometheus.io/)** — coleta e armazenamento de métricas (via Docker Compose)
- **Logging** estruturado em stdout (`logging` padrão do Python)

## Estrutura do projeto

```
app/            # Código da API (FastAPI, logger)
monitoring/     # Configuração do Prometheus (scrape configs)
Dockerfile      # Build da imagem da API
docker-compose.yml
docs/           # (reservado para documentação futura)
kubernetes/     # (reservado para manifests futuros)
scripts/        # (reservado para scripts futuros)
tests/          # (reservado para testes futuros)
```

## Pré-requisitos

- Docker e Docker Compose
- Python 3.12+ (opcional, só se quiser rodar a API fora de container)

## Executando tudo com Docker Compose (recomendado)

```bash
docker compose up -d --build
```

Isso sobe dois containers na mesma rede:

| Serviço      | URL                          | Descrição                          |
|--------------|-------------------------------|--------------------------------------|
| `api`        | http://localhost:8000         | API FastAPI                          |
| `prometheus` | http://localhost:9090         | Coleta e armazenamento de métricas   |

O Prometheus já vem configurado (`monitoring/prometheus.yml`) para coletar métricas da API em `api:8000` (nome do serviço na rede do compose) a cada 5 segundos.

Endpoints da API:

| Endpoint    | Descrição                         |
|-------------|-------------------------------------|
| `/`         | Status do serviço                  |
| `/health`   | Health check                       |
| `/metrics`  | Métricas no formato Prometheus     |

## Executando a API localmente sem Docker

```bash
# criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/macOS

# instalar dependências
pip install -r app/requirements.txt

# rodar a API (a partir da raiz do projeto)
uvicorn app.main:app --reload
```

Se for rodar a API localmente (fora do compose) e ainda quiser coletar métricas com o Prometheus em container, troque o target em `monitoring/prometheus.yml` de `api:8000` para `host.docker.internal:8000`.

## Licença

Este projeto está licenciado sob os termos do arquivo [LICENSE](LICENSE).
