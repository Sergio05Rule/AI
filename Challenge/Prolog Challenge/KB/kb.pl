% Knowledge Base e nozioni Base Prolog

/* variabili */
% Qualsiasi elemento inizi con la notazione ( "_something" or ("Something"));
% tutte le costanti della KB sono espresse in numeri "2" o strighe minuscole "goal", "mario", "silvia".
% Le ',' rappresentano un "AND" logico sono quindi congiunzioni
% i '.' rappresentano un "OR" logico sono quindi i termina sentences

/* Print e Scan di una Variabile */
% write($A). Per LEGGERE il valore della variabile
% read(A). Per SCRIVERE il valore della variabile

/* Trace */
% per attivare il trace digita il comando "trace."
% per attivare il trace digita il comando "notrace."
% il trace mostra come prolog implementa il Backward chaining (or backward reasoning):
% attraverso tutto l'albero e verifico se la mia condizione finale è vera, a quel punto posso fermarmi'

/* Hello World! */
% Alla query se voglio vedere tutti i male: "male(X)"  uso ";" per non fermarsi al primo risultato;
% In questo caso "X = sergio, True.", sempre prima occorrenza nella KB. E quindi IMPORTANTE l ordine delle istruzioni nella KB !
% Si può notare ancora meglio attraverso "trace" come "X = hi" venga totalmente ignorata nella risoluzione della Query
% Ovviamente le nostre Query accettano solo due risultati "True" or "False" !
% X = hi.
male(sergio). % Arity = 1
male(sergiojr).
male(marco).
female(maria).

/* Funzioni -> Functor e Chiamate -> Complex terms */
% Le funzioni "male()" e "female()" sono detti FUNCTOR
% Le funzioni "male(sergio), ..." e "female(maria), ..." sono detti COMPLEX TERMS con Arity = 1.

% definisco i parent e successivamente da parent la funzione child
parent(sergio,marco).  % Arity = 2
parent(sergio,maria).
parent(ciccio,marco).  % Arity = 2
parent(ciccio,maria).
parent(sergiojr,sergio).
child(X,Y) :- parent(Y,X).

% Come sfrutto il debug offerto dal Trace ?
/* DEBUG parent(_,_) restituisce sempre "True" per le n occerrenze VERE.
[trace]  ?- parent(_,_).
   Call: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(sergio, marco) ? c
*/

/* DEBUG parent(_,X) restituisce tutte le variabili X che rispettano il Complex Term ( marco, maria, marco, maria, sergio) ovviamente nelle loro ripetizioni!
[trace]  ?- parent(_,X).
   Call: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(sergio, marco) ? creep
X = marco ;
   Redo: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(sergio, maria) ? creep
X = maria ;
   Redo: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(ciccio, marco) ? creep
X = marco ;
   Redo: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(ciccio, maria) ? creep
X = maria ;
   Redo: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(sergiojr, sergio) ? creep
X = sergio.
*/

/* Maniera ottimale per un veloce debug
[trace]  ?- parent(FIGLIO, GENITORE).
   Call: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(sergio, marco) ? creep
FIGLIO = sergio,
GENITORE = marco ;
   Redo: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(sergio, maria) ? creep
FIGLIO = sergio,
GENITORE = maria ;
   Redo: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(ciccio, marco) ? creep
FIGLIO = ciccio,
GENITORE = marco ;
   Redo: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(ciccio, maria) ? creep
FIGLIO = ciccio,
GENITORE = maria ;
   Redo: (8) parent(_7000, _7002) ? creep
   Exit: (8) parent(sergiojr, sergio) ? creep
FIGLIO = sergiojr,
GENITORE = sergio.
*/

/* Complex Terms avanzati */
% CT che restituisce il papa e mamma crati sfruttando CT esistenti in "AND"
dad(Y, X) :- parent(Y, X), male(X).
mom(Y, X) :- parent(Y, X), female(X).

/* Grafo */
arco(a,d).
arco(d,c).
arco(b,a).
arco(b,d).
arco(c,goal).

path(X,Y) :- arco(X,Y).
path(X,Y) :- arco(X,Z), arco(Z,Y).
% nota bene, lui ripete arco al massimo due volte, il functor dovrebbe chiamarsi path2(_) infatti: path(b,c) -> True ; path(b,goal) -> False


/* Funzioni Matematiche */
% Fattoriale -> factorial(Numberinput, Result).

factorial(0,1).
factorial(N,R):- N1 is N - 1,
                factorial(N1,R1),
                R is N*R1.

% even & odd (Pari e dispari)
even(0).
even(N):- N1 is N - 2,
          N1 >= 0,
          even(N1).

odd(1).
odd(N):- N1 is N - 2,
        N1 >= 0,
        odd(N1).

% power potenza
power(N,1,N).
power(N,E,R) :- E1 is E - 1,
                power(N,E1,R1),
                R is N*R1.

/* Liste in Prolog */

% funzione che verifica se un elemento è presente in una lista
member(E,[H|_]) :- E = H.
member(E, [_|T]) :- member(E,T).

% funzione che copia L1 = L2
copylist([],[]).
copylist([H1|T1],[H2|T2]) :- H1 = H2, copylist(T1,T2).

