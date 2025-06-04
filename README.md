# Haddop - Mapreduce 

Mi Proyecto Haddop - Mapreduce .


## Antes de correr el aplicativo:
0) levantar ambiente virtual

instalar Flask: pip3 install flask

1) levantar hadoop

```bash
cd /opt/hadoop/
./start-all.sh
```
2) levantar ssh

```bash
sudo systemctl start ssh
sudo systemctl enable ssh
sudo systemctl status ssh
```


## Crear directorio hdfs:
```bash
hdfs dfs -mkdir -p 2dato_origen_hdfs
```

## Copiar contenido a carpeta hdfs:
```bash
hdfs dfs -put 1dato_origen/*.* 2dato_origen_hdfs
```

## Para ver el contenido:
```bash
hdfs dfs -ls 2dato_origen_hdfs
```

## Prueba logica de mapper.py
```bash
echo "1,I love Hadoop! It's amazing.,2024-01-01
2,MapReduce is complicated.,2024-01-02
3,Big Data is the future.,2024-01-03" | python3 mapper.py
```

## Prueba logica de mapper.py y reducer.py
```bash
echo "1,I love Hadoop! It's amazing.,2024-01-01
2,MapReduce is complicated.,2024-01-02
3,Big Data is the future.,2024-01-03" | python3 mapper.py | sort -k1,1 | python3 reducer.py
```

## Para ver el contenido de proceso
```bash
hdfs dfs -ls 2dato_origen_hdfs_out
```

## Recuperar resultados:
```bash
hdfs dfs -cat 2dato_origen_hdfs_out/part-00000
```

## Ejecutar aplicativo, en terminal
```bash
python3 app.py
```

## Ver resultados, en navegador:
```bash
http://127.0.0.1:5000/
```
