#!/bin/bash

# Variables
SETUP_FILE="setup.py"
DOWNLOAD_URL="https://huggingface.co/seungheondoh/lp-music-caps/resolve/main/transfer.pth" 
OUTPUT_FILE="model.pth" 

# Instalación con pip
echo "Iniciando la instalación de los paquetes..."
if [ -f "$SETUP_FILE" ]; then
  pip install -e . -q
  if [ $? -eq 0 ]; then
    echo "Paquetes instalados correctamente."
  else
    echo "Error al instalar los paquetes."
  fi
else
  echo "No se encontró el archivo $SETUP_FILE."
fi

echo "" # Línea en blanco para mejor legibilidad

# Descarga con wget
echo "Iniciando la descarga del archivo..."
wget "$DOWNLOAD_URL" -O "$OUTPUT_FILE" -nv
if [ $? -eq 0 ]; then
  echo "Archivo descargado correctamente como $OUTPUT_FILE."
else
  echo "Error al descargar el archivo desde $DOWNLOAD_URL."
fi

echo "Script finalizado."