import requests

# Por 10 segundos não temos certeza se a requisição irá retornar
response = requests.get("https://httpbin.org/delay/10")
print(response)


# ---------------------------------------------------------------------------- #


# Então, podemos pedir um timeout para o request.
# Assim, se a request não retornar, vai gerar um erro.

# Ao gerar o erro, conseguimos pegar na EXCEPTION.
# E aí podemos pedir para solicitar novamente

import requests

try:
    # recurso demora muito a responder
    response = requests.get("http://httpbin.org/delay/10", timeout=2)
except requests.ReadTimeout:
    # vamos fazer uma nova requisição
    print('Trying request again')
    response = requests.get("http://httpbin.org/delay/1", timeout=2)
finally:
    print(response.status_code)

# No exemplo acima, para efeitos didáticos, modificamos a URI do recurso, diminuindo o delay de resposta da requisição, através do timeout , porém normalmente este valor não muda.