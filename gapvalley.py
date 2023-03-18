# import numpy for np array functionality and opencv for image processing
# math to get e and pi constants
import numpy as np
import math
import cv2

# gets the estimated y value for a slice of the image, the image, and the dimensions of the slice (x, y, w, h)
def calculate_valley(estimated_y, img, window):
    # calculate row intensity sums and store them in a depths list
    depths = []
    for i in range(img.shape[0]): # for each row calculate the sum of all the grayscale values and append to the list
        intensity_sum = 0
        # iterate the row over the width of the window
        for j in range(window[0], window[0] + window[2]):
            intensity_sum += img[i, j]
        depths.append(intensity_sum)
    
    # list of probabilities that a valley or given y position is the gap valley
    probs = []
    # loop through depths and calculate the probabilities Pvi(Di, yi)
    for i in range(len(depths)):
        # calculate Pvi(Di)
        p_d = (1 - depths[i] / max(depths))
        # calculate Pvi(yi) sigma = 0.05
        p_y = (math.e **(-((i - estimated_y) ** 2) * (0.05 ** 2))) / (math.sqrt(2 * math.pi))
        # append Pvi(Di, yi), which is Pvi(Di)*Pvi(yi), or p_d * p_y
        probs.append(p_d * p_y)

    # find the gap valley by deciding which is valley has the highest probability
    valley = probs.index(max(probs))
    valley_p = max(probs)
    return (valley, valley_p)
# end calculate_valley

# main function
def main():
    # load the image and convert to grayscale if needed
    # I increased the contrast of the image manually before writing the program using GIMP
    img = cv2.imread("teeth_sample.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # define the slices for the sliding window, define the estimated y value for the slice, and calculate the found y value of the valley, output by printing.
    window1 = (0, 0, 140, 472)
    estimated_y1 = 204
    valley1 = calculate_valley(estimated_y1, img, window1)
    print("The y value of the gap for slice 1 is {} with probability {}".format(valley1[0], valley1[1]))
    window2 = (141, 0, 124, 472)
    estimated_y2 = 220
    valley2 = calculate_valley(estimated_y2, img, window2)
    print("The y value of the gap for slice 2 is {} with probability {}".format(valley2[0], valley2[1]))
    window3 = (265, 0, 105, 472)
    estimated_y3 = 206
    valley3 = calculate_valley(estimated_y3, img, window3)
    print("The y value of the gap for slice 3 is {} with probability {}".format(valley3[0], valley3[1]))
    window4 = (370, 0, 34, 472)
    estimated_y4 = 192
    valley4 = calculate_valley(estimated_y4, img, window4)
    print("The y value of the gap for slice 4 is {} with probability {}".format(valley4[0], valley4[1]))
    window5 = (405, 0, 107, 472)
    estimated_y5 = 176
    valley5 = calculate_valley(estimated_y5, img, window5)
    print("The y value of the gap for slice 5 is {} with probability {}".format(valley5[0], valley5[1]))
# end main

# call the main function
if __name__ == "__main__":
    main()