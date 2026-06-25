from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

response = llm.invoke("What is 100*5?")
print(response.content)