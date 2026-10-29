class order:
    def __init__(self,Id,Total):
        self.Id=Id
        self.Total=Total

    def GetTotal(self):
        return self.Total

def Print_order(o):
    print("Заказ", o.Id, "на сумму", o.GetTotal())
    temp_variable = 123

Order1 = order(1,500)
Print_order(Order1)
