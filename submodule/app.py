import uvicorn
import api as api

if __name__ == "__main__":
    uvicorn.run('api:app', host='0.0.0.0', port=5050, log_level="INFO")