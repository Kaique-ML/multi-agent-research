"""Agente Analista — sintetiza e analisa as informações coletadas."""
from crewai import Agent


def create_analyst() -> Agent:
    return Agent(
        role="Analista de Dados",
        goal="Sintetizar as informações coletadas em insights claros e acionáveis",
        backstory="""Você é um analista especializado em transformar grandes volumes
        de informação em sínteses concisas e relevantes para negócios.""",
        verbose=True,
    )
