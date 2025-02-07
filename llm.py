from langchain_openai import ChatOpenAI

def get_llm(API_KEY):

    llm = ChatOpenAI(model="gpt-4o",
                temperature=0.7, 
                api_key=API_KEY
                )
    return llm
