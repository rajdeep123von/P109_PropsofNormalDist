import random
import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import statistics
time =[]
count =[]

df = pd.read_csv("StudentsPerformance.csv")
math_list = df["math score"].to_list()
reading_list = df["reading score"].to_list()
writing_list = df["writing score"].to_list()

Mmean =  statistics.mean(math_list)
Mmedian = statistics.median(math_list)
Mmode = statistics.mode(math_list)
MstdDev = statistics.stdev(math_list)

MfirstStdDev_srt, MfirstStdDev_end = Mmean - MstdDev, Mmean+ MstdDev
MsecStdDev_srt, MsecStdDev_end = Mmean-(2*MstdDev), Mmean +(2*MstdDev)
MthirdStdDev_srt, MthirdStdDev_end = Mmean-(3*MstdDev), Mmean +(3*MstdDev)

MfirstStdDevL = [result for result in math_list
if(result>MfirstStdDev_srt and result<MfirstStdDev_end) ]

MsecondStdDevL = [result for result in math_list
if(result>MsecStdDev_srt and result<MsecStdDev_end) ]

MthirdtdDevL = [result for result in math_list
if(result>MthirdStdDev_srt and result<MthirdStdDev_end) ]

#wefwf
Rmean =  statistics.mean(reading_list)
Rmedian = statistics.median(reading_list)
Rmode = statistics.mode(reading_list)
RstdDev = statistics.stdev(reading_list)

RfirstStdDev_srt, RfirstStdDev_end = Rmean - RstdDev, Rmean+ RstdDev
RsecStdDev_srt, RsecStdDev_end = Rmean-(2*RstdDev), Rmean +(2*RstdDev)
RthirdStdDev_srt, RthirdStdDev_end = Rmean-(3*RstdDev), Rmean +(3*RstdDev)

RfirstStdDevL = [result for result in reading_list
if(result>RfirstStdDev_srt and result<RfirstStdDev_end) ]

RsecondStdDevL = [result for result in reading_list
if(result>RsecStdDev_srt and result<RsecStdDev_end) ]

RthirdtdDevL = [result for result in reading_list
if(result>RthirdStdDev_srt and result<RthirdStdDev_end) ]

Wmean =  statistics.mean(writing_list)
Wmedian = statistics.median(writing_list)
Wmode = statistics.mode(writing_list)
WstdDev = statistics.stdev(writing_list)

WfirstStdDev_srt, WfirstStdDev_end = Wmean - WstdDev, Wmean+ WstdDev
WsecStdDev_srt, WsecStdDev_end = Wmean-(2*WstdDev), Wmean +(2*WstdDev)
WthirdStdDev_srt, WthirdStdDev_end = Wmean-(3*WstdDev), Wmean +(3*WstdDev)

WfirstStdDevL = [result for result in writing_list
if(result>WfirstStdDev_srt and result<WfirstStdDev_end) ]

WsecondStdDevL = [result for result in writing_list
if(result>WsecStdDev_srt and result<WsecStdDev_end) ]

WthirdtdDevL = [result for result in writing_list
if(result>WthirdStdDev_srt and result<WthirdStdDev_end) ]

MpercentFirst = format(len(MfirstStdDevL)*100.0/len(math_list))
MpercentSecond = format(len(MsecondStdDevL)*100.0/len(math_list))
MpercentThird = format(len(MthirdtdDevL)*100.0/len(math_list))

RpercentFirst = format(len(RfirstStdDevL)*100.0/len(reading_list))
RpercentSecond = format(len(RsecondStdDevL)*100.0/len(reading_list))
RpercentThird = format(len(RthirdtdDevL)*100.0/len(reading_list))

WpercentFirst = format(len(WfirstStdDevL)*100.0/len(writing_list))
WpercentSecond = format(len(WsecondStdDevL)*100.0/len(writing_list))
WpercentThird = format(len(WthirdtdDevL)*100.0/len(writing_list))

print("Reading Score Mean=> "+str(Rmean)+"\nReading Score Median=> "+str(Rmedian)+"\nReading Score Mode=> "+str(Rmode)+"\nReading Score Standard Deviation=> "+str(RstdDev)+"\n")
print("Percentage of Reading Score data lies between the First Standard Deviation "+str(RpercentFirst)+"\nPercentage of Reading Score data lies between the Second Standard Deviation "+str(RpercentSecond)+"\nPercentage of Reading Score data lies between the Third Standard Deviation "+str(RpercentThird)+"\n\n")

print("Math Score Mean=> "+str(Mmean)+"\nMath Score Median=> "+str(Mmedian)+"\nMath Score Mode=> "+str(Mmode)+"\nMath Score Standard Deviation=> "+str(MstdDev)+"\n")
print("Percentage of Math Score data lies between the First Standard Deviation "+str(MpercentFirst)+"\nPercentage of Math Score data lies between the Second Standard Deviation "+str(MpercentSecond)+"\nPercentage of Math Score data lies between the Third Standard Deviation "+str(MpercentThird)+"\n")

print("Writing Score Mean=> "+str(Wmean)+"\nWriting Score Median=> "+str(Wmedian)+"\nWriting Score Mode=> "+str(Wmode)+"\nWriting Score Standard Deviation=> "+str(WstdDev)+"\n")
print("Percentage of Writing Score data lies between the First Standard Deviation "+str(WpercentFirst)+"\nPercentage of Writing Score data lies between the Second Standard Deviation "+str(WpercentSecond)+"\nPercentage of Writing Score data lies between the Third Standard Deviation "+str(WpercentThird)+"\n\n")

#plot.add_trace(go.scatter(x =[WfirstStdDev_srt], y =[]))

#plot = ff.create_distplot([time], ["Value Group"], show_hist=False
#plot.show()