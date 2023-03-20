#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Version  : 1.0.0
# @Author   : HYX
# @Datetime : 2023/3/14 21:00
# @Project  : LimbusCompany
import cv2
import aircv
from PIL import ImageGrab
import numpy as np
import os.path
import pyautogui as pi
import time 

#图片定义
path =  "D:\\WorkSapce\\Script\\"
PicMapSign = "MapSign.png"
PicWinRater = "WinRate.png"
PicStartBattle = "StartBattle.png"
PicStartFight = "StartFight.png"
PicReceive = "Receive.png"

PicDrive = "Drive.png"
PicEnterMirror = "EnterMirror.png"
PicEnterMirror2 = "EnterMirror2.png"
PicEnterMirror3 = "EnterMirror3.png"

PicNormalBattle11 = "NormalBattle11.png"
PicNormalBattle12 = "NormalBattle12.png"
PicNormalBattle13 = "NormalBattle13.png"
PicNormalBattle22 = "NormalBattle22.png"
PicNormalBattle33 = "NormalBattle33.png"
PicAbnormalBattle2 = "AbnormalBattle2.png"
PicAbnormalBattle3 = "AbnormalBattle3.png"
PicBossBattle = "BossBattle.png"
PicBossBattle2 = "BossBattle2.png"
PicBossBattle3 = "BossBattle3.png"
PicEventBattle = "EventBattle.png"
PicEventBattle3 = "EventBattle3.png"
PicEndPoint = "EndPoint.png"
PicEndPoint2 = "EndPoint2.png"
PicEndPoint3 = "EndPoint3.png"
PicEndPoint4 = "EndPoint4.png"
PicEnterBattle = "EnterBattle.png"


PicEventChoice = "EventChoice.png"
PicEventSkip = "EventSkip.png"
PicEventRandomSelect = "EventRandomSelect.png"
PicEventContinue = "EventContinue.png"
PicEventProceed = "EventProceed.png"
PicEventAdvantage = "EventAdvantage.png"
PicEventCommence = "EventCommence.png"
PicEventResult = "EventResult.png"
PicEventLevelUp = "EventLevelUp.png"
PicEventSelectSinnner = "EventSelectSinnner.png"

PicEshake = "Eshake.png"
PicEveryHigh = "EveryHigh.png"
PicEBossApple = "EBossApple.png"

PicAnnouncer = "Announcer.png"
PicNo1 = "No1.png"
PicNo2 = "No2.png"
PicNo3 = "No3.png"
PicNo4 = "No4.png"
PicNo5 = "No5.png"
PicNo6 = "No6.png"
PicNo7 = "No7.png"
PicNo8 = "No8.png"
PicNo9 = "No9.png"
PicNo10 = "No10.png"
PicNo11 = "No11.png"
PicNo12 = "No12.png"
PicNo1Sign = "No1Sign.png"
PicNo2Sign = "No2Sign.png"
PicNo3Sign = "No3Sign.png"
PicNo4Sign = "No4Sign.png"
PicNo5Sign = "No5Sign.png"
PicNo6Sign = "No6Sign.png"
PicNo7Sign = "No7Sign.png"
PicNo8Sign = "No8Sign.png"
PicNo9Sign = "No9Sign.png"
PicNo10Sign = "No10Sign.png"
PicNo11Sign = "No11Sign.png"
PicNo12Sign = "No12Sign.png"

PicNo2SignNew = "No2SignNew.png"
PicNo5SignNew = "No5SignNew.png"
PicNo9SignNew = "No9SignNew.png"
PicNo10SignNew = "No10SignNew.png"
PicNo11SignNew = "No11ignNew.png"
PicNo12SignNew = "No12ignNew.png"


PicNo1_1 = "No1_1.png"
PicNo2_1 = "No2_1.png"
PicNo3_1 = "No3_1.png"
PicNo4_1 = "No4_1.png"
PicNo5_1 = "No5_1.png"
PicNo6_1 = "No6_1.png"
PicNo7_1 = "No7_1.png"
PicNo8_1 = "No8_1.png"
PicNo9_1 = "No9_1.png"
PicNo10_1 = "No10_1.png"
PicNo11_1 = "No11_1.png"
PicNo12_1 = "No12_1.png"
PicNo1_1Ready = "No1_1Ready.png"
PicNo2_1Ready = "No2_1Ready.png"
PicNo4_1Ready = "No4_1Ready.png"
PicNo5_1Ready = "No5_1Ready.png"
PicNo6_1Ready = "No6_1Ready.png"
PicNo9_1Ready = "No9_1Ready.png"
PicNo10_1Ready = "No10_1Ready.png"
PicNo11_1Ready = "No11_1Ready.png"
PicNo12_1Ready = "No12_1Ready.png"
PicSelectSinner = "SelectSinner.png"
PicAleph = "Aleph.png"
PicSelectNewSinner = "SelectNewSinner.png"

