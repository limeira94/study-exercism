def find_anagrams(word, candidates):
    
    palavra_ordenada = ''.join(sorted(word.lower()))
    anagramas_encontrados = []
    
    for palavra in candidates:
        if ''.join(sorted(palavra.lower())) == palavra_ordenada:
            anagramas_encontrados.append(palavra)
    
    anagramas_encontrados = [anagrama for anagrama in anagramas_encontrados if anagrama.lower() != word.lower()]
        
    return anagramas_encontrados


if __name__ == '__main__':
    print(find_anagrams("BANANA", ['Banana']))
    