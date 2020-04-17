already_labeled = input('Have you already labeled some images in this section(yes/no) :')

if already_labeled == 'yes':
    file_annotate = open('sampler_annotate_list.txt','r')
    file_raw = open('sampler_raw_list.txt','r')

    annotate_last = (str.split(file_annotate.read()))[-1][:-3]+'jpg'
    all_images = (str.split(file_raw.read()))

    last_labeled_index = all_images.index(annotate_last)
    sampling_rate = input('Enter sampling rate: ')
    sampled_images = all_images[last_labeled_index::sampling_rate]
    
elif already_labeled == 'no':
    file_raw = open('sampler_raw_list.txt','r')
    all_images = (str.split(file_raw.read()))
    last_labeled_index = 0
    sampling_rate = input('Enter sampling rate: ')
    sampled_images = all_images[last_labeled_index::sampling_rate]

with open(f'sampled_image_srate_{sampling_rate}.txt', 'w') as f:
    for item in sampled_images:
        f.write("%s\n" % item)