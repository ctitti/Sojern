class Version:
    def __init__(self):
        pass

    def versionCompare(self, version_1, version_2):

        if type(version_1) is str and type(version_2) is str:
            if version_1 != '' and version_2 != '':
                vers_1 = [v for v in version_1.split(".") ]
                vers_2 = [v for v in version_2.split(".") ]

                print(vers_1)
                print(vers_2)

                for val in vers_1:
                    if(val.isdigit() == False):
                        return None
                        print("This version is not in a valid format : ", vers_1)
                
                for val in vers_2:
                    if(val.isdigit() == False):
                        return None
                        print("This version is not in a valid format :", vers_2)         

                for i in range (max(len(version_1),len(version_2))):                    
                    v1 = vers_1[i] if i < len(vers_1) else 0
                    v2 = vers_2[i] if i < len(vers_2) else 0 

                    if int(v1) > int(v2):
                        return 1
                    elif int(v1) < int(v2):
                        return -1
                    elif int(v1) < int(v2):
                        return 0                                                
            else:
                print("This version is not in a valid format : ", version_1, version_2) 
        else:
            print("This version is not in a valid format : ", version_1, version_2) 
 

##### Test Cases #####  

obj = Version()
print(obj.versionCompare("","")) 
print(obj.versionCompare("20.3.2","19.3.8"))
print(obj.versionCompare("1.0.1","2.0"))
print(obj.versionCompare("20.3.8dev","20.3.8")) 
print(obj.versionCompare("20.3.8",""))
print(obj.versionCompare("1.2.9.9.9.9","1.3"))
print(obj.versionCompare("0.1","1.1"))
print(obj.versionCompare("1.3","1.3.4"))   