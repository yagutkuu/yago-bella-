def load_image(filename):
    infile = open(filename, "r")
    instr = infile.read().split('\n')
    image["type"] = instr.pop(0)
    if image["comment"]:
        image["comment"] = instr.pop(0)
    image["size"] = list(map(int, instr.pop(0).split(' ')))
    for row in instr:
        image["pixels"].append(list(map(int, row.split(' '))))
    return image


def generate_square(size, colour=True):
    image = {}
    image["type"] = "P1"
    image["size"] = [size, size]
    image["comment"] = ''
    image["pixels"] = []
    for row in range(size):
        line = []
        for col in range(size):
            line.append(1)
        image["pixels"].append(line)
    return image


def generate_diagonal(size):
    


def mirror_y(image):
    for col in range(size)
       if image["pixels"][col] == 0
          image["pixels"][col] == 1
       else:
          image["pixels"][col] == 0 
    return image 


def mirror_x(image):
    pass


def save_image(filename, image):
    """
        Saves an image to a filename.
    """

    outfile = open(filename, "w+")  # Open a filename in a write mode
    outfile.write(image["type"] + "\n")
    if image["comment"]:
        outfile.write("# " + image["comment"] + "\n")  # Add comment if there is any
    outfile.write(' '.join(list(map(str, image["size"]))) + '\n')   # Change ints to strs and join them with spaces
    for row in image["pixels"]:
        outfile.write(' '.join(list(map(str, row))) + '\n') # Change ints to strs and join them with spaces

image = generate_square(3, True)
# image = load_image("test.pgm")
save_image("black.pgm", image)
