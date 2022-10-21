def origem_destino_iguais(origem, destino, listaErros):
    if origem == destino:
        listaErros['destino'] = 'Origem não pode ser igual a destino.'
        
def campo_temNumero (valor_campo, nome_campo, listaErros):
    if any(char.isdigit () for char in valor_campo):
        listaErros[nome_campo] = 'Não inclua n~umeros.'
        
def compara_data_ida_volta (data_ida, data_volta, listaErros):
    if data_ida > data_volta:
        listaErros['data_volta'] = 'Data de ida não pode ser maior que a data de volta'
        
def compara_data_ida_pesquisa(data_ida, data_pesquisa, listaErros):
    if data_ida < data_pesquisa:
        listaErros['data_ida'] = 'Data de ida não pode ser inferior a hoje.'
