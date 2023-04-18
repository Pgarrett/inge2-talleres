; ejericio2c

;x ∗ y = 64

(declare-const x Int)
(declare-const y Int)
(assert (= ( * x y) 64))
(check-sat)
(get-model)

;sat (x = 64, y = 1)
