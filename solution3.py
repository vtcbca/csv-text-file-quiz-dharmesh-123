with open('bca.txt','w') as bca:
    bca.write(bca_info)

A = 0
B = 0
C = 0

from csv import reader

with open('intro.txt','r' ) as intro:
    bca = intro.readlines()

    for i in bca:
        stripped_i = i.strip()

        if stripped_i:
            first_character = stripped_i[0]
            if first_character =="A":
                A +=1
            elif first_character =="B":
                B +=1
            elif first_character =="C":
                C +=1

print(f"Character Starting With An A : {A}")
print(f"Character Starting With B :{B}")
print(f"Character Starting With C :{C}")




