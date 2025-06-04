import subprocess
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return "¡Funciona! Flask está respondiendo.", 200

    try:
        # 1. Eliminar el directorio de salida (si existe)
        subprocess.run(
            ['hdfs', 'dfs', '-rm', '-r', '2dato_origen_hdfs_out'],
            check=False  # No lanzar excepción si falla (directorio no existe)
        )
        
        # 2. Ejecutar el job MapReduce
        subprocess.run([
            'mapred', 'streaming',
            '-files', 'mapper.py,reducer.py',  # Archivos a enviar al cluster
            '-mapper', 'mapper.py',
            '-reducer', 'reducer.py',
            '-input', '2dato_origen_hdfs/tweets_editado.csv',
            '-output', '2dato_origen_hdfs_out'
        ], check=True)  # Falla si el job de Hadoop falla

        # 3. Leer resultados
        result = subprocess.check_output([
            'hdfs', 'dfs', '-cat', '2dato_origen_hdfs_out/part-00000'
        ]).decode('utf-8')

        # Procesar datos para la visualización
        data = {}
        for line in result.split('\n'):
            if line:
                sentiment, count = line.split('\t')
                data[sentiment] = int(count)

        return render_template('index.html', data=data)

    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar Hadoop: {e}", 500

# ¡Este bloque es esencial!
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Asegúrate de que esté presente
