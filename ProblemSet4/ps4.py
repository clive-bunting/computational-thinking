# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        

def performTrial(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, delayBeforeDrugAdded):
    timeSteps = [0 for x in range(delayBeforeDrugAdded + 150)]
    drugResistantParticles = [0 for x in range(delayBeforeDrugAdded + 150)]
    
    viruses = []
    for i in range(numViruses):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        viruses.append(virus)
    patient = TreatedPatient(viruses, maxPop)
    
    for t in range(delayBeforeDrugAdded):
        timeSteps[t] += patient.update()
        drugResistantParticles[t] += patient.getResistPop(['guttagonol'])
    
    patient.addPrescription('guttagonol')
    
    for t in range(delayBeforeDrugAdded, delayBeforeDrugAdded + 150):
        timeSteps[t] += patient.update()
        drugResistantParticles[t] += patient.getResistPop(['guttagonol'])
    return timeSteps, drugResistantParticles

def plotFigure(timeSteps, drugResistantParticles, figureNumber):
    pylab.figure(figureNumber)
    pylab.plot(timeSteps, label='Ave total virus population')
    pylab.plot(drugResistantParticles, label='Ave drug resistant particles')
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('time steps')
    pylab.ylabel('# viruses')
    pylab.legend()   
    
def plotHist(finalVirusPop, figureNumber, delay):
    pylab.figure(figureNumber)
    pylab.hist(finalVirusPop, 20)
    pylab.title('Histogram of Final Virus Populations for Delay of ' + str(delay))
    pylab.xlabel('Final Virus Population')
    pylab.ylabel('Number of trials')
    pylab.legend()   

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    drugDelays = [150]
    maxPop = [1000]
    numViruses = [100]
    maxBirthProb = [0.1]
    clearProb = [0.05]
    resistances = {'guttagonol': False}
    mutProb = 0.005
    
    #drugDelays = [300, 150, 75, 0]
    #numViruses = [100, 250, 500, 750]
    maxPop = [1000, 2000, 4000, 8000]
    #maxBirthProb = [0.1, 0.2, 0.4, 0.8]
    #clearProb = [0.05, 0.08, 0.1, 0.2]
    
    plotCount = 0
    for i in range(len(drugDelays)):
        for j in range(len(numViruses)):
            for k in range(len(maxPop)):
                for l in range(len(maxBirthProb)):
                    for m in range(len(clearProb)):
                        finalVirusPop = []
                        
                        print 'Running trials for delay=',drugDelays[i],' numViruses=',numViruses[j],' maxPop=',maxPop[k],' maxBirthProb=',maxBirthProb[l],' clearProb=',clearProb[m]

                        for trial in range(numTrials):
                            timeSteps, drugResistantParticles = performTrial(numViruses[j], maxPop[k], maxBirthProb[l], clearProb[m], resistances, mutProb, drugDelays[i])
                            finalVirusPop.append(timeSteps[len(timeSteps)-1])
                            
                        #timeSteps = [(x / float(numTrials)) for x in timeSteps]
                        #drugResistantParticles = [(x / float(numTrials)) for x in drugResistantParticles]
                        #plotFigure(timeSteps, drugResistantParticles, i)
                        plotCount += 1
                        plotHist(finalVirusPop, plotCount, drugDelays[i])
        
    pylab.show()   

simulationDelayedTreatment(200)


def performSecondTrial(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, delayBeforeDrugAdded):
    timeSteps = [0 for x in range(delayBeforeDrugAdded + 300)]
    drugResistantParticles = [0 for x in range(delayBeforeDrugAdded + 300)]
    
    viruses = []
    for i in range(numViruses):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        viruses.append(virus)
    patient = TreatedPatient(viruses, maxPop)
    
    for t in range(150):
        timeSteps[t] += patient.update()
        drugResistantParticles[t] += patient.getResistPop(['guttagonol'])
    
    patient.addPrescription('guttagonol')

    for t in range(150, 150 + delayBeforeDrugAdded):
        timeSteps[t] += patient.update()
        drugResistantParticles[t] += patient.getResistPop(['guttagonol'])   
    
    patient.addPrescription('grimpex')
            
    for t in range(150 + delayBeforeDrugAdded, 150 + delayBeforeDrugAdded + 150):
        timeSteps[t] += patient.update()
        drugResistantParticles[t] += patient.getResistPop(['guttagonol'])
    return timeSteps, drugResistantParticles

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    drugDelays = [150]
    maxPop = [1000]
    numViruses = [100]
    maxBirthProb = [0.1]
    clearProb = [0.05]
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    
    drugDelays = [300, 150, 75, 0]
    #numViruses = [100, 250, 500, 750]
    #maxPop = [1000, 2000, 4000, 8000]
    #maxBirthProb = [0.1, 0.2, 0.4, 0.8]
    #clearProb = [0.05, 0.08, 0.1, 0.2]
    
    plotCount = 0
    for i in range(len(drugDelays)):
        for j in range(len(numViruses)):
            for k in range(len(maxPop)):
                for l in range(len(maxBirthProb)):
                    for m in range(len(clearProb)):
                        finalVirusPop = []
                        
                        print 'Running trials for delay=',drugDelays[i],' numViruses=',numViruses[j],' maxPop=',maxPop[k],' maxBirthProb=',maxBirthProb[l],' clearProb=',clearProb[m]

                        for trial in range(numTrials):
                            timeSteps, drugResistantParticles = performSecondTrial(numViruses[j], maxPop[k], maxBirthProb[l], clearProb[m], resistances, mutProb, drugDelays[i])
                            finalVirusPop.append(timeSteps[len(timeSteps)-1])
                            
                        #timeSteps = [(x / float(numTrials)) for x in timeSteps]
                        #drugResistantParticles = [(x / float(numTrials)) for x in drugResistantParticles]
                        #plotFigure(timeSteps, drugResistantParticles, i)
                        plotCount += 1
                        plotHist(finalVirusPop, plotCount, drugDelays[i])
        
    pylab.show()   

#simulationTwoDrugsDelayedTreatment(500)