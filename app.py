from flask import Flask, render_template, request

# Inicializamos la aplicación Flask
app = Flask(__name__)

# RUTA 1: La Página de Inicio (El Menú)
@app.route('/')
def inicio():
    return render_template('index.html')

# RUTA 2: Ejercicio 1 - Cálculo de Notas
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    promedio = None
    estado = None
    
    if request.method == 'POST':
        # Capturamos los datos enviados por el formulario
        try:
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])
            
            # Lógica de Negocio (Cálculo)
            promedio = (nota1 + nota2 + nota3) / 3
            
            # Condiciones para aprobar: Promedio >= 40 AND Asistencia >= 75
            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"
                
            resultado = True # Indicador para mostrar la caja de resultados
            
        except ValueError:
            # Por si alguien envía texto en vez de números
            estado = "Error en los datos ingresados"

    return render_template('ejercicio1.html', resultado=resultado, promedio=promedio, estado=estado)

# RUTA 3: Ejercicio 2 - Nombres y Longitud
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mas_largo = None
    longitud = None
    
    if request.method == 'POST':
        # Capturamos los 3 nombres
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        
        # Guardamos los nombres en una lista para compararlos
        nombres = [nombre1, nombre2, nombre3]
        
        # Lógica para encontrar el más largo
        # Usamos la función max() de Python que busca basándose en el largo (len)
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

    return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud=longitud)

# Lanzador de la aplicación
if __name__ == '__main__':
    app.run(debug=True)