% append to a list #TODO perchè non funziona correttamente?
insert_element([],E , T2):- T2 = E.
insert_element([H1|T1],E,[H2|T2]) :- H2 = H1, insert_element(T1,E,T2).

% NB: forma più compatta con assegnazioni implicite nelle chiamate: (H2=H1 espressa attraverso H=H)!
append2([],X,X).
append2([H|T1],X,[H|T2]):- append2(T1,X,T2).

% Append di UN SOLO elemento in TESTA
addelem(OLDL , EL , NEWL):- NEWL = [EL|OLDL].

% Somma degli elementi di una lista
suml([],0).
suml([H|T],R) :- suml(T,R1),
                  R is R1 + H.

% Conta degli elementi di una lista
countl([],0).
countl([_|T],R) :- countl(T,R1),
                  R is 1 + R1 .

% rimozione PRIMA OCCORENZA di un elemento dalla lista. (el,source,dest)
remove(E,[E|T1],T1).
remove(E,[A|B],[A|D]):- remove(E,B,D).

% rimozione TUTTE LE OCCORENZA di un elemento dalla lista #TODO non elimina istanze multiple (perchè?)
remove_all(_,[],[]).
remove_all(E,[E|T],[_|T2]):- remove_all(E,T,T2).
remove_all(E,[A|B],[A|D]):- remove_all(E,B,D).

% regola per il successore di un elemento nella lista
successor([EL|[H2|_]],EL,H2).
successor([_|T],EL,R) :- successor(T,EL,R).

% divide una lista in due nuove, dove l ultimo elemento della prima nuova lista sarà EL
divide([EL|T],EL,[EL|_],[T|_]).
divide([H|T],EL,[H|T2],L2):- divide(T,EL,T2,L2).

% verifica se tutti gli elementi di una lista sono uguali
allequals([H|T]):- equals(H,T).

equals(_,[]).
equals(E,[E|T]):- equals(E,T).
/* se trova un H diverso da E retur false altrimenti si chiama ricorsivamente con la coda */

% verifica che tutti gli elementi della lista siano diversi
alldiff([]).
alldiff([H|T]):- diff(H,T), alldiff(T).

diff(_,[]).
diff(E,[H|T]):- not(E=H),diff(E,T).

% regola che restituisce l ultimo elemento della lista
lastl([L],L).
lastl([_|T],R):- lastl(T,R).

/* NB: Scomporre sempre il porblema il sottoproblemi ATOMICI */
% regola che controlo se l elemento di partenza di una lista è il più piccolo presente in quest ultima
min(_,[]).
min(E,[H|T]):- E=<H, min(E,T).

% scrivere una regola che trovi il minimo di una lista.
% la prima regola dice che se l H della lista è il minimo lo riporto come da rule "min"
% altrimenti se cosi non è chiamo la seconda regola
findmin([H|T],H):- min(H,T).
findmin([H|T],Min):- not(min(H,T)),
                      findmin(T,Min).

% sorting list. (list, sortedlist).
sort_l([],[]).
sort_l(List,[Min|T2]):- findmin(List,Min),
                      remove(Min,List,NL),
                      sort_l(NL,T2).

% Inverso di una lista (oldl,newl).
mirror([],[]).
mirror(L1,[X|T2]):- last(L1,X),
                    remove(X,L1,NL),
                    mirror(NL,T2).

% regola che trova i-esimo elemento della lista (Lista, PosizioneNellaLista, INDEX). ([1,2,3],2,X).
item([E|_],1,E).
item([_|T],I,E):- Ind is I-1,
                  item(T,Ind,E).

% regola che trova l indice di una lsta, dato l elemento. index_l([a,b,c,c,c,d],d,X). X=6.
index_l([E|_],E,1).
index_l([_|T],E,N):- index_l(T,E,Ind),
                   N is Ind+1.

% regola che effettua il merge di due liste. merge([3,1],[2,4],X). X = [2, 3, 1, 4]. NB seleziona il minore H tra le due liste.
merge([],L2,L2).
merge(L1,[],L1).
merge([X|T1],[Y|T2],[X|T]):- X<Y, merge(T1,[Y|T2],T).
merge([X|T1],[Y|T2],[Y|T]):- X>Y, merge([X|T1],T2,T).

% regola che effettua il merge-sort tra due Liste
merge_sort(V1,V2,Dest):- sort_l(V1,V1ord),
                         sort_l(V2,V2ord), merge(V1ord,V2ord,Dest).

% regola che conta le occorrenze (anche ripetute) di elementi non presenti nella prima lista rispetto alla seconda. notpresent(L1,L2,COUNT).
notpresent([],_,0).
notpresent([H1|T1],L2,N):-  notpresent(T1,L2,Num),
                            diff(H1,L2),
                            N is Num+1.
notpresent([H1|T1],L2,N):- notpresent(T1,L2,N),
                            not(diff(H1,L2)).

/* Classic notation            Prolog Notation */
% 6+2=8                       8 is 6+2.
% 6*2=12                      12 is 6*2.
% 6-2=4                       4 is 6-2.
% 6-8=-2                      -2 is 6-8.
% 6 /2 =3                     3 is 6/2.
% 7 mod 2 = 1                 1 is mod(7,2).

/* Classic notation            Prolog Notation */
% x <= y                        x =< y
% x >= y                        x >= y
% x = y                         x =:= y
% x != y                        x =\= y
