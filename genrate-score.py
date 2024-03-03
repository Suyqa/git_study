import numpy as np
import pandas as pd
import random
df = pd.DataFrame(np.random.normal(80,5,size=(50,5)),dtype=float,columns=['zh','math','english','physical','chemistry'])
# print(random.choices([2,5,9],k=2))# 可以重复
# print(random.sample([1,2,3,4],k=3)) # 不会重复
name = [
    'John', 'Jack', 'James', 'Robert', 'Michael', 'William', 'David', 'Richard', 
    'Charles', 'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 
    'George', 'Kenneth', 'Steven', 'Edward', 'Brian', 'Ronald', 'Anthony', 'Kevin', 
    'Jason', 'Matthew', 'Gary', 'Timothy', 'Jose', 'Larry', 'Jeffrey', 'Frank', 'Scott', 
    'Eric', 'Stephen', 'Andrew', 'Raymond', 'Gregory', 'Joshua', 'Jerry', 'Dennis', 
    'Walter', 'Patrick', 'Peter', 'Harold', 'Douglas', 'Henry', 'Carl', 'Arthur', 'Ryan', 
    'Roger', 'Joe', 'Juan', 'Jackie', 'Lawrence', 'Franklin', 'Russell', 'Bobby', 'Victor', 
    'Martin', 'Leonard', 'Gerald', 'Seth', 'Wesley', 'Dale', 'Bruce', 'Brandon'
]
gender = np.random.randint(2,size=50).reshape((-1,1))
gender = pd.DataFrame(gender,columns=['gender',])
name = pd.DataFrame(random.sample(name,k=50),columns=['name',])
data = pd.concat([name,gender,df],axis=1).round(0)
data['gender']=data['gender'].apply(lambda x: 'man' if x==1 else 'woman')
'''
           name    zh  math  english  physical  chemistry
0          John  82.0  85.0     79.0      83.0       80.0
1        Walter  72.0  90.0     83.0      77.0       83.0
2         Jason  87.0  73.0     80.0      80.0       87.0
'''
data.to_csv('name_score.csv')
data.to_excel('name_score.xlsx')