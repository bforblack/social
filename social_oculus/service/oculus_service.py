from fastapi import FastAPI, Request, responses
from starlette import status

from processor import oculus_processor as oc
from processor import hub_service as hs
from pojos import Oculus_pojo as op
app=FastAPI()


@app.post("/register")
async def register_user(request:Request):
    data = await request.json()
    return responses.RedirectResponse('/'+op.Oculus(**data).registerUser(), status_code=status.HTTP_302_FOUND)


@app.get("/{id}")
async def get_user(id):
    return op.Oculus().get_user(id)



@app.post("/post/{id}/{object}")
async def post(id,object,request:Request):
    return op.Oculus().post_data(id,object,await request.json())


@app.post("{id}/report/")
@app.get("{id}/report/{Obeject}/{mediaId}")
async def report(id,Object,mediaId,request:Request):
    if(Object!=None):
        return op.Oculus().report(id,Object,mediaId=mediaId)
    else:
         return op.Oculus().report(id,object,request=await request.json())


@app.post("{id}/getPost/{Object}/{pageId}")
async def getPosts(id,Object,pageId):
    return op.Oculus().getPosts(id,Object,pageId)

