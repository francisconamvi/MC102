#Nome: Francisco Namias Vicente || RA: 216028

dot_and_his_friends = [",",".","!","?",":"]
original_sentence = input() #Frase a ser analisada
print(original_sentence)
__sentence__ = original_sentence.lower() #transformar tudo em minusculo
__sentence__ = __sentence__.split() #dividindo frase
original_sentence = original_sentence.split()
sentence = __sentence__[:] #copiando frase para mexer nela

while True:
    new_command = input() #Receber comando
    if new_command == "D": #delete
        word_del = input() #palavra a ser deletada
        word_del = word_del.lower()
        for word in __sentence__:
            if word[-1] in dot_and_his_friends: word_aux = word[:len(word)-1]
            else: word_aux = word
            if word_aux == word_del:
                original_sentence.remove(original_sentence[sentence.index(word)])
                sentence.remove(word)
    elif new_command == "I": #Inverter
        drow = input() #palavra a ser invertida
        drow = drow.lower()
        for word in __sentence__:
            letters_drow = [] #letras ao contario serao colocadas aqui
            letters_original_drow = []
            if word[-1] in dot_and_his_friends:
                word_aux = word[:len(word)-1]
                original_word_aux = original_sentence[sentence.index(word)][:len(word)-1]
                dot_of_the_time = word[-1]
            else:
                word_aux = word
                original_word_aux = original_sentence[sentence.index(word)]
                dot_of_the_time = ""
            if word_aux == drow: #se a palavrea lida for igual a palavra que será invertida
                for l in range(1, len(word_aux)+1):
                    letters_drow.append(word_aux[-l]) #mandar pra lista a palavra ao contrario
                letters_drow.append(dot_of_the_time)
                un_drow = "".join(letters_drow)
                for l in range(1, len(word_aux)+1):
                    letters_original_drow.append(original_word_aux[-l]) #mandar pra lista a palavra ao contrario
                letters_original_drow.append(dot_of_the_time)
                original_un_drow = "".join(letters_original_drow)
                original_sentence[sentence.index(word)] = original_un_drow
                sentence[sentence.index(word)] = un_drow
    elif new_command == "R":
        old_word = input()
        old_word = old_word.lower()
        new_word = input()
        new_word_low = new_word.lower()
        for word in __sentence__:
            if word[-1] in dot_and_his_friends:
                word_aux = word[:len(word)-1]
                original_word_aux = original_sentence[sentence.index(word)][:len(word)-1]
                dot_of_the_time = word[-1]
            else:
                word_aux = word
                original_word_aux = original_sentence[sentence.index(word)]
                dot_of_the_time = ""
            if word_aux == old_word:
                original_sentence[sentence.index(word)] = new_word+dot_of_the_time
                sentence[sentence.index(word)] = new_word_low+dot_of_the_time
    elif new_command == "Q":
        quit()
    __sentence__ = sentence[:]
    original_sentence2str = " ".join(original_sentence)
    #sentence2str = " ".join(__sentence__)
    #print(sentence2str)
    print(original_sentence2str)
