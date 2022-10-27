"""
Climate prediction GUI is a package that generates a simple model of vertical
energy transfer and temperatures in the Earth system
"""
# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
# Template:
# from .<file> import <Class> # noqa
# e.g. from .model import Model    # noqa
from .model import Model  # noqa
from .controller import Controller  # noqa
from .view import View  # noqa
from .plot import Plot # noqa
from .plot_general import Plot_general # noqa
from .albedo import get_albedo  # noqa
from .temperature_profile_calculation_general import calculate_temperature_matrix_general # noqa
from .temperature_profile_calculation import calculate_temperature_matrix # noqa
from .input_checker import _check_inputs # noqa
from .model_out_of_range import _check_model_range # noqa