from make_jsonc import Settings
import math
# a= Settings('test')
# data=a.load_settings()
# print(data)
# data = {
#     "search_color": "90,60,90",
#     "title_color": "255,255,255",
# }
# a.update_settings(data)
# data=a.load_settings()
# print(data)


# def main(i,j):
#     """
#     _summary_

#     Args:
#         i (_type_): _description_
#         j (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     root_i=math.sqrt(i)
#     root_j=math.sqrt(j)
#     multi=root_i*root_j
#     return multi

# def adminpanel():
#     print("Adminpanel")


# def guard_clause(wifi, login, password):
#     """
#     _summary_
    
    
    
#     Args:
#         - wifi (_type_): _description_
#         - login (_type_): _description_
#         - password (_type_): _description_
#     """
#     if not wifi:
#         print("No Wifi")
#         return
#     if not login:
#         print("No Login")
#         return
#     if not password:
#         print("No Password")
#         return
#     print("Login")
#     adminpanel()


# guard_clause(True, False, True)
import time

class ReturnStateUntilComplete():
    """
    _summary_
    
    
    """
    def __init__(self,length):
        self.list=self.listgenerator(120000)
        self.length=length
        self.value=0

    def listgenerator(self,max_value)->list[str]:
        # * Importand
        # ! This function is used to generate a list of numbers
        #* TODO
        # TODO: Make this function more efficient
        #? Questions

        list=[]
        for i in range(max_value):
            list.append(i)
        return list
    
    #create a function that counts until max_val is reached, if not it yields the current value, if yes it yields "complete"
    def count_until_complete(self):
        x=0
        #until x has reached the max value, yield x
        #if x has reached the max value, yield max value
        while x<self.length:
            #yield x
            time.sleep(0.8)
            x+=1
            #set self.value to x
            #send x to UI_main
            self.value=x

            yield x
        yield self.length
    def do_stuff(self,number):
        time.sleep(0.15)
        print(number)
        
        return number
    def run(self):
        for i in self.count_until_complete():
            print(i)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    

if __name__ == '__main__':
    x=testfunc(1,2)


