"""
@author: github.com/suleymainci
"""
from locator import LocationFinder
import argparse

parser = argparse.ArgumentParser(description='Template image locator')
parser.add_argument("--template", type=str, default="images/Small_area.png", help="template img")
parser.add_argument("--image", type=str, default="images/StarMap.png", help="original img")
args = parser.parse_args()
print("template:",args.template)

a = LocationFinder(args.template,args.image)
a.finder()

