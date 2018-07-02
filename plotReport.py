import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


#plt.xlabel('x - axis')
# naming the y axis
#plt.ylabel('y - axis')
# giving a title to my graph
# show a legend on the plot
#plt.legend()
# function to show the plot
#plt.savefig("graph.png")


researchDate=[]
TotalHouseholds=[]
TotalViewers=[]
TotalUniverse=[]
TotalExpandedUniverse=[]
TotalRecordsinUPtoDateProgramDB=[]
PanelMatchingRecordsPercentage=[]
CensusMatchingRecordsPercentage=[]
OriginalPanelStatements=[]
CalibratedPanelStatements=[]
TotalCensusTargetedReach=[]
TotalCalibratedReach=[]
TotalPanelCount=[]
TotalExpandedPanelCount=[]
TotalCensusTargetCount=[]
TotalCensusTargetedCount=[]
TotalCalibratedPanelCount=[]
with open('./report.txt', 'r') as f:
	for line in f:
                    
        	# Skip the comment line
        	if line.startswith('#'):
                	continue
                
                line = line.strip()
                columns = line.split('\t', -1)
		researchDate.append(columns[0])
		CalibratedPanelStatements.append(float(columns[1]))
		CensusMatchingRecordsPercentage.append(float(columns[2]))
		OriginalPanelStatements.append(float(columns[3]))
		PanelMatchingRecordsPercentage.append(float(columns[4]))
		TotalCalibratedPanelCount.append(float(columns[5]))
		TotalCalibratedReach.append(float(columns[6]))
		TotalCensusTargetCount.append(float(columns[7]))
		TotalCensusTargetedCount.append(float(columns[8]))
		TotalCensusTargetedReach.append(float(columns[9]))
		TotalExpandedPanelCount.append(float(columns[10]))
		TotalExpandedUniverse.append(float(columns[11]))
		TotalHouseholds.append(float(columns[12]))
		TotalPanelCount.append(float(columns[13]))
		TotalRecordsinUPtoDateProgramDB.append(float(columns[14]))
		TotalUniverse.append(float(columns[15]))
		TotalViewers.append(float(columns[16]))		

# plot for reach
plt.figure(figsize=(20,14))
plt.plot(researchDate, TotalCalibratedReach, label = "TotalCalibratedReach",color='blue')
plt.plot(researchDate, TotalCensusTargetedReach, label = "TotalCensusTargetedReach",color='red')
TotalCalibratedReachMean = sum( TotalCalibratedReach ) / len(TotalCalibratedReach)
TotalCalibratedReachMeanArr=[TotalCalibratedReachMean for i in researchDate]
plt.plot(researchDate, TotalCalibratedReachMeanArr, label = "TotalCalibratedReachMean",linestyle='dashed',color='blue')

plt.xticks(rotation=90)
plt.legend()
plt.savefig("Reach.png")
plt.clf()

# plot for minutes
plt.plot(researchDate, TotalCalibratedPanelCount, label = "TotalCalibratedPanelCount",color='blue')
plt.plot(researchDate, TotalCensusTargetedCount, label = "TotalCensusTargetedCount",color='red')
plt.plot(researchDate, TotalExpandedPanelCount, label = "TotalExpandedPanelCount",color='orange')
plt.plot(researchDate, TotalCensusTargetCount, label = "TotalCensusTargetCount",color='green')
TotalCalibratedPanelCountMean = sum( TotalCalibratedPanelCount ) / len(TotalCalibratedPanelCount)
TotalCalibratedPanelCountMeanArr=[TotalCalibratedPanelCountMean for i in researchDate]
plt.plot(researchDate, TotalCalibratedPanelCountMeanArr, label = "TotalCalibratedPanelCountMeanArr",linestyle='dashed',color='blue')

plt.plot(researchDate, TotalPanelCount, label = "TotalPanelCount",color='yellow')
#TotalPanelCountMean = sum( TotalPanelCount ) / len(TotalPanelCount)
#TotalPanelCountMeanArr=[TotalPanelCountMean for i in researchDate]
#plt.plot(researchDate, TotalPanelCountMeanArr, label = "TotalPanelCountMean",linestyle='dashed',color='yellow')

plt.xticks(rotation=90)
plt.legend()
plt.savefig("Minutes.png")
plt.clf()

