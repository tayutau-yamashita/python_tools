# coding: utf-8
# 指定フォルダ以下の指定拡張子のファイル名の語尾に、全て.txtを足したファイル名に変更する

import os

def checkPath(path):
	files = os.listdir(path)
	for file in files:
		allPath = path + "/" + file
		if os.path.isdir(allPath) == True:
                    checkPath(allPath)
		else:
                    if allPath.find(".atlas") != -1 or allPath.find(".json") != -1:
                        if allPath.find(".txt") == -1:
                            print allPath
                            os.rename(allPath, allPath + ".txt")

checkPath("SpineModels")

