 
Quando trabalhamos com PyQt e aplicações GUI o primeiro passo é definir a aplicação.
Essa aplicação em geral é definida na janela principal (tela principal)

o arquivo `tutotial.py` contémum exemplo de como criar essa tela utilizando linhas de código. Em geral, o foco do desenvolvimento das telas, será utilizando o Qt Designer.

## Passos para gerar uma label

1. Defina a aplicação (app)
2. Set o tamanho da janela
3. Crie a label e insira o conteúdo (no meu caso, um texto)

Ao rodar o código o texto definido não aparecia, fiz diversas tentativas e ainda assim não foi possível. Ainda não compreendi porque, mas ao adicionar o ajustSize() o texto é redimensionado. A dúvida que fica é porque existe a necessidade de auto ajustar, sendo que o texto definido não extrapola o tamanho da janela, inclusive foi o primeiro teste feito, aumentar o tamanho da janela.

## Gerando labels com QtDesigner

É uma ferramenta que permite a criação das interfaces de uma forma mais 
iterativa. Possibilia ao desenvolvedor da aplicação, de forma visual ter entendimento espacial dos componentes, assim como facilita o entendimento do que se propõe a fazer.

Para desenvolver as telas através do Qt Designer, siga os seguintes passos:

1. Caso não tenha inserido o comando `"gerenciado de pacotes" install pyqt5-tools`, insira-o no terminal.
2. Defina o tipo de tela `Main Window`, `Widgets` ou formato desejado, selecione o tamanho da tela (na maioria dos casos Default).
3. Adicione os objetos desejados.
4. Renomeie o nome dos objetos no `Object Inspector` de acordo com a aplicação do objeto. Isso fará muita diferença quando for localizar o objeto no código, além de facilitar manutenção e escalabilidade da aplicação.
5. Após fializada a edição da tela e, caso deseje visualizar, navegue até a opção, Form -> Preview In -> Windows Style.
6. Em seguida, salve a label no formato .ui na pasta do projeto.
7. Abra o prompt de comando na pasta do projeto e insira o comando `pyuic5 -x nomeDoArquivo.ui -o nomeDoArquivoDesejado.py`
   - `pyuic"X",` referencie a verao do PyQt utilizada.
   - `-x` opção que torna o arquivo .ui executável como script.
   - `-o` opção que habilita definir o arquivo de saída nesse caso file.py.
8. Por fim, execute o .py gerado e poderá verificar que a mesma label desenvolvida no Qt Designer será exibida. Caso seja necessário, alterações da label desenvolvida poderão ser relaizadas diretamente no arquivo.py


