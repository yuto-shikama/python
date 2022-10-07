from fastapi import APIRouter

router = APIRouter()

@my_app.get("/getTest")
def getData():
    return [{
        "firstName":"Tanaka"
    },{
        "firstName":"Yamada"
    }]