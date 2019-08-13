# encoding: utf-8

import xmind
from typing import Dict
import typing as typing
import sys

def WalkTopic(dictXmind: Dict, resultDict: Dict):
    strTitle: typing.AnyStr = dictXmind['title']
    if 'topics' in dictXmind:
        pass
        # print(dictXmind['topics'])

        listTopics : typing.List = dictXmind['topics']

        if(listTopics.__len__() > 0):
            resultDict[strTitle] = {}
            for topic in listTopics:
                WalkTopic(topic, resultDict[strTitle])
    else:
        resultDict[strTitle] = strTitle

def Print2MDList(dictOri: typing.Dict) -> typing.AnyStr:
    levelOri = 0
    listStr = []

    def Print2MDListInternal(dictContent: typing.Dict, level):
        if type(dictContent).__name__ != 'dict':
            return
        level = level + 1
        for topic, topicDict in dictContent.items():
            listStr.append('  ' * (level - 1))
            listStr.append('- ')
            listStr.append(topic)
            listStr.append('\n')
            Print2MDListInternal(topicDict, level)

    Print2MDListInternal(dictOri, levelOri)

    return ''.join(listStr)

def main():
    print('sys.argv: ', sys.argv, "\n")

    pathSource = None
    pathOutput = None

    for i, val in enumerate(sys.argv):
        if(val == '-source'):
            pathSource = sys.argv[i + 1]
        if(val == '-output'):
            pathOutput = sys.argv[i + 1]

    pathSource = pathSource.replace('\\', '/')

    if pathOutput == None:
        pathOutput = pathSource.split('/')[-1].split('.')[0] + '.md'


    workbook = xmind.load(pathSource)
    sheet = workbook.getPrimarySheet()
    dictSheet = sheet.getData()
    dictResult: Dict = {}
    WalkTopic(dictSheet['topic'], dictResult)

    strResult = Print2MDList(dictResult)

    with open(pathOutput, 'w', encoding='utf-8') as f:
        f.write(strResult)
        print('Successfully wrote result into file: ' + pathOutput)

    # print(strResult)
    # print(dictSheet)

if __name__ == "__main__":
    main()