; ejercicio3
(declare-const a1 Real)
(declare-const a2 Real)
(declare-const a3 Real)
(assert (= a1 (mod 16 2)));
(assert (= a2 (div 16 4)));
(assert (= a3 (rem 16 5)));
(check-sat)
(get-model)


;sat (a2 = 4.0, a1=0.0. a3=1.0)
