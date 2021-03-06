<<<<<<< HEAD
# -*- coding: utf-8 -*-
import dicom # for reading dicom files
import os # for doing directory operations 
import pandas as pd # for some simple data analysis (right now, just to load in the labels data and quickly reference it)
# Change this to wherever you are storing your data:
# IF YOU ARE FOLLOWING ON KAGGLE, YOU CAN ONLY PLAY WITH THE SAMPLE DATA, WHICH IS MUCH SMALLER
import tensorflow as tf
import numpy as np

data_dir = 'C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/sample_images_Corrected/'
patients = os.listdir(data_dir)
labels_df = pd.read_csv('C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/stage1_labels.csv', index_col=0)

labels_df.head()

for patient in patients[:1]:
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    
    # a couple great 1-liners from: https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
    print(len(slices),label)
    print(slices[0])
    

for patient in patients[:3]:
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    
    # a couple great 1-liners from: https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
    print(slices[0].pixel_array.shape, len(slices))   
    
    len(patients)  
    
    
    
import matplotlib.pyplot as plt

for patient in patients[:1]:
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
    
    #          the first slice
    plt.imshow(slices[0].pixel_array)
    plt.show()
    
    
    
import cv2
import numpy as np

IMG_PX_SIZE = 150

for patient in patients[:1]:
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
    fig = plt.figure()
    for num,each_slice in enumerate(slices[:12]):
        y = fig.add_subplot(3,4,num+1)
        new_img = cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE))
        y.imshow(new_img)
    plt.show()    
    
    
    
import math

def chunks(l, n):
    # Credit: Ned Batchelder
    # Link: http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """Yield successive n-sized chunks from l."""
    count=0
    for i in range(0, len(l), int(n)):
        if(count < HM_SLICES):
            yield l[i:i + int(n)]
            count=count+1

def mean(l):
    return sum(l) / len(l)

IMG_PX_SIZE = 150
HM_SLICES = 20

data_dir = 'C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/sample_images_Corrected/'
patients = os.listdir(data_dir)
labels_df = pd.read_csv('C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/stage1_labels.csv', index_col=0)

for patient in patients[:10]:
    try:
        label = labels_df.get_value(patient, 'cancer')
        path = data_dir + patient
        slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
        slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
        new_slices = []
        slices = [cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE)) for each_slice in slices]
        chunk_sizes = math.floor(len(slices) / HM_SLICES)
        for slice_chunk in chunks(slices, chunk_sizes):
            slice_chunk = list(map(mean, zip(*slice_chunk)))
            new_slices.append(slice_chunk)

        print(len(slices), len(new_slices))
    except:
        # some patients don't have labels, so we'll just pass on this for now
        pass
    
    
    for patient in patients[:10]:
        try:
            label = labels_df.get_value(patient, 'cancer')
            path = data_dir + patient
            slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
            slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
            new_slices = []

            slices = [cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE)) for each_slice in slices]

            chunk_sizes = math.floor(len(slices) / HM_SLICES)


            for slice_chunk in chunks(slices, chunk_sizes):
                slice_chunk = list(map(mean, zip(*slice_chunk)))
                new_slices.append(slice_chunk)

            if len(new_slices) == HM_SLICES-1:
                new_slices.append(new_slices[-1])

            if len(new_slices) == HM_SLICES-2:
                new_slices.append(new_slices[-1])
                new_slices.append(new_slices[-1])

            if len(new_slices) == HM_SLICES+2:
                new_val = list(map(mean, zip(*[new_slices[HM_SLICES-1],new_slices[HM_SLICES],])))
                del new_slices[HM_SLICES]
                new_slices[HM_SLICES-1] = new_val

            if len(new_slices) == HM_SLICES+1:
                new_val = list(map(mean, zip(*[new_slices[HM_SLICES-1],new_slices[HM_SLICES],])))
                del new_slices[HM_SLICES]
                new_slices[HM_SLICES-1] = new_val

            print(len(slices), len(new_slices))
        except Exception as e:
                # again, some patients are not labeled, but JIC we still want the error if something
                # else is wrong with our code
                print(str(e))
                
