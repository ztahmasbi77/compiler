rows, cols = (100, 100)
arr = [[0]*cols]*rows 
i = 0

class SymTabEntry:
    def __init__(self, id, type):
        self.id = id
        self.type = type
        

class SymTab:


    def _error (count_meghdar,count_sotun):
        if count_meghdar != count_sotun:
            print(end='\n')
            print ("error: values != numbers")
        
    def insert(self, symbol):
        global i
        arr[i][i]=(self, symbol)
        i=i+1
        print("", end="")

    def remove(self, id):
        self.cur.remove(id)

    def get(self, id):
        table = self.cur
        while table != None:
            entry = table.get(id)
            if entry != None:
                table = table.prev
            else:
                return entry
        return None
