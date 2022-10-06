# pythomation_mail

## Objetivo
Este projeto foi criado para fins de estudo, visando atender a uma necessidade de automação de comunicação com os clientes.
A solução deve se conectar a um banco de dados (neste caso uma instância de MySQL), executar uma query e com o resultado criar um arquivo de extensão .xlsx.
O Arquivo deve ser então enviado para o(s) destinatário(s), e em seguida ser removido para evitar desperdício de armazenamento no disco.
## Melhorias
Como melhorias, foram implementadas as possibilidades de definição de instância de banco de dados alvo, escolha de query e escolha de grupos diferentes de destinatários
* as possibilidades de instâncias de bancos devem ser armazenadas no diretório **_dbs_** em formato **_json_**, e serem chamadas com o parâmetro **_-db [nome do arquivo sem extenção]_** ou **_--database [nome do arquivo sem extenção]_**. 
Ex.: _$python script.py -db local_ buscará o arquivo _dbs/local.json_
* as queries devem ser armazenadas em arquivos distintos no diretório **_queries_** em formato **_sql_**, e serem chamadas com o parâmetro **_-q [nome do arquivo sem extenção]_** ou **_-query [nome do arquivo sem extenção]_**. 
Ex.: _$python script.py -q query_1_ buscará o arquivo _queries/query_1.sql_
* as listas de destinatários devem ser armazenadas em arquivos distintos no diretório *__mail_group__* em formato **_txt_**, e serem chamadas com o parâmetro **_-mg [nome do arquivo sem extenção]_** ou **_-mailgroup [nome do arquivo sem extenção]_**. 
Ex.: _$python script.py -mg admins_ buscará o arquivo _queries/admins.txt_
* Quando não forem passados nenhum dos parâmetros, o script ira buscar arquivos **_default_** em cada diretório cujo parâmetro tenha sido omitido.

Ex.: A execução da linha *&python script.py -q sells -db mysql_sells -mg group_1* utilizará os arquivos _queries/sells.sql_, _dbs/mysql_sells.json_ e *mail_group/group_1.txt*
