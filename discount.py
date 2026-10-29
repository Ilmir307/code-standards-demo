def Calculate_discount(price,Percent):
  result = price*(100-Percent)/100
  return result

X=Calculate_discount(1000,10)
print("Цена со скидкой:",X)
