ancestor(X,Y):- parent(X,Y).
ancestor(X,Y):- parent(X,Z), ancestor(Z,Y).
parent(sai,ram).
parent(ram,krishna).
parent(ram,devi).
