from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CreateCrewProject():
	"""CreateCrewProject crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def product_owner(self) -> Agent:
		return Agent(
			config=self.agents_config['product_owner'],
			verbose=True
		)

	@agent
	def desenvolvedor_de_agentes(self) -> Agent:
		return Agent(
			config=self.agents_config['desenvolvedor_de_agentes'],
			verbose=True
		)

	@agent
	def desenvolvedor_de_tarefas(self) -> Agent:
		return Agent(
			config=self.agents_config['desenvolvedor_de_tarefas'],
			verbose=True
		)

	@agent
	def desenvolvedor_de_orquestracao(self) -> Agent:
		return Agent(
			config=self.agents_config['desenvolvedor_de_orquestracao'],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def definir_requisitos(self) -> Task:
		return Task(
			config=self.tasks_config['definir_requisitos']
		)

	@task
	def especificar_agentes(self) -> Task:
		return Task(
			config=self.tasks_config['especificar_agentes']
		)

	@task
	def definir_tarefas(self) -> Task:
		return Task(
			config=self.tasks_config['definir_tarefas']
		)

	@task
	def orquestrar_sistema(self) -> Task:
		return Task(
			config=self.tasks_config['orquestrar_sistema']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CreateCrewProject crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
