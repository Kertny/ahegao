import uvicorn
import logging
import socket

log = logging.getLogger()

if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())

    uvicorn.run('api:app', host=host, port=5050, log_level="info")
    log.warning("application stoped")
