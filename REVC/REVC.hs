module REVC where

symComplement :: Char -> Char
symComplement 'A' = 'T'
symComplement 'T' = 'A'
symComplement 'C' = 'G'
symComplement 'G' = 'C'
symComplement _ = 'z'

complement :: String -> String
complement = map symComplement

main = do
        lines <- readFile "data.txt"
        let revc = (reverse . complement) $ filter (/= '\n') lines
        putStrLn revc
