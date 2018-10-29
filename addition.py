import os
import argparse

def aruments():
  parser = argparse.ArgumentParser(description="Hello.......World")
  parser.add_argument('--a',required=True)
  parser.add_argument('--b',required=True)
  return parser.parse_args()

def add(a,b):
  print ("result:", a+b)

if __name__=="__main__":
  print "addition:"
  args = aruments()
  x= args.a
  y= args.b
  add(x,y)