for patient in patients[:1]:
                    label = labels_df.get_value(patient, 'cancer')
                    path = data_dir + patient
                    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
                    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
                    new_slices = []
                
                    slices = [cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE)) for each_slice in slices]
                    
                    chunk_sizes = math.floor(len(slices) / HM_SLICES)
                    for slice_chunk in chunks(slices, chunk_sizes):
                        slice_chunk = list(map(mean, zip(*slice_chunk)))
                        new_slices.append(slice_chunk)
                
                    if len(new_slices) == HM_SLICES-1:
                        new_slices.append(new_slices[-1])
                
                    if len(new_slices) == HM_SLICES-2:
                        new_slices.append(new_slices[-1])
                        new_slices.append(new_slices[-1])
                
                    if len(new_slices) == HM_SLICES+2:
                        new_val = list(map(mean, zip(*[new_slices[HM_SLICES-1],new_slices[HM_SLICES],])))
                        del new_slices[HM_SLICES]
                        new_slices[HM_SLICES-1] = new_val
                        
                    if len(new_slices) == HM_SLICES+1:
                        new_val = list(map(mean, zip(*[new_slices[HM_SLICES-1],new_slices[HM_SLICES],])))
                        del new_slices[HM_SLICES]
                        new_slices[HM_SLICES-1] = new_val
                    
                    fig = plt.figure()
                    for num,each_slice in enumerate(new_slices):
                        y = fig.add_subplot(4,5,num+1)
                        y.imshow(each_slice, cmap='gray')
                    plt.show()
                    

import numpy as np
import pandas as pd
import dicom
import os
import matplotlib.pyplot as plt
import cv2
import math

IMG_SIZE_PX = 50
SLICE_COUNT = 20

def chunks(l, n):
    # Credit: Ned Batchelder
    # Link: http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), int(n)):
        yield l[i:i + int(n)]


def mean(a):
    return sum(a) / len(a)


def process_data(patient,labels_df,img_px_size=50, hm_slices=20, visualize=False):
    
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))

    new_slices = []
    slices = [cv2.resize(np.array(each_slice.pixel_array),(img_px_size,img_px_size)) for each_slice in slices]
    
    chunk_sizes = math.ceil(len(slices) / hm_slices)
    for slice_chunk in chunks(slices, chunk_sizes):
        slice_chunk = list(map(mean, zip(*slice_chunk)))
        new_slices.append(slice_chunk)

    if len(new_slices) == hm_slices-1:
        new_slices.append(new_slices[-1])

    if len(new_slices) == hm_slices-2:
        new_slices.append(new_slices[-1])
        new_slices.append(new_slices[-1])

    if len(new_slices) == hm_slices+2:
        new_val = list(map(mean, zip(*[new_slices[hm_slices-1],new_slices[hm_slices],])))
        del new_slices[hm_slices]
        new_slices[hm_slices-1] = new_val
        
    if len(new_slices) == hm_slices+1:
        new_val = list(map(mean, zip(*[new_slices[hm_slices-1],new_slices[hm_slices],])))
        del new_slices[hm_slices]
        new_slices[hm_slices-1] = new_val

    if visualize:
        fig = plt.figure()
        for num,each_slice in enumerate(new_slices):
            y = fig.add_subplot(4,5,num+1)
            y.imshow(each_slice, cmap='gray')
        plt.show()

    if label == 1: label=np.array([0,1])
    elif label == 0: label=np.array([1,0])
        
    return np.array(new_slices),label

#                                               stage 1 for real.
data_dir = 'C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/sample_images_Corrected/'
patients = os.listdir(data_dir)
labels = pd.read_csv('C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/stage1_labels.csv', index_col=0)

much_data = []
for num,patient in enumerate(patients):
    if num % 100 == 0:
        print(num)
    try:
        img_data,label = process_data(patient,labels,img_px_size=IMG_SIZE_PX, hm_slices=SLICE_COUNT)
        print(img_data.shape,label)
        much_data.append([img_data,label])
    except KeyError as e:
        print('This is unlabeled data!')

np.save('muchdata-{}-{}-{}.npy'.format(IMG_SIZE_PX,IMG_SIZE_PX,SLICE_COUNT), much_data)





IMG_SIZE_PX = 50
SLICE_COUNT = 20

n_classes = 2
batch_size = 10

x = tf.placeholder('float')
y = tf.placeholder('float')

keep_rate = 0.8
print("print x:")
print(x)
def conv3d(x, W):
    return tf.nn.conv3d(x, W, strides=[1,1,1,1,1], padding='SAME')

