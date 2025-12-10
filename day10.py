import re
from itertools import combinations
import pulp

def solve_integer_min_sum(A, b):
    """
    Löst das LGS A*x = b mit x >= 0 und ganzzahlig
    und findet die Lösung mit minimaler Summe.
    
    A: Liste von Listen (m Gleichungen, n Variablen)
    b: Liste der rechten Seiten (m Werte)
    """
    
    m = len(A)       # Anzahl Gleichungen
    n = len(A[0])    # Anzahl Variablen

    # Variablen x0, x1, ..., x(n-1) (alle >=0 und ganzzahlig)
    xs = [
        pulp.LpVariable(f"x{i}", lowBound=0, cat=pulp.LpInteger)
        for i in range(n)
    ]

    # Problem definieren
    problem = pulp.LpProblem("LGS_min_sum_integer", pulp.LpMinimize)#"min_sum_solution"

    # Zielfunktion: min Summe aller Variablen
    problem += sum(xs)

    # Gleichungen hinzufügen
    print(A)
    print(b)
    
    for eq_index in range(m):
        problem += pulp.lpSum(A[eq_index][j] * xs[j] for j in range(n)) == b[eq_index]

    # Lösen
    problem.solve()

    status = pulp.LpStatus[problem.status]
    solution = [int(x.value()) for x in xs]
    total = int(sum(solution))

    return status, solution, total



result1,result2=0,0
with open("in10.txt") as file:
    while line := file.readline().strip('\n'):
        #reading
        length=len(re.findall(r"\[(.*?)\]", line)[0])
        lights=0
        goal=re.findall(r"\[(.*?)\]", line)[0].replace('.','0').replace('#', '1')
        buttons=[]
        for button in re.findall(r"\((.*?)\)", line):
            temp=list('0'*length)
            for butt in button.split(','):
                temp[int(butt)]='1'
            buttons.append(''.join(temp))
        goal2=re.findall(r"\{(.*?)\}", line)[0].split(',')
        goal2 = [int(x) for x in goal2]
        #buttoning
        solutions=[]
        for r in range(len(buttons) + 1):
            for combo in combinations(buttons, r):
                lights=0
                for comb in combo:
                    lights=lights^int(comb, 2)
                if lights==int(goal, 2):
                    solutions.append(len(combo))
        result1+=min(solutions)
        #print(length,buttons)
        
        M = [[int(c) for c in row] for row in buttons]
        MT = list(zip(*M))
        MT = [list(col) for col in MT]
        #print(MT)
          
           
        
        status, solution, total = solve_integer_min_sum(MT, goal2)
        #print("Status:", status)
        #print("Lösung:", solution)
        #print("Minimale Summe:", total)
        result2+=total
#(3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}        
        
#3=e+f
#5=b+f
#4=a+c+d+e
#7=b+d
        
print(result1, result2)