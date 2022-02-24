# wordle-helper
Primera Tarea de Análisis y Procesamiento Inteligente de Textos

Helper básico para Wordle, para obtener las palabras a utilizar se tomó el archivo /usr/share/dict/words de una instalación de Debian configurada con el idioma en español. De esta lista de palabras en español sólo se mantuvieron las que son de cinco caracteres y se eliminaron los acentos y diéresis. Para determinar el orden de las sugerencias se utilizan las frecuencias de las letras en español y cada paalbra tiene un score que es la suma de las frecuencias de sus letras, esto no es lo más óptimo para resolver Wordle, pero al ser un helper básico se optó por esta opción. Al usuario se le muestran las cinco palabras con el mejor score como recomendación o las palabras que queden si ya hay menos de cinco posibles palabras.

## ¿Cómo usar?

El programa muestra las sugerencias, se debe seleccionar una e ir introduciendo los resultados. Estos resultados deben ser una cadena de cinco caracteres donde cada caracter indica el color que regresó el Wordle, v si fue verde, a si fue amarillo y g si fue gris.

![Ejecución](https://github.com/atorr5555/wordle-helper/blob/main/wordle_48/wordle_48_1.PNG?raw=true)

![Resultados](https://github.com/atorr5555/wordle-helper/blob/main/wordle_48/wordle_48_2.PNG?raw=true)
