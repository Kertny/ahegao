import uvicorn
import logging

log = logging.getLogger()

if __name__ == '__main__':
    uvicorn.run('api:app', port=5050, log_level="info")
    log.warning("application stoped")
