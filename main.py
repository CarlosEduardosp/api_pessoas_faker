from faker import Faker
from fastapi import FastAPI
from rotas import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(router=router)  # instanciando as rotas

# Configurar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Substitua pelo domínio do seu aplicativo, * para todos os dominios
    allow_credentials=True,
    allow_methods=["GET"],  # Você pode especificar métodos permitidos, como ["GET", "POST"]
    allow_headers=["Authorization"],  # Você pode especificar cabeçalhos permitidos, como ["Authorization"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

