wall(1,1).
dim(3).
startX(0).
startY(0).
endX(2).
endY(0).


action(X,Y,1):-
    not(wall(X,Y)),
    result(X,Y,1,N,M),
    check(N,M).
action(X,Y,2):-
    not(wall(X,Y)),
    result(X,Y,2,N,M),
    check(N,M).
action(X,Y,3):-
    not(wall(X,Y)),
    result(X,Y,3,N,M),
    check(N,M).
action(X,Y,4):-
    not(wall(X,Y)),
    result(X,Y,4,N,M),
    check(N,M).


result(X,Y,1,N,M):-
    N is X,
    M is Y+1,!.

result(X,Y,2,N,M):-
    N is X+1,
    M is Y,!.

result(X,Y,3,N,M):-
    N is X-1,
    M is Y,!.

result(X,Y,4,N,M):-
    N is X,
    M is Y-1,!.

check(X,Y):-
    dim(D),
    X > -1,
    X < D,
    Y > -1,
    Y < D,
    not(wall(X,Y)),!.

add_visited(X,Y,L,L1):-
    tuple(X,Y,V),
    insert(V,L,L1).

check_visited(X,Y,L):-
    tuple(X,Y,V),
    not(is_in(V,L)),!.

is_in(H,[H|_]):-!.
is_in(X,[H|T]):-
    X \= H,!,
    is_in(X,T),!.

insert(X,[],[X]):-!.
insert(X,L,[X|L]):-!.

tuple([]).
tuple(X,Y,[X|T]):-
    tuple(Y,T).
tuple(Y,[Y|T]):-
    tuple(T).


find_path(Path):-
	startX(Sx),
    startY(Sy),
    add_visited(Sx,Sy,[],Visited),
   	find_path(Sx,Sy,Path,Visited).

find_path(Sx,Sy,[],_):-
    endX(Sx),
    endY(Sy).

find_path(Sx,Sy,[H|T],Visited):-
    action(Sx,Sy,Act),
    result(Sx,Sy,Act,SNx,SNy),
    check_visited(SNx,SNy,Visited),
    add_visited(SNx,SNy,Visited,NVisited),
    H is Act,
    find_path(SNx,SNy,T,NVisited).
