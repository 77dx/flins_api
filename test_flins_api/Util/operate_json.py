# -*- coding:utf-8 -*-
import json

class operateJSON():

    def __init__(self,json_file):

        self.json_data = json_file
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.json_data,'r',encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,key):
        return self.data[key]



if __name__ == '__main__':

    operateJSON('E:/git_flins_api/test_flins_api/Paramters/breast/female.json')

