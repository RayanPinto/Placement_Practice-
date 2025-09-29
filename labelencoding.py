from sklearn.preprocessing import LabelEncoder
import pandas as pd
data=pd.DataFrame({
    'fruit':['apple','banana','orange','apple','banana'],
    'price':[1,2,3,4,5]
})
le=LabelEncoder()
data['fruitEncoded']=le.fit_transform(data['fruit'])
print(data)
print(le.classes_)