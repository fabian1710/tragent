from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from tools.alpaca_market_tool import AlpacaMarketDataTool
from knowledge.trading_strategy import trading_strategy_source
# Uncomment the following line to use an example of a custom tool
# from trading_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool



@CrewBase
class TradingCrew():
	"""TradingCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@before_kickoff # Optional hook to be executed before the crew starts
	def pull_data_example(self, inputs):
		# Example of pulling data from an external API, dynamically changing the inputs
		inputs['extra_data'] = "This is extra data"
		return inputs

	@after_kickoff # Optional hook to be executed after the crew has finished
	def log_results(self, output):
		# Example of logging results, dynamically changing the output
		print(f"Results: {output}")
		return output

	@agent
	def market_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['market_analyst'],
			verbose=True, 
			tools=[AlpacaMarketDataTool()]
		)

	@agent
	def technical_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['technical_analyst'],
			verbose=True,
			tools=[AlpacaMarketDataTool()]
		)

	@agent
	def strategy_evaluator(self) -> Agent:
		return Agent(
			config=self.agents_config['strategy_evaluator'],
			verbose=True

		)

	@agent
	def risk_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['risk_manager'],
			verbose=True
		)	
  
	@task
	def market_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['market_analysis_task']
		)
  
	@task
	def technical_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['technical_analysis_task']
		)
  
	@task
	def strategy_evaluation_task(self) -> Task:
		return Task(
			config=self.tasks_config['strategy_evaluation_task']
		)
  
	@task
	def risk_assessment_task(self) -> Task:
		return Task(
			config=self.tasks_config['risk_assessment_task']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TradingCrew crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			knowledge={"sources": [trading_strategy_source], "metadata": {"trading_strategy": "simple"}}
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
