# LUIS FERNANDO FERNANDEZ GARCIA
# 📝 EXAMEN: Principios SOLID - Sistema de Biblioteca
## ⏱️ DURACIÓN: 2 HORAS
## ⏱️ REPOSITORIO: Subir a Github
### Distribución de Tiempo Sugerida:
- ⏰ **0:00 - 0:10**: Lectura y setup (10 min)
- ⏰ **0:10 - 0:35**: Ejercicio 1 - OCP (25 min)
- ⏰ **0:35 - 1:15**: Ejercicio 2 - SRP (40 min)
- ⏰ **1:15 - 1:50**: Ejercicio 3 - DIP (35 min)
- ⏰ **1:50 - 2:00**: Revisión y entrega (10 min)
---
## 📋 INSTRUCCIONES GENERALES
### ✅ Qué DEBES hacer:
1. Leer completamente este documento
2. Verificar que el código base funciona
3. Crear archivos nuevos para tus refactorizaciones
4. Mantener la funcionalidad original
5. Comentar tus cambios
6. Entregar todos los archivos Python
### ❌ Qué NO debes hacer:
1. Modificar biblioteca_examen.py original
2. Agregar funcionalidades nuevas
3. Usar librerías externas
4. Copiar código
---
## 📊 EVALUACIÓN (100 puntos)
| Ejercicio | Principio | Puntos | Tiempo |
|-----------|-----------|--------|--------|
| Ejercicio 1 | OCP | 30 | 25 min |
| Ejercicio 2 | SRP | 30 | 40 min |
| Ejercicio 3 | DIP | 30 | 35 min |
| Teórico | LSP + ISP | 10 | 20 min |
| **TOTAL** | | **100** | **120 min** |
---

# HICE LOS 3 EJERCICIOS, DEL TERCERO NO HICE EL BONUS, TODO ESTA EN EL MISMO ARCHIVO

## 🟢 EJERCICIO 1: Open/Closed Principle (30 pts - 25 min)
### Problema:
El método `buscar_libro()` viola OCP con múltiples.
### Tu Tarea:
1. Crea clase abstracta para generar una estrategia de búsqueda
2. Implementa 3 estrategias de busqueda
3. Refactoriza el método para usar estrategias
4. Agrega BusquedaPorDisponibilidad SIN modificar código existente
### Entregable:
- Clase abstracta + 4 estrategias
- Método refactorizado
- Documentación demostrando uso (como probar que funciona)
---
DOCUMENTACION:
AGREGUE FUNCIONES EN EL MAIN PARA PROBAR LOS DISTINTOS METODOS NUEVOS CREADOS Y VALIDAR QUE AL BUSCARLOS SI FUNCIONAN
## 🟡 EJERCICIO 2: Single Responsibility Principle (30 pts - 40 min)
### Problema:
`SistemaBiblioteca` tiene múltiples responsabilidades.
### Tu Tarea:
1. Crea `ValidadorBiblioteca` (solo validación)
2. Crea `RepositorioBiblioteca` (solo persistencia)
3. Crea `ServicioNotificaciones` (solo notificaciones)
4. Refactoriza `SistemaBiblioteca` para usar estas clases
### Entregable:
- 3 clases separadas
- SistemaBiblioteca refactorizada
- main() funcionando
- Documentación demostrando uso (como probar que funciona)
---
DOCUMENTACION:
LAS CLASES ESTAN IMPLEMENTADAS EN EL ARCHIVO Y AL CORRERLO FUNCIONA CORRECTAEMENTE

## 🔴 EJERCICIO 3: Dependency Inversion Principle (30 pts - 35 min)
### Problema:
Dependencia directa de implementaciones concretas.
### Tu Tarea:
1. Crea interfaz para el repositorio (clase abstracta)
2. Implementa `RepositorioArchivo`
3. Refactoriza `SistemaBiblioteca` con inyección de dependencias
4. Refactoriza main() con configuración de dependencias
5. BONUS: Crea `RepositorioMemoria`
### Entregable:
- Interfaz IRepositorio
- RepositorioArchivo
- Inyección de dependencias
- main() con DI
---
DOCUMENTACION: 
EN EL MAIN PUSE QUE AHORA EL REPOSITORIO QUE USA ES LA NUEVA REPOSITORIOARCHIVO EN LUGAR DE REPOSITORIOBIBLIETCA
## 📝 PREGUNTAS TEÓRICAS (10 puntos)
### Pregunta 1: LSP (5 pts)
**a) (5 pts)** Explica qué es LSP y cómo se aplica al ejemplo:
```python
class Usuario:
    def calcular_limite_prestamos(self):
        return 3
class Estudiante(Usuario):
    def calcular_limite_prestamos(self):
        return 3
```
**Respuesta:**
```
Que las clases hijas deben poder sustituir a las padres, es decir por ejemplo aqui se ve que Usuario tiene un limite de 3 prestamos por lo tanto el estudiante tambien debe implementar este metodo de la misma forma, no puede no usarlas porque generaria problemas
```
**b) (5 pts)** Da un ejemplo que VIOLE LSP y explica por qué:
```python
# Tu código aquí
class Empleado:
    def calcular_pago(self, horas_trabajadas):
        return horas_trabajadas * 50

class Practicante(Empleado):
    def calcular_pago(self, horas_trabajadas):
        pass
# Explicación:
A los practicantes se le debe pagar de otra forma por lo que la clase practicante ya no pdoria sustituir a la de empleado
que si se le pagan por horas
_________________________________________________________________
```
---
### Pregunta 2: ISP (5 pts)
**a) (5 pts)** ¿Por qué esta interfaz VIOLA ISP?
```python
class IGestionBiblioteca:
    def agregar_libro(self): pass
    def buscar_libro(self): pass
    def realizar_prestamo(self): pass
    def generar_reporte(self): pass
    def hacer_backup(self): pass
```
**Respuesta:**
```
Mezcla funcionalidades que realmente no tendrian que estar forzadas a tener
```
**b) (5 pts)** Propón cómo segregar esta interfaz:
```
Interface 1: IGestionLibros - Métodos: agregar:libro y buscar_libro
Interface 2: IGestionPrestamos - Métodos: realizar_prestamo
Interface 3: IGEstionReportes - Métodos: generar_reporte y hacer_backup
```
---
## 📦 ENTREGA
### Archivos a entregar:
1. Repositorio en GIT
2. Respuestas del examen teorico en un folder aparte on en el README principal
3. Puedes separar los archivos de cada ejercicio en carpetas si así lo deseas
4.PAra puntos extra, puedes generar los archivos de clase y ponerlos en la carpeta llamada "templates"
4. Considera el checklist de abajo como una Guia de entrega
### Checklist:
- [X] Todos los archivos ejecutan sin errores
- [X] Funcionalidad original mantenida
- [X] Código comentado
- [X] Preguntas respondidas
- [X] Nombre en primera página
---
## 💡 CONSEJOS
1. Administra tu tiempo
2. Prueba tu código
3. Comenta tus decisiones
4. Si te atoras, pasa al siguiente
---
**¡MUCHO ÉXITO! 🚀**
