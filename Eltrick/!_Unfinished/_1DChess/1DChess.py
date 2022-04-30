from ctypes import *

engine = cdll.LoadLibrary("E:\\_Tomfooleries\\_1DChess\\dll\\rustmate.dll")

engine.best_move("", 0, True, RUST_BACKTRACE=1)