### Himel_Face_Detection
 
# install 
pip install fastapi pydantic uvicorn pytz


# Himel app 
------------
himel:
--------------------------

auth : ngrok config add-authtoken 2TmkpvbMuZyWWCpWF3kkmiKKepl_3UmLn9nGJygR2sGe6Be42

api : ngrok http --domain=https://caribou-neat-firstly.ngrok-free.app 80


api : ngrok tunnel --label edge=edghts_2WvHdrcQq10h0qzlBwK9gItS7Xy http://localhost:8000