"""
Hello World Multi Linguas. 

Dependendo da lingua configurada 
no ambiente o programa exibe a mensagem
correspondente. 

Como usar: 

Tenha a variável LANG devidamente configuraada ex:

    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.0.1"
__author__ = "Livia Teles"
__license__ = "Unlicense"

import os 

#Dunder - 02 underlines

#$env:LANG = "en_US"
#python .\hello.py

# Este programa imprime Hello World
current_language = os.getenv("LANG")[:5]

msg = "Hello, World"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)
