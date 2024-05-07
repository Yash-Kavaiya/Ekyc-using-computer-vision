import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.tools.google_jobs import GoogleJobsQueryRun
from langchain_community.utilities.google_jobs import GoogleJobsAPIWrapper
from langchain.agents import AgentType, initialize_agent, load_tools

os.environ["SERPAPI_API_KEY"]=""

api_key = ""
tool = GoogleJobsQueryRun(api_wrapper=GoogleJobsAPIWrapper())
tool.run("Can I get an entry level job posting related to AI Engineer")
llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)
tools = load_tools(["google-jobs"], llm=llm)
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
jobsss= agent.run("give me an 2 entry level job posting related to  AI and Data Science")
print("jobsss")
print(type(jobsss))
print(jobsss)