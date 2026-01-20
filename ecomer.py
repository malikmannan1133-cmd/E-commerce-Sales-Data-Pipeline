import pandas as pd
import numpy as np
from datetime import datetime,timedelta
import matplotlib.pyplot as plt

np.random.seed(42)

no_orders=10000

data={
    'Order_ID':np.arange(1,no_orders+1),
    'Customer_ID':np.random.randint(100,250,no_orders),
    'Date': [datetime(2025,1,1)+timedelta(days=np.random.randint(0,365)) for i in range(no_orders)],
    'Amount': np.random.uniform(50,1500,no_orders),
    'Category':np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'],no_orders),
}

df=pd.DataFrame(data)

df.to_csv('ecommerce_orders.csv',index=False)

print(df.head())

df.loc[df.sample(frac=0.05).index,"Amount"]=np.nan
df.loc[df.sample(frac=0.01).index,"Order_ID"]=np.nan
df.loc[df.sample(frac=0.04).index,"Category"]=np.nan

print(df.isnull().sum())

print(df.head(100))

df['Amount']=df['Amount'].fillna(df['Amount'].mean())

# Most Frequent se bharo
df['Category'] = df['Category'].fillna(df['Category'].mode()[0])

df.dropna(subset=['Order_ID'], inplace=True)

print(df.isnull().sum())

print("\nCleaning Done! Ab check karte hain missing values:")
print(df.isnull().sum())

print(df)

Catrgory_sale=df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print(round(Catrgory_sale,2))

Catrgory_sale.plot(kind='bar',color='orange',edgecolor='black')

plt.title("Profit by category")
plt.xlabel("Categories")
plt.ylabel("Amount")

plt.show()

summary = df.groupby('Category')['Amount'].agg(['sum', 'mean', 'count'])
print(summary)


df.to_csv('ecommerce_orders.csv',index=False)