# plot for statements
plt.plot(researchDate, CalibratedPanelStatements, label = "CalibratedPanelStatements",color='blue')
plt.plot(researchDate, OriginalPanelStatements, label = "OriginalPanelStatements",color='green')
plt.plot(researchDate, TotalRecordsinUPtoDateProgramDB, label = "TotalRecordsinUPtoDateProgramDB",color='orange')
CalibratedPanelStatementsMean = sum( CalibratedPanelStatements ) / len(CalibratedPanelStatements)
CalibratedPanelStatementsMeanArr=[CalibratedPanelStatementsMean for i in researchDate]
OriginalPanelStatementsMean = sum( OriginalPanelStatements ) / len(OriginalPanelStatements)
OriginalPanelStatementsMeanArr=[OriginalPanelStatementsMean for i in researchDate]
TotalRecordsinUPtoDateProgramDBMean = sum( TotalRecordsinUPtoDateProgramDB ) / len(TotalRecordsinUPtoDateProgramDB)
TotalRecordsinUPtoDateProgramDBMeanArr=[TotalRecordsinUPtoDateProgramDBMean for i in researchDate]
plt.plot(researchDate, CalibratedPanelStatementsMeanArr, label = "CalibratedPanelStatementsMean",linestyle='dashed',color='blue')
plt.plot(researchDate, OriginalPanelStatementsMeanArr, label = "OriginalPanelStatementsMean",linestyle='dashed',color='green')
plt.plot(researchDate, TotalRecordsinUPtoDateProgramDBMeanArr, label = "TotalRecordsinUPtoDateProgramDBMean",linestyle='dashed',color='orange')


plt.xticks(rotation=90)
plt.legend()
plt.savefig("Statements.png")
plt.clf()

# plot for matching percentage
plt.plot(researchDate, CensusMatchingRecordsPercentage, label = "CensusMatchingRecordsPercentage",color='blue')
CensusMatchingRecordsPercentageMean = sum( CensusMatchingRecordsPercentage ) / len(CensusMatchingRecordsPercentage)
CensusMatchingRecordsPercentageMeanArr=[CensusMatchingRecordsPercentageMean for i in researchDate]
plt.plot(researchDate, CensusMatchingRecordsPercentageMeanArr, label = "CensusMatchingRecordsPercentageMean",linestyle='dashed',color='blue')

plt.plot(researchDate, PanelMatchingRecordsPercentage, label = "PanelMatchingRecordsPercentage",color='green')
PanelMatchingRecordsPercentageMean = sum( PanelMatchingRecordsPercentage ) / len(PanelMatchingRecordsPercentage)
PanelMatchingRecordsPercentageMeanArr=[PanelMatchingRecordsPercentageMean for i in researchDate]
plt.plot(researchDate, PanelMatchingRecordsPercentageMeanArr, label = "PanelMatchingRecordsPercentageMean",linestyle='dashed',color='green')

plt.xticks(rotation=90)
plt.legend()
plt.savefig("MatchingPercentage.png")
plt.clf()


# plot for panel
plt.plot(researchDate, TotalHouseholds, label = "TotalHouseholds",color='blue')
TotalHouseholdsMean = sum( TotalHouseholds ) / len(TotalHouseholds)
TotalHouseholdsMeanArr=[TotalHouseholdsMean for i in researchDate]
plt.plot(researchDate, TotalHouseholdsMeanArr, label = "TotalHouseholdsMean",linestyle='dashed',color='blue')

plt.xticks(rotation=90)
plt.legend()
plt.savefig("PanelHouseHolds.png")
plt.clf()

# plot for panel viewers
plt.plot(researchDate, TotalViewers, label = "TotalViewers",color='orange')
TotalViewersMean = sum( TotalViewers ) / len(TotalViewers)
TotalViewersMeanArr=[TotalViewersMean for i in researchDate]
plt.plot(researchDate, TotalViewersMeanArr, label = "TotalViewersMean",linestyle='dashed',color='orange')


plt.xticks(rotation=90)
plt.legend()
plt.savefig("PanelViewers.png")
plt.clf()

# plot for universe
plt.plot(researchDate, TotalUniverse, label = "TotalUniverse",color='orange')
TotalUniverseMean = sum( TotalUniverse ) / len(TotalUniverse)
TotalUniverseMeanArr=[TotalUniverseMean for i in researchDate]
plt.plot(researchDate, TotalUniverseMeanArr, label = "TotalUniverseMean",linestyle='dashed',color='orange')
#plt.xticks(rotation=90)
#plt.legend()
#plt.savefig("Universe1.png")
#plt.clf()

plt.plot(researchDate, TotalExpandedUniverse, label = "TotalExpandedUniverse",color='red')
TotalExpandedUniverseMean = sum( TotalExpandedUniverse ) / len(TotalExpandedUniverse)
TotalExpandedUniverseMeanArr=[TotalExpandedUniverseMean for i in researchDate]
plt.plot(researchDate, TotalExpandedUniverseMeanArr, label = "TotalExpandedUniverseMean",linestyle='dashed',color='red')


plt.xticks(rotation=90)
plt.legend()
plt.savefig("Universe.png")
plt.clf()

