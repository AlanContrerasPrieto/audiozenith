# Funciones para procesar archivos de audio a texto y de texto a audio.
def saludo():
    print("Hola desde audio.py")

def transcribe_audio(audio_path):
    try:
        # Verificar si el archivo de audio existe
        if not os.path.exists(audio_path):
            print(f"Archivo de audio no encontrado: {audio_path}")
            return ''

        # Transcribir el audio
        result = model.transcribe(audio_path, fp16=False)
        text = result['text']

        print(f"Audio transcrito: {audio_path}")
        print(f"Texto: {text}")
        return text
    except Exception as e:
        print(f"Error al transcribir el audio {audio_path}: {e}")
        return ''

#pip install git+https://github.com/openai/whisper.git
#pip install torch
import os
import whisper

model = whisper.load_model("base")

import os

path_a_probar = r"C:\Users\Alan Contreras P\Documents\1-escuela\Profe\7_semestre\IA 2\Reto\audio\audios\ad1.wav"
path_a_probar = "ad1.wav"

if os.path.exists(path_a_probar):
    print("¡ÉXITO! La ruta es correcta. El archivo existe.")
else:
    print("¡ERROR DE RUTA! El archivo NO se encontró en esa ubicación.")
    print("Verifica si copiaste la ruta correctamente o si el archivo 'ad1.wav' está en esa carpeta.")

audio_file_path = "ad1.wav"
transcription = transcribe_audio(audio_file_path)
print(transcription)