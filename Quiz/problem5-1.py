import random

def sampleQuizzes():
    numTrials = 10000
    numberOfScoresInRange = 0

    for trial in range(numTrials):
        midTerm1 = random.randint(50, 80)
        midTerm2 = random.randint(60, 90)
        finalExam = random.randint(55, 95)
        finalScore = (0.25 * midTerm1) + (0.25 * midTerm2) + (0.5 * finalExam)

        if finalScore >= 70 and finalScore <= 75:
        	numberOfScoresInRange += 1

    return numberOfScoresInRange / float(numTrials)

print sampleQuizzes()
