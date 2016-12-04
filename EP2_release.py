#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Carlos Algusto Neto / Weslei Luiz de Paula Pinto

global posição
posição = 0
def desenho(posição):
	boneco = ['''
	+-------------------+
			    |
			    |
			    |
			    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
			    |
			    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
       /|		    |
			    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
       /|\		    |
			    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
       /|\		    |
       / 		    |
			    |
			    |
			    |
			    |
====================================''','''
	+-------------------+
	|		    |
	O		    |
       /|\		    |
       / \		    |
			    |
			    |
			    |
			    |
====================================''']
	print (boneco[posição])

def jogar_novamente():
	alternativa = input('Deseja jogar novamente? [S/n] ')
	while alternativa.lower() != "s" and  alternativa.lower() != "n": 
		alternativa = input('Digite um valor válido por favor [S/n]: ')
	if alternativa.lower() == 's':
		return jogo()
	elif alternativa.lower() == 'n':
		print('fim de jogo!')

def escolhe():
	global listona
	import urllib.request
	pagina = urllib.request.urlopen('https://www.ime.usp.br/~pf/dicios/br')
	texto = pagina.read().decode('iso8859')
	listona = texto.split('\n')
	jogo()

def testa_palavra():
	global listona
	from random import randint
	return listona[randint(0,int (len (listona)))]
	
def chute(letras):
	while len (letras)!= 1:
		letras = input ("\nDigite APENAS UMA letra: ")
	while letras.lower() not in 'abcdefghijklmnopqrstuvwxyzáàãâéèêẽíìôóòôúùç':
		letras = input ("\nDigite uma LETRA: ")
	return letras.lower()


def jogo():
	clear()
	global palavra_aleatoria
	pos=0
	while (len(testa_palavra())) < 5:
		testa_palavra()
	palavra_aleatoria=testa_palavra()
	palavra_aleatoria=list(palavra_aleatoria)
	sublinhados = '_'*len(palavra_aleatoria)
	sublinhados=list(sublinhados)
	ja_digitou=''
	certas=''
	erradas=''
	letra_validada=''

	while True:
		desenho(pos)
		

		print ("Sua palavra tem %d LETRAS " %(len(palavra_aleatoria)) )

		print (" ".join(sublinhados))

		print ("Você já digitou:","-".join(ja_digitou),'\n')
		if letra_validada in palavra_aleatoria and letra_validada not in certas:
			certas += letra_validada
		print("Letras corretas:",'-'.join(certas),'\n')
		if letra_validada not in palavra_aleatoria and letra_validada not in erradas:
			erradas += letra_validada
		print("Letras erradas:",'-'.join(erradas),'\n')
		letra = input ("Digite uma Letra: ")
		letra = letra.lower()
		letra_validada=chute(letra)
		if letra_validada not in ja_digitou:
			ja_digitou +=(letra_validada)

			k=0
			while k < len (palavra_aleatoria):
				if letra_validada == palavra_aleatoria[k]:
			
					sublinhados[k]=letra_validada	
				k+=1			

			if letra_validada not in palavra_aleatoria:
				clear()
				print("\nERROU!!!")
				pos+=1
				desenho(pos)

			if sublinhados==palavra_aleatoria:
				ganhou()
				break
			if pos==5:
				print ("Você PERDEU, a palavra era:", "".join(palavra_aleatoria))
				jogar_novamente()
				break
		clear()

def ganhou():
	global palavra_aleatoria
	print ("PARABÉNS!!!, Você acertou a palavra:", "".join(palavra_aleatoria))	
	jogar_novamente()

def clear():
	global limpar
	import os
	os.system(limpar)



def main():
	import platform
	global limpar

	#define qual é o so da máquina
	so = platform.system()
	
	if so == 'Linux':
		limpar = 'clear'
		
	elif so == 'Windows':
		limpar = 'cls'		
main()
escolhe()
