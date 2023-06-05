import os
import cv2
path= 'Images'
images= []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in['.jpg','.png','.jpeg','.jfif']:
        file_name= path+"/"+file
        print(file_name)
        images.append(file_name)

        print(len(images))
        count= len(images)
        frame= cv2.imread(images[0])
        height,width,channels= frame.shape
        size=(width,height)
frnds= cv2.VideoWriter("frnds.mp4",cv2.VideoWriter_fourcc(*'DIVX'),5,size)

for i in range (0,count-1):
    frame= cv2.imread(images[i])
    frnds.write(frame)
    
frnds.release()

print("Done")