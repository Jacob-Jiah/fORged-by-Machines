import pandas as pd
import numpy as np
from prediction import *
from inventory import *
from output import *
# from sklearn.externals import joblib
# from keras.models import Sequential
# from keras.layers import LSTM
# from keras.layers import Dense
def data_refine(data):
	years=np.array(data.year)
	for i in range(1,len(years)):
		if np.isnan(years[i]):
			years[i]=years[i-1]
	data.year=years
	return data
if __name__=="__main__":
	data=pd.read_csv("Ten-Year-Demand.csv",names=["year","month","demand"],header=0)
	# clean the data
	data=data_refine(data)
	# make predictions
	results_lstm=predict_LSTM(data)
	result=np.mean(results_lstm,axis=1)
	# built inventory strategy
	choices= strategy(result)
	choices[0]= 73
	report,total_holding_cost,average_holding_cost,total_backorder_cost,average_backorder_cost=printout(choices,np.array(data.demand[-24:]))
	report.to_csv("report.csv", sep='\t',header=True,index=True)
	print("total_holding_cost:",str(total_holding_cost))
	print("average_holding_cost:",str(average_holding_cost))
	print("total_backorder_cost",str(total_backorder_cost))
	print("average_backorder_cost",str(average_backorder_cost))