import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
import statistics 
sns.set() 
train = pd.read_csv('./train.csv') #тренировочная выборка
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
train.pop('Cabin')
test.pop('Cabin')
train.pop('Name')
test.pop('Name')
kolvo_strok_in_train=train.shape[0]
kolvo_strok_in_test=test.shape[0]
#Заполнем train
#Пропущенный возраст заменяем на средний

train_mean_Age=math.ceil(train.describe().Age["mean"])
def impute_age_by_planet(df: pd.DataFrame) -> None:
    for planet in ['Europa', 'Earth', 'Mars']:
        planet_median = df[df['HomePlanet'] == planet]['Age'].median()
        df.loc[
            (df['Age'].isnull()) & (df['HomePlanet'] == planet),
            'Age'
        ] = planet_median


impute_age_by_planet(train)
impute_age_by_planet(test)

for i in range(kolvo_strok_in_train):
    if math.isnan(train["Age"][i]):
        train["Age"][i]=train_mean_Age
train[['Age', 'CryoSleep']].groupby(['Age'], as_index=False).mean()
train[['HomePlanet', 'CryoSleep']].groupby(['HomePlanet'], as_index=False).mean()
#Востанавливаем CryoSleep
for i in range(kolvo_strok_in_train):
    if (train["RoomService"][i]==0.0 and train["FoodCourt"][i]==0.0 and train["ShoppingMall"][i]==0.0 and
    train["Spa"][i]==0.0 and train["VRDeck"][i]==0.0):
        if math.isnan((train["CryoSleep"][i])):
            train["CryoSleep"][i]=False
            
all_ages=[]
for i in range(0,80,1):
    all_ages.append(float(i))
ages1 = dict.fromkeys(all_ages, [])
for i, age in enumerate(train.Age):
    if not pd.isna(train.CryoSleep[i]):
        if(train.CryoSleep[i]==True):
            ages1[age] = ages1[age] + [1]
        elif(train.CryoSleep[i]==False):
            ages1[age] = ages1[age] + [0]

for i, sleep in enumerate(train.CryoSleep):
    if pd.isna(sleep):
        if(round(np.mean(ages1[train.Age[i]]))==1.0):
            train.CryoSleep[i] = True
        elif(round(np.mean(ages1[train.Age[i]]))==0.0):
            train.CryoSleep[i] = False
#Восстанавливаем VIP
for i in range(kolvo_strok_in_train):
    if pd.isna(train["VIP"][i]):
        train["VIP"][i]=train.describe(include=['O']).VIP["top"]
#Восстанавливаем HomePlanet
destinations=['55 Cancri e','PSO J318.5-22','TRAPPIST-1e']
homeDict = dict.fromkeys(destinations, [])
for i, destination in enumerate(train.Destination):
    if not pd.isna(train.HomePlanet[i]):
        if(not pd.isna(destination)):
            homeDict[destination]=homeDict[destination]+[train.HomePlanet[i]]
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
temp = train['VIP'] == False
train.loc[temp, col] = train.loc[temp, col].fillna('Earth')
 
temp = train['VIP'] == True
train.loc[temp, col] = train.loc[temp, col].fillna('Europa')
#Восстанавливаем Destination - восстановили
for i in range(kolvo_strok_in_train):
    if pd.isna(train["Destination"][i]):
        if not pd.isna(train["HomePlanet"][i]):
            train["Destination"][i]=DirectionDict[train["HomePlanet"][i]]
        if pd.isna(train["Destination"][i]):
            train["HomePlanet"][i]=train.describe(include=['O']).Destination["top"]

#Восстанавливаем RoomService
ages3 = dict.fromkeys(all_ages, [])
for i, age in enumerate(train.Age):
    if not pd.isna(train.RoomService[i]):
        ages3[age] = ages3[age] + [train.RoomService[i]]
for i, service in enumerate(train.RoomService):
    if pd.isna(service):
        train.RoomService[i] = np.mean(ages3[train.Age[i]]) 
#Восстанавливаем FoodCourt
ages4 = dict.fromkeys(all_ages, [])
for i, age in enumerate(train.Age):
    if not pd.isna(train.FoodCourt[i]):
        ages4[age] = ages4[age] + [train.FoodCourt[i]]
for i, service in enumerate(train.FoodCourt):
    if pd.isna(service):
        train.FoodCourt[i] = np.mean(ages4[train.Age[i]]) 
#Восстанавливаем ShoppingMall
ages5 = dict.fromkeys(all_ages, [])
for i, age in enumerate(train.Age):
    if not pd.isna(train.ShoppingMall[i]):
        ages5[age] = ages5[age] + [train.ShoppingMall[i]]
for i, service in enumerate(train.ShoppingMall):
    if pd.isna(service):
        train.ShoppingMall[i] = np.mean(ages5[train.Age[i]]) 
#Восстанавливаем Spa
ages6 = dict.fromkeys(all_ages, [])
for i, age in enumerate(train.Age):
    if not pd.isna(train.Spa[i]):
        ages6[age] = ages6[age] + [train.Spa[i]]
for i, service in enumerate(train.Spa):
    if pd.isna(service):
        train.Spa[i] = np.mean(ages6[train.Age[i]]) 
#Восстанавливаем VRDeck
ages7 = dict.fromkeys(all_ages, [])
for i, age in enumerate(train.Age):
    if not pd.isna(train.VRDeck[i]):
        ages7[age] = ages7[age] + [train.VRDeck[i]]
for i, service in enumerate(train.VRDeck):
    if pd.isna(service):
        train.VRDeck[i] = np.mean(ages7[train.Age[i]]) 
#Новые столбцы
new = train["PassengerId"].str.split("_", n=1, expand=True)
train["RoomNo"] = new[0].astype(int)
train["PassengerNo"] = new[1].astype(int)
train['Expences'] = train['RoomService'] + train['FoodCourt'] + train['ShoppingMall'] + train['Spa'] + train['VRDeck']

