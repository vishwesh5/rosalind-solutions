let rec fib n = 
    if n = 2 || n = 1 then 1
    else fib (n-1) + fib(n-2);;

fib 24;;
