from app.models import *
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import json
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import ExtraTreesRegressor
from django.db.models import F
import time
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO


dataset_clean = ''
splited_data = DatasetSpliter(dataset_clean)
regressor = RandomForestRegressor()
regressor.train(splited_data)


class DatasetSpliter :
    def split(dataset_clean):
        pass

class Regressor:
    def __init__(dataset_splited):
        self.model = None
        self.test_score = None
        self.test_score = None
        self.MSE = None
        self.x_train, self.y_train, self.x_test, self.y_test = dataset_splited


class RandomForestRegressor(Regressor) :
    def fit():
        self.model = RandomForestRegressor(n_estimators=100,max_depth=5, random_state=33)
        self.model.fit(self.x_train, self.y_train)

    def get_result():
        self.train_score = self.model.score(self.x_train, self.y_train)
        self.test_score = self.model.score(self.x_test, self.y_test)
        self.y_pred = self.model.predict(self.x_test)
        self.MSE = mean_squared_error(y_test, y_pred, multioutput='uniform_average')

    def calculate():
        self.fit()
        self.get_result()


def cleaning_dataset():
    dataset_raw = DatasetRaw.objects.all()
    df = dataset_raw.to_dataframe(fieldnames=['id', 'year', 'month', 'carrier__carrier', 'carrier__carrier_name', 'airport__airport_name', 'airport__airport', 'arr_flights', 'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct', 'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay', 'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'])
    df_null = df[df.isna().any(axis=1)]
    df_non_null =df.dropna(axis=0, how='any', inplace=False)
    df_duplicate = df_non_null[df_non_null.duplicated()]
    df_clean = df_non_null[~df_non_null.duplicated()]
    dataset_null_json = json.loads(df_null.to_json(orient="records"))
    dataset_duplicate_json = json.loads(df_duplicate.to_json(orient="records"))
    dataset_clean_json = json.loads(df_clean.to_json(orient="records"))

    success = 1
    context = {
        "dataset_null": dataset_null_json,
        "dataset_duplicate": dataset_duplicate_json,
        "dataset_clean": dataset_clean_json,
        'success': success
    }

    return context

def dataset_clean():
    df = DatasetClean.objects.all()
    df = df.to_dataframe()
    return df



def random_forest_regressor(train_test):
    x_train,x_test,y_train,y_test = train_test
    RandomForestRegressorModel = RandomForestRegressor(n_estimators=100,max_depth=5, random_state=33)
    RandomForestRegressorModel.fit(x_train, y_train)
    train_score = RandomForestRegressorModel.score(x_train, y_train)
    test_score = RandomForestRegressorModel.score(x_test, y_test)
    y_pred = RandomForestRegressorModel.predict(x_test)
    MSEValue = mean_squared_error(y_test, y_pred, multioutput='uniform_average')

    context = {
        'train_score': train_score * 100,
        'test_score': test_score * 100,
        'y_test' : y_test.tolist(),
        'y_pred' : y_pred.tolist(),
        'MSEValue': MSEValue,
    }

    return context

def linear_regression(train_test):
    x_train,x_test,y_train,y_test = train_test
    linear_regression = LinearRegression()
    linear_regression.fit(x_train, y_train)
    train_score = linear_regression.score(x_train, y_train)
    test_score = linear_regression.score(x_test, y_test)
    y_pred = linear_regression.predict(x_test)
    MSEValue = mean_squared_error(y_test, y_pred, multioutput='uniform_average')

    context = {
        'train_score': train_score * 100,
        'test_score': test_score * 100,
        'y_test' : y_test.tolist(),
        'y_pred' : y_pred.tolist(),
        'MSEValue': MSEValue,
    }

    return context

def decision_tree_regressor(train_test):
    x_train,x_test,y_train,y_test = train_test
    decision_tree = DecisionTreeRegressor()
    decision_tree.fit(x_train, y_train)
    train_score = decision_tree.score(x_train, y_train)
    test_score = decision_tree.score(x_test, y_test)
    y_pred = decision_tree.predict(x_test)
    MSEValue = mean_squared_error(y_test, y_pred, multioutput='uniform_average')

    context = {
        'train_score': train_score * 100,
        'test_score': test_score * 100,
        'y_test' : y_test.tolist(),
        'y_pred' : y_pred.tolist(),
        'MSEValue': MSEValue,
    }

    return context

def extra_trees_regressor(train_test):
    x_train,x_test,y_train,y_test = train_test
    extra_trees = ExtraTreesRegressor()
    extra_trees.fit(x_train, y_train)
    train_score = extra_trees.score(x_train, y_train)
    test_score = extra_trees.score(x_test, y_test)
    y_pred = extra_trees.predict(x_test)
    MSEValue = mean_squared_error(y_test, y_pred, multioutput='uniform_average')

    context = {
        'train_score': train_score * 100,
        'test_score': test_score * 100,
        'y_test' : y_test.tolist(),
        'y_pred' : y_pred.tolist(),
        'MSEValue': MSEValue,
    }
    return context

def predict(_type, train_test):
    if (_type == 'LR'):
        return linear_regression(train_test)
    if (_type == 'RFR'):
        return random_forest_regressor(train_test)
    if (_type == 'ETR'):
        return extra_trees_regressor(train_test)
    if (_type == 'DTR'):
        return decision_tree_regressor(train_test)


def split_data(dataset_clean):
    df_1 = dataset_clean
    x = df_1.drop('late_aircraft_delay', axis=1)
    y = df_1['late_aircraft_delay']
    return train_test_split(x,y,test_size=20,random_state=44)

def get_plot_flights_per_month(dataset):
    plt.figure(layout="constrained",  )
    sns.countplot(dataset, x='month')
    plt.xticks(size = 5)
    plt.yticks(size = 5)
    plt.xlabel("Months", size = 10)
    plt.ylabel("Frequency", size = 10)
    imgdata = StringIO()
    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)
    return imgdata.getvalue()

def get_plot_most_number_of_flights(dataset):
    plt.figure(layout='constrained')
    sns.countplot(dataset, x='carrier')
    plt.xticks(size = 5)
    plt.yticks(size = 5)
    plt.xlabel("Carriers", size = 10)
    plt.ylabel("Frequency", size = 10)
    imgdata = StringIO()
    plt.savefig(imgdata, format='svg')
    imgdata.seek(0)
    return imgdata.getvalue()
