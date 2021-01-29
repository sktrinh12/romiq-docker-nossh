from fastapi import FastAPI, Request, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from functions import *
from concurrent.futures import ThreadPoolExecutor
import socket
import uvicorn

executor = ThreadPoolExecutor(2)
app = FastAPI()


@app.get("/run/{script_name}/{barcode}")
async def runOmiq(script_name: str, barcode: str, re_run: Optional[str] = 'false'):
    # print(f'barcode: {barcode}')
    # print(f'script_name: {script_name}')
    output = {'barcode' : barcode, 'script_name' : script_name }
    if re_run:
        # print(f're_run: {re_run}')
        output.update({'re_run' : re_run})
    executor.submit(run_Rscript, script_name, barcode=barcode, re_run=re_run)
    return output


@app.get("/")
def home():
    return {"ping" : f"from server: {socket.gethostbyname(socket.gethostname())}"}


if __name__ == "__main__":
    uvicorn.run('app:app', port=5000, host='0.0.0.0', reload=True)
