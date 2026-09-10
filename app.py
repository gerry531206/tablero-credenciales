import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Configuración de la pantalla
st.set_page_config(page_title="Control Operativo", layout="wide")
st.title("Tablero de Seguimiento de Escuelas")

# 1. Establecer conexión con Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# REEMPLAZA ESTA URL POR LA DE TU GOOGLE SHEETS
URL_DE_TU_TABLA = "https://docs.google.com/spreadsheets/d/1Mmn2S1mpMSon-eF0Ue6PvP95hqy6cUqOdv3m3rhRsSo/edit?gid=0#gid=0"

try:
    # 2. Leer los datos de tu tabla
    df = conn.read(spreadsheet=URL_DE_TU_TABLA, usecols=None)
    
    st.write("Marca las casillas para actualizar el progreso:")
    
    # 3. Mostrar la tabla interactiva
    df_editado = st.data_editor(df, use_container_width=True)
    
    # 4. Botón para guardar cambios en la nube
    if st.button("Guardar Cambios"):
        conn.update(spreadsheet=URL_DE_TU_TABLA, data=df_editado)
        st.success("¡Datos actualizados correctamente en Google Sheets!")

except Exception as e:
    st.error(f"Hubo un error al conectar: {e}")