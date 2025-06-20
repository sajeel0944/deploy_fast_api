from fastapi import FastAPI, Query

app = FastAPI()

from agents import Runner, Agent, set_tracing_disabled, ItemHelpers, function_tool
from dotenv import load_dotenv
from agents.extensions.models.litellm_model import LitellmModel
from openai.types.responses import ResponseTextDeltaEvent
import os
import litellm
import warnings
import asyncio





#-------------------------------------------------------------------------------------

set_tracing_disabled(disabled=True)
# enable_verbose_stdout_logging()

# 🔕 output main litellm ki kuch warning arahe thi is sy warning nhi aye gi
litellm.disable_aiohttp_transport=True

# 🔕 output main pydantic ki kuch warning arahe thi is sy warning nhi aye gi
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    message="Pydantic serializer warnings"
)

set_tracing_disabled(disabled=True)
# .env file load karo
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL = "gemini/gemini-1.5-flash"


#                                   streaming Text code


agent = Agent(
    name = "agent",
    instructions="my are help full agent",
    model=LitellmModel(model=MODEL, api_key=OPENAI_API_KEY)
)

# AI endpoint
@app.post("/ai")
async def ai_agent(prompt: str = Query(..., description="Prompt from user")):
    try:
        result = await  Runner.run(agent, prompt)
        return {"ai": result.final_output}
    except Exception as e:
        return {"error": str(e)}


# @app.post("/post")
# def hello_word():
#     """Basic root endpoint"""
#     return {"message": "this is post request"}
