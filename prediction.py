import numpy as np
from sklearn.externals import joblib
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
def predict_LSTM(data):
	report=np.zeros((25,15))
	for w in range(15):
		model=joblib.load('saved_model_'+str(w)+'.pkl')
		start= len(data)-24
		n_steps=12
		res=[]
		for i in range(start,len(data)+1):
			x_input = np.array(data.demand[i-n_steps:i])
			x_input = x_input.reshape((1, n_steps,1))
			yhat = model.predict(x_input, verbose=0)
			res.append(yhat[0][0])
		report[:,w]=np.array(res)
	return report