Piclv10 = "lv10.png"
Piclv15 = "lv15.png"
Piclv20 = "lv20.png"
Piclv25 = "lv25.png"

PicChoseLvUp = "ChoseLvUp.png"
PicConfirm = "Confirm.png"
PicConfirmW = "ConfirmW.png"
PicConfirmW2 = "ConfirmW2.png"
PicToEgo = "ToEgo.png"
PicSelected = "Selected.png"
PicSelectGift = "SelectGift.png"
PicRandomGift = "RandomGift.png"

def Path(pic):
    return path + pic

def pil2np(pil_img):
    '''
    PIL.Image.Image===>numpy.ndarray
    :param pil_img: pil模块的图片数据  PIL.Image.Image
    :return: numpy 支持的narray 数据结构   numpy.ndarray
    '''
    return np.array(pil_img)  # numpy.ndarray

def FindPic(small_picture_path, similarity=0.85):
    '''
    区域找图
    :param small_picture_path:目标小图的路径
    :param similarity:相似度,0.95
    :return: (0,100) |(-1,-1)
    '''
    if not os.path.exists(small_picture_path):
        return None
    bag = ImageGrab.grab()
    #bag.show()
    small = cv2.imread(small_picture_path)
    res = aircv.find_template(pil2np(bag), small, similarity)
    return res["result"] if res else (-1, -1)

def FindPicList(small_picture_path, similarity=0.85):
    '''
    区域找图
    :param small_picture_path:目标小图的路径
    :param similarity:相似度,0.95
    :return: (0,100) |(-1,-1)
    '''
    if not os.path.exists(small_picture_path):
        return None
    bag = ImageGrab.grab()
    #bag.show()
    small = cv2.imread(small_picture_path)
    res = aircv.find_all_template(pil2np(bag), small, similarity)
    return res

def Wait(x):
    print("Wait loading for " +str(x) + " seconds")
    time.sleep(10)
    
def ClickPic(pic_path):
    r = FindPic(pic_path)
    pi.moveTo(r,duration=0.25)
    time.sleep(.7)
    pi.click()
    

def ClickXY(r):
    pi.moveTo(r,duration=0.25)
    time.sleep(.7)
    pi.click()
    
def StartBattle():
    if FindPic(Path(PicMapSign)) != (-1,-1):
        return
    print("Start Battle")
    retryCount = 1
    battleCount = 1
    while retryCount <  50:
        if FindPic(Path(PicChoseLvUp)) != (-1,-1):
            break
        if FindPic(Path(PicSelectGift)) != (-1,-1):
            break
        if FindPic(Path(PicEventSkip)) != (-1,-1):
            print("Boss battle event choice")
            while FindPic(Path(PicEventContinue)) == (-1,-1):
                ClickPic(Path(PicEventSkip))
                if FindPic(Path(PicEBossApple)) != (-1,-1):
                    print("Boss Apple Queen")
                    while FindPic(Path(PicEventResult)) == (-1,-1):
                        print("Charge Progress")
                        ClickPic(Path(PicEveryHigh))
                        ClickPic(Path(PicEventCommence))
                        if FindPic(Path(PicEventContinue)) != (-1,-1):
                            print("Charge Stop")
                            break
            ClickPic(Path(PicEventContinue))
                    
          
        print("Battle Icon check "+ str(retryCount) + " times")
        if FindPic(Path(PicWinRater)) == (-1,-1):
            retryCount = retryCount + 1
        else:
            print("Do Battle in Turn " + str(battleCount))
            ClickPic(Path(PicWinRater))
            ClickPic(Path(PicStartFight))
            battleCount = battleCount + 1
        time.sleep(3)
    print("Battle Finshed")
        
