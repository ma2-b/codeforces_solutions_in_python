n = int(input())
count=0
for i in range(n):
    faces = input()
    if faces == "Icosahedron":
        count+=20
    elif faces == "Cube":
        count+=6
    elif faces == "Tetrahedron":
        count+=4
    elif faces == "Dodecahedron":
        count+=12
    elif faces == "Octahedron":
        count+=8
print(count)