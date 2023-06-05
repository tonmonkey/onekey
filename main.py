import urllib3
import argparse
from queryData import *


def args_deal():
    parse = argparse.ArgumentParser(prog="QAQC.py")
    parse.add_argument("-i","--id",action="store",help="Input you wang query company ID")
    opt = parse.parse_args()
    return opt


# Main program
if __name__ == "__main__":
    print(banner)
    name = args_deal()
    urllib3.disable_warnings()
    if name.id is not None:
        page = get_page(name.id)
        get_date(name.id,page)
        print("Task accomplished!")
    else:
        print("Input not detected！")