def SeachrFor(pic):
    print("Search for " + str(pic))
    r = FindPicList(Path(pic))
    for i in r:
        ClickXY(i["result"])
        print("Find "+str(pic) + " in " + str(i["result"])+ " Try to get the Entrance")
        time.sleep(1)
        if FindPic(Path(PicEnterBattle)) != (-1,-1):
            print("Get Battle Entrace Ready to Start")
            ClickPic(Path(PicEnterBattle))
            return True
    return False

def Searching():
    print("Start seachring")
    while True:
        if SeachrFor(PicEventLevelUp):
            print("Level up event")
            while FindPic(Path(PicEventChoice)) == (-1,-1):
                ClickPic(Path(PicEventSkip))
            while FindPic(Path(PicEventResult)) == (-1,-1):
                ClickPic(Path(PicEventRandomSelect))
                ClickPic(Path(PicEventSkip))
            while FindPic(Path(PicEventContinue)) == (-1,-1):
                ClickPic(Path(PicEventContinue))
            ClickPic(Path(PicEventContinue))    
            for i in range(3):
                print("Try to Level up for " + str(i)+ " times")
                if FindPic(Path(PicChoseLvUp)) != (-1,-1):
                    print("Select the sinner to Level Up")
                    if FindPic(Path(Piclv10)) != (-1,-1):
                        ClickPic(Path(Piclv10))
                    if FindPic(Path(Piclv15)) != (-1,-1):
                        ClickPic(Path(Piclv15))
                    if FindPic(Path(Piclv20)) != (-1,-1):
                        ClickPic(Path(Piclv20))
                    if FindPic(Path(Piclv25)) != (-1,-1):
                        ClickPic(Path(Piclv25))
                    ClickPic(Path(PicConfirm))
                    ClickPic(Path(PicToEgo))
                    ClickPic(Path(PicSelected))
                    ClickPic(Path(PicConfirm))
                    ClickPic(Path(PicConfirm))
            return False
            
        if SeachrFor(PicNormalBattle11):
            return False
        if SeachrFor(PicNormalBattle22):
            return False
        if SeachrFor(PicNormalBattle33):
            return False
        if SeachrFor(PicAbnormalBattle2):
            return False
        if SeachrFor(PicAbnormalBattle3):
            return False
        if SeachrFor(PicBossBattle):
            return False
        if SeachrFor(PicBossBattle2):
            return False
        if SeachrFor(PicBossBattle3):
            return False   
        if SeachrFor(PicEndPoint):
            print("Finished the floor")
            return True
        if SeachrFor(PicEndPoint2):
            print("Finished the floor")
            return True
        if SeachrFor(PicEndPoint3):
            print("Finished the floor")
            return True
        if SeachrFor(PicEndPoint4):
            print("Finished the floor")
            return True
        if SeachrFor(PicEventSelectSinnner):
            while FindPic(Path(PicEventChoice)) == (-1,-1):
                ClickPic(Path(PicEventSkip))
            while FindPic(Path(PicEventResult)) == (-1,-1):
                ClickPic(Path(PicEventRandomSelect))
                ClickPic(Path(PicEventSkip))
            while FindPic(Path(PicEventContinue)) == (-1,-1):
                ClickPic(Path(PicEventContinue))
            ClickPic(Path(PicEventContinue))    
            CheckNew()
            return False
        if SeachrFor(PicEventBattle):
            EventChoice()
            return False
        if SeachrFor(PicEventBattle3):
            EventChoice()
            return False
       
        pi.scroll(-10) # 向下滚动10格
        pi.scroll(-10) # 向下滚动10格

def EventChoice():
    print("Start Event Choice ")
    while FindPic(Path(PicEventChoice)) == (-1,-1):
        ClickPic(Path(PicEventSkip))
    while FindPic(Path(PicEventResult)) == (-1,-1):
        if FindPic(Path(PicEventAdvantage)) != (-1,-1):#如需判定进入判定阶段
            break
        if FindPic(Path(PicEventContinue)) != (-1,-1):#如如果提前结束跳出
            break
        #选择阶段
        print("Select Choice ")
        #咖啡杯EGO专用
        if FindPic(Path(PicEshake)) != (-1,-1):
            print("Coffee cup EGO")
            ClickPic(Path(PicEshake))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        else:
            print("All unknown ，select a random choice")
            ClickPic(Path(PicEventRandomSelect))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
            
    #判定阶段
    while FindPic(Path(PicEventAdvantage)) != (-1,-1):
        print("Event charge Progress")
        if FindPic(Path(PicEventContinue)) != (-1,-1):
            break
        ClickPic(Path(PicEveryHigh))
        ClickPic(Path(PicEventCommence))
        ClickPic(Path(PicEventSkip))
            
        
    #结束阶段
    while FindPic(Path(PicEventContinue)) == (-1,-1):
        print("Event end Progress")
        ClickPic(Path(PicEventSkip))
    ClickPic(Path(PicEventContinue))
    ClickXY((900,900))
        
