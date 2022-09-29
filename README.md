# Prova-ABD-3-Bimestre
 
## User Story

### #1
Como dono de um clube, quero registrar meu clube, a partir de um sitema de cadastro de clubes, para que as pessoas possam se increver no meu clube e para que o meu clube tenha visibilidade nesse sistema

### #2
Como membro de um clube, quero me increver em um clube, a partir de um sistema de cadastro em clubes, para facilitar o resgistro no clube que desejo entrar.

### #3
Como dono de um clube, quero gerenciar os menbros do meu clube, a partir de um sistema para contar os membros, para que tenha um maior controle do meu clube.
 
## Critérios de aceitação

### Gerais
- O banco deve respeitar todos os valores da tabela, portanto nenhum dos dados de um cadastro(seja de clube ou de menbros) pode ser nulo, todos os dados da tabelas tem que estar completos e respeitando o formato;
- Membros podem pertencer à vários clubes;
- As tabelas devem ter uma relação, para interligar os menbros com seus respectivos clubes.

### 1º funcionalidade
O sistema deve realizar o cadastro do clube em uma tabela "Clubes" com as informações: id_clube(chave primaria),nome(tipo string),id_dono(chave estrangeira),data_criacao(tipo data), quantidade de membros(tipo inteiro), no qual nenhuma pode ser um valor nulo.

### 2º funcionalidade
O sistema deve realizar o cadastro de um membro dentro de um clube com as seguintes informações: cpf(chave primária), nome(tipo string), natalidade(data de nacimento, tipo data), telefone de contato(tipo inteiro, uma pessoa se relaciona com apenas um telefone) e fornecer uma relação com a tabela de "Clubes".

### 3º funcionalidade
O sistema deve gerar uma tabela(Quantidade_Menbros) com uma consulta sql exibindo a quantidade de menbros de um clube.

 
## Defenition of Done
 
 Ao final do teste e aprovação de cada funcionalidade é nescessário fazer uma revisão no código, realização de um teste geral com todas as funcionalidades, realizar um feedback final do Projeto.
