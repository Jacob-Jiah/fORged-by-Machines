import numpy as np
# we will implement monte carlo to find the heuristic of optimal
def cost(inp):  # cost of a given array of inventory
    return (inp[inp>90]-90).sum()+inp.sum()
def cost_all(samp,curr,nextp,nums): # overall cost: samp are samples, curr is the current state, nextp is the expect value of next state, nums is the number of samples I draw
    backorder=samp[samp>curr]-curr 
    bacoordercost=sum(backorder)*3 #back order cost
    restorecost=curr*nums+(curr>90)*(curr-90)*nums #storage cost
    ecost=cost(backorder+nextp)-nextp*len(backorder)+(nextp>90)*(nextp-90)*len(backorder) # expect cost due to delay order
    esave=cost(backorder+curr)-len(backorder)*curr+(curr>90)*(curr-90)*len(backorder) # expect save due to delay order
    result=restorecost+ecost+bacoordercost-esave
    return result
def optimal(xhat,k,std=2.06): # implement hill-climping to find a proper expection
    curr=xhat[k]
    nextp=xhat[k+1]
    nums=10000
    for i in range(1,500):
        det=5/i
        samp=np.random.normal(xhat[k],std,nums)
        cst1=cost_all(samp,curr+det,nextp,nums)
        cst2=cost_all(samp,curr-det,nextp,nums)
        curr+=det*((cst1<cst2)*2-1)
    return curr
def strategy(xhat):
	select=[]
	for i in range(len(xhat)-1):
	    select.append(round(optimal(xhat,i),2))
	return select

