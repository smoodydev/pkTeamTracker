import os
 
# A Helpful Renamer - I used to convert Num-Name format to Just name format - incase I need to redo
def main():
   
    folder = "gifs"
    for count, filename in enumerate(os.listdir(folder)):
        print(filename)
        src =f"{folder}/{filename}"  
        dst =f"{folder}/{filename[4:]}"
         

        os.rename(src, dst)
 

if __name__ == '__main__':
    main()