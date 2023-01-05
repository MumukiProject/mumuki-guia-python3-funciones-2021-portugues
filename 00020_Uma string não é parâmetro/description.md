Como vimos, uma string pode ser passada como argumento de uma função...

```python
ム e_biblioteca("Biblioteca Mário de Andrade")
True
ム e_biblioteca("Biblioteca Nacional do Brasil")
True
ム e_biblioteca("Teatro Amazonas")
False
```

...e além disso, as funções podem ter parâmetros, um para cada argumento que necessite receber.

> Mas espera lá! Vamos ter que escrever de forma diferente nossos parâmetros quando estes _forem do tipo_ string? :thinking:
>
> Por exemplo, observe a seguinte definição de `e_biblioteca`...
>
> ```python
> def e_biblioteca("lugar"):
>  return "biblioteca" in "lugar"
> ```
> ...está bem escrita? :eyes:
