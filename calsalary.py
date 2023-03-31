def overtimesal(func):
    def sal(*kargs):


        print(f"{15000}")
        result=func(*kargs)
        print(result)
    return sal


@overtimesal
def calculate_salary(basicsal,hra,da):
    return basicsal+hra+da
calculate_salary(12000,1200,500)