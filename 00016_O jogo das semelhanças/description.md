Agora vamos ver a definição de outra função...
...

```python
def e_pergunta(oracao):
  return str.endswith(oracao, "?")
```
...a qual podemos usar assim:

```python
ム e_pergunta("Que horas são?")
True
ム e_pergunta("Nesta casa obedecemos as leis da termodinâmica!")
False
```

A definição dessa função é parecida com a anterior? Por que será?

> :mag: Compare esta nova definição com a que vimos anteriormente...
>
> ```python
> def e_mais_longo_que(uma_string, outra_string):
>   return len(uma_string) > len(outra_string)
> ```
>
> ...e responda o que elas têm em comum.

