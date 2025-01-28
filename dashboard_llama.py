import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import io
import logging
import ollama

# ----------------------------------------------------------------------
# Configurações Iniciais
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="LLaMA Vision Analyzer",
    page_icon="🔍",
    layout="wide"
)

# Configuração de logs (opcional)
logging.basicConfig(level=logging.INFO)

# ----------------------------------------------------------------------
# Funções de Processamento
# ----------------------------------------------------------------------
def process_image(image_bytes: bytes, lang="por"):
    """
    Processa a imagem e realiza OCR para extrair texto.
    """
    try:
        # Abrir a imagem
        image = Image.open(io.BytesIO(image_bytes))
        logging.info("Imagem carregada com sucesso.")

        # Etapas de pré-processamento
        image = image.convert("L")  # Converter para escala de cinza
        logging.info("Imagem convertida para escala de cinza.")

        image = image.filter(ImageFilter.SHARPEN)  # Melhorar a nitidez
        logging.info("Nitidez aplicada à imagem.")

        enhancer = ImageEnhance.Contrast(image)  # Ajustar o contraste
        image = enhancer.enhance(2.0)
        logging.info("Contraste ajustado na imagem.")

        # Executar OCR com configurações otimizadas
        config = "--psm 6"  # Configuração para supor um bloco único de texto
        extracted_text = pytesseract.image_to_string(image, lang=lang, config=config)

        logging.info(f"Texto extraído da imagem: {extracted_text}")
        return extracted_text.strip()

    except Exception as e:
        logging.error(f"Erro ao processar imagem com OCR: {e}")
        st.error("Erro ao processar a imagem. Verifique se o arquivo está correto.")
        return ""

def generate_response_with_llama(extracted_text: str):
    """
    Gera uma resposta usando o modelo LLaMA via Ollama.
    """
    try:
        # Estruturar o prompt
        modified_prompt = f"""
        Você é um assistente treinado para analisar textos extraídos de imagens.

        Aqui está o texto extraído:
        {extracted_text}

        Sua tarefa:
        1. Identificar informações relevantes no texto.
        2. Fornecer possíveis interpretações ou temas relacionados.

        Por favor, responda com clareza e objetividade.
        """

        # Configurar a mensagem para o Ollama
        messages = [{'role': 'user', 'content': modified_prompt}]
        
        # Aqui, ajustamos o nome do modelo e outras configurações conforme necessidade
        # Certifique-se de que seu Ollama está instalado, configurado e com o modelo disponível
        response = ollama.chat(
            model="llama3.2:3b",  # Exemplo de modelo (ajuste de acordo com o que você tem)
            messages=messages
        )
        
        # Dependendo da versão, o retorno pode variar. Ajuste para acessar o conteúdo da resposta corretamente.
        content = response["message"]["content"] if "message" in response else response.get("content", "")
        
        return content.strip()

    except Exception as e:
        logging.error(f"Erro ao gerar resposta com LLaMA: {e}")
        st.error(f"Erro ao consultar o modelo LLaMA: {e}")
        return ""

def analisar_imagem(uploaded_file):
    """
    Processa a imagem enviada (OCR) e gera a resposta (LLaMA) localmente.
    """
    if uploaded_file is not None:
        # Ler bytes da imagem
        image_bytes = uploaded_file.getvalue()

        # Realizar OCR
        ocr_text = process_image(image_bytes, lang="por")

        if ocr_text:
            # Gerar resposta usando LLaMA via Ollama
            llama_response = generate_response_with_llama(ocr_text)

            # Exibir resultado
            st.success("✅ Análise concluída com sucesso!")
            with st.expander("📝 Ver Resposta Detalhada", expanded=True):
                st.markdown(f'<div class="response-box">{llama_response}</div>', unsafe_allow_html=True)
        else:
            st.warning("Não foi possível extrair texto da imagem.")
    else:
        st.warning("Nenhuma imagem selecionada.")


# ----------------------------------------------------------------------
# Layout da Aplicação
# ----------------------------------------------------------------------
def main():
    # CSS Personalizado
    st.markdown(
        """
        <style>
        .main {background-color: #f9f9f9;}
        .header {padding: 2rem 0px 2rem;}
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .response-box {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Cabeçalho
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title("🔍 LLaMA Vision Analyzer")
    st.markdown("**Transforme imagens em insights** - Envie uma imagem contendo texto para análise avançada")
    st.markdown('</div>', unsafe_allow_html=True)

    # Divisão em colunas
    col1, col2 = st.columns([2, 3], gap="large")

    with col1:
        st.subheader("📤 Upload de Imagem")
        uploaded_file = st.file_uploader(
            "Selecione uma imagem (PNG, JPG, JPEG):",
            type=["png", "jpg", "jpeg"],
            label_visibility="collapsed"
        )

    with col2:
        if uploaded_file:
            st.subheader("🖼️ Pré-visualização")
            img = Image.open(uploaded_file)
            st.image(img, caption="Imagem selecionada", width=400)

            if st.button("🔍 Analisar Imagem", type="primary", use_container_width=True):
                with st.spinner("Processando... Isso pode levar alguns segundos"):
                    analisar_imagem(uploaded_file)
        else:
            st.info("ℹ️ Selecione uma imagem à esquerda para começar a análise")

    # Seção de ajuda
    with st.expander("❓ Como usar", expanded=False):
        st.markdown("""
        **Guia Rápido:**
        1. Selecione uma imagem contendo texto usando o painel esquerdo
        2. Verifique a pré-visualização da imagem
        3. Clique no botão 'Analisar Imagem'
        4. Aguarde o processamento e visualize os resultados

        **Requisitos:**
        - Formatos suportados: PNG, JPG, JPEG
        - Tamanho máximo recomendado: 5MB
        - O texto na imagem deve estar legível e em orientação preferencialmente horizontal
        - É necessário ter o Tesseract instalado e configurado
        - É necessário ter o Ollama instalado e com o modelo LLaMA desejado disponível
        """)

    # Rodapé
    st.markdown("---")
    st.caption("Desenvolvido por Felipe Snitynski Camillo para o projeto de extensão Engenharia de Prompt- © 2025 LLaMA Vision Analyzer v1.3")


if __name__ == "__main__":
    main()

