from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from Secret_code import cohere_key
from langchain_cohere.chat_models import ChatCohere
import os
os.environ['COHERE_API_KEY'] = "AQWILHeT6TLrmqR94NrY4xDqAZSwUp1MmjsSPqV8"


chat = ChatCohere(model="command-r-plus", temperature=0.3)

def J_I(cuisine):
    prompt_template_name = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
    )

    name_chain =LLMChain(llm=chat, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template="Suggest some menu items for {restaurant_name}."
    )

    food_items_chain =LLMChain(llm=chat, prompt=prompt_template_items, output_key="menu_items")

    from langchain.chains import SequentialChain

    chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name','menu_items']
    )

    response = chain({'cuisine':cuisine})
    return response

