from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    # Datos actualizados para Heisel
    habilidades = ["Diseño de Modas", "Gestión de Ventas", "Atención al Cliente", "Control de Inventarios"]
    proyectos = [
        {"nombre": "Diseños de Ropa", "desc": "Creación y confección de prendas exclusivas con estilos modernos."},
        {"nombre": "Sajameño", "desc": "Asistente de administración y atención en negocio de comida."},
        {"nombre": "Full Motos Bolivia", "desc": "Gestión de base de datos para venta de motocicletas."}
    ]
    return render_template('index.html', habilidades=habilidades, proyectos=proyectos)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        return "¡Gracias por contactarme, Heisel! He recibido tu mensaje."
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)