module SUBS where
import qualified Data.ByteString.Char8 as B
import qualified Data.List as D

-- The perceived hackiness of this code increases quadratically as a function 
-- of the number of characters you read. In hindsight, this program is more
-- coercing Haskell and its built-in features into doing what I wanted, then
-- and algorithm challenge. Alas, "it works"

main = do
    raw <- fmap lines $ readFile "data.txt"
    let s = B.pack $ raw !! 0
    let t = B.pack $ raw !! 1
    let result = D.intersperse " " $ map (show . (+1)) $ B.findSubstrings t s
    putStrLn (show (concat result))
