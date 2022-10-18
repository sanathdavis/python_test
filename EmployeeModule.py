#class which contains framework for an employee


#helper functions
#defines functions that print error text and success text
#also resets to normal colors after usage

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

class Employee:

  TAX_RATE = 13.5
  BENEFITS_RATE = 5.5
  GOVT_REDUCTIONS_RATE = 2.5  

  def __init__(self,first_name,last_name,position, base_annual_salary):
    self.id = 'job-card-' + str(len(employees) + 1) + '-2022-temp'
    self.first_name = first_name
    self.last_name = last_name
    self.position = position
    self.base_annual_salary = base_annual_salary
 
  def print_employee_details(self):
    print(f'Employee ID: {self.id}')
    print(f'Employee Name: {self.first_name} {self.last_name}')
  
  def get_bonus_rate(self):
    if self.base_annual_salary <= 21000:
      self.bonus_rate = 12.5
    elif 21000 < self.base_annual_salary <= 51000:
      self.bonus_rate = 11.5
    elif 51000 < self.base_annual_salary <= 59000:
      self.bonus_rate = 0
    else:
      self.bonus_rate = 60
    return self.bonus_rate 

  def rate_calculator(self, n):
    return lambda a : a * n / 100   

  def get_net_income(self):    
    annual_net_income = self.prepare_values_for_printing(ANNUAL)['net_income']
    return {
        'Annual Net Income' : format_currency(annual_net_income),
        'Monthly Net Income' : format_currency(annual_net_income / DIVIDE_BY[MONTHLY]),
        'Bi-Weekly Net Income' : format_currency(annual_net_income / DIVIDE_BY[BI_WEEKLY]),
    }

  def prepare_values_for_printing(self, stub_type = ANNUAL): 

    get_bonus = self.rate_calculator(self.get_bonus_rate())
    get_tax_deductible = self.rate_calculator(self.TAX_RATE)
    get_benefits_deductible = self.rate_calculator(self.BENEFITS_RATE)
    get_govt_deductible = self.rate_calculator(self.GOVT_REDUCTIONS_RATE) 

    bonus = get_bonus(self.base_annual_salary)
    gross_income = self.base_annual_salary + bonus
    tax_deductible = get_tax_deductible(gross_income)
    benefits_deductible = get_benefits_deductible(gross_income)
    govt_deductible = get_govt_deductible(gross_income)
    total_deductible = tax_deductible + benefits_deductible + govt_deductible
    net_income = gross_income - total_deductible
       
    divide_by = DIVIDE_BY[stub_type]

    return {
        'bonus' : bonus / divide_by,
        'gross_income' : gross_income / divide_by,
        'tax_deductible' : tax_deductible / divide_by,
        'benefits_deductible' : benefits_deductible / divide_by,
        'govt_deductible' : govt_deductible / divide_by,
        'total_deductible' : total_deductible / divide_by,
        'net_income' : net_income / divide_by
    }

  def print_pay_stub(self, stub_type = ANNUAL):
    pay_stub_table = PrettyTable()
    display_time = datetime.now().strftime("%Y-%m-%d")
    line = "---------------------------------------------"

    if stub_type != ALL_TOGETHER:
      values = self.prepare_values_for_printing(stub_type)
      column_names = [STUB_TYPES[stub_type]]
      
      rows = [
        [line],
        ["Company name: Software Associates"],
        [f'Date of Pay-Stub: {display_time}'],
        [line],
        [f'Employee: “{return_bold(self.first_name)}, {return_bold(self.last_name)}"'],
        [f'Position: "{return_bold(self.position)}"'],
        [f'Annual Salary: {return_bold(format_currency(self.base_annual_salary))}'],
        [f'Bonus({return_bold(format_currency(self.bonus_rate))}%):{return_bold(format_currency(values["bonus"]))}'],
        [f'Gross Annual Income:{return_underline(return_bold(format_currency(values["gross_income"])))}'],
        [line],
        [f'Deductible (Taxes {self.TAX_RATE}%): {return_bold(format_currency(values["tax_deductible"]))}'],
        [f'Deductible (Benefits {self.BENEFITS_RATE}%): {return_bold(format_currency(values["benefits_deductible"]))}'],
        [f'Deductible (Reductions  {self.GOVT_REDUCTIONS_RATE}%): {return_bold(format_currency(values["govt_deductible"]))}'],
        [f'Deductible (Total): {return_underline(return_bold(format_currency(values["total_deductible"])))}'],
        [line],
        [f'Net {return_bold("Annual")} Income: {return_underline(return_bold(format_currency(values["net_income"])))}'],
        [line]
      ]
      
    else:
      column_names = STUB_TYPES.values()
      values_annual = self.prepare_values_for_printing(ANNUAL)
      values_monthly = self.prepare_values_for_printing(MONTHLY)
      values_bi_weekly = self.prepare_values_for_printing(BI_WEEKLY)

      rows = [
        [line,line,line],
        ["Company name: Software Associates", "Company name: Software Associates", "Company name: Software Associates"],
        [f'Date of Pay-Stub: {display_time}', f'Date of Pay-Stub: {display_time}', f'Date of Pay-Stub: {display_time}'],
        [line,line,line],
        [f'Employee: “{return_bold(self.first_name)}, {return_bold(self.last_name)}"', f'Employee: “{return_bold(self.first_name)}, {return_bold(self.last_name)}"', f'Employee: “{return_bold(self.first_name)}, {return_bold(self.last_name)}"'],
        [f'Position: "{return_bold(self.position)}"', f'Position: "{return_bold(self.position)}"', f'Position: "{return_bold(self.position)}"'],
        [f'Annual Salary: {return_bold(format_currency(self.base_annual_salary))}', f'Monthly Salary: {return_bold(format_currency(self.base_annual_salary / DIVIDE_BY[MONTHLY]))}', f'Bi-weekly Salary: {return_bold(format_currency(self.base_annual_salary/ DIVIDE_BY[BI_WEEKLY]))}'],
        [f'Bonus({return_bold(format_currency(self.bonus_rate))}%):{return_bold(format_currency(values_annual["bonus"]))}', f'Bonus({return_bold(format_currency(self.bonus_rate))}%):{return_bold(format_currency(values_monthly["bonus"]))}', f'Bonus({return_bold(format_currency(self.bonus_rate))}%):{return_bold(format_currency(values_bi_weekly["bonus"]))}'],
        [f'Gross Annual Income:{return_underline(return_bold(format_currency(values_annual["gross_income"])))}', f'Gross Monthly Income:{return_underline(return_bold(format_currency(values_monthly["gross_income"])))}', f'Gross Bi-Weekly Income:{return_underline(return_bold(format_currency(values_bi_weekly["gross_income"])))}'],
        [line,line,line],
        [f'Deductible (Taxes {self.TAX_RATE}%): {return_bold(format_currency(values_annual["tax_deductible"]))}', f'Deductible (Taxes {self.TAX_RATE}%): {return_bold(format_currency(values_monthly["tax_deductible"]))}', f'Deductible (Taxes {self.TAX_RATE}%): {return_bold(format_currency(values_bi_weekly["tax_deductible"]))}'],
        [f'Deductible (Benefits {self.BENEFITS_RATE}%): {return_bold(format_currency(values_annual["benefits_deductible"]))}', f'Deductible (Benefits {self.BENEFITS_RATE}%): {return_bold(format_currency(values_monthly["benefits_deductible"]))}', f'Deductible (Benefits {self.BENEFITS_RATE}%): {return_bold(format_currency(values_bi_weekly["benefits_deductible"]))}'],
        [f'Deductible (Reductions  {self.GOVT_REDUCTIONS_RATE}%): {return_bold(format_currency(values_annual["govt_deductible"]))}', f'Deductible (Reductions  {self.GOVT_REDUCTIONS_RATE}%): {return_bold(format_currency(values_monthly["govt_deductible"]))}', f'Deductible (Reductions  {self.GOVT_REDUCTIONS_RATE}%): {return_bold(format_currency(values_bi_weekly["govt_deductible"]))}'],
        [f'Deductible (Total): {return_underline(return_bold(format_currency(values_annual["total_deductible"])))}', f'Deductible (Total): {return_underline(return_bold(format_currency(values_monthly["total_deductible"])))}', f'Deductible (Total): {return_underline(return_bold(format_currency(values_bi_weekly["total_deductible"])))}'],
        [line,line,line],
        [f'Net {return_bold("Annual")} Income: {return_underline(return_bold(format_currency(values_annual["net_income"])))}', f'Net {return_bold("Monthly")} Income: {return_underline(return_bold(format_currency(values_monthly["net_income"])))}', f'Net {return_bold("Bi-Weekly")} Income: {return_underline(return_bold(format_currency(values_bi_weekly["net_income"])))}'],
        [line,line,line],
      ]
    
    pay_stub_table.field_names = column_names
    for row in rows:
      pay_stub_table.add_row(row)
    print(pay_stub_table)

  

