import sys
from src.initial_data import DATA
from src.class_objects import Order, Store, Motoboy

def handler(data):
    motoboyList = [Motoboy(motoboy.get('id'), motoboy.get('name'), motoboy.get('fixedPrice'), motoboy.get('exclusivity')) for motoboy in data['motoboys']]
    storeList = [Store(store.get('id'), store.get('name'), store.get('comission')) for store in data['stores']]
    orderList = [Order(order.get('id'), order.get('value'), storeList[order.get('store')-1]) for order in data['orders']]

    motoboyWaitList = None

    for order in orderList:
        
        if not motoboyWaitList:
            motoboyWaitList = motoboyList.copy()
        exclusiveMotoboys = [motoboy for motoboy in motoboyWaitList if motoboy.exclusivity == order.store.id]
        nonExclusiveMotoboys = [motoboy for motoboy in motoboyWaitList if not motoboy.exclusivity]
        
        if not nonExclusiveMotoboys and not exclusiveMotoboys:
            motoboyWaitList = motoboyList.copy()
            exclusiveMotoboys = [motoboy for motoboy in motoboyWaitList if motoboy.exclusivity == order.store.id]
            nonExclusiveMotoboys = [motoboy for motoboy in motoboyWaitList if not motoboy.exclusivity]
        
        currentMotoboy = exclusiveMotoboys[0] if exclusiveMotoboys else nonExclusiveMotoboys[0] 
        currentMotoboy.setOrder(order)
        motoboyWaitList.remove(currentMotoboy)

    return(motoboyList)

def run(MotoboyID = None):
    motoboyList = handler(DATA)
    if not MotoboyID:
        for motoboy in motoboyList:
            motoboy.printResult()
        return
    else:
        for motoboy in motoboyList:
            if motoboy.id == MotoboyID:
                motoboy.printResult()
                return
        print("Não existe motoboy com o ID apresentado")
    return



if __name__ == "__main__":
    if len(sys.argv) > 1:
        motoboyId = int(sys.argv[-1])
        run(motoboyId)
    
    else:
        run()