import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        print("Arquivo vazio")  # debug
        return
    
    print("Data lida:", data)  # debug

    # código aqui:  
    n = int(data[0])
    A = list(map(int, data[1:1+n]))
        
    # debug    
    print("N =", n) 
    print("Lista =", A)
    
   
    soma = 0
    for num in A:
        if num % 2 == 0:
            soma += num
    pass
    
    print("SOMA =", soma)  # print final

if __name__ == "__main__":
    solve()