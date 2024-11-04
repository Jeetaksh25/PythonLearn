class DSAClass:
    def Dictionary(self):
        number_of_value=int(input("Enter the number of values: "))
        d={}
        for i in range(number_of_value):
            key=input(f"Enter #{i+1} key: ")
            value=input(f"Enter #{i+1} value: ")
            d[key]=value
        print(d)

        key_pop=input("Enter the index to pop: ")
        d.pop(key_pop)
        print(d)

        d.popitem()
        print(d)

    def list_to_dict(self):
        Key=map(str,input("Enter the keys: ").split(" "))
        Values=map(str,input("Enter the values: ").split(" "))
        d=dict(zip(Key,Values))
        print(d)

    def 

obj=DSAClass()
obj.list_to_dict()