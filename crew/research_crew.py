"""Orquestração da CrewAI com os 4 agentes."""
from crewai import Crew, Task
from agents.researcher import create_researcher
from agents.analyst import create_analyst
from agents.writer import create_writer


class ResearchCrew:
    def __init__(self, topic: str, depth: str = "standard"):
        self.topic = topic
        self.depth = depth
        self.researcher = create_researcher()
        self.analyst = create_analyst()
        self.writer = create_writer()

    def run(self) -> str:
        research_task = Task(
            description=f"Pesquise sobre: {self.topic}. Colete no mínimo 5 fontes confiáveis.",
            agent=self.researcher,
            expected_output="Lista estruturada de informações com fontes",
        )
        analysis_task = Task(
            description=f"Analise as informações coletadas sobre {self.topic} e identifique os principais insights.",
            agent=self.analyst,
            expected_output="Análise com insights e tendências principais",
            context=[research_task],
        )
        report_task = Task(
            description=f"Escreva um relatório executivo completo sobre {self.topic}.",
            agent=self.writer,
            expected_output="Relatório executivo em português com 3-5 páginas",
            context=[research_task, analysis_task],
        )
        crew = Crew(
            agents=[self.researcher, self.analyst, self.writer],
            tasks=[research_task, analysis_task, report_task],
            verbose=True,
        )
        return crew.kickoff()
