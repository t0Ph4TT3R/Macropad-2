import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules macros import Press, Release, Tap, Marcos

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D6, board.D8, board.D9, board.D10]

keyboard.matrix = KeysScanner(
  pins = PINS,
  value_when_pressed = false,
)

copy = (
  Press(KC.LCTL),
  Tap(KC.C),
  Release(KC.LCTL),
)

paste = (
  Press(KC.LCTL),
  Tap(KC.V),
  Release(KC.LCTL),
)

select_all = (
  Press(KC.LCTL),
  Tap(KC.A),
  Release(KC.LCTL),
)

keyboard.keymap = [
  #[KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC,Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD]
  [KC.ENTER, KC.LEFT_ARROW, KC.ESC, KC.UP_ARROW, KC.DOWN_ARROW, select_all, KC.BACKSPACE, KC.RIGHT_ARROW, KC.TAB, paste, copy]
]

if __name__ == '__main__':
  keyboard.go()
