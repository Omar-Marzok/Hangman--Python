lst=('b','a','n','a','n','a')
in_li = ['0']
remander_times = 6
im=['_','_','_','_','_','_']
print ("-------- Fruits ---------")
print (*im)

while 1 :
        letter = input("Enter a letter : ")
        if letter.isalpha() and len(letter) == 1:
            print("valid input")
        else:
            print("invalid input")
            continue
        letter=letter.lower()

        if letter in in_li:
            print("you enter this leeter before choose anothe one.")
            continue
        in_li.append(letter)
        
        if letter in lst:
            for index, elem in enumerate(lst):
                if elem == letter:
                    im[index] = letter
            print(*im)
        else:
            remander_times= remander_times-1
            if remander_times == 0:
                print("game over")
                break
            else:
                print(f'remander times = {remander_times}')
        
        if '_' in im:
            continue
        else:
            print("congratulations")
            break
print("END")  