import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Configuración de los scopes necesarios
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",  # Acceso a Google Sheets
    "https://www.googleapis.com/auth/drive"         # Acceso a Google Drive
]

# Configuración de las credenciales
ruta_credenciales = "config/credenciales.json"  # Cambiar según la ubicación del archivo
credentials = Credentials.from_service_account_file(ruta_credenciales, scopes=SCOPES)
client = gspread.authorize(credentials)  # Crear el cliente de Google Sheets

# Título de la aplicación
st.title("Prueba de Conexión y Gestión de Google Sheets")

# Entrada para la URL del Google Sheet
sheet_url = st.text_input("Introduce la URL del Google Sheet:")

if sheet_url:
    try:
        # Conectar con Google Sheet
        spreadsheet = client.open_by_url(sheet_url)
        sheet = spreadsheet.sheet1  # Seleccionar la primera hoja
        st.success("¡Conexión exitosa al Google Sheet!")

        # Verificar los datos en la hoja
        st.write("Verificando los datos en la hoja...")
        data = sheet.get_all_records()  # Obtener los datos
        if data:
            st.write("Datos actuales en la hoja:")
            st.write(data)
        else:
            st.warning("La hoja está vacía. Agrega datos para realizar pruebas.")

        # Botón para agregar datos de ejemplo
        if st.button("Agregar datos de ejemplo a la hoja"):
            ejemplo_datos = [
                ["Nombre", "Edad", "Correo"],  # Fila de encabezados
                ["Ana", 25, "ana@example.com"],  # Primera fila de datos
                ["Luis", 30, "luis@example.com"],  # Segunda fila de datos
                ["María", 28, "maria@example.com"]  # Tercera fila de datos
            ]
            sheet.update(ejemplo_datos)
            st.success("Datos de ejemplo añadidos a la hoja. Recarga la aplicación para verlos.")

    except Exception as e:
        st.error(f"Error al conectar con el Google Sheet: {e}")
else:
    st.info("Introduce la URL del Google Sheet para verificar la conexión.")
