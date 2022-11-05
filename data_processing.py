import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.getcwd()  # get current working directory
os.chdir('C:/Users/Daipei/Nutstore/1/Experiment_Data/muscle2/damping')  # change working directory
path = 'C:/Users/Daipei/Nutstore/1/Experiment_Data/muscle2/damping'  # set path
os.listdir(path)  # list files in the path

datalist = []  # create an empty list
for i in os.listdir(path):  # loop through all files in the path
    if i.endswith('.txt'):  # only import txt files
        datalist.append(i)  # append the file name to the list
datalist  # check the list

save_list = []  # create an empty list
df = pd.DataFrame()  # create an empty dataframe
t = 1

for txt in datalist:  # loop all files in the list
    name = 'muscle2_damping_' + str(t)
    data_path = os.path.join(path, txt)  # set the path for each file
    df_txt = pd.read_table(data_path, index_col= False)  # read the file
    df_txt = df_txt.drop(['设备名称', ')角速度(°/S', ')温度(°C'], axis = 1)  # drop the columns
    df_txt.rename(columns = {'时间':'time','角度(°': 'Angle', ')转数(': 'Turn_num', ')': 'angle_num'},
                  inplace = True)  # rename the columns
    # angle_num = Turn_num*360 + Angle
    df_txt['angle_num'] = df_txt['Turn_num']*360 + df_txt['Angle']
    for i in range(1, len(df_txt)-1):
        if abs(df_txt['angle_num'][i]-df_txt['angle_num'][i-1]) >= 100 :
            # delete the data with large difference
            df_txt['angle_num'][i] = df_txt['angle_num'][i-1]
    plt.plot(df_txt['angle_num'])
    plt.show()
    df_txt.to_csv('C:/Users/Daipei/Desktop/Test Data/artificial_muscle_2/Damping/muscle2_damping_'
              + str(t) + '.csv', index = False)
    exec ('muscle2_damping_' + str(t) + '=' + 'df_txt')  # create a name for each file
    t += 1
