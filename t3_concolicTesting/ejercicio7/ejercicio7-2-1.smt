(declare-const k Real)
(assert (< 0 3))
(assert (not (= (+ 5.0 k) 0.0)))
(assert (< 1 3))
(assert (not (= (+ 1.0 k) 0.0)))
(assert (not (< 2 3)))
(check-sat)
(get-model)