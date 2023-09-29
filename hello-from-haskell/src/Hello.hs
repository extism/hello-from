module Hello where

import Extism.PDK
import Data.Int

hello :: IO Int32
hello = do
  s <- input
  output (s ++ "\nHello from Haskell!")
  return 0 

foreign export ccall "hello" hello ::  IO Int32
