on(floor,monkey).
on(floor,chair).
in(room,monkey).
in(room,chair).
in(room,banana).
at(cieling,banana).
strong(monkey).
grasp(monkey).
climb(monkey,chair).
push(monkey,chair):- strong(monkey).
under(banana,chair):- push(monkey,chair).

canreach(banana,monkey):-
	on(floor,banana),
	in(room,banana),
	at(cieling,banana),
	under(banana,chair),
	climb(banana,chair).

canget(banana,monkey):-
	canreach(banana,monkey),grasp(monkey).
