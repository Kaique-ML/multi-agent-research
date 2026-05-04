"""Agente Pesquisador — busca e coleta informações na web."""
from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


def create_researcher() -> Agent:
    return Agent(
        role="Pesquisador Sênior",
        goal="Encontrar informações precisas e atualizadas sobre o tema solicitado",
        backstory="""Você é um pesquisador experiente com habilidade para encontrar
        fontes confiáveis e coletar dados relevantes sobre qualquer tema.""",
        tools=[search_tool, scrape_tool],
        verbose=True,
        max_iter=5,
    )
