Exatamente! Todas as opções estão corretas. :ok_hand:

Uma função pode _declarar_ tantos parâmetros quanto necessite em sua definição; para cada um deles devemos passar um argumento ao invocar a função. O interessante é que não importa quais argumentos vamos utilizar, já que cada um estará descrito com o nome do parâmetro. Nesse exemplo, se escrevemos no console...

```python
ム soma_longitudes("aprendendo", "programação")
```
...dentro da função `soma_longitudes` o argumento `"aprendendo"` será `uma_string` e `"programação"` será `outra_string`:

```python
def soma_longitudes(uma_string, outra_string):
  #                 	▲       	▲
  #          	"aprendendo"  "programação"
  return len(uma_string) + len(outra_string)  
  #        	▲              	▲
  # 	len("aprendendo")  len("programação")
```

No entanto, se invocamos escrevendo...

```python
ム soma_longitudes("conhecendo", "Python")
```

... agora o parâmetro `uma_string` tem como valor `"conhecendo"` e `outra_string` _vale_ `"Python"`.

Por isso é tão importante dar um bom nome à função!
