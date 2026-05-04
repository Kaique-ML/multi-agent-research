# 🧠 Multi-Agent AI Research System — CrewAI + LangChain
> Sistema multi-agente para pesquisa autônoma, síntese e geração de relatórios com CrewAI

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.28-FF6B35)](https://crewai.com)
[![LangChain](https://img.shields.io/badge/LangChain-0.2-1C3C3C)](https://langchain.com)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED?logo=docker)](https://docker.com)
[![Demo](https://img.shields.io/badge/🚀_API_Demo-Online-00C851)](https://gabriel-multiagent.fly.dev/docs)

## 🎯 Sobre

Sistema com **4 agentes especializados** que colaboram para pesquisar um tema, verificar fatos, sintetizar informações e gerar relatórios estruturados em PDF — de forma totalmente autônoma.

> *"Pesquise o mercado de IA no Brasil em 2025 e gere um relatório executivo"*
> → 4 minutos depois: relatório de 5 páginas com fontes, análise e conclusões.

## 🤖 Agentes

| Agente | Função | Ferramentas |
|--------|--------|------------|
| 🔍 Pesquisador | Busca e coleta informações | Web search, scraping |
| ✅ Verificador | Valida fatos e fontes | Cross-reference, fact-check |
| ✍️ Analista | Sintetiza e analisa | LLM reasoning |
| 📄 Redator | Gera relatório final | Template engine, PDF |

## 🛠️ Stack

| Componente | Tech |
|-----------|------|
| Agentes | CrewAI 0.28 |
| LLM | OpenAI GPT-4o |
| Orquestração | LangChain 0.2 |
| Ferramentas | Tavily Search, Playwright |
| API | FastAPI + WebSocket (progresso) |
| Deploy | Docker + Fly.io |

## 🚀 Rodando

```bash
git clone https://github.com/Kaique-ML/multi-agent-research
cd multi-agent-research

cp .env.example .env
docker compose up --build
# API: http://localhost:8000/docs
```

---
**Gabriel Kaique Portel Silva** | [LinkedIn](https://linkedin.com/in/gabriel-kaique-881475284) | [GitHub](https://github.com/Kaique-ML)
