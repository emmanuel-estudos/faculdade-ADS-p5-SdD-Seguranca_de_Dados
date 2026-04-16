# Criptografia Básica

## Sumário

- [Criptografia Básica](#criptografia-básica)
  - [Sumário](#sumário)
  - [Introdução](#introdução)
  - [Como falar da Criptografia](#como-falar-da-criptografia)
    - [Conceitos de Criptografia](#conceitos-de-criptografia)
  - [Princípios de Kerckhoffs](#princípios-de-kerckhoffs)
  - [Cifra de Substituição Simples](#cifra-de-substituição-simples)
  - [Definição de Segurança](#definição-de-segurança)
  - [Cifra de Transposição Dupla](#cifra-de-transposição-dupla)
    - [Exemplo Prático](#exemplo-prático)
  - [Preenchimento de um Bloco por Vez (One Time Pad)](#preenchimento-de-um-bloco-por-vez-one-time-pad)
    - [Tabela XOR (ou Exclusivo)](#tabela-xor-ou-exclusivo)

## Introdução

&emsp; Esta aula lançará as bases para outras aulas de criptografia. Vamos evitar o rigor matemático, tanto quanto possível, mas vamos tentar fornecer o suficiente dos detalhes para que você não somente entenda o que é a criptografia, mas também pode apreciar o porquê. A criptografia é centrada em 4 temas:

- Chave de criptografia simétrica
- Criptografia de chave pública
- Funções de hash
- Criptoanálise avançada

## Como falar da Criptografia

&emsp; A terminologia básica da criptografia inclui o seguinte [1]:

- **Criptologia** é a arte e a ciência de fazer e quebrar "códigos secretos."
- **A criptografia** é a criação de "códigos secretos."
- **Criptoanálise** é a ruptura de "códigos secretos."
- **Crypto** é um sinônimo para qualquer ou todas as anteriores (e mais).

&emsp; Um exemplo de criptografia é quando uma mensagem é encriptada por uma chave, é passada para o destino, é desencriptada por outra chave e assim é possível visualizar.

&emsp; Usando qualquer tipo de criptografia, o objetivo é ter um sistema onde uma chave é necessária para recuperar a mensagem cifrada. Mesmo que o atacante tenha conhecimento completo dos algoritmos utilizados e muitas outras informações, só é possível recuperar a mensagem com a chave.

### Conceitos de Criptografia

- **Chave (key) / cifra / Sistema de Encriptação**: é usada para criptografar dados.
- O **dado original** é conhecido como texto plano (plaintext)
- O **resultado da criptografia** é o texto cifrado (ciphertext)
- **Descriptografamos** o texto cifrado, para recuperar o texto plano original. 

- **Chave de cifra simétrica** é usada para para criptografia e descriptografia, como ilustrado na "caixa preta" da figura anterior.
- **Chave Pública ou Assimétrica** onde as chaves de criptografia e descriptografia são diferentes.

&emsp; Desde que sejam usadas chaves diferentes, é possível fazer uma **criptografia de chave pública**. Nesta, a chave de criptografia é apropriadamente conhecida como **chave pública**, enquanto a chave de decodificação, que deve permanecer em segredo, é a **chave privada**.

## Princípios de Kerckhoffs

&emsp; Cifras não precisam necessariamente serem secretas, mas elas devem ser capazes de caírem nas mãos do inimigo sem inconveniência (sem causar danos), isto é, o projeto da cifra não é secreto.

&emsp; Qual é o ponto do Princípio de Kerckhoffs? Afinal, a vida deve certamente ser mais difícil para o atacante se ele não sabe como funciona uma cifra. Embora isso possa ser verdade, também é verdade que **os detalhes dos sistemas de encriptação raramente permanecem em segredo por muito tempo**. Esforços de engenharia reversa podem facilmente recuperar os algoritmos de software e algoritmos embutidos em hardware são suscetíveis a ataques semelhantes.

&emsp; Os algoritmos de criptografia secretos têm uma longa história de não serem seguros, uma vez que o algoritmo tenha sido exposto ao escrutínio público. Por estas razões, a comunidade de criptografia não irá aceitar um algoritmo como
seguro até que ele resista a análises extensas de criptógrafos, por um período de tempo prolongado.

&emsp; A questão de fundo é que qualquer sistema de encriptação não satisfaz. Ou seja, uma cifra é **“culpada até que se prove inocente”**.

## Cifra de Substituição Simples

&emsp; Em uma cifra de substituição simples, a mensagem é criptografada substituindo a letra do alfabeto por **n posições** à frente da cada letra. Por exemplo, com **n = 3**, a substituição que atua como a chave é:

| Mensagem | Mensagem Criptografada |
| :------: | :--------------------: |
| A | D |
| B | E |
| C | F |
| D | G |
| E | H |
| F | I |
| G | J |
| H | K |
| I | L |
| J | M |
| K | N |
| L | O |
| M | P |
| N | Q |
| O | R |
| P | S |
| Q | T |
| R | U |
| S | V |
| T | W |
| U | X |
| V | Y |
| W | Z |
| X | A |
| Y | B |
| Z | C |

&emsp; Seguiremos a convenção de que a mensagem está em letras minúsculas e a mensagem criptografada está em letras maiúsculas.

&emsp; Neste exemplo, a chave podia indicar sucintamente como 3 a quantidade de deslocamentos a cada chave. Usando a chave 3, pode-se criptografar a mensagem de texto plano:

- Mensagem: fourscoreandsevenyearsago (quatrocentos e sete anos atrás)
- Mensagem criptografada: IRXUVFRUHDAGVHYHABHDUVDIR

&emsp; A abordagem de **força bruta tenta todas as chaves possíveis**, até que ache exaustivamente uma chave. Uma vez que este ataque é sempre uma opção, é necessário (embora longe de ser suficiente) que o número de chaves possíveis seja muito grande, assim o atacante simplesmente pode julgá-las num período de tempo razoável.

&emsp; Qual o tamanho de uma chave grande o suficiente? Suponha que o atacante tem um computador incrivelmente rápido que é capaz de testar 240 $2^{40}$ chaves a cada segundo. Então uma cifra de tamanho $2^{56}$ pode ser esgotado em $2^{16}$ segundos, ou cerca de 18 horas, enquanto um keyspace (cifra) de tamanho $2^{64}$ levaria mais de meio ano para ser achada.

PBFPVYFBOXZTYFPBFEQJHDXXQVAPTPOJKTOYQNIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEỌNTOZÇGGOLFXQWAKVWLXQNAEBIPBEXFOVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFЕЛЕИСЮРЕОИРОСИРРВЕТІХРЕНХИНУЕАСЕОТНЕЕЕВОИЕТЕНУВОРОТЕАТУЕТОЮХОНЕТDРТОСНЕОРВОНАОТТТОПХОНЕООРОТАDННІХОVАРВЕZОНСРИРРНРРЭТPRОЮКFARVYУDZВОТНРВОРОЈТООТОСНЕОАРВЕЕОЈНОХХОИАИХЕВОРЕВZВУБОЈТИЕЕАСЕССЕНОЮАUИІНІQHGFXVAFXOHFUFHILTTAVWAFFANTEVOITDНЕНЕQАIТІХРЕНХАFQНЕFZQWGFLVWРТОFЕА

&emsp; Será muito trabalhoso para o atacante tentar todas as $2^{88}$ chaves possíveis ($2^{64}$ ≈ 26!), mas ela pode ser mais inteligente? Suponha que a mensagem está em Inglês, o atacante pode fazer uso da Contagens da Frequência de Letras em Inglês, juntamente com Contagem da Frequência para o texto cifrado.

&emsp; A partir da Contagem de Frequência do texto cifrado, o atacante pode ver que "F" é a letra mais comum na mensagem de texto cifrado. "E" é a letra mais comum no idioma Inglês. O atacante, portanto, supõe que é provável que o "F" foi substituída por "E." Continuando, o atacante pode tentar prováveis substituições até que ela reconheça as palavras.

&emsp; Inicialmente, a palavra mais fácil de determinar poderia ser a primeira palavra, pois o atacante não sabe onde são os espaços do texto. Desde que a terceira letra é "E", e dada a contagens de alta frequência das duas primeiras letras, o atacante pode razoavelmente supor que a primeira palavra do texto original é o "the". Fazendo essas substituições no texto cifrado restante, ele será capaz de adivinhar mais letras no enigma, e este será rapidamente desvendado. O atacante provavelmente cometerá erros durante a descoberta, mas com o uso racional da informação estatística disponível, ela vai encontrar o texto original em menos de 4450 mil anos.

## Definição de Segurança

&emsp; Existem várias definições razoáveis de uma cifra segura. Idealmente, nós gostaríamos de ter prova matemática de que não há ataque viável no sistema.

&emsp; Um sistema de encriptação seguro com um pequeno número de chaves poderia ser mais fácil de quebrar do que um sistema criptográfico inseguro com um grande número de chaves.

&emsp; A justificativa para a nossa definição é que, se um ataque de atalho (shortcut attack) é conhecido, o algoritmo falha ao fornecer "anunciados" em nível de segurança, conforme indica o tamanho da chave. Tal ataque indica que a cifra possui falha de projeto. Na prática, temos de selecionar uma cifra que seja segura (no sentido de nossa definição) e tem uma chave bastante grande para que uma busca exaustiva de chaves seja impraticável.

## Cifra de Transposição Dupla

&emsp; Para criptografar com uma cifra de transposição dupla, primeiro escreva o texto simples em um vetor de tamanho determinado e depois permute as linhas e colunas de acordo com permutações especificadas. Por exemplo, suponha que nós escrevemos o texto plano attackatdawn em uma matriz 3 × 4:

$$
\begin{bmatrix}
a & t & t & a \\
c & k & a & t \\
d & a & w & n
\end{bmatrix}
$$

&emsp; Agora, se transpormos (ou permutarmos) as linhas de acordo com (1, 2, 3) → (3, 2, 1) e, em seguida transpormos as colunas de acordo com (1, 2, 3, 4) → (4, 2, 1, 3), obtemos:

$$
\begin{bmatrix}
  a & t & t & a \\
  c & k & a & t \\
  d & a & w & n
\end{bmatrix}

\xRightarrow[(1, 2, 3) \rightarrow (3, 2, 1)]{Linhas}

\begin{bmatrix}
  d & a & w & n \\
  c & k & a & t \\
  a & t & t & a
\end{bmatrix}

\xRightarrow[(1, 2, 3, 4) \rightarrow (4, 3, 2, 1)]{Colunas}

\begin{bmatrix}
  n & a & d & w \\
  t & k & c & a \\
  a & t & a & t
\end{bmatrix}
$$

### Exemplo Prático

&emsp; O texto final cifrado seria: **NADWTKCAATAT**.

&emsp; Para a transposição dupla, a chave consiste no tamanho da matriz, e as permutações de linhas e colunas. O destinatário que conhece a chave pode simplesmente colocar o texto cifrado no tamanho apropriado da matriz e desfazer as permutações para recuperar o texto.

$$
\begin{bmatrix}
  N & A & D & W \\
  T & K & C & A \\
  A & T & A & T
\end{bmatrix}

\xRightarrow[(4, 2, 1, 3) \rightarrow (1, 2, 3, 4)]{Colunas (Reverso)}

\begin{bmatrix}
  D & A & W & N \\
  C & K & A & T \\
  A & T & T & A
\end{bmatrix}

\xRightarrow[(3, 2, 1) \rightarrow (1, 2, 3)]{Linhas (Reverso)}

\begin{bmatrix}
  A & T & T & A \\
  C & K & A & T \\
  D & A & W & N
\end{bmatrix}
$$

- Texto recuperado: **attackatdown**.

&emsp; Ao contrário de uma substituição simples, a transposição dupla não faz nada para disfarçar as letras que aparecem na mensagem. Mas isso parece não impedir um ataque que se baseia em informações estatísticas contidas no texto original, uma vez que as estatísticas do texto plano são debruçadas ao longo do texto cifrado. A transposição dupla não é uma cifra trivial de quebrar. A ideia de informação de texto plano manchado com o texto cifrado é tão útil que é empregado por cifras de blocos modernas.

## Preenchimento de um Bloco por Vez (One Time Pad)

&emsp; Também conhecido como **Vernam**, é um sistema de encriptação comprovadamente seguro. Historicamente foi utilizada em vários momentos, mas não é muito prática para a maioria das situações. No entanto, ele serve para ilustrar alguns conceitos importantes.

&emsp; Para simplificar, vamos considerar um alfabeto com apenas **oito letras**. O nosso alfabeto e a correspondente representação binária de letras são dadas na Tabela. É importante notar que o mapeamento entre as letras e os bits não é segredo. Esse mapeamento serve como um efeito similar com o código ASCII, que não é secreto.

&emsp; Suponha que uma espiã chamada Alice quer criptografar a mensagem de texto plano: **heilhitler**.

&emsp; Usando um bloco por vez, ela consulta a Tabela a seguir para converter as letras para uma string de bits: **001 000 010 100 001 010 111 100 000 101**.

| Letra | Binário |
| :---: | :------ |
| e | 000 |
| h | 001 |
| i | 010 |
| k | 011 |
| l | 100 |
| r | 101 |
| s | 110 |
| t | 111 |

### Tabela XOR (ou Exclusivo)

| x | y | z |
| :-: | :-: | :-: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

---------

&emsp; Um bloco por vez exige uma chave que consiste de uma sequência de bits selecionados aleatoriamente que têm o **mesmo comprimento da mensagem**. A chave é então calculada com **XOR (ou exclusivo)** com o texto para produzir o texto cifrado.

&emsp; Denotamos o bit XOR de x com o bit y, como x ⊕ y. Desde x ⊕ y ⊕ y = x. Logo, a decodificação é realizada também por XOR com a mesma chave do texto cifrado.

| | h | e | i | l | h | i | t | l | e | r |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ciphertext** | 001 | 000 | 010 | 100 | 001 | 010 | 111 | 100 | 000 | 101 |
| **key** | 111 | 101 | 110 | 101 | 111 | 100 | 000 | 101 | 110 | 000 | 
| **plaintext** | 110 | 101 | 100 | 001 | 110 | 110 | 111 | 001 | 110 | 101 |
| | s | r | l | h | s | s | t | h | s | r |

&emsp; Vamos considerar um par de cenários:

> 1ª) Suponha que Alice tem um inimigo, Charlie, dentro de sua organização de espionagem. Charlie afirma que a chave real usada para criptografar mensagens de Alice é: **101 111 000 101 111 100 000 101 110 000**.

&emsp; Quando Bob decifra o texto cifrado usando essa chave, ele encontrará:

| | h | e | i | l | h | i | t | l | e | r |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **ciphertext** | 110 | 101 | 100 | 001 | 110 | 110 | 111 | 001 | 110 | 101 |
| **key** | 101 | 111 | 000 | 101 | 111 | 100 | 000 | 101 | 110 | 000 | 
| **plaintext** | 011 | 010 | 100 | 100 | 001 | 010 | 111 | 100 | 000 | 101 |
| | k | i | l | l | h | i | t | h | e | r |

> 2ª) Suponha que Alice é capturada por seus inimigos, que também interceptaram o texto cifrado. Os sequestradores estão ansiosos para ler a mensagem, e Alice é incentivada a fornecer a chave para esta mensagem “secreta”. Alice alega que ela é na verdade um agente duplo e para provar que é, ela afirma que a chave é: **111 101 000 011 101 110 001 011 101 101**.

&emsp; Quando os captores de Alice "decifrarem" o texto cifrado usando esta chave, eles acham:

| Mensagem Enviada | s | r | l | h | s | s | t | h | s | r |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ciphertext | 110 | 101 | 100 | 001 | 110 | 110 | 111 | 001 | 110 | 101 |
| key | 111 | 101 | 000 | 011 | 101 | 110 | 001 | 011 | 101 | 101 |
| plaintext | 001 | 000 | 100 | 010 | 011 | 000 | 110 | 010 | 011 | 000 |
| Mensagem Receida | H | E | L | I | K | E | S | I | K | E |