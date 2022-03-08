import os
import sys


PARENT_PATH = os.path.abspath("..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
PARENT_PATH = os.path.abspath("../../..")
from common_iOS.environment_iOS import Environment
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
PARENT_PATH = os.path.abspath("../..")
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)
from common.driver_manager import DriverManager


def before_scenario(context,scenario):
    Environment.set_capabilities(context)


def after_scenario(context, scenario):
    DriverManager.quit_app(context)