# API Testing – Automatización con Python y Requests

## 📌 Descripción del proyecto

Este proyecto contiene **pruebas automatizadas de una API REST** enfocadas en la validación del parámetro `firstName` durante la creación de un/a usuario/a.

El objetivo principal es **verificar el correcto comportamiento de la API ante distintos escenarios**, incluyendo datos válidos, inválidos y casos límite, asegurando que la API responda de acuerdo con los requisitos funcionales y técnicos.

Este proyecto fue desarrollado como parte de mi formación en **Quality Assurance**, aplicando buenas prácticas de testing automatizado y validación de APIs.

---

## 🧪 Alcance de las pruebas

Las pruebas automatizadas cubren, entre otros, los siguientes escenarios:

* Creación de usuario con `firstName` válido
* Validación de longitud mínima y máxima del campo `firstName`
* Envío de caracteres no permitidos
* Envío de valores vacíos o nulos
* Verificación de códigos de estado HTTP
* Validación del contenido de la respuesta (body)

---

## 🛠️ Tecnologías y herramientas

* **Python**
* **Requests** (envío de solicitudes HTTP)
* **Pytest** (framework de pruebas)
* **API REST**

---

## ⚙️ Requisitos previos

Antes de ejecutar las pruebas, asegúrate de tener instalado:

* Python 3.x
* pip

Instala las dependencias necesarias con:

```bash
pip install pytest requests
```

---

## ▶️ Ejecución de las pruebas

Para ejecutar todas las pruebas automatizadas, utiliza el comando:

```bash
pytest
```

Pytest mostrará un resumen de las pruebas ejecutadas, indicando cuáles pasaron y cuáles fallaron.

---

## 🎯 Objetivo de calidad

Este proyecto busca:

* Detectar errores de validación en la API
* Garantizar la integridad de los datos enviados
* Asegurar respuestas consistentes y confiables
* Facilitar la detección temprana de defectos

---

## 💬 Frase personal

> “No pruebo para romper, pruebo para mejorar.”

---

## 👤 Autor

**Jezer Ávila**
QA Tester Jr

🔗 GitHub: [https://github.com/JezerAvila](https://github.com/JezerAvila)

