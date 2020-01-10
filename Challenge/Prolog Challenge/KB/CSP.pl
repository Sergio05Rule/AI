/* Regole per defiire la lista di PERSONE, le liste di FAMIGLIE e LITIGI -> return una o più LISTE!*/
persone([antonella,domenico,raffaella,tommaso,vincenzo,azzurra,cristiano,francesca,luigi,giovanni,marcella,daniela,nunzio,leonardo,silvia]).
famiglia([[antonella,domenico,raffaella,tommaso,vincenzo],[azzurra,cristiano,francesca,luigi]]).
litigi([[giovanni,marcella],[marcella,daniela],[luigi,leonardo]]).


/* regola principale da lanciare che guida la risoluzione del CSP
    carico le variabili in P e poi passo lo stesso P alla regola assign_to_table*/
program(L1,L2,L3) :- persone(P), assign_to_table(P,[],[],[],L1,L2,L3).


assign_to_table([],L1,L2,L3,L1,L2,L3).
assign_to_table([H|T],L1,L2,L3,L1R,L2R,L3R):-
    addTable(H,L1,L2,L3,L1N,L2N,L3N),
    famiglia(F),
    check_famiglie(F,L1N,L2N,L3N),
    litigi(L),
    check_litigi(L,L1N,L2N,L3N),
    check_lenght_tavoli(L1N,L2N,L3N),
    assign_to_table(T,L1N,L2N,L3N,L1R,L2R,L3R).

addTable(X,L1,L2,L3,[X|L1],L2,L3).
addTable(X,L1,L2,L3,L1,[X|L2],L3).
addTable(X,L1,L2,L3,L1,L2,[X|L3]).


check_lenght_tavoli(L1,L2,L3):-
    lenght_tavolo(L1,N1), N1 < 7, !,
    lenght_tavolo(L2,N2), N2 < 7, !,
    lenght_tavolo(L3,N3), N3 < 7, !.

lenght_tavolo([],0).
lenght_tavolo([_|T],N):-
    lenght_tavolo(T,N1),
    N is N1 + 1.

check_famiglie([],_,_,_).
check_famiglie([F|T],L1,L2,L3):-
    check_famiglia(F,L1,L2,L3,R1,R2,R3),
    check_count(R1,R2,R3),
    check_famiglie(T,L1,L2,L3), !.

check_count(_,0,0).
check_count(0,_,0).
check_count(0,0,_).

check_famiglia([],_,_,_,0,0,0).
check_famiglia([H|T],L1,L2,L3,R11,R21,R31):-
    check_membro_famiglia(H,L1,R12),
    check_membro_famiglia(H,L2,R22),
    check_membro_famiglia(H,L3,R32),
    check_famiglia(T,L1,L2,L3,R1,R2,R3),
    R11 is R1 + R12, R21 is R2 + R22, R31 is R3 + R32.

check_membro_famiglia(_,[],0):- !.
check_membro_famiglia(M,[M|_],1):- !.
check_membro_famiglia(M,[_|T],R) :- check_membro_famiglia(M,T,R),!.


check_litigi([],_,_,_).
check_litigi([H|T],L1,L2,L3):-
    check_famiglia(H,L1,L2,L3,R1,R2,R3),
    check_litigio(R1,R2,R3),
    check_litigi(T,L1,L2,L3), !.

check_litigio(C1,C2,C3):-
    C1 < 2, !,
    C2 < 2, !,
    C3 < 2, !.
