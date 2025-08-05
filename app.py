import uvicorn

if '__main__' == __name__:
    uvicorn.run('main:app', port=5050, log_level="info")