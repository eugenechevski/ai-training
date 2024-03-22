using ImageBinarization

img = load("./julia-roberts.jpg")

binarized_img = Otsu.binarize(img)

using ImageView
view(binarized_img)


