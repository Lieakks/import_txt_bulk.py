import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.getcwd()  # get current working director
path = str(input('please input the path of the folder:'
                 '(for example: ''C:/Users/Daipei/Nutstore/1/Experiment_Data/muscle2/damping'') '))  # input the load path of the folder
# for example: 'C:/Users/Daipei/Nutstore/1/Experiment_Data/muscle2/damping'
os.chdir(path)  # change working directory
os.listdir(path)  # list files in the path

datalist = []  # create an empty list
for i in os.listdir(path):  # loop through all files in the path
    if i.endswith('.txt'):  # only import txt files
        datalist.append(i)  # append the file name to the list
datalist  # check the list

save_list = []  # create an empty list
df = pd.DataFrame()  # create an empty dataframe
t = 1

save_path = str(input('please input the path to save the data:'
                      '(for example: ''C:/Users/Daipei/Desktop/Test Data/artificial_muscle_2/Damping/'') '))
# for example: 'C:/Users/Daipei/Desktop/Test Data/artificial_muscle_2/Damping/'
prefix = str(input('please input the prefix of the file:(for example: ''muscle2_damping_'') '))
# for example: 'muscle2_damping_'

for txt in datalist:  # loop all files in the list
    data_path = os.path.join(path, txt)  # set the path for each file
    df_txt = pd.read_table(data_path, index_col= False)  # read the file
    df_txt = df_txt.drop(['设备名称', ')角速度(°/S', ')温度(°C'], axis = 1)  # drop the columns
    df_txt.rename(columns = {'时间':'time','角度(°': 'Angle', ')转数(': 'Turn_num', ')': 'angle_num'},
                  inplace = True)  # rename the columns
    # angle_num = Turn_num*360 + Angle
    df_txt['angle_num'] = df_txt['Turn_num']*360 + df_txt['Angle']

    # delete the data with large difference
    for i in range(1, len(df_txt)-1):
        if abs(df_txt['angle_num'][i]-df_txt['angle_num'][i-1]) >= 100 :
            df_txt['angle_num'][i] = df_txt['angle_num'][i-1]

    # plot the data
    plt.plot(df_txt['angle_num'])
    plt.show()
    df_txt.to_csv(save_path + prefix + str(t) + '.csv', index = False)
    exec(prefix + str(t) + '=' + 'df_txt')  # create a name for each file
    t += 1
