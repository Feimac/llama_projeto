#!/usr/bin/env bash
#
# Script de instalação das dependências necessárias:
# - Verificação/Instalação de Python3 e pip
# - Tesseract OCR (com pacotes de idioma, ex.: português)
# - Bibliotecas Python via pip (streamlit, pillow, pytesseract, ollama)
#
# Uso:
#   1. chmod +x install.sh
#   2. ./install.sh

# -----------------------------
# Verificar/Instalar Python 3
# -----------------------------
if ! command -v python3 &> /dev/null
then
    echo "🔍 Python3 não encontrado. Instalando..."
    sudo apt-get update -y
    sudo apt-get install -y python3
else
    echo "✅ Python3 já está instalado."
fi

# -----------------------------
# Verificar/Instalar pip3
# -----------------------------
if ! command -v pip3 &> /dev/null
then
    echo "🔍 pip3 não encontrado. Instalando..."
    sudo apt-get update -y
    sudo apt-get install -y python3-pip
else
    echo "✅ pip3 já está instalado."
fi

# -----------------------------
# Instalar Tesseract (OCR) e pacotes de idioma
# -----------------------------
echo "🔍 Instalando Tesseract OCR (pacote principal + português)..."
sudo apt-get update -y
sudo apt-get install -y tesseract-ocr tesseract-ocr-por libtesseract-dev

# -----------------------------
# Instalar bibliotecas Python necessárias
# -----------------------------
echo "🐍 Instalando bibliotecas Python: streamlit, pillow, pytesseract, ollama..."
pip3 install --upgrade pip setuptools wheel
pip3 install streamlit pillow pytesseract ollama

# -----------------------------
# Mensagem de conclusão
# -----------------------------
echo ""
echo "✅ Instalação concluída!"
echo "    - Python3 e pip3 garantidos."
echo "    - Tesseract instalado (com idioma por)."
echo "    - Bibliotecas Python instaladas (streamlit, pillow, pytesseract, ollama)."
echo ""
echo "Para executar a aplicação Streamlit, use o comando:"
echo "  streamlit run dashboard_llama.py"


