from django.shortcuts import render
import getXJTUNews
import weather_spider
from getXJTUAttendanceInfo import getXJTUAttendanceData
#在这里填写自己的学号
studentNumber = ''

def index(request):
    newsContentDict = {}
    newsContentDict['zxxx'] = getXJTUNews.getXJTUEduNews('')
    return render(request,'index.html',{'newsContent':newsContentDict,'weather':weather_spider.getWeather('xian', '57036'),'indexactive':'class="active"'})

def perinfo(request):
    personalinfoContentDict={}
    personalinfoContentDict['attendance'] = getXJTUAttendanceData(studentNumber)
    return render(request,'perinfo.html',{'personalinfoContent':personalinfoContentDict,'perinfoactive':'class="active"'})

def edunews(request):
    typeList = ['xjgl','ksap','kcap','xjjl','jsap','zyfx','dcxm']
    #typeDict = {'xjgl':'学籍管理','ksap':'考试安排','kcap':'课程安排','xjjl':'校际交流','jsap':'竞赛安排','zyfx':'专业辅修','dcxm':'大创项目'}
    newsContentDict={}
    for type in typeList:
        newsContentDict[type] = getXJTUNews.getXJTUEduNews(type)
    return render(request,'edunews.html',{'newsContent':newsContentDict,'edunewsactive':'class="active"'})

def notice(request):
    newsContentDict={}
    newsContentDict['lib'] = getXJTUNews.getXJTULibNews()
    return render(request,'notice.html',{'newsContent':newsContentDict,'noticeactive':'class="active"'})

def activity(request):
    newsContentDict = {}
    newsContentDict['act'] = getXJTUNews.getXJTUCampAct()
    return render(request, 'activity.html', {'newsContent': newsContentDict,'activityactive':'class="active"'})
