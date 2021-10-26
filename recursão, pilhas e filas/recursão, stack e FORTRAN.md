# recursão, stack e FORTRAN

## introdução - o que é recursão

Recursão, em termos computacionais é quando você chama uma função dentro dela mesma.

Mas não é tão simples assim, para ser uma real recursão **o problema** deve ser recursivo.

----

Um problema recursivo é um problema que possui 2 propriedades importantes...

Uma simetria, esta bastante interessante, de que **para resolver o problema total deve-se resolver uma versão "menor" deste embutido**.

----

Outra propriedade que um problema recursivo deve ter (para ser computável) é um caso base.

Isso é importante já que, se realmente queremos computar algum resultado, a recursão não deve repetir infinitamente.

----

### exemplo

Podemos usar como exemplo a função Fatorial, muito utilizada em análise combinatória.

Essa função é definida como: `n! = n * (n - 1)!` e `0! = 1`

Para implementarmos ela em C podemos fazer da seguinte forma:

    unsigned int fatorial(unsigned int n) {
        /// caso base
        if(n == 0) return 1;

        /// passo de recursão
        return n * fatorial(n - 1);
    }

----

Podemos verificar o caso base quando `n = 0` que para a cadeia de chamadas.

E o passo de recursão que chama a própria função, porém, com o n decrementado.

----

Dado um `n` qualquer (maior ou igual a 0), esta função vai "expandindo" o problema, até chegar no caso base, o qual retorna apenas um simples valor, `1`.

Esse valor retorna multiplicando os outros, resultando, finalmente, no fatorial do número dado.

Podemos dizer que a solução recursiva para esse problema é bastante elegante e concisa.

----

## desenvolvimento 1 - estruturas de dados e impactos na resolução de problemas

### recursão não é pau pra toda obra

Mas então, vamos aplicar recursão a todo problema que tem essas duas propriedades?

Como diz o ditado: quando temos um martelo tudo parece prego.

Da mesma forma, quando aprendemos uma ferramenta nova queremos utiliza-lá em todos os problemas que encontramos.

----

Porém, se alguém nos pedisse para implementar uma função, a qual contasse de `1 a n`, provavelmente não a faríamos utilizando recursão.

O problema dado não é inerentemente recursivo, sendo assim, sua implementação pela abordagem recursiva tem uma aparência forçada

Enquanto a iterada pode parecer mais intuitiva neste exemplo.

----

Isso por algumas razões, uma delas é por inteligibilidade (ou seja, clareza).

E a clareza no código é algo que buscamos sempre.

Buscamos pois podemos não ser os únicos mantenedores daquele código, outras pessoas também precisam entender e modificar aquilo que implementamos.

E a facilidade de compreensão torna melhor a vida dos nossos colegas e até de nós mesmos.

----

### a recursão e a stack

A recursão em código existe desde a primeira linguagem de programação (de alto nível), FORTRAN. Mas não nas primeiras versões de FORTRAN.

Para entender por que FORTRAN não tinha recursão nas suas primeiras versões, precisamos entender duas coisas: a stack e como uma função é chamada.

----

#### a stack

Stack (pilha em português) é uma estrutura de dados e se comporta da seguinte maneira:

Na inserção: quando um item é adicionado, ele é colocado no topo do ultimo item.

Na remoção: apenas o item do topo da stack é removido.

Isso cria o efeito de o último a entrar é o primeiro a sair (Last In First Out - LIFO).

As stacks como estrutura de dados são normalmente representadas crescendo para baixo, no sentido crescente dos endereços de memória.

----

#### chamada de função

Uma chamada de função (em resumo) segue os seguintes passos:

Os argumentos passados são alocados em memória e atribuidos os valores, um na frente do outro.

As variáveis locais (do escopo da função chamada) são alocadas em memória.

O ponteiro de instrução, que aponta para onde o código está sendo executado dentro de um programa, é salvo na stack.

E seu valor é passado da função chamadora para a função chamada.

#### how FORTRAN did it

No FORTRAN cada função possuia um lugar em memória estático.

E quando uma função tentava chamar a si mesma, o procedimento de chamada sobreescrevia os valores da função chamadora, tornando recursão impráticavel.

Na hora de implementar a chamada de função em FORTRAN, não foi considerado a ideia de que uma função poderia chamar a si mesma, fazendo com que qualquer código que possuisse recursão quebrasse.

Normalmente, as funções são chamadas e os dados necessários para a chamada (argumentos, variáveis locais, ponteiro de instrução) são colocados na stack.

Fazendo assim possível que uma função chame a si mesmo sem sobreescrever os dados que a própria utiliza.

### a tail recursion

Existe uma técnica na recursão chamada "tail recursion".

Ela nada mais é do que uma função recursiva que, após feitos os calculos necessários, faz a chamada recursiva, passando o que já foi calculado na chamada.

### exemplo

considerando o seguinte código da função fatorial:

    int fatorial(unsigned int x) {
        /// caso base
        if(x == 0) return 1;

        /// passo de recursão
        return x * fatorial(x - 1);
    }

Quando fazemos uma chamada, essa pode ser `fatorial(5)`, o stack trace do programa vai se comportar da seguinte maneira:

    fatorial(5)
    5 * fatorial(4)
    5 * 4 * fatorial(3)
    5 * 4 * 3 * fatorial(2)
    5 * 4 * 3 * 2 * fatorial(1)
    5 * 4 * 3 * 2 * 1
    120

Agora, se implementarmos a função fatorial da seguinte maneira:

    int fatorial(unsigned int x) {
        return tail_fatorial(x, 1);
    }

    int tail_fatorial(unsigned int x, unsigned int res) {
        if(x == 0) return res;

        return tail_fatorial(x - 1, x * res);
    }

Nesse caso, podemos ver que o stack trace das chamadas ficaria o seguinte:

    fatorial(5)
    tail_fatorial(5, 1)
    tail_fatorial(4, 5)
    tail_fatorial(3, 20)
    tail_fatorial(2, 60)
    tail_fatorial(1, 120)
    tail_fatorial(0, 120)
    120

Podemos verificar que o calculo dos valores é feito anterior a chamada das funções e o caso base faz com que o valor, já calculado, retorne pelas funções até a inicial.

A razão de utilizar recursive tail é aparente no stack trace, já que o espaço necessário para a chamada recursiva de `1000!` acaba crescendo com as chamadas.

Mas o stack trace da call em tail é aparente que o espaço é melhor utilizado.

fonte: https://stackoverflow.com/questions/310974/what-is-tail-call-optimization

### adendo - memoizing

...

## desenvolvimento 2 - performance recursão vs iteração

A performance de um código pode ser medido de duas formas:
* A memória utilizada.
* A quantidade de instruções executadas.

Se fizessemos a comparação com a versão iterada do código a partir de vários tamanhos de entradas, podemos plotar e verificar a diferença real.

// discussão do resultado dos testes



## conclusão - elegância e performance
