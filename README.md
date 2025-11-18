1. Estructura de Datos:
Partidas: Cada partida (elemento de construcción) se representa como una lista con la siguiente estructura: [nombre, tipo, dimensiones[], precio_unitario].
nombre: Una cadena de texto que describe la partida (ej: "Zapata Z1").
tipo: Una cadena de texto que indica el tipo de partida. Los tipos posibles son: "zapata", "columna", "muro", "viga". El tipo determina qué dimensiones son necesarias.
dimensiones[]: Una lista de números que representa las dimensiones de la partida. El número y significado de las dimensiones depende del tipo.
"zapata": [largo, ancho, altura]
"columna": [seccion_lado, seccion_lado, altura]
"muro": [largo, espesor, altura]
"viga": [base, peralte, largo]
precio_unitario: Un número que representa el precio por unidad de volumen (ej: precio por m³).
partidas (Lista Principal): Es una lista que contiene múltiples partidas. Cada elemento de esta lista es una de las listas descritas anteriormente.
presupuesto (Matriz): Esta lista almacenará el presupuesto final. Cada fila representará una partida y contendrá: [nombre, volumen, precio_unitario, costo_total].
2. Función calcular_volumen(partida):
Esta función toma como entrada una partida (una de las listas de la lista partidas).
Determina el tipo de la partida.
Accede a las dimensiones de la partida.
Realiza el cálculo del volumen en función del tipo:
"zapata": largo * ancho * altura
"columna": seccion_lado * seccion_lado * altura
"muro": largo * espesor * altura
"viga": base * peralte * largo
Si el tipo no coincide con ninguno de los anteriores, devuelve 0.
3. Generación del Presupuesto:
Se inicializa una lista vacía llamada presupuesto.
Se itera sobre cada partida en la lista partidas.
Para cada partida:
Se extrae el nombre.
Se calcula el volumen utilizando la función calcular_volumen().
Se extrae el precio_unitario (pu).
Se calcula el costo total (volumen * pu).
Se crea una nueva lista [nombre, volumen, pu, costo] y se añade a la lista presupuesto.
4. Impresión de Resultados:
Se imprime un encabezado "PRESUPUESTO DE OBRA".
Se inicializa una variable total en 0 para almacenar el costo total de todas las partidas.
Se itera sobre cada item (fila) en la lista presupuesto.
Para cada item:
Se desempaquetan los valores: nombre, vol, pu, costo.
Se imprime una línea con el nombre, volumen, precio unitario y costo total, formateados para una mejor legibilidad.
Se añade el costo al total.
Finalmente, se imprime una línea separadora y el total general del presupuesto.
