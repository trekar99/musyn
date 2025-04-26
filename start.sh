#!/bin/bash

# ANSI Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Variables
SETUP_FILE="setup.py"

URL_MUSIC2TXT_MODEL="https://huggingface.co/seungheondoh/lp-music-caps/resolve/main/transfer.pth" 
URL_TXT2IMG_MODEL="https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sd_xl_turbo_1.0_fp16.safetensors"

MUSIC2TXT_MODEL="lpmusiccaps.pth" 
TXT2IMG_MODEL="sdxlturbo.safetensors"

OUTPUT_DIR="assets/models"


# Installation with pip
echo -e "${YELLOW}Starting packages installation...${NC}"
if [ -f "$SETUP_FILE" ]; then
  pip install -e . -q
  if [ $? -eq 0 ]; then
    echo -e "${GREEN}Package installed successfully.${NC}"
  else
    echo -e "${RED}Error installing the package.${NC}"
  fi
else
  echo -e "${RED}Error: File $SETUP_FILE not found.${NC}"
fi

echo "" # Empty line for better readability

# Download with wget if the models does not exist
echo -e "${YELLOW}Checking and creating the download directory if needed...${NC}"
mkdir -p "$OUTPUT_DIR"

echo -e "${YELLOW}Checking if $MUSIC2TXT_MODEL already exists...${NC}"
if [ ! -f "$MUSIC2TXT_MODEL" ]; then
  echo -e "${YELLOW}Starting file download...${NC}"
  wget "$URL_MUSIC2TXT_MODEL" -O "$OUTPUT_DIR/$MUSIC2TXT_MODEL" -nv
  if [ $? -eq 0 ]; then
    echo -e "${GREEN}File downloaded successfully as $MUSIC2TXT_MODEL.${NC}"
  else
    echo -e "${RED}Error downloading the file from $URL_MUSIC2TXT_MODEL.${NC}"
  fi
else
  echo -e "${YELLOW}The file $MUSIC2TXT_MODEL already exists. Skipping download.${NC}"
fi

echo -e "${YELLOW}Checking if $TXT2IMG_MODEL already exists...${NC}"
if [ ! -f "$TXT2IMG_MODEL" ]; then
  echo -e "${YELLOW}Starting file download...${NC}"
  wget "$URL_TXT2IMG_MODEL" -O "$OUTPUT_DIR/$TXT2IMG_MODEL" -nv
  if [ $? -eq 0 ]; then
    echo -e "${GREEN}File downloaded successfully as $TXT2IMG_MODEL.${NC}"
  else
    echo -e "${RED}Error downloading the file from $URL_TXT2IMG_MODEL.${NC}"
  fi
else
  echo -e "${YELLOW}The file $TXT2IMG_MODEL already exists. Skipping download.${NC}"
fi

echo -e "${YELLOW}Script finished.${NC}"
