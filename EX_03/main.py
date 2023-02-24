# Importando as libs
import _aux 
import nltk
from nltk.corpus import mac_morpho
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger

# Baixando bases, nessário executar caso seja a primeira vez
#nltk.download('mac_morpho') # Baixa a base para treinar o modelo de classificação em portuguẽs
#nltk.download('punkt') # Baixa a base para treinar e executar a tokenização das palavras 
#nltk.download('averaged_perceptron_tagger') # Baixa o modelo já treinado para classificação de palavras em inglês

def treinar_modelo_pt():
    # Definindo uma classe padrão para tokens não identificados pelo modelo
    classe_padrao = DefaultTagger("N")
    # Adiquirindo os dados de treino da base
    treino = mac_morpho.tagged_sents()
    # Gerando o modelo
    return UnigramTagger(treino, backoff=classe_padrao)

# Função que separa as palavras da frase em tokens
def get_tokens(frase):
    frase = frase.lower()
    frase = nltk.word_tokenize(frase)
    return frase

# Função que chama o modelo que classifica as palavras em inglês
def modelo_en(tokens):
    return nltk.pos_tag(tokens)

# Função que treina o modelo em português e o chama para classificar as palavras
def modelo_pt(tokens):
    modelo_pt_br = treinar_modelo_pt()
    return modelo_pt_br.tag(tokens)

# Função que escolhe qual modelo chamar
def modelo(tokens, lingua):
    if lingua == 'pt':
        return modelo_pt(tokens)
    return modelo_en(tokens)

frase = input("Digite a frase:\n")
idioma_frase = _aux.get_idioma(frase)
tokens = get_tokens(frase)

classificacao_palavras = modelo(tokens, idioma_frase)
_aux.imprimir(classificacao_palavras, idioma_frase)