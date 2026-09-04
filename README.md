# Video privado de 1 ano

Este projeto cria uma pagina Streamlit simples, com senha, para assistir ao video `1ano.mp4`.

## Testar no computador

1. Abra esta pasta no terminal.
2. Rode:

```powershell
.venv\Scripts\python.exe -m streamlit run app.py
```

3. Acesse o endereco mostrado pelo Streamlit.
4. A senha inicial esta em `.streamlit/secrets.toml`.

## Trocar a senha

Edite `.streamlit/secrets.toml`:

```toml
APP_PASSWORD = "sua-senha-aqui"
PAGE_TITLE = "1 ano de nós"
PAGE_SUBTITLE = "Um pedacinho da nossa história, feito para guardar esse primeiro ano."
LOVE_NOTE = "Obrigado por cada riso, cada cuidado e cada lembrança que virou lar em mim."
```

O arquivo `.streamlit/secrets.toml` esta no `.gitignore` para nao ir para o GitHub.

## Publicar com privacidade

O caminho recomendado:

1. Crie um repositorio privado no GitHub.
2. Envie `app.py`, `requirements.txt`, `README.md`, `.gitignore`, `.streamlit/secrets.example.toml` e `1ano.mp4`.
3. No Streamlit Community Cloud, crie um app a partir desse repositorio privado.
4. Em "Secrets", cadastre os mesmos valores do `secrets.toml`, principalmente `APP_PASSWORD`.
5. Em "Sharing", deixe o app privado e convide apenas o e-mail da pessoa que deve assistir.

Mesmo com senha, um video exibido no navegador pode ser gravado por quem tem acesso. A privacidade aqui serve para limitar quem consegue abrir a pagina.
