(ns rosalind.core)

(def probs '(1, 1, 1, 0.75, 0.5, 0))

(def nums '(17149 19383 19283 16766 17766 18667))

(defn multiply-together
  [x]
  (reduce * x))

(defn Expected-Value
  []
  (* 2 (reduce + (map multiply-together (map list nums probs)))))
