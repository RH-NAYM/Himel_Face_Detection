from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from typing import List, Union
from team_main import *
from teamData import *
import uvicorn


app = FastAPI()
class item(BaseModel):
    url:str

# @app.post("/tech")
# async def create_items(item: item):
#     try:
#         rrr = await detect_object(teamModel,item.url)
#         return rrr
#     finally:
#         pass


async def process_item(item: item):
    try:
        rrr = await detect_object(teamModel,item.url)
        return rrr
    finally:
        torch.cuda.empty_cache()
        pass

async def process_items(items: Union[item, List[item]]):
    print(type(items))
    if type(items)==list:
        coroutines = [process_item(item) for item in items]
        results = await asyncio.gather(*coroutines)
        # print("multi : ",results)
    else:
        results = await process_item(items)
        # print("single : ", results)
    return results



@app.get("/status")
async def status():
    return "AI Server in running"

@app.post("/tech")
async def create_items(items: Union[item, List[item]]):
    try:
        print(items)
        results = await process_items(items)
        print("Result Sent to User:", results)
        print("###################################################################################################")
        print(items)
        return results
    finally:
        torch.cuda.empty_cache()
        pass

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="127.0.0.1", port=8000)
    finally:
        torch.cuda.empty_cache()
