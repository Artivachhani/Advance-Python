
import urllib.request
from PIL import Image

def readUrl():
    
    try:
        url  = input("Please Enter Url: ")
        response = urllib.request.urlopen(url)
        output = response.read()
        output = output.decode('utf-8')
        print(output)
        
    except Exception as e :
        print(str(e))
        
    #img = Image.open("c:\\Users\\khush\\Desktop\\arti\\Test.jpg")
    #img.show()



def main():
    readUrl()

if __name__ == '__main__':
    main()
