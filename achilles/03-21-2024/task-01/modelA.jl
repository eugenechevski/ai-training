using ImageBinarization

# Load your image
img = readimage("./julia-roberts.jpg")

# Choose your preferred algorithm
binarized_image = Otsu()(img)  # Example using Otsu's method

# Display or save the result
display(binarized_image)
save("binarized_output.jpg", binarized_image)