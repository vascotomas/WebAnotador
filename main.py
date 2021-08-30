from website import create_app

app = create_app()

# Solo Funciona si lo ejecutamos main.py, NO si lo importamos

if __name__ == '__main__':
    app.run(debug=True)  # Debug = Re lanza el servidor web cuando se realiza un cambio en codigo