def maxpool3d(x):
    #                        size of window         movement of window as you slide about
    return tf.nn.max_pool3d(x, ksize=[1,2,2,2,1], strides=[1,2,2,2,1], padding='SAME')

def convolutional_neural_network(x):
    #                # 5 x 5 x 5 patches, 1 channel, 32 features to compute.
    weights = {'W_conv1':tf.Variable(tf.random_normal([3,3,3,1,32])),
               #       5 x 5 x 5 patches, 32 channels, 64 features to compute.
               'W_conv2':tf.Variable(tf.random_normal([3,3,3,32,64])),
               #                                  64 features
               'W_fc':tf.Variable(tf.random_normal([54080,1024])),
               'out':tf.Variable(tf.random_normal([1024, n_classes]))}

    biases = {'b_conv1':tf.Variable(tf.random_normal([32])),
               'b_conv2':tf.Variable(tf.random_normal([64])),
               'b_fc':tf.Variable(tf.random_normal([1024])),
               'out':tf.Variable(tf.random_normal([n_classes]))}

    #                            image X      image Y        image Z
    x = tf.reshape(x, shape=[-1, IMG_SIZE_PX, IMG_SIZE_PX, SLICE_COUNT, 1])

    conv1 = tf.nn.relu(conv3d(x, weights['W_conv1']) + biases['b_conv1'])
    conv1 = maxpool3d(conv1)


    conv2 = tf.nn.relu(conv3d(conv1, weights['W_conv2']) + biases['b_conv2'])
    conv2 = maxpool3d(conv2)

    fc = tf.reshape(conv2,[-1, 54080])
    fc = tf.nn.relu(tf.matmul(fc, weights['W_fc'])+biases['b_fc'])
    fc = tf.nn.dropout(fc, keep_rate)

    output = tf.matmul(fc, weights['out'])+biases['out']

    return output

	# Citation : https://www.kaggle.com/sentdex/first-pass-through-data-w-3d-convnet
=======
# -*- coding: utf-8 -*-
import dicom # for reading dicom files
import os # for doing directory operations 
import pandas as pd # for some simple data analysis (right now, just to load in the labels data and quickly reference it)
# Change this to wherever you are storing your data:
# IF YOU ARE FOLLOWING ON KAGGLE, YOU CAN ONLY PLAY WITH THE SAMPLE DATA, WHICH IS MUCH SMALLER
import tensorflow as tf
import numpy as np

data_dir = 'C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/sample_images_Corrected/'
patients = os.listdir(data_dir)
labels_df = pd.read_csv('C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/stage1_labels.csv', index_col=0)

labels_df.head()

for patient in patients[:1]:
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    
    # a couple great 1-liners from: https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
    print(len(slices),label)
    print(slices[0])
    

for patient in patients[:3]:
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    
    # a couple great 1-liners from: https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
    print(slices[0].pixel_array.shape, len(slices))   
    
    len(patients)  
    
    
    
import matplotlib.pyplot as plt

for patient in patients[:1]:
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
    
    #          the first slice
    plt.imshow(slices[0].pixel_array)
    plt.show()
    
    
    
import cv2
import numpy as np

IMG_PX_SIZE = 150

for patient in patients[:1]:
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
    fig = plt.figure()
    for num,each_slice in enumerate(slices[:12]):
        y = fig.add_subplot(3,4,num+1)
        new_img = cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE))
        y.imshow(new_img)
    plt.show()    
    
    
    
import math

def chunks(l, n):
    # Credit: Ned Batchelder
    # Link: http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """Yield successive n-sized chunks from l."""
    count=0
    for i in range(0, len(l), int(n)):
        if(count < HM_SLICES):
            yield l[i:i + int(n)]
            count=count+1

def mean(l):
    return sum(l) / len(l)

IMG_PX_SIZE = 150
HM_SLICES = 20

data_dir = 'C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/sample_images_Corrected/'
patients = os.listdir(data_dir)
labels_df = pd.read_csv('C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/stage1_labels.csv', index_col=0)

