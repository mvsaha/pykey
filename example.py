from keycodes import *


# Shifting the Y-H-N column to the right to make room for the heavy hitters:
#     Escape-Delete-Enter
# in the middle row (AKA "middle out")
rules = {
    
    # '6' column
    key_y: key_escape,
    key_h: key_backspace,
    key_n: key_return,
    
    # '7' column
    key_u: key_y,
    key_j: key_h,
    key_m: key_n,
    
    # '8' column
    key_i: key_u,
    key_k: key_j,
    key_comma_gt: key_m,
    
    # '9' column
    key_o: key_i,
    key_l: key_k,
    key_period_lt: key_comma_gt,
    
    # '0' column
    key_p: key_o,
    key_semicolon_colon: key_l,
    key_slash_question: key_period_lt,
    
    # '-' column
    key_left_bracket: key_p,
    key_quote_doublequote: key_semicolon_colon,
    key_shift_right: key_slash_question,
    
    # '=' column
    key_right_bracket: key_left_bracket,
    key_return: key_quote_doublequote,
    
    # Miscellaneous
    key_backspace: key_backslash_pipe,  # have to put the backslash somewhere
    key_command_right: key_shift_right,  # And the shift key as well
    key_control_right: key_shift_right,
}


if __name__ == "__main__":
	print(build_remap_command(remappings=rules))
