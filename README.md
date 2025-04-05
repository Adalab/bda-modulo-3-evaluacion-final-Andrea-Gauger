# ✈️ Análisis de Clientes – Programa de Fidelización de Aerolínea
Este proyecto consiste en el análisis de datos reales simulados de un programa de fidelidad de una aerolínea. Se explora y visualiza el comportamiento de los clientes, así como características demográficas, tipo de tarjeta y actividad mensual de vuelos.

## 📂 Conjuntos de Datos
Se utilizan dos archivos:

- Customer Flight Analysis.csv: Datos mensuales de vuelos y puntos de clientes.

- Customer Loyalty History.csv: Perfil demográfico, financiero y de membresía de cada cliente.

Ambos se enlazan por la columna Loyalty Number.

## 🧹 Fase 1: Exploración y Limpieza
- Carga y visualización inicial de datos (head, info, describe).

- Revisión de valores nulos y duplicados.

- Conversión y validación de tipos de datos.

- Unificación de los datasets por Loyalty Number.

- Limpieza de:

    - Valores negativos (convertidos a absolutos).

    - Salarios nulos (imputados por mediana).

    - Registros irrelevantes o inconsistentes.

## 📊 Fase 2: Visualización
Se realizaron diversas visualizaciones para responder preguntas clave del negocio:

- 📅 Reservas mensuales: vuelos reservados por mes y por mes/año.

- 📈 Relación entre distancia y puntos acumulados.

- 🗺️ Distribución de clientes por provincia.

- 🎓 Comparación de salario promedio por nivel educativo.

- 💳 Proporción de clientes según tipo de tarjeta de fidelidad.

- ⚧️ 💍 Distribución de clientes por género y estado civil.

Se utilizaron matplotlib y seaborn para la representación gráfica.

## 🧠 Fase 3: Análisis, Conclusiones y Next Steps.
- Este análisis proporciona insights clave para entender el valor de los clientes, su comportamiento a lo largo del tiempo y cómo diferentes variables (educación, género, tipo de tarjeta) se relacionan con su actividad en el programa de lealtad.

- En el documento también se podran conocer las conclusiones finales así como los próximos pasos del proyecto.

## 🛠️ Fase 4: ETL in progress.

- En la carpeta ETL se puede encontrar el proceso ETL solo para la parte de exploración de archivos y creación de un nuevo archivo csv con la información relevante unificada.

- Ejecutando el archivo main.py desde la terminal se podrá ver esta primera parte del proceso.

