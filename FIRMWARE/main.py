import board
from kb import keyboard, encoder_handler
from kmk.keys import KC
from kmk.modules.layers import Layers

layers_mod = Layers()
keyboard.modules.append(layers_mod)

_______ = KC.TRNS  # transparent — falls through to layer below
XXXXXXX = KC.NO    # blocked — does nothing

BASE = 0
FN   = 1

keyboard.keymap = [

    [
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,
        KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.PSCR, KC.SLCK, KC.PAUS,
        XXXXXXX,

        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,
        KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.INS,  KC.HOME,
        KC.PGUP,

        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,
        KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL,  KC.END,
        KC.PGDN,

        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,
        KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,

        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,
        KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, XXXXXXX, XXXXXXX, XXXXXXX, KC.UP,
        XXXXXXX,

        KC.LCTL, KC.LGUI, KC.LALT, XXXXXXX, XXXXXXX, KC.SPC,  XXXXXXX, KC.RALT,
        KC.MO(FN), KC.RCTL, XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN, KC.RGHT,
        XXXXXXX,
        KC.MUTE,  
    ],

    [
        _______, KC.MPLY, KC.MSTP, KC.MPRV, KC.MNXT, KC.MUTE, KC.VOLD, KC.VOLU,
        KC.BRID, KC.BRIU, _______, _______, _______, _______, _______, _______,
        XXXXXXX,

        _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, KC.DEL,  _______, _______,
        _______,

        _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, _______, _______, _______,
        _______,

        _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,

        _______, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, XXXXXXX, XXXXXXX, XXXXXXX, _______,
        XXXXXXX,

        _______, _______, _______, XXXXXXX, XXXXXXX, _______, XXXXXXX, _______,
        _______, _______, XXXXXXX, XXXXXXX, _______, _______, _______,
        XXXXXXX,
        _______,
    ],
]

encoder_handler.map = [
    # BASE — rotate for volume
    ((KC.VOLD, KC.VOLU),),
    # FN — rotate for track prev/next
    ((KC.MPRV, KC.MNXT),),
]

if __name__ == '__main__':
    keyboard.go()