import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score



def read_data(filename):
    data = pd.read_csv(filename)
    return data

def drop_column(colum_name):
    data.drop(colum_name, inplace=True, axis=1)
    return data

def map_gender(data):
    gender = {'Male': 1, 'Female': 2}
    data.Gender = [gender[item] for item in data.Gender]
    return data

def split_data(data,test_size):
    X = data[["Gender", "Age", "AnnualSalary"]]
    y = data["Purchased"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)
    return X_train, X_test, y_train, y_test

def log(logger,model,split,accuracy):
    logger.info("model="+model+", split="+split+", accuracy="+str(round(accuracy, 2)))

if __name__ == '__main__':
    logging.basicConfig(filename="ML_Task.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    # Creating an object
    logger = logging.getLogger()
    # Setting the threshold of logger to INFO
    logger.setLevel(logging.INFO)

    gnb = GaussianNB()
    data=read_data('Datasets/car_data.csv')
    data=drop_column('User ID')
    data=map_gender(data)
    #Train models with diffrent train:test set ratio
    #50:50
    X_train05, X_test05, y_train05, y_test05=split_data(data,0.5)
    y_pred05 = gnb.fit(X_train05, y_train05).predict(X_test05)
    accuracy05 = accuracy_score(y_test05, y_pred05)
    # 70:30
    X_train03, X_test03, y_train03, y_test03 = split_data(data, 0.3)
    y_pred03 = gnb.fit(X_train03, y_train03).predict(X_test03)
    accuracy03 = accuracy_score(y_test03, y_pred03)
    # 80:20
    X_train02, X_test02, y_train02, y_test02 = split_data(data, 0.2)
    y_pred02 = gnb.fit(X_train02, y_train02).predict(X_test02)
    accuracy02 = accuracy_score(y_test02, y_pred02)
    #log info
    log(logger,"Gaussian Naive Bayes","50-50",accuracy05)
    log(logger,"Gaussian Naive Bayes", "70-30", accuracy03)
    log(logger,"Gaussian Naive Bayes", "80-20", accuracy02)

