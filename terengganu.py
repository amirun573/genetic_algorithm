def randomize(x):

    size = x

    cities = ['A','B','C','D','E','F','G','H','I','J','K','L']
    population = []
    
    for i in range(size):
        x = random.sample(cities, len(cities))
        population.append(x)

    return population
def return_location_Reverse(x):
    
    new=[]
    for i in x:
        
        if(i=="A"):
            new.append("Kuala Terengganu")
        elif(i=="B"):
            new.append("Kuala Berang")
        elif(i=="C"):
            new.append("Bandar Permaisuri")
        elif(i=="D"):
             new.append("Jertih")
        elif(i=="E"):
             new.append("Kampung Raja")
        elif(i=="F"):
             new.append("Marang")
        elif(i=="G"):
             new.append("Dungun")
        elif(i=="H"):
             new.append("Paka")
        elif(i=="I"):
             new.append("Kertih")
        elif(i=="J"):
             new.append("Kemasik")
        elif(i=="K"):
            new.append("Kijal")
        elif(i=="L"):
            new.append("Chukai")
    
    print("<br/><h2>Shortest Path</h2><br/><h3>",'->'.join(new),":",x[12],"km</h3>")
    #displayRoute(a)
    #return a   #print("<a href=www.google/maps/dir/",",".join(new),">Visit Here</a>")
    #print("<a href=",new,">Visit Here</a>")
    

def return_location(x):
    if(x.lower()=="kuala terengganu"):
       return "A"
    elif(x.lower()=="kuala berang"):
        return "B"
    elif(x.lower()=="bandar permaisuri"):
        return "C"
    elif(x.lower()=="jertih"):
        return "D"
    elif(x.lower()=="kampung raja"):
        return "E"
    elif(x.lower()=="marang"):
        return "F"
    elif(x.lower()=="dungun"):
        return "G"
    elif(x.lower()=="paka"):
        return "H"
    elif(x.lower()=="kertih"):
        return "I"
    elif(x.lower()=="kemasik"):
        return "J"
    elif(x.lower()=="kijal"):
        return "K"
    elif(x.lower()=="cukai"):
        return "L"

def distance(population):
    a=0
    b=0
    new_pop = []
    for i in range(len(population)):
        for j in range(12):
            if population[i][j:j+2] in sat :
               temp= sat.index(population[i][j:j+2])
               a=a + int(distances[temp][2])
               #print(str(population[i][j:j+2])+":"+str(int(distances[temp][2])))     
            elif population[i][j:j+2][::-1] in sat:
                temp=sat.index(population[i][j:j+2][::-1])
                a=a + int(distances[temp][2])
                #print(str(population[i][j:j+2][::-1])+":"+str(int(distances[temp][2])))
        #print(a)
        population[i].insert(len(population[i]),a)
        a=0
    return population

def sort_(solution):

    solution = sorted(solution,key=fit)

    return solution

def fit(element):
    return element[12]

def swapMutation(children):

    mutated = []
    
    for swapped in range(len(children)):
        
        x=secrets.randbelow(len(children[swapped][:11]))
        y=secrets.randbelow(len(children[swapped][:11]))

        while(x==y):
            y=secrets.randbelow(len(children[swapped][:11]))
        
        city1= children[swapped][x]
        #print(city1)
        city2=children[swapped][y]
        #print(city2)
        

        children[swapped][x]=city2
        children[swapped][y]=city1

        mutated.append(children[swapped])
        
    return mutated
        
def crossover(solution,n):

    results = []
    even = False
    if n % 2 == 0:
        even = True
    print()    
    for x in range(0,n,2):
        parent1 = solution[x]
        parent2 = solution[x+1]
        limit = random.sample(range(11), 2)

        start = min(limit[0],limit[1])
        end = max(limit[0],limit[1])
        children1 = []
        children2 = []
        index = 0
        for i in range(12):
            if i in range(start,end):
                children1.append(parent1[index])
                children2.append(parent2[index])
            else:
                children1.append('')
                children2.append('')
            index = index + 1
            
        index = end
        for i in range(12-(end-start)):
            index2 = end
            for t in range(12):
                if parent2[index2] not in children1:
                    children1[index] = parent2[index2]
                    break
                index2 = index2 + 1
                if index2 == 12:
                    index2 = 0
            index = index + 1    
            if index == 12:
                index = 0
        results.append(children1)
                
        index = end
        for i in range(12-(end-start)):
            index2 = end
            for t in range(12):
                if parent1[index2] not in children2:
                    children2[index] = parent1[index2]
                    break
                index2 = index2 + 1
                if index2 == 12:
                    index2 = 0
            index = index + 1    
            if index == 12:
                index = 0

        results.append(children2)
    return results


import random
import secrets
import sys
f = open("terengganu.csv")

initial = int(sys.argv[1])
n_solution = int(sys.argv[2])
n_children = int(sys.argv[3])
n_best = int(sys.argv[4])
n_iteration = int(sys.argv[5])


#read distance

distances = []
sat=[]
b=0
for line in f:
    temp = line.split(',')
    #print(temp)
    x = return_location(temp[2])
    y = return_location(temp[3])
    z = int(temp[4])
    ls = [x,y,z]
    ls2=[x,y]
    ls3=[z]
    
    distances.append(ls)
    sat.append(ls2)

population = randomize(initial)

#fitness evaluation
solution = distance(population)
solution = sort_(solution)

best_solution = solution[0]

print("<h2 class='page-header' >Distance Optimization For Road</h2><br/>")
def displayRoute(a):
    print("<div><h3>Shortest Route:</h3><h4>",a,"</h4></div>")
print("<div class='jumbotron' style='margin:40px'> <h3 class='page-header'>Initial Population</h3> <table class='text-center table table-bordered table-hover table-striped'>")

for i in solution:
    print("<tr>")
    print("<td>",i,"</td>")
    print("</tr>")
print("<tr><td>Best solution: ", best_solution,"</td></tr>")
    #print("<br/>")
print("</table> </div><br>")
#print("<div style='margin:40px'><h3>Generations</h3>")
#print("<table class='text-center table table-bordered table-hover table-striped' border='1'>")
#print("<tr><td>Best solution: ", best_solution,"</td></tr>")
#print("<br>")
nloop = n_iteration

next_gen = solution
print("<div style='margin:40px'><h3>Generations</h3>")
gen = 1
for main in range(nloop):
    
    print("<table class='text-center table table-bordered table-hover table-striped' border='1'>")

    solution = distance(next_gen)
    solution = sort_(solution)

    new_children = crossover(solution,n_children)
    new_children = swapMutation(new_children)
    
    next_gen = []
    best = n_best
    
    for i in range(best):
        next_gen.append(solution[i][0:12])

    for i in new_children:
        next_gen.append(i)

    random_numbers = random.sample(range(n_solution), n_solution-len(next_gen))
    for i in range(n_solution-len(next_gen)):
        next_gen.append(solution[random_numbers[i]][:12])
        
    solution = next_gen
    next_gen = distance(next_gen)
    
    print("<tr><td>Generation #"+str(gen)+" :</td></tr>")
    for i in next_gen:
        if best_solution[12] >= i[12]:
            best_solution = i
        print("<tr><td>",i,"</td></tr>")
    print("<tr><td>Current Best solution:  ", best_solution,"</td></tr>")
    
    #return_location_Resverse(best_solution)

    gen = gen + 1
    print("</table>")
    

return_location_Reverse(best_solution)
print("</div>")


