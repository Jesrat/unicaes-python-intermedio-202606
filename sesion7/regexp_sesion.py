import re

name_pattern = re.compile(r"^Nombre:\s([a-zA-Z\sáéíóú]+)$", flags=re.MULTILINE)
email_pattern = re.compile(r"^Email:\s([a-zA-Z\sáéíóú.]+@[a-zA-Z\sáéíóú.]+)", flags=re.MULTILINE)
ip_pattern = re.compile(r"^IP:\s([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3})", flags=re.MULTILINE)
web_patter = re.compile(r"^Web:\s(https:\/\/[a-zA-Z.\/?=0-9&]+)", flags=re.MULTILINE)

text = """
Nombre: Juan Pérez López
Email: juan.perez@example.com, otro.correo123@sub.dominio.co
Teléfonos: +34 612-345-678, (011) 4567-8901, 555.123.4567, 91 234 56 78
Fecha de nacimiento: 15/03/1990, otras fechas: 2024-01-05, 07-22-2023
Dirección: Calle Falsa 123, Piso 4B, CP 28080, Madrid, España
Web: https://www.ejemplo.com/pagina?ref=123&user=abc, http://sub.dominio.org
IP: 192.168.1.1, 10.0.0.255, 256.100.50.1 (inválida a propósito)
Precio: $1,250.99 USD, 45,00 €, 1.000.000 ARS
Hashtags: #RegexPower #Python2026 #test_123
Usuarios: @juanperez, @maria_lopez99
Código postal EE.UU.: 90210, 10001-1234
DNI/NIF: 12345678A, X1234567L
Tarjeta: 4111-1111-1111-1111, 5500 0000 0000 0004
Hora: 14:30:00, 09:05 AM, 23:59
IPv6 simple: fe80::1ff:fe23:4567:890a
Frase con espacios raros:   Hola    mundo   con   espacios   múltiples.
Palabras repetidas: el el gato gato corre corre
Comentario HTML: <!-- esto es un comentario --> <div class="test">contenido</div>
Cadena vacía y nulos: "" null NULL None
Números: 3.14159, -42, 1e10, 0x1F, 007
Guion bajo_y-guion.medio
"""

"""
SS
s.s.
S.s.
San Salvador
san Salvador
sanSalvador
Sansalvad0r
sanSlavodr



San Salvador

(?i)^(s\.?\s?s\.?|san\s?(salvad[o0]r|slavodr))$

if texto == "SS" or texto == "s.s." or texto == "S.s.":
    texto = "San Salvador"
"""
