sum_list([], 0).  % Базовый случай: сумма пустого списка равна 0

sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),  % Рекурсивно считаем сумму оставшейся части списка
    Sum is Head + TailSum.   % Сумма списка равна голове плюс сумма оставшейся части

?- sum_list([1, 2, 3, 4, 5], Sum).
% Sum = 15.

?- sum_list([10, 20, 30], Sum).
% Sum = 60.

?- sum_list([], Sum).
% Sum = 0.