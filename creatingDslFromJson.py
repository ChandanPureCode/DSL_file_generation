import json
import pc

from model import TreeNode

from utils import isContained, findDSL



def objectList(data):
    node = []
    count=0
    for item in data['0-1eVuGnuAWHnhIHPbRRj']['bounding_box_data']:
        tmp_node = TreeNode(item['id'],item['label'],item['xmin'],item['xmax'],item['ymin'],item['ymax'],[])
        node.append(tmp_node)
        count=count+1
    return node


def makingPrentChildRelationship(node):
    node.sort()
    parent = [-1]*len(node)
    parent[0] = node[0]
    for index in range(1,len(node)):
        for j in range(index-1,-1,-1):
            if isContained(node[j], node[index]):
                parent[index] = node[j]
                break;

    for i in range(len(parent)-1,0,-1):
        parent[i].children.append(node[i])
        node[i].parent = parent[i]

def createDSL(file):
    f = open (file, "r")
    data = json.loads(f.read())
    f.close()

    node = objectList(data);
    

    makingPrentChildRelationship(node)

    return findDSL(node[0])


print(createDSL('mock_response_data.json'))






