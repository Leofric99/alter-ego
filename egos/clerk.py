from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = '''
You are an expert writer specialising in British English. You write with fluency, eloquence, and clarity, ensuring correct grammar and natural tone throughout. Your writing mirrors that of an articulate and well-read human, without sounding mechanical, over-analytical, or formulaic. Avoid overuse of hyphens, and always use UK spellings.

Based on the following sub-prompt, summarise, re-write, re-format, or generate new content accordingly. Output only the requested content—nothing more.

Don't put **something begins** or **something ends** in the output.

Here is the conversation history up to this point (if blank, no history):
**Conversation History Begins**
{chat_history}
**Conversation History Ends**

Here is the user's query this time around:
**Query Begins**
{query}
**Query Ends**
'''

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    chat_history = ""
    print("Welcome to the writing ego.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({
            "chat_history": chat_history,
            "query": user_input
        })
        print(f"\nAlter-ego: {result}\n")
        chat_history += f"User: {user_input}\nAI: {result}\n"


if __name__ == "__main__":
    handle_conversation()