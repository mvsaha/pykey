key_a = 0x04
key_b = 0x05
key_c = 0x06
key_d = 0x07
key_e = 0x08
key_f = 0x09
key_g = 0x0A
key_h = 0x0B
key_i = 0x0C
key_j = 0x0D
key_k = 0x0E
key_l = 0x0F
key_m = 0x10
key_n = 0x11
key_o = 0x12
key_p = 0x13
key_q = 0x14
key_r = 0x15
key_s = 0x16
key_t = 0x17
key_u = 0x18
key_v = 0x19
key_w = 0x1A
key_x = 0x1B
key_y = 0x1C
key_z = 0x1D

key_1 = 0x1E
key_2 = 0x1F
key_3 = 0x20
key_4 = 0x21
key_5 = 0x22
key_6 = 0x23
key_7 = 0x24
key_8 = 0x25
key_9 = 0x26
key_0 = 0x27

key_return = 0x28
key_escape = 0x29
key_backspace = 0x2A
key_tab = 0x2B
key_spacebar = 0x2C
key_minus = 0x2D
key_plus = 0x2E
key_left_bracket = 0x2F
key_right_bracket = 0x30
key_backslash_pipe = 0x31
key_non_US_pound_tilde = 0x32
key_semicolon_colon = 0x33
key_quote_doublequote = 0x34
key_grave_tilde = 0x35
key_comma_gt = 0x36
key_period_lt = 0x37
key_slash_question = 0x38
key_capslock = 0x39

key_f1 = 0x3A
key_f2 = 0x3B
key_f3 = 0x3C
key_f4 = 0x3D
key_f5 = 0x3E
key_f6 = 0x3F
key_f7 = 0x40
key_f8 = 0x41
key_f9 = 0x42
key_f10 = 0x43
key_f11 = 0x44
key_f12 = 0x45

key_printscreen = 0x46
key_scroll_lock = 0x47
key_pause = 0x48
key_insert = 0x49
key_home = 0x4A
key_page_up = 0x4B
key_forward_delete = 0x4C
key_end = 0x4D
key_page_down = 0x4E
key_right_arrow = 0x50
key_left_arrow = 0x51
key_down_arrow = 0x52
key_up_arrow = 0x53

key_application = 0x65
key_power = 0x66
key_equals_plus = 0x67

key_f13 = 0x68
key_f14 = 0x68
key_f15 = 0x68
key_f16 = 0x68
key_f17 = 0x68
key_f18 = 0x68
key_f19 = 0x68
key_f20 = 0x68
key_f21 = 0x68
key_f22 = 0x68
key_f23 = 0x68
key_f24 = 0x68

key_control_left = 0xE0
key_shift_left = 0xE1
key_alt_left = 0xE2
key_gui_left = 0xE3
key_command_left = key_gui_left  # More common name

key_control_right = 0xE4
key_shift_right = 0xE5
key_alt_right = 0xE6
key_gui_right = 0xE7
key_command_right = key_gui_right


command_phrase = """hidutil property --set '{{"UserKeyMapping":[{}]}}'"""
kbsrc = '"HIDKeyboardModifierMappingSrc"'
kbdst = '"HIDKeyboardModifierMappingDst"'


def build_rule_string(from_to):
    return "{" + "{0}: {1}, {2}: {3}".format(
        kbsrc, hex(from_to[0]), kbdst, hex(from_to[1])) + "}"


def build_remap_command(*, remappings=None, swaps=None):
    """Build a command that will perform a remapping using macos' `hidutil`.
    
    Parameters
    ----------
    remappings : dict(int: int)
        Multiple rules that remap one physical key into another.
        These mappings are one way. Each key item of the dictionary will
        be mapped to its corresponding value, but the value key will
        not be remapped.
    
    swaps : list((int, int))
        A sequence of rules in the form of 2-tuples.
    
    Returns
    -------
    A string that can be copied and pasted into the terminal to execute
    the remapping.
    """
    remappings = remappings or dict()
    assert type(remappings) is dict
    remappings = set(remappings.items())
    
    swaps = swaps or []
    swaps = set(s for s in swaps) | set(tuple(reversed(s)) for s in swaps)
    
    rules = sorted(remappings | swaps)
    rules = list((k | 0x700000000, v | 0x700000000) for k, v in rules)
    
    cmd = command_phrase.format(', '.join(list(map(build_rule_string, rules))))
    return cmd