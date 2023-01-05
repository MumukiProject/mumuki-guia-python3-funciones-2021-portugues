Sim, Python nos dá operações que podem ser combinadas e que nos permitem resolver diferentes tarefas, mas o verdadeiro poder da programação é que também podemos criar nossas próprias operações.

E para fazer isso vamos dar as boas-vindas  para  _as funções_ :confetti_ball:! Nossas novas amigas vão nos permitir "ensinar"  ao computador a realizar uma tarefa que originalmente não estava incluída na linguagem mediadora. Como? _Escrevendo uma definição_ como a seguinte **apenas uma vez** :one:...

```python
def e_mais_longo_que(uma_string, outra_string):
  return len(uma_string) > len(outra_string)
```

...e em seguida  _invocando_ esta função **quantas vezes quisermos** :1234::

```python
ム e_mais_longo_que("Vale da Lua", "Chapada dos Veadeiros")
False
ム e_mais_longo_que("Vale da Lua", "Chapada dos Veadeiros")
False # as duas vezes retornam o mesmo
```

E não é apenas isso! Cada vez que  invocamos poderemos fazer isso com _argumentos_ diferentes :open_mouth: :

```python
ム e_mais_longo_que("Bahia", "Tocantins")
False
ム e_mais_longo_que("Lençóis maranhenses", "Vale do Paraíba")
True # se os argumentos mudam, o resultado pode ser diferente também
```

> Vamos ver se você está compreendendo:
>
>  1. Copie a _definição_ da função `e_mais_longo_que` no editor que está abaixo;
>  2. No `Console`, invoque a função `e_mais_longo_que` várias vezes com argumentos diferentes;
>  3. Em seguida, volte para a guia de `Solução` e pressione o botão `Enviar`.