def CheckSinner():
    if FindPic(Path(PicMapSign)) != (-1,-1):
        return
    print("Begin the sinner check progress")
    if FindPic(Path(PicNo1_1Ready)) == (-1,-1):
        print("No1 is not Ready,Check it on")
        ClickPic(Path(PicNo1_1))     
    if FindPic(Path(PicNo2_1Ready)) == (-1,-1):
        print("No2 is not Ready,Check it on")
        ClickPic(Path(PicNo2_1))      
    if FindPic(Path(PicNo4_1Ready)) == (-1,-1):
        print("No4 is not Ready,Check it on")
        ClickPic(Path(PicNo4_1))
    if FindPic(Path(PicNo5_1Ready)) == (-1,-1):
         print ("No5 is not Ready,Check it on")
         ClickPic(Path(PicNo5_1))
    if FindPic(Path(PicNo6_1Ready)) == (-1,-1):
        print ("No6 is not Ready,Check it on")
        ClickPic(Path(PicNo6_1))
    if FindPic(Path(PicNo9_1Ready)) == (-1,-1):
         print ("No9 is not Ready,Check it on")
         ClickPic(Path(PicNo9_1))
    if FindPic(Path(PicNo10_1Ready)) == (-1,-1):
         print ("No10 is not Ready,Check it on")
         ClickPic(Path(PicNo10_1))
    if FindPic(Path(PicNo11_1Ready)) == (-1,-1):
         print ("No11 is not Ready,Check it on")
         ClickPic(Path(PicNo11_1))
    if FindPic(Path(PicNo12_1Ready)) == (-1,-1):
        print ("No12 is not Ready,Check it on")
        ClickPic(Path(PicNo12_1))
    print("Check Finished")
    ClickPic(Path(PicStartBattle))

def SeleSinner(pic_s,pic_p):
    ClickPic(pic_s)
    ClickPic(pic_p)
    while FindPic(Path(PicConfirmW)) != (-1,-1):
        print("sinner confirm")
        ClickPic(Path(PicConfirmW))
    pi.click()
        
def CheckNew():
    print("Select new sinner")
    if FindPic(Path(PicNo2SignNew)) != (-1,-1):
        print("No2 was detected，Ready to fight")
        ClickPic(Path(PicNo2Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo2_1))
        return
    # 小唐无可用人格
    # if FindPic(Path(PicNo3Sign)) == (-1,-1):
    #     print("No3 was detected，Ready to fight")
    #     ClickPic(Path(PicNo3Sign))      
    #     ClickPic(Path(PicSelectNewSinner))
    #     return
    if FindPic(Path(PicNo5SignNew)) != (-1,-1):
        print("No5 was detected，Ready to fight")
        ClickPic(Path(PicNo5Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo5_1))
        return
    # 希斯克里夫无可用人格
    # if FindPic(Path(PicNo7Sign)) == (-1,-1):
    #     print("No7 was detected，Ready to fight")
    #     ClickPic(Path(PicNo7Sign))      
    #     ClickPic(Path(PicSelectNewSinner))
    #     return
    # 驯鹿内奸不用
    # if FindPic(Path(PicNo8Sign)) == (-1,-1):
    #     print("No8 was detected，Ready to fight")
    #     ClickPic(Path(PicNo8Sign))      
    #     ClickPic(Path(PicSelectNewSinner))
    #     return
    if FindPic(Path(PicNo9SignNew)) != (-1,-1):
        print("No9 was detected，Ready to fight")
        ClickPic(Path(PicNo9Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo9_1))
        return
    if FindPic(Path(PicNo10SignNew)) != (-1,-1):
        print("No10 was detected，Ready to fight")
        ClickPic(Path(PicNo10Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo10_1))
        return
    if FindPic(Path(PicNo11SignNew)) != (-1,-1):
        print("No11 was detected，Ready to fight")
        ClickPic(Path(PicNo11Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo11_1))
        return
    if FindPic(Path(PicNo12Sign)) != (-1,-1):
        print("No12 was detected，Ready to fight")
        ClickPic(Path(PicNo12Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo12_1))
        return

