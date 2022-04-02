# fit prophet model on the dataset
from pandas import read_csv
from pandas import to_datetime
from fbprophet import Prophet
from pandas import DataFrame
from matplotlib import pyplot

# define the model
model = Prophet()
# fit the model
model.fit(df)