from main_simple_lib import *
import os

imageFolderPath = "C:/Users/Felix/viper/testing/images"
queryTextPath = "C:/Users/Felix/viper/testing/query.txt"
logFolderPath  = "C:/Users/Felix/viper/testing/logs"

useImageDisplay = False

def log_query(query, code, imagePath, result):
    # Get log file count
    count = len([name for name in os.listdir(logFolderPath) if os.path.isfile(os.path.join(logFolderPath, name))])
    # Create log file
    with open(f'{logFolderPath}/log_{count}.txt', 'w') as f:
        f.write('\n')
        f.write('------------------------------\n')
        f.write('\n')
        f.write(f'Image: {imagePath}\n')
        f.write(f'Query: {query}\n')
        f.write(f'Code: {code}\n')
        f.write(f'Result: {result}\n')
        f.write('\n')
        f.write('------------------------------\n')
        f.write('\n')

    print(f'Logged query {count} to {logFolderPath}/log_{count}.txt')
    return

print("Starting batch processing...")

# Initialize all queries and images
queries = []
images = []
with open(queryTextPath, 'r') as f:
    for line in f:
        # Split at | to get the image name and query
        query = line.split('|')[1]
        image = line.split('|')[0]

        # Add the query to the list
        queries.append(query)

        # Add the image corresponding to the queryto the list
        images.append(imageFolderPath + "/" + image)


# Get all codes
codes = []
syntaxes = []
for query in queries:
    code_and_syntax = get_code(query, "lm_studio")

    code = code_and_syntax[0]
    syntax = code_and_syntax[1]

    # Add the code to the list
    codes.append(code)

    # Add the syntax to the list
    syntaxes.append(syntax)


# Load all images
loaded_images = []
for image in images:
    loaded_images.append(load_image(image))

# print the codes
for code in codes:
    print(code)

# print the syntaxes
for syntax in syntaxes:
    print(syntax)



# Check if image display is activated
if useImageDisplay:

    # Display all images
    for image in loaded_images:
        show_single_image(image) 


# Log all queries + codes + images
#for query, code, image, result in zip(queries, codes, images, results):
#    log_query(query, code, image, result)




#m = load_image('https://viper.cs.columbia.edu/static/images/kids_muffins.jpg')
#query = 'How many muffins can each kid have for it to be fair?'

#show_single_image(im)
#code = get_code(query, "lm_studio")