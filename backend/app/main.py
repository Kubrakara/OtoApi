from fastapi import FastAPI, UploadFile, File
from .parser import parse_openapi_file
from .test_runner import run_schemathesis_test


app = FastAPI()

@app.get("/")
def root():
    return {"message": "API Test Aracı Başladı!"}

@app.post("/upload-swagger/")
async def upload_swagger(file: UploadFile = File(...)):
    content = await file.read()
    parsed = parse_openapi_file(content)
    return parsed

@app.post("/test-swagger/")
async def test_swagger(file: UploadFile = File(...)):
    content = await file.read()
    result = run_schemathesis_test(content)
    return result

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Ali"}, {"id": 2, "name": "Ayşe"}]

@app.get("/users/{id}")
def get_user_by_id(id: int):
    return {"id": id, "name": f"Kullanıcı {id}"}


