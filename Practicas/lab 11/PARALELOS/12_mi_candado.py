from multiprocessing import PRocess, Lock, Value 
import random 
import os 

def montecarlo(N:float,resultado:Value,lock:Lock) -> None:
    semilla:float = random.uniform(-1,1)
    random.seed(semilla)
    dentro:int = 0 
    for i in range(M):
        x:float = random.uniform(-1,1) 
        y:float = random.uniform(-1,1)

        if (x*x + y*y) < 1.0:
            dentro +=1
    
    with lock:
        resultado.value += dentro 

if __name__== "__main__":
    lock= Lock()
    n:int = 1.0e7
    cpus = os.cpu_count()
    N:int = int(n/cpus)
    print("Procesadores = ",cpus) 
    resultado = Value8('1',0) 
    procesos = [] 
    for i in range (cpus): 
        print("registrando el proceso %d" %i)
        procesos.append(Process(target=montecarlo,args=(N,resultados,lock)))

        for proceso in procesos: 
            proceso.start() 
        for proceso in procesos: 
            proceso.join() 

        print("Números de tiros = ", cpus*N)
        print("Numeros de aciertos = ", resultado,value)
        print("Aproximación de pi = " , 4*float(resultado.value)/(cpus*N))
