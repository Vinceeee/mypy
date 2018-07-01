
#Calculate the salary of this month

BASEHOUR = 38
OVERRATE = 1.3

def cal_salary(base,hour):
 sum = 0
 over_hour = hour - BASEHOUR
 if ( over_hour > 0 ):
   sum = base * BASEHOUR + base*over_hour*OVERRATE
 else:
   sum = base * hour
 return sum

base = raw_input("base in this month: ")
hour = raw_input("working hours in this month: ")
print "Salary:"+str(cal_salary(int(base),int(hour)))
