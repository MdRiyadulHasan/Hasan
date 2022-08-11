from mtcnn import MTCNN
import numpy as np
import rotate

def align_image(img):
    detector=MTCNN()
    data=detector.detect_faces(img)
    for face in data:
        box=face['box']
        keypoints=face['keypoints']
        left_eye=keypoints['left_eye']
        right_eye=keypoints['right_eye'] 
        lx,ly=left_eye        
        rx,ry=right_eye
        dx=rx-lx
        dy=ry-ly
        tan=dy/dx
        theta=np.arctan(tan)
        theta=np.degrees(theta)  
        img=rotate.rotate_bound(img, theta)
        return (True,img)