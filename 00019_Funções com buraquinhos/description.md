Provavelmente você deve ter notado que as funções que definimos até agora podiam retornar tanto números como booleanos. E tem mais: **podem retornar qualquer tipo de dado** :exploding_head:. Mas, o que dizer do que _entra_ na função? Quantos argumentos podemos passar para ela? E o que são  exatamente os parâmetros?

A resposta é que os parâmetros são _...muitos tambores :drum:..._  pequenos buracos! :face_with_raised_eyebrow:

Por exemplo, nesta definição estamos _declarando_ **um** parâmetro chamado `um_numero`...

```python
def metade(um_numero): # um_numero é um parâmetro
  return um_numero / 2  
```

...que serve para que `metade` possa receber exatamente **um** argumento:

```python
ム metade(4) # 4 é um argumento
2
```

Por exemplo, quando invocamos `metade` com o argumento `4`, através deste "buraquinho" chamado `um_numero` vai chegar para ele o valor `4`, que logo nossa função poderá dividir por dois e retornar o resultado. No entanto, se  invocarmos assim...


```python
ム metade(10) # 10 é outro argumento
5
```

...através do parâmetro `um_numero` chegará a `metade` o `10` com o que invocamos a função. E novamente, irá dividir por dois e retornar o `5`.    

> Mais devagar! Vamos voltar para a função do exercício anterior...
>
> ```python
> def soma_longitudes(uma_string, outra_string):
>   return len(uma_string) + len(outra_string)  
> ```
>
> ... e marque as opções corretas.

