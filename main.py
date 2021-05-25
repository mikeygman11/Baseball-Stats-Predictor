#Copyright 2021 Michael Galanaugh
#An algorithm that predicts results of Major League Baseball games

#home team winning will be classified as a 1 and away team winning is classified as 0


from numpy.core.fromnumeric import sort
import pandas as pd

sortedBattingData=pd.read_excel('2021_hittingstats.ods', engine='odf', index_col = "Tm")
battingData=pd.read_excel('2021_hittingstats.ods', engine='odf')
sortedPitchingData=pd.read_excel('2021_pitchingstats.ods', engine='odf', index_col = "Tm")
pitchingData=pd.read_excel('2021_pitchingstats.ods', engine='odf')

def main():
    organize()
    
def organize():
    battingDict = {}
    pitchingDict = {}
    for teams in battingData["Tm"]:
        battingDict[teams] = None
    for item in battingDict: #putting hitting data for each team into a dictionary with key being team names and values being dictionaries of statistical categories
        battingDict[item] = sortedBattingData.loc[item]
    for teams in pitchingData["Tm"]:
        pitchingDict[teams] = None
    for item in pitchingDict: #putting pitching data for each team into a dictionary with key being team names and values being dictionaries of statistical categories
        pitchingDict[item] = sortedPitchingData.loc[item]
    print('\n\n\n\n')
    compute_proj_winperc(battingDict, pitchingDict)

def compute_proj_winperc(batting, pitching):
    winDict = {} #initializing a dictionary to hold projected win percentages of each team
    for teams in battingData["Tm"]:
        runs_scored = batting[teams]["R"] 
        runs_allowed = pitching[teams]["R"] 
        projectedWinPerc = (float) (runs_scored**2/(runs_scored**2 + runs_allowed**2))
        winDict[teams] = projectedWinPerc #creating dictionary of teams and projected win percentage
    print(winDict)




main()
