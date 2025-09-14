from fastapi import FastAPI,HTTPException  
from pydantic import BaseModel
from typing import List 
from app.core.ai_agent import get_response_from_ai_agents
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException #Adding the Custom Exception..

logger =   get_logger(__name__)

#Now we will initialize the FastAPI app.
app = FastAPI(title="MUlTI AI AGENT")

class RequestState(BaseModel):
    model_name:str
    system_prompt:str
    messages:List[str] #The messages will be in a list.
    allow_search:bool

@app.post("/chat")
def chat_endpoint(request:RequestState):  
    logger.info(f"Received request for model: {request.model_name}")

    if request.model_name not in settings.ALLOWED_MODEL_NAMES:
        logger.warning("Invalid model name")
        raise HTTPException(status_code=400, detail="Invalid model name")
    try:
        response = get_response_from_ai_agents(
            request.model_name,
            request.messages,
            request.allow_search,
            request.system_prompt
        )

        logger.info(f"Successfully got response from AI Agent {request.model_name}")

        #Now return our response as below:

        return {"response" : response}
    
    except Exception as e:
        logger.error("Some error occurred during response generation")

        raise HTTPException(status_code=500, detail=str(CustomException("Failed to get AI Response",error_detail=e)))
    

    
#500 error is the fail API message.




#The HTTP exception is used to handle the exception related to the API.
#The pydantic is used to validate the structure of incoming data.




