import asyncio
import pandas as pd
from teamData import *
import json

async def detect_object(model, url):
    model.conf = 0.8
    result = await asyncio.get_event_loop().run_in_executor(None, model, url)
    result = result.pandas().xyxy[0]
    df = pd.DataFrame(result)
    name_counts = df.groupby('name').size().to_dict()
    # print("na" , name_counts)
    re = {}

    a = len(name_counts)
    
    if a <= 0:
        d = {"AI":"Not Found"}
        re.update(d)
    else:   
        for item in name_counts:
            if item in member_details:
                info = member_details[item]
                d = {item:info}
            elif len(name_counts)==0:
                detect = {item:"Not Found"}
                d = json.dumps(detect)
            re.update(d)
            print(re)
    return re