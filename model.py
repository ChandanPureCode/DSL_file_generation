class TreeNode:
    
    def __init__(self,id,label,xmin,xmax,ymin,ymax, children):
        self.id = '$' + id
        self.label = label
        self.xmin = self._is_valid_cordinate(xmin)
        self.xmax = self._is_valid_cordinate(xmax)
        self.ymin = self._is_valid_cordinate(ymin)
        self.ymax = self._is_valid_cordinate(ymax)
        self.area = (self.ymax - self.ymin)*(self.xmax - self.xmin)
        self.children = children or []
        self.parent = None
    def __lt__(self, other):
         return self.area > other.area
    def _is_valid_cordinate(self,val):
        try:
            return float(val)
        except:
            raise TypeError("Only integers and float are allowed")
        