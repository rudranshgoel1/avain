import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    column_pins=(
        board.GP0,  board.GP1,  board.GP2,  board.GP3,
        board.GP4,  board.GP5,  board.GP6,  board.GP7,
        board.GP8,  board.GP9,  board.GP10, board.GP11,
        board.GP12, board.GP13, board.GP14, board.GP15,
        board.GP16,
    ),
    row_pins=(
        board.GP17, board.GP18, board.GP19,
        board.GP20, board.GP21, board.GP22,
    ),
    diode_orientation=DiodeOrientation.COL2ROW,
)

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP27, board.GP26, None, False),)

keyboard.modules.append(encoder_handler)