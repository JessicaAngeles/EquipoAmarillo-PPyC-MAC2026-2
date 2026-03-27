## Funcionamiento
### Map
Cada hilo descarga un libro desde Project Gutenberg y cuenta la frecuencia de palabras.
### Reduce
Se combinan todos los conteos parciales en un único resultado utilizando `Counter().update()`.
## Resultados
Se muestran las 20 palabras más frecuentes considerando todos los libros.
## Librerias 
- threading
- urllib
- collections.Counter
- re
