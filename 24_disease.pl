symptom(murali, fever).
symptom(murali, cold).
symptom(murali, cough).
symptom(murali, difficulty_in_breathing).

symptom(krishna, fever).
symptom(krishna, sneezing).
symptom(krishna, headache).
symptom(krishna, bodypains).

symptom(mohan, fever).
symptom(mohan, cold).
symptom(mohan, platelets_reduction).

hypothesis(Patient, covid):-
	symptom(Patient, fever),
	symptom(Patient, cold),
	symptom(Patient, cough),
	symptom(Patient, difficulty_in_breathing),
	write('Follow quarentine for 15 days').

hypothesis(Patient, normal_fever):-
	symptom(Patient, fever),
	symptom(Patient, sneezing),
	symptom(Patient, headache),
	symptom(Patient, bodypains),
	write('Eat healthy food').

hypothesis(Patient, dengue):-
	symptom(Patient, fever),
	symptom(Patient, cold),
	symptom(Patient, platelets_reduction),
	symptom(Patient, throat_pain),
	write('Do the blood test immediately'),
	write('Eat fruits and drink fruit juices frequently').
