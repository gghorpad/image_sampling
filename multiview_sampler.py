already_labeled = input('Have you already labeled some images in this section(yes/no) :')
sampled_images=[]
if already_labeled == 'yes':
    file_annotate = open('sampler_annotate_list.txt','r')
    file_raw = open('sampler_raw_list.txt','r')

    annotate_last = (str.split(file_annotate.read()))[-1][:-3]+'jpg'
    all_images = (str.split(file_raw.read()))

    last_labeled_index = all_images.index(annotate_last)
    sampling_rate = int(input('Enter sampling rate: '))
    for i in range(last_labeled_index,len(all_images)-3,sampling_rate):
        image_path1 = all_images[i]
        image_path2 = all_images[i+1]
        image_path3 = all_images[i+2]
        image_path4 = all_images[i+3]
        
        sampled_images.append(image_path1)
        sampled_images.append(image_path2)
        sampled_images.append(image_path3)
        sampled_images.append(image_path4)
    
elif already_labeled == 'no':
    file_raw = open('sampler_raw_list.txt','r')
    all_images = (str.split(file_raw.read()))
    last_labeled_index = 0
    sampling_rate = int(input('Enter sampling rate: '))
    for i in range(last_labeled_index,len(all_images)-3,sampling_rate):
        image_path1 = all_images[i]
        image_path2 = all_images[i+1]
        image_path3 = all_images[i+2]
        image_path4 = all_images[i+3]
        
        sampled_images.append(image_path1)
        sampled_images.append(image_path2)
        sampled_images.append(image_path3)
        sampled_images.append(image_path4)

with open(f'multiview_sampled_image_srate_{sampling_rate}.txt', 'w') as f:
    for item in sampled_images:
        f.write("%s\n" % item)