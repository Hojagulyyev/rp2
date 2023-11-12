from django import template

register = template.Library()


@register.filter(name="get_level_color_by_index")
def get_level_color_by_index(level, gradient_index=0):
    LEVEL_STEP_THAT_CHANGE_COLOR_DESIGN = 5
    LEVEL_COLOR_DESIGN = {
        1: ("#9b5c33", "#ae6f46"),
        2: ("#a3814e", "#a3814e"),
        3: ("#d99f23", "#fedd68"),
        4: ("#67b888", "#93d6ae"),
        5: ("#5a401e", "#607e28"),
        6: ("#c81b1b", "#c2bc61"),
        7: ("#aaa999", "#ff6c00"),
        8: ("#145e7c", "#89b8cb"),
        9: ("#d99f23", "#145e7c"),
        10: ("#ff0000", "#00aaff"),
    }

    # get color index by level
    color_index = int(level / LEVEL_STEP_THAT_CHANGE_COLOR_DESIGN) + 1
    if color_index > len(LEVEL_COLOR_DESIGN):
        color_index = list(LEVEL_COLOR_DESIGN.keys())[-1]

    return LEVEL_COLOR_DESIGN[color_index][gradient_index]
