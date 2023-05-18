python
def min_distance(l: list[int]) -> int:
     l.sort()
    
distance = 0
for i in range(len(l)):
    distance += l[i] * i
    
return distance

offices = [10, 5, 3, 7, 2]
min_d = min_distance(offices)
print(min_d) 
