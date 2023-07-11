import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from skimage.measure import label, regionprops

def droplet_detection(sender_image, receiver_image):
    """
    Identify the locations of the sender and receiver droplets.
    """
    # Create Binary for better signal to noise
    binary = sender_image > (sender_image.mean() + sender_image.std())

    # use labeling function to identify connected blobs
    label_im = label(binary)
    blob_lists = regionprops(label_im)

    # Remove small blobs
    senders = [i for i in blob_lists if i.area > 500]
    
    # Mask to document all sender locations
    mask = np.zeros_like(img_array)
    for i in senders:
        minr, minc, maxr, maxc = i.bbox
        mask[minr:maxr, minc:maxc] = 1
        
    # Create Binary for better signal to noise
    binary = img2 > (img2.mean() + img2.std())
    
    # use labeling function to identify connected blobs
    label_im = label(binary)
    blob_lists = regionprops(label_im)

    # Remove small blobs
    receivers = [i for i in blob_lists if i.area > 500]

    # Extract receiver droplets
    true_receivers = []
    for i in receivers:
        minr, minc, maxr, maxc = i.bbox
        if mask[int((minr+maxr)/2), int((minc+maxc)/2)] == 0:
            true_receivers.append(i)
            
    return senders, true_receivers