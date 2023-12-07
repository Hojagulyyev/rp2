import datetime

from django import template

from rp2.business_logic import LEVEL_STEP_THAT_CHANGE_COLOR_DESIGN


register = template.Library()


LEVEL_COLOR_DESIGN = {
    1: ("#9b5c33", "#ae6f46"),
    2: ("#3d5646", "#3d5646"),
    3: ("#d99f23", "#fedd68"),
    4: ("#67b888", "#93d6ae"),
    5: ("#5a401e", "#607e28"),
    6: ("#c81b1b", "#c2bc61"),
    7: ("#aaa999", "#ff6c00"),
    8: ("#145e7c", "#89b8cb"),
    9: ("#d99f23", "#145e7c"),
    10: ("#ff0000", "#00aaff"),
}

STATISTIC_COLOR_DESIGN = {
    1: "#4ff461",
    2: "#08b8f1",
    3: "#7750f8",
}


@register.filter(name="get_color_index_by_level")
def get_color_index_by_level(level: int):
    return int(level / LEVEL_STEP_THAT_CHANGE_COLOR_DESIGN) + 1


@register.filter(name="get_level_color_by_color_index")
def get_level_color_by_color_index(color_index, gradient_index=0):

    if color_index > len(LEVEL_COLOR_DESIGN):
        color_index = list(LEVEL_COLOR_DESIGN.keys())[-1]

    return LEVEL_COLOR_DESIGN[color_index][gradient_index]


@register.filter(name="get_level_color_by_level")
def get_level_color_by_level(level, gradient_index=0):
    color_index = get_color_index_by_level(level)
    return get_level_color_by_color_index(color_index, gradient_index)


@register.filter(name="get_statistic_color_by_color_index")
def get_statistic_color_by_color_index(color_index):

    if color_index > len(STATISTIC_COLOR_DESIGN):
        color_index = list(STATISTIC_COLOR_DESIGN.keys())[-1]

    return STATISTIC_COLOR_DESIGN[color_index]


@register.filter(name='range_list')
def range_list(number):
    return range(1, number + 1)


@register.filter()
def remove_days(days):
    new_date = datetime.date.today() - datetime.timedelta(days=days)
    return new_date
