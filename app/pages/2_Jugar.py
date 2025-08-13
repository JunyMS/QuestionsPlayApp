import streamlit as st

st.title("🎮 Jugar")

if 'juego' not in st.session_state or st.session_state.juego is None:
    st.warning("Primero debes crear a los jugadores en la pestaña '👥 Crear jugadores'.")
    st.stop()

# ---------- Paso 2: Jugar ----------
if st.session_state.juego:
    juego = st.session_state.juego
    st.subheader("🎮 Turno del juego")

    # Mostrar categorías
    categorias = juego.banco.categorias()
    categoria = st.selectbox("Elige una categoría (o dejalo vacío para seleccionar aleatoriamente):", [""] + categorias)

    # Botón para siguiente turno
    st.text("Presiona el botón 'Comenzar Juego'")
    if st.button("🎯 Comenzar Juego"):
        categoria_elegida = categoria if categoria != "" else None
        pregunta = juego.siguiente_turno(categoria_elegida)
        st.session_state.categoria_seleccionada = categoria_elegida

    # Mostrar pregunta actual
    if juego.ultima_pregunta:
        st.markdown("---")
        st.subheader(f"❓ Pregunta para {juego.jugador_actual.nombre}")
        # st.markdown(f"Turno de: ")
        # st.subheader(f"{juego.jugador_actual.nombre}")

        st.markdown(f"### 👉 {juego.ultima_pregunta.texto}")

        st.markdown(f"📚 **Categoría:** *{juego.ultima_pregunta.categoria}*")
    
    if juego.ultima_pregunta:
        if st.button("✅ Respondido"):
            categoria_elegida = categoria if categoria != "" else None
            pregunta = juego.siguiente_turno(categoria_elegida)
            st.session_state.categoria_seleccionada = categoria_elegida
            st.rerun()


    # Botón para reiniciar
    if st.button("🔁 Reiniciar juego"):
        for key in st.session_state.keys():
            del st.session_state[key]
        # st.rerun()
        st.switch_page("pages/1_Crear_Jugadores.py")