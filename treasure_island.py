print('Bem vindo a ilha do tesouro')



print('Sua missão é encontrar o tesouro:')



choise1= input('Voce esta em uma encruzilhada, Onde você quer ir ? Digite esuqerda ou direita ').lower()

if choise1 == 'esquerda':
  choise2=input('Voce chegou em um lago, Existe uma ilha no meio do lago.Tecle w para espear por um barco ou s para nadar atraves do lago').lower()
  if choise2 == 'w':
      choice3=input('voce chegou na ilha desarmado,existe uma casa com 3 portas, Uma vermelho, outra amarela, outra azul. Qual  cor você escolhe:').lower()
      if choice3 == 'vermelho':
        print('A sala esta cheia de fogo. fim de jogo')
      elif choice3 == 'amarela':
          print('Voce encontrou o tesouro. Parabêns')
      elif choise3 == 'azul':
          print('A sala esta cheia de feras, fim de jogo.')
      else:
          print('É uma sala com fogo, fim de jogo.')
        
  else:
      print('Voce foi atacado por uma besta marinha, fim de jogo')

else:
  print('Voce caiu em uma armadilha, fim de jogo')