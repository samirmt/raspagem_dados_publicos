# -*- coding: utf-8 -*-
import os
import urllib
import json
import executa_api
from os import system
from executa_api import listar_escolas_por_estados
from executa_api import buscar_escola_por_nome

titulo = """
            ****************************************************
            * RASPAGEM DE DADOS DE ESCOLAS PUBLICAS COM PYTHON *
            *                                                  *
            * by Samir Marques Teixeira - samate82@hotmail.com *
            ****************************************************
        """

opt = 0

def limpar_tela():
    system('clear')


def main():
    limpar_tela()
    print(titulo)
    menu_inicial()

def menu_inicial():
    print """
        MENU INICIAL!

        1 - VER ESCOLAS POR ESTADO:
        2 - INFORMAÇÕES DA ESCOLA:
    """
    opt = raw_input('digite uma opção: ')
    if (opt=='1'):
        menu_por_estados()
    elif (opt=='2'):
        menu_informacoes_escolas()
                    

def menu_por_estados():
    limpar_tela()
    print """
        VER ESCOLAS POR ESTADO

        OPÇÃO-ESTADO--------------SIGLA	 
 	 	 
        1-->  Acre----------------AC	 
        2-->  Alagoas-------------AL	 
        3-->  Amapá---------------AP	 
        4-->  Amazonas------------AM	 
        5-->  Bahia---------------BA	 
        6-->  Ceara---------------CE	 
        7-->  Distrito Federal----DF	 
        8-->  Espírito Santo------ES	 
        9-->  Goiás---------------GO	 
        10--> Maranhão------------MA	 
        11--> Mato Grosso---------MT	 
        12--> Mato Grosso do Sul--MS	 
        13--> Minas Gerais--------MG	 
        14--> Pará----------------PA	 
        15--> Paraíba-------------PB	 
        16--> Paraná--------------PR	 
        17--> Pernambuco----------PE	 
        18--> Piauí---------------PI	 
        19--> Rio de Janeiro------RJ	 
        20--> Rio Grande do Norte-RN	 
        21--> Rio Grande do Sul---RS	 
        22--> Rondônia------------RO	 
        23--> Roraima-------------RR	 
        24--> Santa Catarina------SC	 
        25--> São Paulo-----------SP	 
        26--> Sergipe-------------SE	 
        27--> Tocantins-----------TO

        0--> p/ voltar
    """
    opt = raw_input("digite uma opção: ")
     
    if(opt=='0'): main()
    elif (opt=='1'): estado = 'AC'
    elif (opt=='2'): estado = 'AL'
    elif (opt=='3'): estado = 'AP'
    elif (opt=='4'): estado = 'AM'
    elif (opt=='5'): estado = 'BA'
    elif (opt=='6'): estado = 'CE'
    elif (opt=='7'): estado = 'DF'
    elif (opt=='8'): estado = 'ES'
    elif (opt=='9'): estado = 'GO'
    elif (opt=='10'): estado = 'MA'
    elif (opt=='11'): estado = 'MT'
    elif (opt=='12'): estado = 'MS'
    elif (opt=='13'): estado = 'MG'
    elif (opt=='14'): estado = 'PA'
    elif (opt=='15'): estado = 'PB'
    elif (opt=='16'): estado = 'PR'
    elif (opt=='17'): estado = 'PE'
    elif (opt=='18'): estado = 'PI'
    elif (opt=='19'): estado = 'RJ'
    elif (opt=='20'): estado = 'RN'
    elif (opt=='21'): estado = 'RS'
    elif (opt=='22'): estado = 'RO'
    elif (opt=='23'): estado = 'RR'
    elif (opt=='24'): estado = 'SC'
    elif (opt=='25'): estado = 'SP'
    elif (opt=='26'): estado = 'SE'
    elif (opt=='27'): estado = 'TO'                

    resp = listar_escolas_por_estados(estado)

    print('\nLista de escolas do estado: %s\n' %estado)
    
    x = 0
    qtd = len(resp)
    print('CODIGO:NOME')
    while (x<qtd):
        print(resp[x])
        x+=1

    print('\nTotal: %i escolas' %x) 
    opt = raw_input("\n[1]Nova Pesquisa -- [2]Voltar: ")
    if(opt=='1'):
        menu_por_estados()
    else:
        main()     

def menu_informacoes_escolas():
    limpar_tela()
    print """
            INFORMAÇÕES DA ESCOLA

            0--> p/ voltar
         """        
    opt = raw_input('digite o nome da escola: ')
    if(opt=='0'): main()
    else: 
        resp = buscar_escola_por_nome(opt)


    i = 1
    qtd = len(resp)

    print('\nEscola(s) encontrada(s): %i ' %resp[0])


    while(i<qtd):
        for x in resp[1]:
            print('\n')
            print('NOME: %s' %x['nome'])
            print('CIDADE: %s' %x['cidade'])
            print('ESTADO: %s' %x['estado'])
            print('REGIAO: %s' %x['regiao'])
            print('ADMINISTRACAO: %s' %x['dependenciaAdministrativaTxt'])
            print('IDEB AF: %s' %x['idebAF'])
            print('SITUACAO: %s' %x['situacaoFuncionamentoTxt'])
            print('ANO CENSO: %s' %x['anoCenso'])
        i+=1    

    opt = raw_input("\n[1]Nova Pesquisa -- [2]Voltar: ")
    if(opt=='1'):
        menu_informacoes_escolas()
    else:
        main()    

if __name__ == "__main__": main()