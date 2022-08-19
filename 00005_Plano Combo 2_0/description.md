Podemos combinar estas funções da mesma forma que fazíamos com os operadores e funções que já vinham em Python? Com certeza! :heart_eyes: Em outras palavras, _podemos invocar funções dentro de definições_. Por exemplo:

```python
def dobro(numero):
  return 2 * numero

def seguinte_do_dobro(numero):
  return dobro(numero) + 1
```

Ou melhor:

```python
def dobro(numero):
  return 2 * numero

def seguinte(numero):
  return numero + 1

def seguinte_do_dobro(numero):
  return seguinte(dobro(numero))
```

> Vamos ver se ficou claro; defina as seguintes funções:
>
> * `anterior`: escolhe um número e retorna esse número menos um.
> * `triplo`: devolve o triplo de um número.
> * `anterior_do_triplo`, que combina as duas funções anteriores: multiplica um número por 3 e subtrai 1.
>

