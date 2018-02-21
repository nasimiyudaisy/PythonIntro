#loan calculator

monthlyPayment = 0
numberOfPayments=0
numberOfYears=0

loanAmount=int(input("What is the cost if the loan? "))
interestRate=int(input("What your interest rate? "))
numberOfYears= int(input("What's the number of years of the loan? "))

numberOfYears=numberOfPayments

monthlyPayment= loanAmount*(interestRate *(1+interestRate)*numberOfPayments)/ ((1+interestRate)*(numberOfPayments-1))
print(monthlyPayment)

 