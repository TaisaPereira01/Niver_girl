import hmac
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).parent
VIDEO_PATH = BASE_DIR / "1ano.mp4"


st.set_page_config(
    page_title="1 ano de nós",
    page_icon="♡",
    layout="centered",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
    <style>
    :root {
        color-scheme: light;
    }

    .stApp {
        background:
            radial-gradient(circle at 12% 8%, rgba(255, 196, 196, 0.42), transparent 26rem),
            radial-gradient(circle at 90% 12%, rgba(168, 218, 220, 0.38), transparent 24rem),
            linear-gradient(135deg, #fff8f2 0%, #f7ece9 44%, #eef7f4 100%);
        color: #2f2526;
    }

    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stDecoration"] {
        display: none;
    }

    .block-container {
        max-width: 920px;
        padding: 3.4rem 1.2rem 2rem;
    }

    .intro {
        text-align: center;
        padding: 0.35rem 0 1.4rem;
    }

    .kicker {
        color: #8d5d5f;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 0;
        margin-bottom: 0.55rem;
        text-transform: uppercase;
    }

    h1 {
        color: #2f2526;
        font-family: Georgia, "Times New Roman", serif;
        font-size: clamp(2.35rem, 6vw, 4.3rem);
        line-height: 1;
        margin: 0 0 0.8rem;
        text-align: center;
    }

    .subtitle {
        color: #5d4d4e;
        font-size: 1.06rem;
        line-height: 1.7;
        margin: 0 auto;
        max-width: 680px;
        text-align: center;
    }

    .video-frame {
        background: rgba(255, 255, 255, 0.56);
        border: 1px solid rgba(119, 82, 83, 0.16);
        border-radius: 8px;
        box-shadow: 0 24px 70px rgba(76, 44, 48, 0.14);
        margin: 1.7rem auto 1.25rem;
        padding: 0.75rem;
    }

    video {
        border-radius: 6px;
        display: block;
        width: 100%;
    }

    .letter {
        color: #443738;
        font-size: 1.02rem;
        line-height: 1.8;
        margin: 1.7rem auto 0;
        max-width: 720px;
        text-align: center;
    }

    .footer-note {
        color: #7a6869;
        font-size: 0.9rem;
        margin-top: 2rem;
        text-align: center;
    }

    [data-testid="stTextInput"] input {
        border-radius: 8px;
    }

    .stButton > button {
        border-radius: 8px;
        font-weight: 700;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def get_secret(name: str, default: str = "") -> str:
    try:
        return str(st.secrets.get(name, default))
    except Exception:
        return default


def password_is_valid(password: str) -> bool:
    expected_password = get_secret("APP_PASSWORD")
    return bool(expected_password) and hmac.compare_digest(password, expected_password)


def show_login() -> None:
    st.markdown(
        """
        <div class="intro">
            <div class="kicker">acesso privado</div>
            <h1>1 ano de nós</h1>
            <p class="subtitle">
                Uma surpresa guardada com carinho. Coloque a senha para assistir.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("login_form"):
        password = st.text_input("Senha", type="password", label_visibility="collapsed")
        submitted = st.form_submit_button("Entrar")

    if submitted:
        if password_is_valid(password):
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Senha incorreta.")


def show_video() -> None:
    title = get_secret("PAGE_TITLE", "1 ano de nós")
    subtitle = get_secret(
        "PAGE_SUBTITLE",
        "Um pedacinho da nossa história, feito para guardar esse primeiro ano.",
    )
    letter = get_secret(
        "LOVE_NOTE",
        "Obrigado por cada riso, cada cuidado e cada lembrança que virou lar em mim.",
    )

    st.markdown(
        f"""
        <div class="intro">
            <div class="kicker">para assistir com calma</div>
            <h1>{title}</h1>
            <p class="subtitle">{subtitle}</p>
        </div>
        <div class="video-frame">
        """,
        unsafe_allow_html=True,
    )

    if VIDEO_PATH.exists():
        st.video(str(VIDEO_PATH))
    else:
        st.error("Não encontrei o arquivo de vídeo. Confirme se ele se chama 1ano.mp4.")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(f'<p class="letter">{letter}</p>', unsafe_allow_html=True)
    st.markdown('<p class="footer-note">feito com amor</p>', unsafe_allow_html=True)


if not st.session_state.get("authenticated"):
    show_login()
else:
    show_video()
