# problema 8
def is_prime(x):
    '''

    :param x: numarul pe care il verificam daca este prim
    :return: returneaza true daca x e prim si false daca x nu este prim

    '''
    if x < 2:
        return False
    elif x == 2:
        return False
    for i in range(3,(x//2)+1,1):
        if x % i == 0:
            return False
    return True

def get_longest_sum_is_prime(list):
    '''

    :param list: lista din care determinam subsecventa ceruta
    :return: subsecventa ceruta
    '''

    sum = 0
    max = 0 # max = lungimea maxima a subsecventei
    head = end = 0 #head = indicele de inceput al subsecventei selectate; end = indicele de sfarsit
    list2 = [] #subsecventa selectata la final
    for i in range(0, len(list), 1):
        sum = sum + list[i]
    if is_prime(sum) == True:
        return list
    else:
        for i in range(0,len(list),1):
            sum1 = sum
            for j in range(len(list) - 1, -1, 1):
                sum1 = sum1 - list[j]
                if is_prime(sum1) == True:
                    x = j
                    break
            if is_prime(sum1) == True:
                length = x - i + 1  #length = lungimea subsecventei luata in calcul
                if length > max:
                    max = length
                    head = i
                    end = x
            sum = sum - list[i]
        for i in range(head, end, 1):
            list2.append(list[i])
        return list2

def read(list):
    n = int(input("Dimensiune lista: "))
    for i in range(0,n,1):
        list.append(int(input("Itroduceti un element: ")))
def print_lista(list):
    for i in range(0,len(list),1):
        print(list[i])

def test_is_prime():
    assert is_prime(2) == False
    assert is_prime(3) == True
    assert is_prime(1) == False
    assert is_prime(19) == True
    assert is_prime(21) == False
    assert is_prime(29) == True
    assert is_prime(200) == False
    assert is_prime(101) == True
def is_digit_count_desc(x):
    '''

    :param x: verifica daca cifrele lui x sunt in ordine descrescatoare
    :return: True daca x are cifrele in ordine descrescatoare, si false daca nu

    '''
    k = x % 10
    x = x // 10
    while x != 0:
        if x % 10 < k:
            return False
        else:
            k = x % 10
            x = x // 10
    return True

def get_longest_digit_count_desc(list):
     max = 0
     head = end = 0
     list2 = []

     for i in range(0,len(list),1):
         if is_digit_count_desc(list[i]) == True:
             for j in range(i + 1, len(list),1):
                 if is_digit_count_desc(list[j]) == False:
                     break
             length = j - i + 1
             if length > max:
                 max = length
                 head = i
                 end = j
     for i in range(head, end, 1):
         list2.append(list[i])
     return list2
def test_is_digit_count_desc():
       assert is_digit_count_desc(987654321) == True
       assert is_digit_count_desc(1224) == False
       assert is_digit_count_desc(31) == True
       assert is_digit_count_desc(90876) == False
       assert is_digit_count_desc(23456543) == False

def main():
    list = []
    read(list)
    while True:
        print('1.Secveta de lungime maxima de numere prime')
        print('2.Secventa de lungime maxima de numere cu cifre in ordine descrescatoare')
        print('3.Exit')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            print_lista(get_longest_sum_is_prime(list))
        if optiune == '2':
            print_lista(get_longest_digit_count_desc(list))
        if optiune == '3':
            break
        else:
            print('optiune invalida')
test_is_prime()
test_is_digit_count_desc()
main()







