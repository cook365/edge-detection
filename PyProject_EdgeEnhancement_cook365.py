import numpy as np
import matplotlib.pyplot as plt
import GreyScale as g 




def edge_enhancement(image, filt):
    def combo(image, filt):
        image = g.grey(image)
        image_row, image_col, a = image.shape
        filt_row, filt_col = filt.shape
        output = np.zeros((image.shape[0], image.shape[1], image.shape[2]))

        for row in range(image_row):
            for col in range(image_col):
                output[row, col] = np.sum(filt * image)#[row:row + filt_row, col:col + filt_col])
                # if average:
                #     output[row, col] /= filt.shape[0] * filt.shape[1]
    
        
    x_image = combo(image, filt)
        
    y_image = combo(image, np.flip(filt.T, axis = 0))
    
    
    
    mag = np.sqrt(np.square(x_image) + np.square(y_image))
    mag *= 255/mag.max()
    
    plt.show()
    return mag
        
        # image = np.array(image)
        # image = image/255
        
image = plt.imread('Purdue_Arch.png')
filt = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float)

print(f'{image.shape}')
plt.show()

edge_enhancement(image, filt)