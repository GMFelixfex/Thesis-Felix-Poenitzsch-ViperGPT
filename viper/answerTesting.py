import os


# QA file path
qaFilePath = "testing/query and answer.txt"

# Log folder path
logFolderPath = "testing/logs"

ShowResults = True


# Load the Question and Answer text file
with open(qaFilePath) as f:
    lines = f.readlines()

    queries = []
    answers = []
    images = []    

    for line in lines:

        if line[0] == '#':
            # Split at | to get the image name and query
            query = line.split('|')[1]
            image = line.split('|')[0]

            # Add the query to the list and remove the # character
            queries.append(query.replace('\n', ''))

            # Add the image corresponding to the query to the list
            images.append(image[2:])
        else:
            # Add the answer to the list
            answers.append(line.replace('\n', '').lower())


# Possible Answers for each query are sperated by commas 
for i in range(len(answers)):
    answerlist = answers[i].split(',')
    for j in range(len(answerlist)):
        answerlist[j] = answerlist[j].lstrip().rstrip()
    answers[i] = answerlist


# Get All log files in the log folder
logFiles = os.listdir(logFolderPath)

allResults = []

aiNames = []


# for each log file get all results
for logFile in logFiles:
    aiNames.append(logFile[7:-4])
    with open(os.path.join(logFolderPath, logFile)) as f:
        lines = f.readlines()
        currentQuery = ""
        currentImage = ""
        preResults = []
        totalResults = []
        firstQuery = True
        firstImage = True
        changed = False
        currentResult = ""
        for i in range(len(lines)):
            if lines[i].startswith("Image:"):
                if currentImage != lines[i]:
                    # Start a new image
                    currentImage = lines[i]
                    if not firstImage:
                        changed = True
                    firstImage = False
                if currentQuery != lines[i+1]:
                    # Start a new query
                    currentQuery = lines[i+1]
                    if not firstQuery:
                        changed = True
                    firstQuery = False


            if changed:
                totalResults.append(preResults)
                preResults = []
            changed = False
            
            
            if lines[i].startswith("Result:"):
                currentResult = lines[i][7:].replace('\n', '').lower().lstrip().rstrip() #.replace(' ', '')) 
            if lines[i].startswith("Code:"):
                if "def execute_command" in lines[i]:
                    preResults.append(currentResult)    
                else:
                    preResults.append("Execute function missing, cannot execute code") 
        totalResults.append(preResults)
        allResults.append(totalResults)


totalpasses = 0

csvContent = []
if ShowResults:
    firstCsvLine = "Query;Image;Answer;TheBloke_CodeLlama-7B-GGUF;Passed;"
else:
    firstCsvLine = "Query;Image;Answer;TheBloke_CodeLlama-7B-GGUF;"
for ai in aiNames:
    firstCsvLine += ai + ";"
    if ShowResults:
        firstCsvLine +=  "Passed;"

csvContent.append(firstCsvLine)


# Loop through all queries and results
for query in range(len(queries)):
    if ShowResults:
        csvLine = queries[query] + ";" + images[query] + ";" + str(answers[query]) + ";[Execute function missing, cannot execute code];0;"
    else:
        csvLine = queries[query] + ";" + images[query] + ";" + str(answers[query]) + ";0;"
    for model in range(len(allResults)):
        listOfResults = allResults[model][query]
        listOfAnswers:list = answers[query]
        if ShowResults:
            csvLine += str(listOfResults) + ";"
        #print(queries[i])
        #print(listOfResults)
        #print(listOfAnswers)
        
        passed = False
        for result in listOfResults:
            for answer in listOfAnswers:
                answer = answer
                if answer in result:
                    passed = True

        if passed:
            csvLine += "1;"
            totalpasses += 1
        else:
            csvLine += "0;"




        # check if one of the results is in the list of answers
        #if any(x in listOfResults for x in listOfAnswers):
        #    csvLine += "1;"
        #    totalpasses += 1
        #else:
        #    csvLine += "0;"

    csvContent.append(csvLine)
        
print("Total Passed: " + str(totalpasses))


if ShowResults:
    with open("testing/results.csv", "w") as f:
        for line in csvContent:
            f.write(line + "\n")
else:
    with open("testing/resultless.csv", "w") as f:
        for line in csvContent:
            f.write(line + "\n")