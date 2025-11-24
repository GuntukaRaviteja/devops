from collections import deque
g={}
for i in range(int(input("enter number of nodes"))):
  u,v=input("edges(u,v)").split()
  g.setdefault(u,[]).append(v)
  g.setdefault(v,[]).append(u)

s=input("enter starting node")

v={s}
q=deque([s])

while q:
  x=q.popleft()
  print(x,end=" ")
  for i in g.get(x,[]):
    if i not in v:
      v.add(i)
      q.append(i)
      print(q)
  
  
  