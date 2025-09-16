import pytest

import sender_stand_request
import data

# Esta funcion crea una copia de un usuario y le cambia el parámetro "firstName"
def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body



# Función de prueba positiva (para evitar repetir código en cada test)
def positive_assert(first_name):
    user_body = get_user_body(first_name)                               #crea el usuario
    user_response = sender_stand_request.post_new_user(user_body)       #lo agrega al db

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""
    #authToken es un valor que el servidor devuelve cuando un usuario se crea exitosamente

    users_table_response = sender_stand_request.get_users_table()

    str_user = (
        user_body["firstName"] + "," +
        user_body["phone"] + "," +
        user_body["address"] + ",,," +
        user_response.json()["authToken"]
    )

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1



# Función de prueba negativa (para evitar repetir código en cada test)
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)                               #crea el usuario
    user_response = sender_stand_request.post_new_user(user_body)       #intenta agregarlo al db

    # Comprueba si el código de estado es 400
    assert user_response.status_code == 400   #codigo HTTP q devuelve el SERVIDOR ->Bad Request este valor esta fuera del cuerpo JSON
    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert user_response.json()["code"] == 400  #cuerpo de la respuesta que envia la API (programado x el backend)
    #Comprueba si el atributo "message" en el cuerpo de la respuesta es correcto
    assert user_response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino, "\
                                         "la longitud debe ser de 2 a 15 caracteres."



# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_no_firstname(user_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"





# Prueba 1. Creación de un nuevo usuario con firstName de 2 caracteres
# @pytest.mark.smoke   #pruebas de humo  (decoradores)
# @pytest.mark.regression   #pruebas de humo  (decoradores) eje API  se pueden agrupar con diccionarios
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")   #2 caracteres

# Prueba 2. Creación de un usuario con firstName de 15 caracteres
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")  # 15 caracteres

# Prueba 3. Intenta crear un usuario con firstName de 1 caracter (Prueba Negativa)
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")  # 1 caracter

# Prueba 4. Intenta crear un usuario con firstName de 16 caracteres (Prueba Negativa)
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Аааааааааааааааа")  # 16 caracteres

# Prueba 5. Intenta crear un usuario con un espacio en firstName (Prueba Negativa)
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("А Aaa")  # space caracter

# Prueba 6. Intenta crear un usuario con caracter-especial en firstName (Prueba Negativa)
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol('"№%@",')  # Si usas comillas simples para delimitar el string en Python, las comillas dobles no necesitan escape

# Prueba 7. Intenta crear un usuario con numeros en firstName (Prueba Negativa)
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")  # digits

# Prueba 8. La solicitud no contiene el parámetro "firstName" (Prueba Negativa)
def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName", None)  #usamos pop con parametro none por si la key no existe no de error al intentar borrarla
    #del user_body["firstName"]  #tambien se podria nos quedaremos con .pop
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 9. Intenta crear un usuario, el parámetro "firstName" contiene un string vacío (Prueba Negativa)
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

# Prueba 10. Intenta crear un usuario con valores numericos int (Prueba Negativa)
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400



#pom page object model
# En pytest los decoradores se usan muchisimo los marks en pytest son etiquetas que puedes poner en tus test
# para agruparlos ej. smoke, regression, api, skip, skipif, xfail)  filtrarlos al ejecutar o aplicar configuraciones especiales
# ponlos antest de tu testcase
# @pytest.mark.smoke
# def test_login_valid():
#     assert 1 + 1 == 2
# y los ejecutas por marca
# pytest -m smoke
# En versiones modernas de pytest, se recomienda registrar tus marcas en el archivo pytest.ini para evitar advertencias:
# # pytest.ini
# [pytest]
# markers =
#     smoke: quick checks to see if main features work
#     regression: complete test suite for deeper checks
#
# Otros marks útiles de pytest
#
# @pytest.mark.skip → salta el test.
#
# @pytest.mark.skipif(condition, reason="...") → salta si se cumple una condición.
#
# @pytest.mark.xfail → marca el test como esperado a fallar
#
# En pytest un mismo test puede tener varias marcas al mismo tiempo, simplemente las pones en forma de múltiples decoradores (o en una sola línea).
# asi corre con uno u otro pero si quieres que corra solo si cumple ambas entonces: pytest -m "smoke and regression"
# pytest -m "smoke or regression"


