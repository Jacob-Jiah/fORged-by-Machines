import pandas as pd
import copy
import numpy as np
def printout(predict,real):
    beginning_inventory=np.array(predict)
    order_quantity = copy.deepcopy(np.array(real))
    ending_inventory = []
    back_order = [] 
    hoding_cost=[]
    # backorder_cost=[]
    i=0
    ending_inventory.append((beginning_inventory[i]>order_quantity[i])*(beginning_inventory[i]-order_quantity[i]))
    back_order.append((beginning_inventory[i]<order_quantity[i])*(-beginning_inventory[i]+order_quantity[i]))
    hoding_cost.append( (beginning_inventory[i]>90)*(beginning_inventory[i]-90) + beginning_inventory[i] )
    for i in range(1,24):
        beginning_inventory[i]+=back_order[i-1]
        order_quantity[i]+=back_order[i-1]
        ending_inventory.append((beginning_inventory[i]>order_quantity[i])*(beginning_inventory[i]-order_quantity[i]))
        back_order.append((beginning_inventory[i]<order_quantity[i])*(-beginning_inventory[i]+order_quantity[i]))
        hoding_cost.append((beginning_inventory[i]>90)*(beginning_inventory[i]-90) + beginning_inventory[i] )
    # backorder_cost.append(3*(beginning_inventory[i]<order_quantity[i])*(-beginning_inventory[i]+order_quantity[i]))

    ending_inventory=np.array(ending_inventory)
    back_order = np.array(back_order )
    hoding_cost = np.array(hoding_cost)
    report= pd.DataFrame({"beginning_inventory":beginning_inventory})
    report["order_quantity"]=np.array(real)
    report["ending_inventory"]=ending_inventory
    report["back_order"]=back_order
    report["hoding_cost"]=hoding_cost
    report["back_order_cost"]=back_order*3
    total_holding_cost=sum(hoding_cost)
    average_holding_cost=np.mean(hoding_cost)
    total_backorder_cost=sum(back_order)*3
    average_backorder_cost=np.mean(back_order)*3
    report.index=pd.date_range(start='1/1/2006', periods=24, freq='M')
    return report,total_holding_cost,average_holding_cost,total_backorder_cost,average_backorder_cost
