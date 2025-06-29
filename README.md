
# Llama Projeto

Um dashboard web em **Streamlit** que permite:

- Capturar ou fazer upload de imagens.
- Aplicar filtros básicos de tratamento (brilho, contraste e nitidez).
- Extrair texto de imagens via **Tesseract OCR**.
- Enviar prompts para um modelo **Llama** (via API Ollama) e exibir respostas.
- Fazer download da imagem tratada ou do texto extraído.

---

## 🛠 Pré-requisitos

1. **Python 3.8+**  
2. **Tesseract OCR** instalado no sistema  
   - No Ubuntu/Debian:  
     ```bash
     sudo apt update && sudo apt install tesseract-ocr libtesseract-dev
     ```
   - No macOS (via Homebrew):  
     ```bash
     brew install tesseract
     ```
3. **Git** (para clonar o repositório)  

---

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/llama_projeto.git
   cd llama_projeto
````

2. Execute o script de instalação das dependências:

   ```bash
   bash install.sh
   ```

   Esse script deve criar um ambiente virtual e instalar:

   * `streamlit`
   * `pillow`
   * `pytesseract`
   * `ollama`
   * entre outras bibliotecas listadas em `requirements.txt`.

3. Ative o ambiente virtual (se não for ativado automaticamente):

   ```bash
   source .venv/bin/activate
   ```

---

## 🔧 Configuração

Este app usa a variável de ambiente `OLLAMA_API_URL` para conectar-se ao servidor Ollama:

```bash
export OLLAMA_API_URL="http://<SEU_HOST>:5000/api/generate"
```

Você pode opcionalmente ajustar:

* `MODEL_LLM` — modelo LLM a ser usado (padrão `llama3.2`).
* `MODEL_EMBEDDING` — modelo de embeddings, se aplicável.

---

## ▶️ Execução

No diretório do projeto, com o ambiente virtual ativo:

```bash
streamlit run dashboard_llama.py
```

Isso iniciará um servidor local (normalmente em [http://localhost:8501](http://localhost:8501)). Abra essa URL no seu navegador.

---

## 🚀 Como usar

1. **Upload** ou **captura** de imagem pelo widget de câmera.
2. Ajuste brilho, contraste e nitidez pelos controles na barra lateral.
3. Clique em **Extrair texto** para obter o OCR da imagem.
4. Digite seu prompt para o Llama e veja a resposta.
5. Faça **download** da imagem tratada ou do texto extraído, quando desejar.

---

## 🤝 Contribuição

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-coisa`).
3. Faça commits das suas alterações (`git commit -m "Adiciona nova coisa"`).
4. Envie para o seu fork (`git push origin feature/nova-coisa`).
5. Abra um Pull Request aqui.

---

## 📄 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---



> **Observação:**  
> - Se o script `install.sh` não cobrir alguma dependência do seu sistema (por exemplo, bibliotecas nativas para o Tesseract), instale-as manualmente conforme o seu SO.  
> - Ajuste URLs e nomes de variáveis conforme suas necessidades.

