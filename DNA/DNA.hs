module DNA where

count :: Char -> String -> Int
count ch str = length $ filter (\x -> x == ch) str

printNum :: Int -> IO ()
printNum x = do putStr $ (show x) ++ " "

main = do
        lines <- readFile "data.txt"
        let a = count 'A' lines
        let c = count 'C' lines
        let g = count 'G' lines
        let t = count 'T' lines
        printNum a
        printNum c
        printNum g
        putStr (show t)
