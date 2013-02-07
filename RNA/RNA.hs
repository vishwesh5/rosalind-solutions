module RNA where

main = do
        lines <- readFile "data.txt"
        let rna = map (\x -> if x == 'T' then 'U' else x) lines
        putStrLn rna
