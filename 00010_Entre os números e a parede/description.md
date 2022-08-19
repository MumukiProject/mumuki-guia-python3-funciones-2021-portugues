Vamos fazer uma breve revisão dos booleanos antes de continuar!

* É possível fazer a conjunção lógica entre dois booleanos (_e lógico_), por meio do operador `and`. Por exemplo: `esta_chovendo and faz_calor`
* É possível fazer a disjunção lógica entre dois booleanos (_ou lógico_), por meio do operador `or` fazendo `e_verao or e_primavera`

E além desses dois operadores, contamos com um terceiro: o operador de negação `not`, que converte o `True` em `False` y vice-versa:

```python
ム not True
False
ム not False
True
```

> Vamos praticar! :muscle: Defina as seguintes funções:
>
> * `esta_entre`, que utilize três números e diga se o primeiro é maior que o segundo e menor que o terceiro.
> * `esta_fora_de_alcance`: que utilize três números e diga se o primeiro é menor que o segundo ou maior que o terceiro.
>
> ```python
> ム esta_entre(3, 1, 10)
> True
> ム esta_entre(90, 1, 10)
> False
> ム esta_entre(10, 1, 10)
> False
> ム esta_fora_de_alcance(17, 1, 10)
> True
> ```
>
