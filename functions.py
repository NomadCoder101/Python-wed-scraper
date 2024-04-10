import os

def create_dir(folde_name):
    if not os.path.exists(folde_name):
        os.makedirs(folde_name)




def remove_dir(folde_name):
    os.rmdir(folde_name)
    
  
def create_new_file(path):
    
   f = open(path, 'w')
   f.write("")
   f.close()
   

def write_to_file(path,data):
    
    with open(path, 'a') as file:
        file.write(data + '\n')
        file.close()     
        
        
def clear_file(path):
    
    f= open(path, 'w')
    f.close()


def does_file_exists(path):
     return  os.path.isfile(path)
   
    

def read_file(path):
    with open(path,'rt') as file:
        for line in file:
            print(line.replace('\n',''))
            

 
 
def read_lines(path,lines):
    
    with open(path,'rt') as file:
        current_line=0
        for line in file:
            if current_line == lines:
                break
            current_line =current_line +1
            print(line.replace('\n',''))


#calling the functions below:

#remove_dir('wiki')

#create_dir('Wiki2')

#create_new_file('Wiki/test.txt')

#write_to_file("Wiki/test.txt","This is the data we like to store ")



#clear_file("Wiki/test.txt")

#print(does_file_exists('Wiki/test.txt'))
              
#read_file('Wiki/test.txt')