for patient in patients[:10]:
    try:
        label = labels_df.get_value(patient, 'cancer')
        path = data_dir + patient
        slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
        slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
        new_slices = []
        slices = [cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE)) for each_slice in slices]
        chunk_sizes = math.floor(len(slices) / HM_SLICES)
        for slice_chunk in chunks(slices, chunk_sizes):
            slice_chunk = list(map(mean, zip(*slice_chunk)))
            new_slices.append(slice_chunk)

        print(len(slices), len(new_slices))
    except:
        # some patients don't have labels, so we'll just pass on this for now
        pass
    
    
    for patient in patients[:10]:
        try:
            label = labels_df.get_value(patient, 'cancer')
            path = data_dir + patient
            slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
            slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
            new_slices = []

            slices = [cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE)) for each_slice in slices]

            chunk_sizes = math.floor(len(slices) / HM_SLICES)


            for slice_chunk in chunks(slices, chunk_sizes):
                slice_chunk = list(map(mean, zip(*slice_chunk)))
                new_slices.append(slice_chunk)

            if len(new_slices) == HM_SLICES-1:
                new_slices.append(new_slices[-1])

            if len(new_slices) == HM_SLICES-2:
                new_slices.append(new_slices[-1])
                new_slices.append(new_slices[-1])

            if len(new_slices) == HM_SLICES+2:
                new_val = list(map(mean, zip(*[new_slices[HM_SLICES-1],new_slices[HM_SLICES],])))
                del new_slices[HM_SLICES]
                new_slices[HM_SLICES-1] = new_val

            if len(new_slices) == HM_SLICES+1:
                new_val = list(map(mean, zip(*[new_slices[HM_SLICES-1],new_slices[HM_SLICES],])))
                del new_slices[HM_SLICES]
                new_slices[HM_SLICES-1] = new_val

            print(len(slices), len(new_slices))
        except Exception as e:
                # again, some patients are not labeled, but JIC we still want the error if something
                # else is wrong with our code
                print(str(e))
                
for patient in patients[:1]:
                    label = labels_df.get_value(patient, 'cancer')
                    path = data_dir + patient
                    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
                    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))
                    new_slices = []
                
                    slices = [cv2.resize(np.array(each_slice.pixel_array),(IMG_PX_SIZE,IMG_PX_SIZE)) for each_slice in slices]
                    
                    chunk_sizes = math.floor(len(slices) / HM_SLICES)
                    for slice_chunk in chunks(slices, chunk_sizes):
                        slice_chunk = list(map(mean, zip(*slice_chunk)))
                        new_slices.append(slice_chunk)
                
                    if len(new_slices) == HM_SLICES-1:
                        new_slices.append(new_slices[-1])
                
                    if len(new_slices) == HM_SLICES-2:
                        new_slices.append(new_slices[-1])
                        new_slices.append(new_slices[-1])
                
                    if len(new_slices) == HM_SLICES+2:
                        new_val = list(map(mean, zip(*[new_slices[HM_SLICES-1],new_slices[HM_SLICES],])))
                        del new_slices[HM_SLICES]
                        new_slices[HM_SLICES-1] = new_val
                        
                    if len(new_slices) == HM_SLICES+1:
                        new_val = list(map(mean, zip(*[new_slices[HM_SLICES-1],new_slices[HM_SLICES],])))
                        del new_slices[HM_SLICES]
                        new_slices[HM_SLICES-1] = new_val
                    
                    fig = plt.figure()
                    for num,each_slice in enumerate(new_slices):
                        y = fig.add_subplot(4,5,num+1)
                        y.imshow(each_slice, cmap='gray')
                    plt.show()
                    

import numpy as np
import pandas as pd
import dicom
import os
import matplotlib.pyplot as plt
import cv2
import math

IMG_SIZE_PX = 50
SLICE_COUNT = 20

def chunks(l, n):
    # Credit: Ned Batchelder
    # Link: http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), int(n)):
        yield l[i:i + int(n)]


def mean(a):
    return sum(a) / len(a)


