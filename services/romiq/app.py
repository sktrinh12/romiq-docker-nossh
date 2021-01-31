from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from typing import Optional
from functions import *
# from concurrent.futures import ThreadPoolExecutor, as_completed
import socket
import uvicorn

app = FastAPI()


@app.get("/run/{script_name}/{barcode}")
async def runOmiq(script_name: str, barcode: str, background_tasks: BackgroundTasks, re_run: Optional[str] = 'false'):
    # print(f'barcode: {barcode}')
    # print(f'script_name: {script_name}')
    if not validate_barcode(barcode):
        raise HTTPException(status_code=404, detail='Barcode does not have correct date format prefix')
    output = {'barcode' : barcode, 'script_name' : script_name }
    if re_run:
        # print(f're_run: {re_run}')
        output.update({'re_run' : re_run})
    # processes = []
    # with ThreadPoolExecutor(max_workers=2) as TPExc:
    #     TPExc.submit(run_Rscript, script_name, barcode=barcode, re_run=re_run)
        # processes.append(TPExc.submit(run_Rscript, script_name, barcode=barcode))
        # for _ in as_completed(processes):
        #     output.append(_.result())
    background_tasks.add_task(run_Rscript, script_name, barcode=barcode, re_run=re_run)
    return output


@app.get("/")
def home():
    return {"ping" : f"from server: {socket.gethostname()}"}


if __name__ == "__main__":
    uvicorn.run('app:app', port=5000, host='0.0.0.0', reload=True)
