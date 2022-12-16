import json
import pc

# Reading data from Json file
f = open ("mock_response_data.json", "r")

data = json.loads(f.read())

f.close()

class Node:
    
    def __init__(self,id,label,xmin,xmax,ymin,ymax, children):
        self.id = '$' + id
        self.label = label
        self.xmin = int(xmin)
        self.xmax = int(xmax)
        self.ymin = int(ymin)
        self.ymax = int(ymax)
        self.area = (self.ymax - self.ymin)*(self.xmax - self.xmin)
        self.children = children or []
        self.parent = None
    def __lt__(self, other):
         return self.area > other.area

node = []

count=0
for item in data['0-1eVuGnuAWHnhIHPbRRj']['bounding_box_data']:
    tmp_node = Node(item['id'],item['label'],item['xmin'],item['xmax'],item['ymin'],item['ymax'],[])
    node.append(tmp_node)
    count=count+1



node.sort()

def isContained(parent,child):
    if parent.xmin <= child.xmin and parent.xmax >= child.xmax and parent.ymin <= child.ymin and parent.ymax >=child.ymax:
        return True
    return False

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

def printTree(node):
    queue = []
 
    # Enqueue Root and initialize height
    queue.append(node)
 
    while(len(queue) > 0):
        
        
        level_length = len(queue);
        
        while level_length > 0:
            node = queue.pop(0)
            print(node.label, end = " ")
            for child in node.children:
                queue.append(child)
            level_length= level_length -1;
        print()
        print('********************')

#printTree(node[0])


# creating a dsl instance to add the layers as well as the elements in it.
dsl_instance = pc.DSL()

# creating a component instance where we can add components in it.
component_instance = pc.Component(node[0].id)




# adding a component instance in the dsl instance that would enable us to add the components.
dsl_instance.add_component(component_instance)


# root_layer = pc.Layer(root_node.data.split('.')[1])
# root_layer = pc.Layer(root_node.data[::-1])
# print(root_layer)

# root_layer.import_library = 'mui'
# root_layer.import_name = root_node.data.split('.')[1]
# root_layer.is_root = True
# print(root_layer)
# parse_node(root_node)
def parse_node(node):

    layer = pc.Layer(node.id)
    component_instance.add_layer(layer)
    layer.import_library = 'mui'
    layer.import_name = node.label
    if node.parent == None:
        layer.is_root = True
    else:
        layer.parent = pc.Identifier(node.parent.id)
    for child in node.children:
        parse_node(child)
    


parse_node(node[0])
print(dsl_instance)