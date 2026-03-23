# Contextualização a Segurança da Informação

- Arquivo da [aula 02](https://drive.google.com/file/d/1u6l8_qFh2uO7lvJyLswK4qXnUlaxKX_q/view?usp=sharing).
- Data de Postagem: 12/03/2026

## Sumário

- [Contextualização a Segurança da Informação](#contextualização-a-segurança-da-informação)
  - [Sumário](#sumário)
  - [Problematização](#problematização)
  - [Evolução da Segurança da Informação](#evolução-da-segurança-da-informação)
  - [Pilares da Segurança da Informação](#pilares-da-segurança-da-informação)
  - [Criptografia](#criptografia)
  - [Tipos de Criptografia](#tipos-de-criptografia)
  - [Controle de Acesso](#controle-de-acesso)
  - [CERT.BR](#certbr)
  - [Incidentes de Segurança](#incidentes-de-segurança)

## Problematização

&emsp; As informações são os bens mais preciosos que possuímos hoje em dia, por isso veremos um dos principais focos das empresas que é a **Segurança de Dados** e como ela pode proteger esse bem tão precioso que temos.

## Evolução da Segurança da Informação

- 1940 - Mark I
  - Aplicação: Otimizar a trajetória dos mísseis
- 1957 - Satélite Sputnik
- 1962 - Arpanet ou Darpanet (Defense Advanced Research Projects Agency)
  - Aplicação: Trocar dados sigilosos entre bases militares, mesmo quando uma ou várias destas ficarem sem conexão, funcionando em forma de grafo

- 1970 - Início da Arquitetura TCP/IP
  - E-mail (1969) e Primeira aplicação: 1972
  - DNS
  - TCP evolução do NCP
  - [x] Store and Forward (único mecanismo de segurança) [1]
  - [x] Fim da década de 70: separação do TCP em 'TCP' e 'IP'

- 1980
  - Popularização dos Computadores
  - Padronização TCP/IP (1983) [2]
  - NFSNET
  - Surgimento da Cultura Hacker [3]
  - WWW (1989)

- 1990
  - Internet
  - Vândalos da Internet
  - Wireless Fidelity (Wi-Fi)

- 2000/2010/2020
  - Crimes profissionais na internet
  - Popularização da Computação Móvel
  - Computação em Nuvem
  - IoT (MANET, VANET, etc)
  - SDN, 5G
  - Smart Cities

## Pilares da Segurança da Informação

- Estados da Informação
  - Transmissão
  - Armazenamento
  - Processamento
- Propriedades da Segurança da Informação
  - Confidencialidade
  - Integridade
  - Disponibilidade
- Medidas de Segurança
  - Tecnologias
  - Políticas e Procedimentos
  - Conscientização

&emsp; As informações estão em diversos locais e a segurança depende de múltiplos fatores. Imagine cada **Pilar de Segurança** sendo uma face de um cubo.

- CID [5]
  - **Confidencialidade**: visa impedir a leitura não autorizada de informações.
  - **Integridade**: se dá, caso uma escrita não autorizada for proibida.
  - **Disponibilidade**: fazer com que os sistemas estejam sempre disponíveis ao usuário.
- Segundo [5]
  - **Criptologia**: é a arte e a ciência de fazer e quebrar "códigos secretos".
  - A **Criptografia** é a criação de "códigos secretos".
  - **Criptoanálise** é a ruptura de "códigos secretos".

## Criptografia

&emsp; De acordo com [6]:

- Teve origem no Egito, em meados de 1900 A.C.
- Usado no Império Romano com a Cifra de César (substituição por _n_)
- Disco de Cifra - Início da Mecanização de Cifragem
  - Século XV: italiano Leon Battista Alberti (1404-1472) com dois cilindros para implementar a Cifra de César
  - Século XVIII: cilindro de Jefferson (Thomas Jefferson) com 36 discos implementando uma cifra de substituição polialfabética.
  - Cifra polialfabética consiste em usar uma tabela 26x26 que cria 26 alfabetos.
- Em 1918, Arthur Scherbius patenteou a máquina de criptografia denominada Enigma. [Vídeo de explicação](https://www.youtube.com/watch?v=mdSvGUd0_c).
  - Baseada no Princípio de Kerchhoff
- Em 1949, Claude Shannon criou a Teoria Matemática da Comunicação ([link de vídeo](https://www.youtube.com/watch?v=yIEnE-jfI54)).
- Em 1972: DES (Data Encryption Standard)
- Década de 90: AES (Advanced Encryption Standard).

```js
plain_text = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

cipher_text = [D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, A, B, C]
```

<p align="right" class="legenda">
  <ins><i>Cifra de César com n = 3</i></ins>
</p>

## Tipos de Criptografia

- **Simétrica**: só uma chave é compartilhada entre origem e destino. Exemplos:
  - RC4
  - A5/1
  - DES (3DES)
  - AES
- **Assimétrica** ou **Criptografia de Chaves**: um par de chaves é trocado, uma para cifrar (pública) e outra diferente para decifrar (privada). Exemplos:
  - RSA
  - Curvas Elípticas

&emsp; Exemplos de Tipos de Criptografia:

```txt
1. Mensagem original enviada
2. Algoritmo de criptografar (Chave Secreta Compartilhada)
3. Texto Cifrado (Meio Seguro)
4. Algoritmo de descriptografar (Chave Secreta Compartilhada)
5. Mensagem original recebida
```

<p align="right" class="legenda">
  <ins><i>Criptografia Simétrica</i></ins>
</p>

```txt
1. Mensagem original enviada
2. Algoritmo para criptografar (Chave Pública)
3. Texto cifrado
4. Algoritmo para descriptografar (Chave Privada)
5. Mensagem original recebida
```

<p align="right" class="legenda">
  <ins><i>Criptografia Assimétrica</i></ins>
</p>

## Controle de Acesso

- **Autenticação**: forma de um usuário provar que ele é ele mesmo, através de provar:
  - Algo que você sabe (senha)
  - Algo que você tem (smartcard, cartão de banco, assinatura digital)
  - Algo que você é (biometria: leitor digital, leitor da íris e análise da palma da mão)
- **Autorização**: após a autenticação, o usuário estará apto ao sistema, seguindo restrições impostas pelo mesmo

## CERT.BR

> &emsp; Grupo de Resposta a Incidentes de Segurança para a Internet no Brasil. mantido pelo NIC.br, do Comitê Gestor da Internet no Brasil. É responsável por tratar incidentes de segurança em computadores que envolvam redes conectadas à Internet no Brasil.
>
> &emsp; Atua como um ponto central para notificações de incidentes de segurança no Brasil, provendo a coordenação e o apoio no processo de resposta a incidentes e, quando necessário, colocando as partes envolvidas em contato.
>
> &emsp; Além do processo de tratamento a incidentes em si, o CERT.br também atua através do trabalho de conscientização sobre os problemas de segurança, da análise de tendências e correlação entre eventos na Internet brasileira e do auxílio ao estabelecimento de novos CSIRTs no Brasil.
>
> &emsp; Estas atividades têm como objetivo estratégico aumentar os níveis de segurança e de capacidade de tratamento de incidentes das redes conectadas à Internet no Brasil.
>
> &emsp; As atividades conduzidas pelo CERT.br fazem parte das atribuições do CGI.br de:
> 
> - I - estabelecer diretrizes estratégicas relacionadas ao uso e desenvolvimento da Internet no Brasil;
> - IV - promover estudos e recomendar procedimentos, normas e padrões técnicos e operacionais, para a
segurança das redes e serviços de Internet, bem assim para a sua crescente e adequada utilização pela sociedade
> - VI - ser representado nos fóruns técnicos nacionais e internacionais relativos à Internet; Bem como dos objetivos do NIC.br, conforme seu Estatuto:
> - IV - atender aos requisitos de segurança e emergências na Internet Brasileira em articulação e cooperação com as entidades e os órgãos responsáveis;
> - VII - promover ou colaborar na realização de cursos, simpósios, seminários, conferências, feiras e congressos, visando contribuir para o desenvolvimento e aperfeiçoamento do ensino e dos conhecimentos nas áreas de suas especialidades.

## Incidentes de Segurança

&emsp; Como afirma o CERT (Centro de Estudos, Resposta e Tratamento de Incidentes de Segurança no Brasil), em [5]:

> "Qualquer evento adverso, confirmado ou sob suspeita, relacionado à segurança dos sistemas de computação ou das redes de computadores".
>
> "O ato de violar uma política de segurança, explícita e implícita".