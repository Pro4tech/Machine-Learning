import os                           #To enable file traversal of pics
import cv2,random,numpy,pickle
import matplotlib.pyplot as plt

#Initialization of Variables
DataDir='/home/pritesh/Desktop/ML/python/Tensorflow/Data-Sets/PetImages'
categories=['Dog','Cat']
img_size=70     #Sets the square resolution of the downscaled image
training_data=[]
count=0

#Setting of the Data
for category in categories:
    path=os.path.join(DataDir,category) #gives the location of the images folders
    #ie DataDir/(Cats/Dogs)
    class_num=categories.index(category)
    for img in os.listdir(path):        #Gives the location of individual files
        count+=1
        percent=count*100/len(os.listdir(path))
        print('Progress:',percent/2,end='\r')
        try:
            im_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)    #directly gives the grayscale images
            new_array=cv2.resize(im_array,(img_size,img_size))
        except:
            pass

        training_data.append([new_array,class_num]) #Seting of the training_data

#Randomize the Images for the Training Data
random.shuffle(training_data)
x,y=[],[]

for features,labels in training_data:
     x.append(features)
     y.append(labels)

#To change the shape of list x and numpy.array is used to provide numpy array input to the ML Logic
x=numpy.array(x).reshape(-1,img_size,img_size,1)    #1 is given since it is greyscale and for RGB it is given to be 3

print()
#Saving the Processed Data for Further Processing
#Saving the Image data
pickle_out=open("pickle/x.pickle",'wb')
pickle.dump(x,pickle_out)                   #will transfer the images in a file as saving of the Data
pickle_out.close()                          #Closes of the file(File Operation)
print('Image-File is complete')

#Saving of the label Data
pickle_out=open("pickle/y.pickle",'wb')
pickle.dump(y,pickle_out)                   #will transfer the images data in a file as saving of the Data
pickle_out.close()                          #Closes of the file(File Operation)
print('Label-File is complete')
