import random
import pylab

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    finalScores = []

    for trial in range(numTrials):
        midTerm1 = random.randint(50, 80)
        midTerm2 = random.randint(60, 90)
        finalExam = random.randint(55, 95)
        finalScore = (0.25 * midTerm1) + (0.25 * midTerm2) + (0.5 * finalExam)

        finalScores.append(finalScore)

    return finalScores

def plotQuizzes():
    numTrials = 10000
    scores = generateScores(numTrials)
    pylab.hist(scores, bins=7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()

plotQuizzes()
