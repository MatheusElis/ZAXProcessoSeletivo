class Order:
    def __init__(self, id, value, store):
        self.id = id
        self.value = value
        self.store = store


class Store:
    def __init__(self, id, name, comission):
        self.id = id
        self.name = name
        self.comission = comission
        
    


class Motoboy:
    def __init__(self, id, name, fixedPrice, exclusivity):
        self.id = id
        self.name = name
        self.fixedPrice = fixedPrice
        self.exclusivity = exclusivity
        self.orderExecuted = []
    
    def setOrder(self, order):
        self.orderExecuted.append(order)
    
    def setEarnings(self):
        earnings = 0
        for order in self.orderExecuted:
            earnings += self.fixedPrice + order.value * order.store.comission
        return earnings
            
    def getOrdersList(self):
        executedList = """"""
        for order in self.orderExecuted:
            executedList += f'\nPedido N {order.id} - Valor: R${order.value} - {order.store.name}'
        return executedList

    def printResult(self):
        print(
        f"""
        --------------------------------------------
        {self.name} - {len(self.orderExecuted)} Pedidos
        {self.getOrdersList()}
        Ganho Total: R${self.setEarnings()}
        """)