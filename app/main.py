import subprocess
import threading
import time
from dotenv import load_dotenv

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger=get_logger(__name__)

load_dotenv()

def run_backend():
    try:
        logger.info("Starting backend service..")
        subprocess.run(["uvicorn","app.backend.api:app", "--host", "127.0.0.1", "--port", "9999"], check=True)
    except Exception as e:
        logger.error("Problem with backend service")
        raise CustomException("Failed to start backend", e)
    

def run_frontend():
    try:
        logger.info("Starting frontend service")
        subprocess.run(["streamlit", "run", "app/frontend/ui.py"],check=True)
    except Exception as e:
        logger.error("Problem with frontend service")
        raise CustomException("Failed to start frontend", e)
    

#Now we have to merge the frontend and the backend:


if __name__ == "__main__": # This mains if someone runs this file, whatever inside the file is gets triggered.

    try:
        threading.Thread(target=run_backend).start()
        time.sleep(2)  #Give the backend some time to start

        run_frontend()

    except Exception as e:
        logger.exception(f"CustomException occurred : {str(e)}")









