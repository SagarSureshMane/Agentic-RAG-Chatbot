from langchain_core.tools import tool
import wikipedia

@tool
def wikipedia_search(query:str) ->str:
   """
     search wikipedia
   """
   try:
      return wikipedia.summary(
         query,
         sentences=5
      )
   except Exception as e:
      return str(e)