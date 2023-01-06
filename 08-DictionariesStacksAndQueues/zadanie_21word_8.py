import stack

wyraz=str(input("Wpisz wyrażenie: "))
ops = {
  "+": (lambda a, b: a + b),
  "-": (lambda a, b: a - b),
  "*": (lambda a, b: a * b),
  "/": (lambda a, b: a / b),
}


for i in wyraz:
    if i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8 or i==9 or i==0:
        stack.push(int(i))
    if i in ops:
        arg2 = stack.pop()
        arg1 = stack.pop()
        result = ops[i](arg1, arg2)
        stack.push(result)
    if i == '=':
        break 

stack.display()    