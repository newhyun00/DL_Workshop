import numpy as np
import os, shutil, glob
from skimage.io import imread, imsave

patient_list = sorted(glob.glob('./Data/Original/*/'))
num_patients = len(patient_list)

np.random.shuffle(patient_list)

data_summary = np.zeros((num_patients, 2), np.int16)

for i in range(num_patients):
	num_ben = len(sorted(glob.glob(patient_list[i]+'0/*.png')))
	num_mal = len(sorted(glob.glob(patient_list[i]+'1/*.png')))

	data_summary[i][0] = num_ben
	data_summary[i][1] = num_mal


print(data_summary)
print('Number of patients: ', num_patients) 
print('Minimum number benign images', np.min(data_summary[:,0]))
print('Minimum number malignant images',np.min(data_summary[:,1]))  
print('Maximum number benign images', np.max(data_summary[:,0]))
print('Maximum number malignant images',np.max(data_summary[:,1]))   

training_ben_path = './Data/Train/0/'
training_mal_path = './Data/Train/1/'

validation_ben_path = './Data/Valid/0/'
validation_mal_path = './Data/Valid/1/'

testing_ben_path = './Data/Test/0/'
testing_mal_path = './Data/Test/1/'

data_folders = []
data_folders.append(training_ben_path)
data_folders.append(training_mal_path)
data_folders.append(validation_ben_path)
data_folders.append(validation_mal_path)
data_folders.append(testing_ben_path)
data_folders.append(testing_mal_path)

for i in range(len(data_folders)):
	if os.path.exists(data_folders[i]):
		shutil.rmtree(data_folders[i])
	os.makedirs(data_folders[i]) 

#Number of training patients: 223
#Number of validation patients: 28
#Number of testing patients: 28

train_patients = patient_list[0:223]
valid_patients = patient_list[223:223+28]
test_patients = patient_list[223+28:]

print('Num Train Patients: ', len(train_patients))
print('Num Valid Patients: ', len(valid_patients))
print('Num Test Patients: ', len(test_patients))

#Relocating Training images
for i in range(len(train_patients)):
	#Benign and malignant images
	ben_image_list = sorted(glob.glob(train_patients[i] + '0/*.png'))
	mal_image_list = sorted(glob.glob(train_patients[i] + '1/*.png'))

	#Randomly shuffle
	np.random.shuffle(ben_image_list)
	np.random.shuffle(mal_image_list)

	for j in range(10):
		shutil.copyfile(ben_image_list[j], training_ben_path+os.path.basename(ben_image_list[j]))
		shutil.copyfile(mal_image_list[j], training_mal_path+os.path.basename(mal_image_list[j]))

#Relocating Validation images
for i in range(len(valid_patients)):
	#Benign and malignant images
	ben_image_list = sorted(glob.glob(valid_patients[i] + '0/*.png'))
	mal_image_list = sorted(glob.glob(valid_patients[i] + '1/*.png'))

	#Randomly shuffle
	np.random.shuffle(ben_image_list)
	np.random.shuffle(mal_image_list)

	for j in range(10):
		shutil.copyfile(ben_image_list[j], validation_ben_path+os.path.basename(ben_image_list[j]))
		shutil.copyfile(mal_image_list[j], validation_mal_path+os.path.basename(mal_image_list[j]))

#Relocating Testing images
for i in range(len(test_patients)):
	#Benign and malignant images
	ben_image_list = sorted(glob.glob(test_patients[i] + '0/*.png'))
	mal_image_list = sorted(glob.glob(test_patients[i] + '1/*.png'))

	#Randomly shuffle
	np.random.shuffle(ben_image_list)
	np.random.shuffle(mal_image_list)

	for j in range(10):
		shutil.copyfile(ben_image_list[j], testing_ben_path+os.path.basename(ben_image_list[j]))
		shutil.copyfile(mal_image_list[j], testing_mal_path+os.path.basename(mal_image_list[j]))    
