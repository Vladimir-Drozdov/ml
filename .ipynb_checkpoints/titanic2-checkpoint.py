from titanic1 import train
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import statistics 
sns.set() 
#train = pd.read_csv('./train.csv') #тренировочная выборка
test = pd.read_csv('./test.csv') #тестовая выборка
submission = pd.read_csv('./sample_submission.csv') 
import math
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
pd.options.mode.chained_assignment = None #предотвращаем ошибку
#Произвести очистку данных и обработать пустые значения.

test.pop('Cabin')

test.pop('Name')
kolvo_strok_in_train=train.shape[0]
kolvo_strok_in_test=test.shape[0]
###Заполняем test
test_mean_Age=math.ceil(test.describe().Age["mean"])
for i in range(kolvo_strok_in_test):
    if math.isnan(test["Age"][i]):
        test["Age"][i]=test_mean_Age
test[['Age', 'CryoSleep']].groupby(['Age'], as_index=False).mean()
test[['HomePlanet', 'CryoSleep']].groupby(['HomePlanet'], as_index=False).mean()
#Востанавливаем CryoSleep
for i in range(kolvo_strok_in_test):
    if (test["RoomService"][i]==0.0 and test["FoodCourt"][i]==0.0 and test["ShoppingMall"][i]==0.0 and
    test["Spa"][i]==0.0 and test["VRDeck"][i]==0.0):
        if math.isnan((test["CryoSleep"][i])):
            test["CryoSleep"][i]=False
            
all_ages=[]
for i in range(0,80,1):
    all_ages.append(float(i))
ages1 = dict.fromkeys(all_ages, [])
for i, age in enumerate(test.Age):
    if not pd.isna(test.CryoSleep[i]):
        if(test.CryoSleep[i]==True):
            ages1[age] = ages1[age] + [1]
        elif(test.CryoSleep[i]==False):
            ages1[age] = ages1[age] + [0]

for i, sleep in enumerate(test.CryoSleep):
    if pd.isna(sleep):
        if(round(np.mean(ages1[test.Age[i]]))==1.0):
            test.CryoSleep[i] = True
        elif(round(np.mean(ages1[test.Age[i]]))==0.0):
            test.CryoSleep[i] = False
#Восстанавливаем VIP
for i in range(kolvo_strok_in_test):
    if pd.isna(test["VIP"][i]):
        test["VIP"][i]=test.describe(include=['O']).VIP["top"]
#Восстанавливаем HomePlanet
destinations=['55 Cancri e','PSO J318.5-22','TRAPPIST-1e']
homeDict = dict.fromkeys(destinations, [])
for i, destination in enumerate(test.Destination):
    if not pd.isna(test.HomePlanet[i]):
        if(not pd.isna(destination)):
            homeDict[destination]=homeDict[destination]+[test.HomePlanet[i]]
homeDict2={
    '55 Cancri e': most_frequent(homeDict["55 Cancri e"]),#'Europa'
    'PSO J318.5-22': most_frequent(homeDict["PSO J318.5-22"]),#'Earth'
    'TRAPPIST-1e': most_frequent(homeDict["TRAPPIST-1e"])#'Earth'
}
DirectionDict={
    most_frequent(homeDict["55 Cancri e"]):'55 Cancri e',
    most_frequent(homeDict["PSO J318.5-22"]):'PSO J318.5-22',
    most_frequent(homeDict["TRAPPIST-1e"]):'TRAPPIST-1e',
    'Mars':train.describe(include=['O']).Destination["top"]
}
col = 'HomePlanet'
temp = test['VIP'] == False
test.loc[temp, col] = test.loc[temp, col].fillna('Earth')
 
temp = test['VIP'] == True
test.loc[temp, col] = test.loc[temp, col].fillna('Europa')
#Восстанавливаем Destination 
for i in range(kolvo_strok_in_test):
    if pd.isna(test["Destination"][i]):
        if not pd.isna(test["HomePlanet"][i]):
            test["Destination"][i]=DirectionDict[test["HomePlanet"][i]]
        if pd.isna(test["Destination"][i]):
            test["HomePlanet"][i]=test.describe(include=['O']).Destination["top"]

#Восстанавливаем RoomService
ages3 = dict.fromkeys(all_ages, [])
for i, age in enumerate(test.Age):
    if not pd.isna(test.RoomService[i]):
        ages3[age] = ages3[age] + [test.RoomService[i]]
for i, service in enumerate(test.RoomService):
    if pd.isna(service):
        test.RoomService[i] = np.mean(ages3[test.Age[i]]) 
#Восстанавливаем FoodCourt
ages4 = dict.fromkeys(all_ages, [])
for i, age in enumerate(test.Age):
    if not pd.isna(test.FoodCourt[i]):
        ages4[age] = ages4[age] + [test.FoodCourt[i]]
for i, service in enumerate(test.FoodCourt):
    if pd.isna(service):
        test.FoodCourt[i] = np.mean(ages4[test.Age[i]]) 
#Восстанавливаем ShoppingMall
ages5 = dict.fromkeys(all_ages, [])
for i, age in enumerate(test.Age):
    if not pd.isna(test.ShoppingMall[i]):
        ages5[age] = ages5[age] + [test.ShoppingMall[i]]
for i, service in enumerate(test.ShoppingMall):
    if pd.isna(service):
        test.ShoppingMall[i] = np.mean(ages5[test.Age[i]]) 
#Восстанавливаем Spa
ages6 = dict.fromkeys(all_ages, [])
for i, age in enumerate(test.Age):
    if not pd.isna(test.Spa[i]):
        ages6[age] = ages6[age] + [test.Spa[i]]
for i, service in enumerate(test.Spa):
    if pd.isna(service):
        test.Spa[i] = np.mean(ages6[test.Age[i]]) 
#Восстанавливаем VRDeck
ages7 = dict.fromkeys(all_ages, [])
for i, age in enumerate(test.Age):
    if not pd.isna(test.VRDeck[i]):
        ages7[age] = ages7[age] + [test.VRDeck[i]]
for i, service in enumerate(test.VRDeck):
    if pd.isna(service):
        test.VRDeck[i] = np.mean(ages7[test.Age[i]]) 
#Новые столбцы
new = test["PassengerId"].str.split("_", n=1, expand=True)
test["RoomNo"] = new[0].astype(int)
test["PassengerNo"] = new[1].astype(int)
test['Expences'] = test['RoomService'] + test['FoodCourt'] + test['ShoppingMall'] + test['Spa'] + test['VRDeck']

#используем нейросеть RandomForestClassifier

features = ['HomePlanet', 'CryoSleep','Destination','VIP','VRDeck']
y = train['Transported']
X = pd.get_dummies(train[features])
X_test = pd.get_dummies(test[features])
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)  # обучаем модель
prediction = model.predict(X_test)  # делаем предсказание
output = pd.DataFrame({'PassengerId':test.PassengerId, 'Transported':prediction})
coinsidence=0
kolvo_strok_in_submission=submission.shape[0]
for i in range(kolvo_strok_in_submission):
    if submission["Transported"][i]==output["Transported"][i]:
        coinsidence=coinsidence+1
print("Accuracy: ",coinsidence/42.77, "%")
print("Самыми значимыми столбцами считаю Age, Destination и CryoSleep, так как они обеспечивают наибольшую точкность")