def AfterWin():
    # if FindPic(Path(PicMapSign)) != (-1,-1):
    #     return
    # count =1 
    # print("Check the afterwin branch for " +str(count)+" time")
    #while 1:
    if FindPic(Path(PicChoseLvUp)) != (-1,-1):
        print("Select the sinner to Level Up")
        if FindPic(Path(Piclv10)) != (-1,-1):
            ClickPic(Path(Piclv10))
        if FindPic(Path(Piclv15)) != (-1,-1):
            ClickPic(Path(Piclv15))
        if FindPic(Path(Piclv20)) != (-1,-1):
            ClickPic(Path(Piclv20))
        if FindPic(Path(Piclv25)) != (-1,-1):
            ClickPic(Path(Piclv25))
        ClickPic(Path(PicConfirm))
        ClickPic(Path(PicToEgo))
        ClickPic(Path(PicSelected))
        ClickPic(Path(PicConfirm))
        ClickPic(Path(PicConfirm))
        return
    if FindPic(Path(PicSelectGift)) != (-1,-1):
        print("Select the Ego Gift")
        ClickPic(Path(PicRandomGift))
        ClickPic(Path(PicSelectGift))
        time.sleep(2)
        ClickXY((900,900))    
        #WaitFor(PicConfirmW)
        return
    
if __name__ == '__main__':
    pi.FAILSAFE=False
    pi.PAUSE = 1
    loop = 1 
    pi.keyDown('alt')
    time.sleep(.2)
    pi.press('tab')
    time.sleep(.2)
    pi.keyUp('alt')
    while True:
        floor = 1
        step = 1
        finish = 0
        status = True
        #activeWindowTitle = pi.getActiveWindowTitle()
        #print(activeWindowTitle)
        # ClickPic(Path(PicDrive))
        # ClickPic(Path(PicEnterMirror))
        # ClickPic(Path(PicEnterMirror2))
        # ClickPic(Path(PicEnterMirror3))
      
        # print("Start " +str(floor)+" times loop") 
        # #初期礼物
        # print("Select the inital Ego gift") 
        # ClickPic(Path(PicRandomGift))
        # ClickPic(Path(PicSelectGift))
        # #初期人物选择
        # print("Selcet the inital sinners") 
        # ClickPic(Path(PicNo1))
        # ClickPic(Path(PicNo4))
        # ClickPic(Path(PicNo6))
        # ClickPic(Path(PicSelectSinner))
        # print("Change the personal") 
        # SeleSinner(Path(PicNo1Sign),Path(PicNo1_1))
        # SeleSinner(Path(PicNo4Sign),Path(PicNo4_1))
        # SeleSinner(Path(PicNo6Sign),Path(PicNo6_1))
        # time.sleep(2)
        # ClickPic(Path(PicConfirmW2))
        # Wait(30)
        
        #迷宫循环
        while step <= 9:
            if FindPic(Path(PicReceive)) != (-1,-1):
                loop = loop + 1
                print("Finished the loop " +str(loop))
                ClickPic(Path(PicReceive))
                ClickPic(Path(PicConfirmW))
                Wait(30)
                break
            print("Auto Run " +str(floor)+" floor and " +str(step)+" step")
            pi.scroll(10) # 向上滚动10格
            pi.scroll(10) # 向上滚动10格
            pi.scroll(10) # 向上滚动10格
            pi.scroll(10) # 向上滚动10格
            pi.scroll(10) # 向上滚动10格
            status = Searching()
            if step == 1:
                CheckSinner()
            else:
                ClickPic(Path(PicStartBattle))
            StartBattle()
            AfterWin()
            if status :
                print("Finish the " +str(floor)+" floor")
                floor = floor + 1
                step = 1
                CheckNew()
                time.sleep(5)
                ClickXY((900,900))           
            else:
                step = step + 1
        while FindPic(Path(PicEventChoice)) == (-1,-1):
            ClickPic(Path(PicEventSkip))
    
    

   
    
        
    
