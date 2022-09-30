# Prova-ABD-3-Bimestre: Projeto de Clubes
 
## User Story (US)

### #1
Como dono de um clube, quero registrar meu clube, a partir de um sitema de cadastro de clubes, para que as pessoas possam se increver no meu clube como membros e para que o mesmo tenha visibilidade com sistema.

### #2
Como membro de um clube, quero me increver em um clube, a partir de um sistema de cadastro em clubes, para facilitar o resgistro no clube que desejo entrar.

### #3
Como dono de um clube, quero gerenciar os membros do meu clube, a partir de um sistema de contagem de membros, para que tenha um maior controle do meu clube.
 
## Critérios de aceitação (CA)

### Gerais
- O banco deve respeitar todos os valores da tabela, portanto os dados de um cadastro (seja de clube ou de membros) não podem podem ser nulo, todos os dados das tabelas tem que estar completos e respeitando o formato;
- Nescessário uma tabela "Pessoa" que servirá como base para definir Donos e Menbros de um Clube;
- Os membros/pessoas podem pertencer à vários clubes;
- É nescessário uma tabela apenas com Clubes inscritos com suas respectivas informações e uma tabela individual para cada clube com seus respectivos membros;
- As tabelas devem ter uma relação, para interligar os menbros com seus respectivos clubes.

### 1º funcionalidade
O sistema deve realizar o cadastro do clube em uma tabela "Clubes" com as informações: id_clube(chave primaria),nome(tipo string),id_dono(chave estrangeira),data_criacao(tipo data), quantidade de membros(tipo inteiro) e o CNPJ(locais onde realizam seus encontros e atidades, no qual os Clubes podem utilizar mais de um lugar).

### 2º funcionalidade
O sistema deve realizar o cadastro de um membro dentro de um clube com as seguintes informações: id_menbro(chave primária) cpf(chave estrangeira), nome(tipo string), natalidade(data de nacimento, tipo data), telefone de contato(tipo inteiro) e fornecer uma relação com a tabela de "Clubes".

### 3º funcionalidade
O sistema deve gerar uma tabela(Quantidade_Menbros) com uma consulta sql exibindo a quantidade de menbros de um clube.

 
## Defenition of Done (DoD)
 
- Ao final dos testes e aprovação de cada funcionalidade é nescessário fazer uma revisão no código, realização de um teste geral com todas as funcionalidades; 
- Realizar um feedback final das funcionalidades;
- Análise sobre os critérios e metas, para ver o nivel de progresso, verificar se as metas formaram atingidas, segundo o que está descrito na User Story;
- Nescessário uma revisão na User Story, para realizar adptações nos objetivos, caso haja alguma alteração/ mudança durante o processo de realização do Projeto, ou seja, fazer adaptações e correções na User Story e nos Critérios de Aceitação;
- Fazer uma avaliação final do Projeto.
 
 # Modelo Relacional - Projeto de Clubes
 
 ![Modelo relacional- Projeto de Clubes](https://user-images.githubusercontent.com/114430817/193036177-b546d6fa-25f1-4da2-9895-63034d22e4ec.png)
 
 
 
 
 
