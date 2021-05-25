#Copyright 2021 Michael Galanaugh
#An algorithm that generates an updated ELO for each MLB team based on performance


sortedBattingData=pd.read_excel('2021_hittingstats.ods', engine='odf', index_col = "Tm")
battingData=pd.read_excel('2021_hittingstats.ods', engine='odf')
sortedPitchingData=pd.read_excel('2021_pitchingstats.ods', engine='odf', index_col = "Tm")
pitchingData=pd.read_excel('2021_pitchingstats.ods', engine='odf')

from main import *



