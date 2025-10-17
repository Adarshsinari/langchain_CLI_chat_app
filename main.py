import os
from secret import OAI_KEY, SERP_API_KEY
os.environ["OPENAI_API_KEY"] = OAI_KEY
os.environ["SERPAPI_API_KEY"] = SERP_API_KEY
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain_community.utilities import SerpAPIWrapper

lang_model = OpenAI(temperature=0)

text = "what would be a good company name for a company that makes colourful socks?"

# print(llm(text))


prompt_llm = PromptTemplate(
    input_variables=["product"],
    template = "what would be a good company name for a company that makes {product}?"
)

# print(prompt.format(product="colourful socks"))

# chain = LLMChain(prompt=prompt_llm, llm=lang_model)

# print(chain.run(product="colourful socks"))

search = SerpAPIWrapper()

print(search.run("Who is the current best test player?"))