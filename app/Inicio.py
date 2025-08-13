# app.py
import streamlit as st
from models.play_models import Jugador, Pregunta, BancoPreguntas, Juego
from data.play_questions import PREGUNTAS_POR_CATEGORIA

# ---------- Inicialización del estado ----------
if 'jugadores' not in st.session_state:
    st.session_state.jugadores = []

if 'juego' not in st.session_state:
    st.session_state.juego = None

if 'categoria_seleccionada' not in st.session_state:
    st.session_state.categoria_seleccionada = None

# ---------- Estilo general ----------
st.set_page_config(page_title="Juego de Preguntas 🎲", layout="centered")
st.title("🎲 Juego de Preguntas")
st.markdown("¡Bienvenido! Crea jugadores, selecciona una categoría (si quieres) y comienza a jugar.")

st.markdown("---")
st.markdown("Dale click al botón para registrar a los jugadores.")

if st.button("✅ Registrar jugadores"):
    st.switch_page("pages/1_Crear_Jugadores.py")


