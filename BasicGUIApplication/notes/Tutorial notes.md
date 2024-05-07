 
Quando trabalhamos com PyQt e aplicações GUI o primeiro passo é definir a aplicação.
Essa aplicação em geral é definida na janela principal (tela principal)

o arquivo `tutotial.py` contémum exemplo de como criar essa tela utilizando linhas de código. Em geral, o foco do desenvolvimento das telas, será utilizando o Qt Designer.

## Passos para gerar uma label

1. Defina a aplicação (app)
2. Set o tamanho da janela
3. Crie a label e insira o conteúdo (no meu caso, um texto)

Ao rodar o código o texto definido não aparecia, fiz diversas tentativas e ainda assim não foi possível. Ainda não compreendi porque, mas ao adicionar o ajustSize() o texto é redimensionado. A dúvida que fica é porque existe a necessidade de auto ajustar, sendo que o texto definido não extrapola o tamanho da janela, inclusive foi o primeiro teste feito, aumentar o tamanho da janela.



