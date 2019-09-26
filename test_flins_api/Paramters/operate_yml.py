# -*- coding:utf-8 -*-
import json
import yaml

class operateYaml():

    def __init__(self,yml_file=None):
        if yml_file:
            self.yml_file = yml_file
        else:
            self.yml_file = "E:/git_flins_api/test_flins_api/Paramters/breast/breast_params.yaml"
        self.data = self.read_data()

    #读取yml文件
    def read_data(self):
        yml = open(self.yml_file,'r',encoding="utf-8")
        data = yaml.load(yml)
        return data



if __name__ == '__main__':
    yaml = operateYaml().read_data()
    value = yaml["restrict"][0]["breast"]
    print(value)

