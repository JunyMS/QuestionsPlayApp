# app.py
import streamlit as st
from play_models import Jugador, Pregunta, BancoPreguntas, Juego
from play_questions import PREGUNTAS_POR_CATEGORIA

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
st.markdown("¡Bienvenido! Crea jugadores, selecciona una categoría y comienza a jugar.")


# ---------- Paso 1: Crear jugadores ----------
if not st.session_state.jugadores and st.session_state.juego is None:
    st.subheader("👥 Registro de jugadores")
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
            st.success("Juego iniciado 🎉")
            st.rerun()  # 👈 Fuerza recarga tras inicializar el juego
        else:
            st.warning("Por favor, completa todos los nombres.")


# ---------- Paso 2: Jugar ----------
if st.session_state.juego:
    juego = st.session_state.juego
    st.subheader("🎮 Turno del juego")

    # Mostrar categorías
    categorias = juego.banco.categorias()
    categoria = st.selectbox("Elige una categoría (o dejalo vacío para seleccionar aleatoriamente):", [""] + categorias)

    # Botón para siguiente turno
    st.text("Presiona el botón 'Siguiente turno'")
    if st.button("🎯 Siguiente turno"):
        categoria_elegida = categoria if categoria != "" else None
        pregunta = juego.siguiente_turno(categoria_elegida)
        st.session_state.categoria_seleccionada = categoria_elegida

    # # Mostrar pregunta actual
    # if juego.ultima_pregunta:
    #     st.markdown("---")
    #     st.subheader("❓ Pregunta del turno")
    #     st.markdown(f"**Turno de:** {juego.jugador_actual.nombre}")
    #     st.markdown(f"**Pregunta para:** {juego.jugador_objetivo.nombre}")
    #     st.markdown(f"👉 *{juego.ultima_pregunta.texto}*")
    #     st.markdown(f"📚 Categoría: *{juego.ultima_pregunta.categoria}*")

    # Mostrar pregunta actual
    if juego.ultima_pregunta:
        st.markdown("---")
        st.subheader("❓ Pregunta del turno")

        col1, col2 = st.columns(2)

        with col1:
            st.write("🟢 **Pregunta de:**")
            st.code(juego.jugador_actual.nombre, language='')  # Muestra con estilo resaltado

        with col2:
            st.write("🔴 **Pregunta para:**")
            st.code(juego.jugador_objetivo.nombre, language='')  # Igual para el otro jugador

        # st.markdown("### 👉 Pregunta")
        # st.info(juego.ultima_pregunta.texto)  # Usamos un bloque de información para estilo
        st.markdown(f"### 👉 {juego.ultima_pregunta.texto}")

        st.markdown(f"📚 **Categoría:** *{juego.ultima_pregunta.categoria}*")



    # # Puntuaciones (en desarrollo)
    # st.markdown("---")
    # st.subheader("📊 Puntuaciones")
    # for jugador in juego.jugadores:
    #     st.markdown(f"- **{jugador.nombre}**: 0 puntos")  # Añade puntaje real si deseas

    # Botón para reiniciar
    if st.button("🔁 Reiniciar juego"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
