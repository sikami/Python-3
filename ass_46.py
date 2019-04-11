def computepay(hrs, pay) :
    pay = float(pay)
    a = float(hrs)
    if a <= 40 :
        return pay * a
    elif a > 40 :
        overtime_hour = a - 40
        overtime_pay = (a - 40) * pay * 1.5
        normal_pay = (a - overtime_hour) * pay
        return overtime_pay + normal_pay

hrs = input("Enter Hours:")
pay = input("Enter Pay:")
print(computepay(hrs,pay))