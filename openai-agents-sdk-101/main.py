from dotenv import load_dotenv

load_dotenv()

from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant who only answers questions related to Harry Potter.")

result = Runner.run_sync(agent, "Order top 20 wizards ordered by how powerful they are.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.