
import streamlit as st
from models.play_models import Jugador, Pregunta, BancoPreguntas, Juego
from data.play_questions import PREGUNTAS_POR_CATEGORIA
from streamlit_extras.switch_page_button import switch_page  # Necesitarás este si usas extras

st.title("👥 Registro de jugadores")

if 'jugadores' not in st.session_state:
    st.session_state.jugadores = []

if 'juego' not in st.session_state:
    st.session_state.juego = None

if st.session_state.juego:
    st.success("Ya has iniciado el juego. Ve a la pestaña 🎮 Jugar.")
    st.stop()

num_jugadores = st.number_input("¿Cuántos jugadores?", min_value=2, max_value=20, step=1)
nombres = []

for i in range(num_jugadores):
    nombre = st.text_input(f"Nombre del jugador {i+1}", key=f"jugador_{i}")
    nombres.append(nombre)

if st.button("✅ Iniciar juego"):
    if all(nombres):
        jugadores = [Jugador(nombre) for nombre in nombres]
        st.session_state.jugadores = jugadores

        # Crear banco y agregar preguntas
        banco = BancoPreguntas()
        for categoria, preguntas in PREGUNTAS_POR_CATEGORIA.items():
            for texto in preguntas:
                banco.agregar(Pregunta(texto, categoria))

        # Crear juego
        st.session_state.juego = Juego(jugadores, banco)

        # 🔁 Redireccionar a página "2_🎮_Jugar"
        st.success("Juego iniciado 🎉. Redirigiendo a la pestaña 🎮 Jugar...")
        st.switch_page("pages/2_Jugar.py")  # 👉 Asegúrate de usar el nombre correcto
    else:
        st.warning("Por favor, completa todos los nombres.")
