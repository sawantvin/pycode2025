import pandas as pd

dd=pd.read_csv("/workspaces/pycode2025/my-repo/data/jamesbond.csv").convert_dtypes()
df=pd.DataFrame(dd)

new_columns={
"Year":"year",
"Movie":"movie",
"Bond":"bond_actor",
"Director":"director",
"Composer":"composure",
"Writer":"writer",
"Cinematographer":"cinematographer",
"Depicted_Film_Loc":"depicted_film_loc",
"Shooting_Loc":"shooting_loc",
"Bond_Car_MFG":"car_manufacturer",
"Bond_Girl_Nat":"bond_girl",
"US_Gross":"us_earning",
"US_Adj":"us_adjustment",
"World_Gross":"world_earning",
"World_Adj":"world_adjustment",
"Budget":"budget",
"Budget_Adj":"budget_adjustment",
"Film_Length":"film_duration",
"Avg_User_IMDB":"imdb",
"Avg_User_Rtn_Tom":"rotten_tomotoes",
"Conquests":"conquest",
"Martinis":"martinis",
"BJB":"bjb",
"Kills_Bond":"bond_kills",
"Kills_Others":"other_kill",
"Top_100":"top_100",
"Video_Game":"video_game"
}
james_bond_data=df.rename(columns=new_columns)


#print(james_bond_data[james_bond_data.isna().any(axis="columns")])

#print(james_bond_data.isna().any(axis="columns"))

#print(james_bond_data)
#print(james_bond_data.select_dtypes(include='number').aggregate([sum,min,max]))

#print(james_bond_data.aggregate({"us_earning": [max,min], "world_earning":[max, min], "budget":[max, min]}))
#print(james_bond_data.select_dtypes(include="number").apply(lambda x: x*x ))

#print(james_bond_data.select_dtypes(include="number").transform(lambda x: x*x))

#print(james_bond_data.groupby(['director','bond_actor'])['budget'].transform(lambda x: x.rank(ascending=False)))

#james_bond_data.drop(james_bond_data[james_bond_data['year']]==2006)

data1 = {'Name': ['John', 'Alice', 'Bob', 'Eve'],
        'Age': [25, 30, 22, 35],
        'Gender': ['Male', 'Female', 'Male', 'Female']}

df1= pd.DataFrame(data1)
#print(df1)

data2 = {'Name': ['John', 'Alice', 'Bob', 'Charlie'],
         'Salary': [50000, 55000, 40000, 48000]}

df2 = pd.DataFrame(data2)



#print (pd.merge(df1,df2,on='Name',how='inner'))

#df1.set_index('Name', inplace=True)
#df2.set_index('Name',inplace=True)
#print (df1)
#print(df2)
#print(df1.join(df2))

#print(pd.concat([df1,df2], axis=1))
print(james_bond_data)

test=pd.DataFrame( { "Name":['Vinod','Advay','Swara'],
              "Age":[48,30,11]
              }
             )

index_=pd.date_range('2025 05 20 08:45', periods=3 , freq='h' )





