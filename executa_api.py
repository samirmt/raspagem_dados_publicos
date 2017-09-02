# -*- coding: utf-8 -*-
import urllib
import json

def listar_escolas_por_estados(estado):
    url = 'http://educacao.dadosabertosbr.com/api/cidades/' + estado
    resp = urllib.urlopen(url).read()
    resp = json.loads(resp.decode('utf-8'))
    return resp

def buscar_escola_por_nome(nome):
    url = 'http://educacao.dadosabertosbr.com/api/escolas?nome=' + nome
    resp = urllib.urlopen(url).read()
    resp = json.loads(resp.decode('utf-8'))
    return resp