Combinar operações é muito útil, mas tem o problema de que agora precisamos lembrar (ou pensar :thought_balloon:) como fazer isso cada vez que necessitemos combinar. Isso pode nos levar a cometer erros...

```python
# queremos saber se o primeiro é  mais longo que o segundo
ムlen("Santiago del Estero") < len("Misiones")
False # Ups, era para o outro lado!
```
...ou simplesmente nos chateamos fazendo a mesma coisa :rolling_eyes:. Não seria muito melhor se pudéssemos escrever diretamente assim?:

```python
ムe_mais_longo_que("Santiago del Estero", "Misiones")
```

> :octagonal_sign: Um momento! Será que isso vai funcionar? Verifique testando no console.


