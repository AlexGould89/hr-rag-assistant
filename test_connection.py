from dotenv import load_dotenv
load_dotenv()
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")
response = llm.invoke("Say hello and confirm you're working.")
print(response.content)