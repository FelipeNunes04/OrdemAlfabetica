# -*- coding: utf-8 -*-

__author__='Felipe Nunes'
__date__='$30/03/2016 20:54'

def cadastrar():
	nAlunos=int(input("Quantos alunos voce deseja cadastrar? "))
	lAlunos=[]
	for i in range(nAlunos):
	    lAlunos.append([0]*nAlunos)
	    lAlunos[i]=str(raw_input("Digite o nome do aluno %d (Digite apenas letras maiusculas): "%(i+1)))
	    while lAlunos[i].isupper()==False:
	        lAlunos[i]=str(raw_input("Digite apenas letras maiusculas!\nNome do Aluno: "))
	lAlunos.sort()
	for i in range(nAlunos):
	    print i+1,'-',lAlunos[i]

	remove = 1
	op = ''
	while op != 'sim' or op != 'Sim' or op!='SIM' or op!='SIm' or op!='sIM' or op!='nao' or op!='não' or op!='NAO' or op!='NÃO' or op!='Não' or op!='NÃo':
		op=str(raw_input("Deseja remover algum aluno da lista?(sim ou nao): "))
		while op == 'sim' or op == 'Sim' or op=='SIM' or op=='SIm' or op=='sIM':
		    remove=int(input("Qual o numero do aluno?(digite 0 para sair)"))
		    if remove>nAlunos or remove <0:
		    	print "Aluno nao encontrado!"
		    elif remove>0:
			    del lAlunos[remove-1]
			    nAlunos-=1
			    print "Aluno %d removido.(quando um aluno eh removido, todos que vem depois dele diminuem uma posicao.)"%remove
			    op=str(raw_input("Deseja remover outro aluno da lista?(sim ou nao): "))
		    else:
			    break
		if op=='nao' or op=='não' or op=='NAO' or op=='NÃO' or op=='Não' or op=='NÃo' or remove==0:
		    arquivo=open('Lista.txt','w')
		    i=0
		    for i in range(nAlunos):
		        arquivo.write('%d - '%(i+1))
		        arquivo.write(lAlunos[i])
		        arquivo.write('\n')
		    arquivo.close()
		    print "\nSua lista foi salva!"
		    break
		else:
		    print "opcao invalida!"
	
	
def listar():
	import os.path
	if os.path.exists('Lista.txt'):
		print "\nSua lista de alunos eh:\n" 
		arquivo=open('Lista.txt','r')
		print arquivo.read()
		arquivo.close()
	else:
		print "\n!! Voce ainda nao cadastrou seus alunos, por favor realize o cadastro dos mesmos. !!"


op=1
while op != 0:
	print "\n\n|--------------------- Alunos em ordem alfabetica - MENU -----------------------------|"
	print "|1 - Cadastrar Alunos (essa acao substitui todos os alunos cadastrados anteriormente).|"
	print "|2 - Listar Alunos jah cadastrados.                                                   |"
	print "|0 - Sair do programa.                                                                |"
	print "|-------------------------------------------------------------------------------------|\n\n"
	op = input("Digite a opcao desejada: ")
	if op ==1:
		cadastrar()
	elif op==2:
		listar()
	elif op==0:
		exit()
	else:
		print "Opcao Invalida!"



    
