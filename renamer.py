import os
 
# A Helpful Renamer - I used to convert Num-Name format to Just name format - incase I need to redo
def rename():
    folder = "gifs"
    for count, filename in enumerate(os.listdir(folder)):
        print(filename)
        src =f"{folder}/{filename}"  
        dst =f"{folder}/{filename[4:]}"
         

        os.rename(src, dst)
 
# Helper function to create a list of all name based off gif/png/bmp files available
def writeNames():
    folder = "gifs"
    with open("randomfile.txt", "a") as o:
        for names in os.listdir(folder):
            print(names)
            o.write(f'"{names[:-4]}",')
        #     print(names)
        # o.write('Hello')
        # o.write('This text will be added to the file')

if __name__ == '__main__':
    writeNames()