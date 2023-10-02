from fastapi import FastAPI, Request, responses
from service_layers import oculus as op
from entity_layer import register

app = FastAPI()


@app.post("/register")
async def register_user(request: Request):
    data = await request.json()
    return op.Oculus(**data).registerUser()


@app.post("/registration")
async def register_user(request: Request):
    data = await request.json()
    return register.User(**data).process_user_registration()



@app.post("/add_platform")
async def register_user(request: Request):
    data = await request.json()
    return register.Media(**data).process_media_registration()



@app.get("/{id}")
async def getUserById(id):
    return op.Oculus(registrationId=id).getUserById(id)


@app.get("/posts/{id}")
async def allpost(id, request: Request):
    return op.Oculus().getpostDetails(id, **await request.json())


@app.post("/create/{id}")
async def create_post(id, request: Request):
    return op.Oculus().createPost(id, **await request.json())

# get all the post of a particular media Page

# @app.get("/posts/{id}")
# async def allpost(id,request:Request):
#     return op.Oculus().getpostDetails(id, request=await request.json())


#
# @app.post("/createPost/{id}")
# async def createPost(id,request:Request):
#     return op.Oculus().postData(id,await request.json())
#
#
# @app.get("/report/{id}")
# async def report(id,request:Request):
#     return op.Oculus().analytics(id,await request.json())


# @app.post("/post/{id}/{object}")
# async def post(id,object,request:Request):
#     return op.Oculus().post_data(id,object,await request.json())


# @app.get("/post/{id}")
# async def report(id,request:Request):
#     return op.Oculus().singlePostDetails(id,await request.json())


#
# @app.post("{id}/getPost/{Object}/{pageId}")
# async de f getPosts(id,Object,pageId):
#     return op.Oculus().getPosts(id,Object,pageId)
