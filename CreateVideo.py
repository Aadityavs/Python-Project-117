import os
import cv2

path='Images'
image=[]

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        image.append(file_name)

count=len(image)
frame=cv2.imread(image[0])
heigth,width,channels=frame.shape
size=(width,heigth)
print(size)

out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):
    frame=cv2.imread(image[i])
    out.write(frame)

print('done')

out.release()