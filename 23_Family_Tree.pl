female(sita).
female(radha).

male(ram).
male(krishna).

parent(sita,ram).
parent(radha,krishna).

mother(X,Y):- parent(X,Y), female(X).
father(X,Y):- parent(X,Y), male(Y).
sister(X,Y):- parent(Z,X), parent(Z,Y), female(X),X\==Y.
brother(X,Y):- parent(Z,X), parent(Z,Y), male(X),X\==Y.
