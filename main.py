# uvicorn main:app --reload

import io
import numpy as np
import time

from fastapi import FastAPI, Depends, Path, Response, UploadFile
from PIL import Image
from sympy import isprime

from utils import get_current_username


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Succesful connection"}

@app.get("/prime/{number}")
async def prime(
    number: int = Path(title="Liczba do sprawdzenia", ge=0, lt=9223372036854775807)
):
    return {"isPrime": isprime(number)}

@app.post("/picture/invert")
async def invert(file: UploadFile):
    img = Image.open(file.file)

    img_arry = np.array(img)
    I_max = 255
    img_arry = I_max - img_arry
    inverted_image = Image.fromarray(img_arry)

    imgByteArr = io.BytesIO()
    inverted_image.save(imgByteArr, format=img.format)
    imgByteArr = imgByteArr.getvalue()

    return Response(content=imgByteArr, media_type="image/png")

@app.get("/currenttime")
def current_time(username: str = Depends(get_current_username)):
    return {"currenttime": time.strftime("%a, %d %b %Y %H:%M:%S %z", time.localtime())}


# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run("app.api:app", host="0.0.0.0", port=8080, reload=True)



# how to deploy python api for free
# https://wiki.python.org/moin/FreeHosts
# https://fastapi.tiangolo.com/deployment/concepts/

# https://www.youtube.com/watch?v=gVymPpepQco
# https://www.youtube.com/watch?v=SgSnz7kW-Ko
# https://www.youtube.com/watch?v=L0aXq0BEjbI

# https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-with-fastapi-docker-and-github-actions-13374cbd638a
# https://testdriven.io/blog/fastapi-machine-learning/

# https://towardsdatascience.com/step-by-step-approach-to-build-your-machine-learning-api-using-fast-api-21bd32f2bbdb