'''
Image Embedding
J.Griffin Harrington
November 4, 2020
'''

''' 3rd Party Library '''
from PIL import Image               # pip install pillow

# Pixel tuple index
RED   = 0
GREEN = 1
BLUE  = 2

''' Obtain the Basic image information '''
try:
    img       = Image.open('monalisa.bmp')   
    height, width = img.size    
    
    pix = img.load()  
    
    # Pixel to Modify
    r = 0  # Row
    c = 0  # Col
    
    # Read the Pixel
    
    for x in range(0,5):
        pixel = pix[x, c]
        redPx = pixel[RED]      # Extract the RGB
        grnPx = pixel[GREEN]
        bluPx = pixel[BLUE]
            
        # Print the Current Value of the Pixel
        print("\nOrginal Pixel: " ,x)
        print("RED: ", '{:08b}'.format(redPx))
        print("GRN: ", '{:08b}'.format(grnPx))
        print("BLU: ", '{:08b}'.format(bluPx))
        if(x == 1):
            # Alter the Pixel RGB
            redPx = redPx | 0
            grnPx = grnPx | 0
            bluPx = bluPx | 1
        if(x == 2):
            # Alter the Pixel RGB
            redPx = redPx | 0
            grnPx = grnPx | 1
            bluPx = bluPx | 1
        if(x == 3):
            # Alter the Pixel RGB
            redPx = redPx | 1
            grnPx = grnPx | 1
            bluPx = bluPx | 0
        if(x == 4):
            # Alter the Pixel RGB
            redPx = redPx | 1
            grnPx = grnPx | 1
            bluPx = bluPx | 1            
        # Print the New Value of the Pixel
        print("\nAlterned Pixel")
        print("RED: ", '{:08b}'.format(redPx))
        print("GRN: ", '{:08b}'.format(grnPx))
        print("BLU: ", '{:08b}'.format(bluPx))
            
        # Update the pixel
        pixel = (redPx, grnPx, bluPx)
        
        # Save the changed Pixel in the pixel proper
        pix[r,c] = pixel
        
    # Save this as a new image
    img.save('monaLisaSteg.bmp')
    
    print("\nSingle Pixel Steganography Done")

except Exception as err:
    print("Steg Failed: ", str(err))
    
    
        
    
