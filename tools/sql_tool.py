from langchain_core.tools import tool
from sqlalchemy import create_engine,text

DB_Url= "sqlite:///database/sample.db"


@tool
def sql_query(query:str)->str:
    """
    Execute Sql query on database.
    """

    try:
        engine = create_engine(DB_Url)
        with engine.connect() as conn:
            result = conn.execute(
                text(query)
            )

            rows = result.fetchall()

            return str(rows)
        
    except Exception as e:
        return str(e)
