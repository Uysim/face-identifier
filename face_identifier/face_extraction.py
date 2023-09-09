def extract_image_box(img, box):
    x1, y1, width, height = box
    y2 = y1 + height
    x2 = x1 + width

    if x1 < 0:
        x1 = 0
    
    if y1 < 0:
        y1 = 0
    
    if x2 > img.shape[1]:
        x2 = img.shape[1]

    if y2 > img.shape[0]:
        y2 = img.shape[0]
    
    return img[y1:y2, x1:x2]