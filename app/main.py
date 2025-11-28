from fastapi import FastAPI, UploadFile, File, HTTPException
import whisper
import os
import uuid

app = FastAPI()

# Carga de modelos al iniciar
models = {}
try:
    models["small"] = whisper.load_model("small")
    models["medium"] = whisper.load_model("medium")
except Exception as e:
    print(f"Error al cargar un modelo de Whisper: {e}")

@app.post("/transcribe")
async def transcribe_audio(
    # Parámetro de consulta: se puede acceder a través de ?model_name=medium
    model_name: str = "small", 
    file: UploadFile = File(...)
):
    # Validar y seleccionar el modelo
    if model_name not in models:
        # Devuelve un código de estado 400 (Bad Request)
        raise HTTPException(
            status_code=400, 
            detail="Modelo no válido. Elija 'small' o 'medium'."
        )
    
    current_model = models[model_name]
    
    # Ruta temporal para guardar el archivo
    temp_name = f"/tmp/{uuid.uuid4()}_{file.filename}"

    try:
        # Guardar archivo temporalmente
        with open(temp_name, "wb") as f:
            # Esperar la lectura del archivo subido
            f.write(await file.read())

        # Transcribir usando el modelo seleccionado
        result = current_model.transcribe(temp_name)
        
        return {"text": result["text"]}

    finally:
        # Asegurarse de que el archivo temporal se borre, incluso si hay un error
        if os.path.exists(temp_name):
            os.remove(temp_name)
