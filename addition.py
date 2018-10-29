import os
import argparse

def aruments()
  parser = argparse.ArumentParser(description="Hello.......World")
  parser.add_argument('--a',required=true)
  parser.add_argument('--b',required=true)
  return parser.parse_args()

def add(a,b):
  print ("result:", a+b)

if __name=="__main__":
  print "addition:"
  args = aruments()
  x= args.a
  y= args.b
  add(x,y)
