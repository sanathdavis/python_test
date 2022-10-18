#helper functions
#defines functions that print error text and success text
#also resets to normal colors after usage

employees = []
ALL_TOGETHER = 0
ANNUAL = 1
MONTHLY = 2
BI_WEEKLY = 3

STUB_TYPES = {
  ANNUAL : return_bold(return_underline('Annual View')),
  MONTHLY : return_bold(return_underline('Monthly View')),
  BI_WEEKLY : return_bold(return_underline('Bi-Weekly View')),
}

DIVIDE_BY = {    
  ANNUAL : 1,
  MONTHLY : 12,
  BI_WEEKLY : 24,
}
