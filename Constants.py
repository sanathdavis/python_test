#helper functions
#defines functions that print error text and success text
#also resets to normal colors after usage

#from .Helpers import *

employees = []
ALL_TOGETHER = 0
ANNUAL = 1
MONTHLY = 2
BI_WEEKLY = 3

STUB_TYPES = {
  ANNUAL : 'Annual View',
  MONTHLY : 'Monthly View',
  BI_WEEKLY : 'Bi-Weekly View',
}

DIVIDE_BY = {    
  ANNUAL : 1,
  MONTHLY : 12,
  BI_WEEKLY : 24,
}
