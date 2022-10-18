RED ='\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[30m'

def reset_font():
  print(RESET)

def print_error(text):
  print(RED + text)
  reset_font()

def return_error(text):
  return RED + text + RESET
  
def print_success(text):
  print(GREEN + text)
  reset_font()

def print_info(text):
  print(BLUE + text)
  reset_font()

def return_underline(text):
  return "\x1B[4m" + text + "\x1B[0m"

def return_bold(text):
  return "\x1B[1m" + text + "\x1B[0m"

def format_currency(amt):
  return "${:0,.2f}".format(amt)
