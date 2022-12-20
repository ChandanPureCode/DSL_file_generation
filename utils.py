import pc
from pc.encoder import encode


def isContained(parent,child):
    if parent.xmin <= child.xmin and parent.xmax >= child.xmax and parent.ymin <= child.ymin and parent.ymax >=child.ymax:
        return True
    return False



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


def findDSL(node):
    # creating a dsl instance to add the layers as well as the elements in it.
    dsl_instance = pc.DSL()

    # creating a component instance where we can add components in it.
    component_instance = pc.Component(node.id)
    
    # adding a component instance in the dsl instance that would enable us to add the components.
    dsl_instance.add_component(component_instance)

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
    
    parse_node(node)
    

    return encode(dsl_instance)

        

        