def process_data(patient,labels_df,img_px_size=50, hm_slices=20, visualize=False):
    
    label = labels_df.get_value(patient, 'cancer')
    path = data_dir + patient
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key = lambda x: int(x.ImagePositionPatient[2]))

    new_slices = []
    slices = [cv2.resize(np.array(each_slice.pixel_array),(img_px_size,img_px_size)) for each_slice in slices]
    
    chunk_sizes = math.ceil(len(slices) / hm_slices)
    for slice_chunk in chunks(slices, chunk_sizes):
        slice_chunk = list(map(mean, zip(*slice_chunk)))
        new_slices.append(slice_chunk)

    if len(new_slices) == hm_slices-1:
        new_slices.append(new_slices[-1])

    if len(new_slices) == hm_slices-2:
        new_slices.append(new_slices[-1])
        new_slices.append(new_slices[-1])

    if len(new_slices) == hm_slices+2:
        new_val = list(map(mean, zip(*[new_slices[hm_slices-1],new_slices[hm_slices],])))
        del new_slices[hm_slices]
        new_slices[hm_slices-1] = new_val
        
    if len(new_slices) == hm_slices+1:
        new_val = list(map(mean, zip(*[new_slices[hm_slices-1],new_slices[hm_slices],])))
        del new_slices[hm_slices]
        new_slices[hm_slices-1] = new_val

    if visualize:
        fig = plt.figure()
        for num,each_slice in enumerate(new_slices):
            y = fig.add_subplot(4,5,num+1)
            y.imshow(each_slice, cmap='gray')
        plt.show()

    if label == 1: label=np.array([0,1])
    elif label == 0: label=np.array([1,0])
        
    return np.array(new_slices),label

#                                               stage 1 for real.
data_dir = 'C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/sample_images_Corrected/'
patients = os.listdir(data_dir)
labels = pd.read_csv('C:/Users/rajan/Desktop/Sem5/ADataScience/Project/ProjectData/stage1_labels.csv', index_col=0)

much_data = []
for num,patient in enumerate(patients):
    if num % 100 == 0:
        print(num)
    try:
        img_data,label = process_data(patient,labels,img_px_size=IMG_SIZE_PX, hm_slices=SLICE_COUNT)
        print(img_data.shape,label)
        much_data.append([img_data,label])
    except KeyError as e:
        print('This is unlabeled data!')

np.save('muchdata-{}-{}-{}.npy'.format(IMG_SIZE_PX,IMG_SIZE_PX,SLICE_COUNT), much_data)





IMG_SIZE_PX = 50
SLICE_COUNT = 20

n_classes = 2
batch_size = 10

x = tf.placeholder('float')
y = tf.placeholder('float')

keep_rate = 0.8
print("print x:")
print(x)
def conv3d(x, W):
    return tf.nn.conv3d(x, W, strides=[1,1,1,1,1], padding='SAME')

def maxpool3d(x):
    #                        size of window         movement of window as you slide about
    return tf.nn.max_pool3d(x, ksize=[1,2,2,2,1], strides=[1,2,2,2,1], padding='SAME')

def convolutional_neural_network(x):
    #                # 5 x 5 x 5 patches, 1 channel, 32 features to compute.
    weights = {'W_conv1':tf.Variable(tf.random_normal([3,3,3,1,32])),
               #       5 x 5 x 5 patches, 32 channels, 64 features to compute.
               'W_conv2':tf.Variable(tf.random_normal([3,3,3,32,64])),
               #                                  64 features
               'W_fc':tf.Variable(tf.random_normal([54080,1024])),
               'out':tf.Variable(tf.random_normal([1024, n_classes]))}

    biases = {'b_conv1':tf.Variable(tf.random_normal([32])),
               'b_conv2':tf.Variable(tf.random_normal([64])),
               'b_fc':tf.Variable(tf.random_normal([1024])),
               'out':tf.Variable(tf.random_normal([n_classes]))}

    #                            image X      image Y        image Z
    x = tf.reshape(x, shape=[-1, IMG_SIZE_PX, IMG_SIZE_PX, SLICE_COUNT, 1])

    conv1 = tf.nn.relu(conv3d(x, weights['W_conv1']) + biases['b_conv1'])
    conv1 = maxpool3d(conv1)


    conv2 = tf.nn.relu(conv3d(conv1, weights['W_conv2']) + biases['b_conv2'])
    conv2 = maxpool3d(conv2)

    fc = tf.reshape(conv2,[-1, 54080])
    fc = tf.nn.relu(tf.matmul(fc, weights['W_fc'])+biases['b_fc'])
    fc = tf.nn.dropout(fc, keep_rate)

    output = tf.matmul(fc, weights['out'])+biases['out']

    return output

	# Citation : https://www.kaggle.com/sentdex/first-pass-through-data-w-3d-convnet
>>>>>>> 085003715712a966ace9afaab2c02774669f6f61
