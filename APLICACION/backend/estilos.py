
# Aplicar estilo al título y a la tabla con la fuente personalizada
titulo_estilo = {
    'text-align': 'center',  # Centrar horizontalmente el texto
    'background-color': 'black',  # Color de fondo negro
    'color': 'white',  # Texto en color blanco
    'padding': '10px',  # Espacio interior para el título
    'font-family': 'cursive'  # Usar una fuente personalizada
}

tabla_estilo = {
    'backgroundColor': '#FFFF99'  # Color de fondo amarillo para la tabla
}





# Aplicar estilo diferente a la columna 'Retenido'
estilo_columna_retenido = [
    {
        'if': {
            'column_id': 'Retenido',
        },
        'backgroundColor': '#FF5733',  # Color de fondo diferente para la columna 'Retenido'
        'color': 'white',  # Texto en color blanco en la columna 'Retenido'
    }
]

# Establecer el ancho fijo de las celdas de la tabla
ancho_fijo = '100px'  # Cambia el valor según tus preferencias