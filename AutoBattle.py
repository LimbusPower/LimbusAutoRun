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
import logging
import logging.handlers
import datetime

#图片定义
path =  "D:\\WorkSapce\\Script\\"
PicMapSign = "MapSign.png"
PicWinRater = "WinRate.png"
PicStartBattle = "StartBattle.png"
PicStartFight = "StartFight.png"
PicReceive = "Receive.png"
PicRewards = "Rewards.png"

PicDrive = "Drive.png"
PicEnterMirror = "EnterMirror.png"
PicEnterMirror2 = "EnterMirror2.png"
PicEnterMirror3 = "EnterMirror3.png"

PicNormalBattle11 = "NormalBattle11.png"
PicNormalBattle12 = "NormalBattle12.png"
PicNormalBattle13 = "NormalBattle13.png"
PicNormalBattle22 = "NormalBattle22.png"
PicNormalBattle33 = "NormalBattle33.png"
PicAbnormalBattle = "AbnormalBattle.png"
PicAbnormalBattle2 = "AbnormalBattle2.png"
PicAbnormalBattle3 = "AbnormalBattle3.png"
PicAbnormalBattle32 = "AbnormalBattle32.png"
PicBossBattle = "BossBattle.png"
PicBossBattle2 = "BossBattle2.png"
PicBossBattle22 = "BossBattle22.png"
PicBossBattle3 = "BossBattle3.png"
PicBossBattle32 = "BossBattle32.png"
PicEventBattle = "EventBattle.png"
PicEventBattle3 = "EventBattle3.png"
PicEndPoint = "EndPoint.png"
PicEndPoint2 = "EndPoint2.png"
PicEndPoint22 = "EndPoint22.png"
PicEndPoint23 = "EndPoint23.png"
PicEndPoint3 = "EndPoint3.png"
PicEndPoint32 = "EndPoint32.png"
PicEndPoint33 = "EndPoint33.png"
PicEndPoint34 = "EndPoint34.png"
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


PicElvup = "Elvup.png"
PicESelectSinner = "ESelectSinner.png"
PicEshake = "Eshake.png"
PicEbloodPack = "EbloodPack.png"
PicEAshesChoice = "EAshesChoice.png"
PicEeletronicSheep = "EeletronicSheep.png"
PicEnixieDivergencee = "EnixieDivergence.png"
PicEstandardBattery = "EstandardBattery.png"
PicElateTatto = "ElateTatto.png"
PicEZippoLighter = "EZippoLighter.png"
PicEPerversion = "EPerversion.png"
PicEPickRose = "EPickRose.png"
PicEPhantom = "EPhantom.png"
PicEFieryDown = "EFieryDown.png"
PicEHellTerfly = "EHellTerfly.png"
PicEGadget = "EGadget.png"
PicEBundle = "EBundle.png"
PicEGrayCoat = "EGrayCoat.png"
PicEtree = "Etree.png"
PicETown = "ETown.png"
PicETown22 = "ETown22.png"

PicEveryHigh = "EveryHigh.png"
PicEBossApple = "EBossApple.png"
PicEBossFactory = "EBossFactory.png"
PicEBossFactory2 = "EBossFactory2.png"
PicEBossCalendar = "EBossCalendar.png"
PicEBossShoes = "EBossShoes.png"

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

PicNo1SignNew = "No1SignNew.png"
PicNo2SignNew = "No2SignNew.png"
PicNo3SignNew = "No3SignNew.png"
PicNo4SignNew = "No4SignNew.png"
PicNo5SignNew = "No5SignNew.png"
PicNo6SignNew = "No6SignNew.png"
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
PicNo3_1Ready = "No3_1Ready.png"
PicNo4_1Ready = "No4_1Ready.png"
PicNo5_1Ready = "No5_1Ready.png"
PicNo6_1Ready = "No6_1Ready.png"
PicNo7_1Ready = "No7_1Ready.png"
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


def u8ones(shape): 
    return np.ones(shape, dtype=np.uint8)

def ipm(img): 
    image_points = np.float32([
      (539, 540), (749, 540), (959, 540), (1169, 540),
                  (727, 705),             (1192, 705)
    ])
    rectified_points = np.float32([
      (-2, 0), (-1, 0), (0, 0), (1, 0),
               (-1, 1),         (1, 1)
    ]) * 200 + np.float32([1920, 1080]) / 2

    T = cv2.getPerspectiveTransform(image_points[[1,3,4,5]], rectified_points[[1,3,4,5]])
    return cv2.warpPerspective(img,T,(img.shape[1], img.shape[0]))

def trim_border(img):
  h, w, _ = img.shape
  return img[:int(h * 0.87)]

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

def FindPic_IMP(small_picture_path, similarity=0.85):
    '''
    区域找图
    :param small_picture_path:目标小图的路径
    :param similarity:相似度,0.95
    :return: (0,100) |(-1,-1)
    '''
    if not os.path.exists(small_picture_path):
        return None
    bag = ipm(pil2np(ImageGrab.grab()))
    #Image.fromarray(bag).show()
    small = cv2.imread(small_picture_path)
    #Image.fromarray(small).show()
    res = aircv.find_all_template(bag, small, 0.7)
    return res

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
    logging.info("Wait loading for " +str(x) + " seconds")
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
    if FindPic(Path(PicEnterBattle)) != (-1,-1):
        ClickXY((200,200))#误触发退回用
    if FindPic(Path(PicMapSign)) != (-1,-1):
        return
    logging.info("Start Battle")
    retryCount = 1
    battleCount = 1
    while retryCount <  80:
        if FindPic(Path(PicEnterBattle)) != (-1,-1):
            ClickXY((200,200))#误触发退回用
        if FindPic(Path(PicRewards)) != (-1,-1):
            break
        if FindPic(Path(PicChoseLvUp)) != (-1,-1):
            break
        if FindPic(Path(PicSelectGift)) != (-1,-1):
            break
        if FindPic(Path(PicEventSkip)) != (-1,-1):
            logging.info("Boss battle event choice")
            while FindPic(Path(PicEventContinue)) == (-1,-1):
                ClickPic(Path(PicEventSkip))
                if FindPic(Path(PicEBossApple)) != (-1,-1):
                    logging.info("Boss Apple Queen")
                    while FindPic(Path(PicEventResult)) == (-1,-1):
                        logging.info("Charge Progress")
                        ClickPic(Path(PicEveryHigh))
                        ClickPic(Path(PicEventCommence))
                        if FindPic(Path(PicEventContinue)) != (-1,-1):
                            logging.info("Charge Stop")
                            break
                if FindPic(Path(PicEBossShoes)) != (-1,-1):
                    logging.info("Boss Pink Shoes")
                    ClickPic(Path(PicEBossShoes))
                    while FindPic(Path(PicEventContinue)) == (-1,-1):
                        logging.info("Charge Progress")
                        ClickPic(Path(PicEventProceed))
                        ClickPic(Path(PicEventSkip))
                        if FindPic(Path(PicEventContinue)) != (-1,-1):
                            logging.info("Charge Stop")
                            break
                if FindPic(Path(PicEBossFactory)) != (-1,-1):
                    logging.info("Boss Factory")
                    ClickPic(Path(PicEBossFactory))
                    while FindPic(Path(PicEventContinue)) == (-1,-1):
                        logging.info("Charge Progress")
                        ClickPic(Path(PicEventProceed))
                        ClickPic(Path(PicEventSkip))
                        if FindPic(Path(PicEventContinue)) != (-1,-1):
                            logging.info("Charge Stop")
                            break
                if FindPic(Path(PicEBossFactory2)) != (-1,-1):
                    logging.info("Boss Factory2")
                    while FindPic(Path(PicEventContinue)) == (-1,-1):
                        logging.info("Repeat No")
                        ClickPic(Path(PicEBossFactory2))
                        ClickPic(Path(PicEventProceed))
                        ClickPic(Path(PicEventSkip))
                        if FindPic(Path(PicEventContinue)) != (-1,-1):
                            logging.info("Charge Stop")
                            break
                if FindPic(Path(PicEBossCalendar)) != (-1,-1):
                    logging.info("Boss Calendar")
                    ClickPic(Path(PicEBossCalendar))
                    ClickPic(Path(PicEventProceed))
                    ClickPic(Path(PicEventSkip))
                    #判定阶段
                    while FindPic(Path(PicEventAdvantage)) != (-1,-1):
                        logging.info("Event charge Progress")
                        if FindPic(Path(PicEventContinue)) != (-1,-1):
                            break
                        ClickPic(Path(PicEveryHigh))
                        ClickPic(Path(PicEventCommence))
                        ClickPic(Path(PicEventSkip))
            ClickPic(Path(PicEventContinue))
                    
          
        logging.info("Battle Icon check "+ str(retryCount) + " times")
        if FindPic(Path(PicWinRater)) == (-1,-1):
            retryCount = retryCount + 1
        else:
            logging.info("Do Battle in Turn " + str(battleCount))
            ClickPic(Path(PicWinRater))
            if FindPic(Path(PicStartFight)) != (-1,-1):
                ClickPic(Path(PicStartFight))
            else:
                pi.click()
                ClickPic(Path(PicStartFight))
            battleCount = battleCount + 1
        time.sleep(3)
    logging.info("Battle Finshed")
        
def SeachrFor(pic,s):
    logging.info("Search for " + str(pic))
    r = FindPicList(Path(pic),s)
    
    for i in r:
        ClickXY(i["result"])
        logging.info("Find "+str(pic) + " in " + str(i["result"])+ " Try to get the Entrance")
        time.sleep(1)
        if FindPic(Path(PicEnterBattle)) != (-1,-1):
            logging.info("Get Battle Entrace Ready to Start")
            ClickPic(Path(PicEnterBattle))
            return True
    return False

def EventLevelUp():
    logging.info("Level up event")
    while FindPic(Path(PicEventChoice)) == (-1,-1):
        ClickPic(Path(PicEventSkip))
    while FindPic(Path(PicEventResult)) == (-1,-1):
        ClickPic(Path(PicEventRandomSelect))
        ClickPic(Path(PicEventSkip))
    while FindPic(Path(PicEventContinue)) == (-1,-1):
        ClickPic(Path(PicEventContinue))
    ClickPic(Path(PicEventContinue))    
    for i in range(3):
        logging.info("Try to Level up for " + str(i)+ " times")
        if FindPic(Path(PicChoseLvUp)) != (-1,-1):
            logging.info("Select the sinner to Level Up")
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
            
def EventSelectSinnner():
    while FindPic(Path(PicEventChoice)) == (-1,-1):
        ClickPic(Path(PicEventSkip))
    while FindPic(Path(PicEventResult)) == (-1,-1):
        ClickPic(Path(PicEventRandomSelect))
        ClickPic(Path(PicEventSkip))
    while FindPic(Path(PicEventContinue)) == (-1,-1):
        ClickPic(Path(PicEventContinue))
    ClickPic(Path(PicEventContinue))    
    CheckNew()

def Searching():
    logging.info("Start seachring")
    while True:
        if FindPic(Path(PicEnterBattle)) != (-1,-1):
            ClickXY((200,200))#误触发退回用
        if FindPic(Path(PicRewards)) != (-1,-1):
            logging.info("Finished the loop ？？？" )
            ClickPic(Path(PicConfirmW))
            pi.click()
            time.sleep(3)
            ClickPic(Path(PicReceive))
            pi.click()
            Wait(10)
            break
        if SeachrFor(PicEventLevelUp,0.85):
            EventLevelUp()
            return False
            
        if SeachrFor(PicNormalBattle11,0.85):
            return False
        if SeachrFor(PicNormalBattle22,0.85):
            return False
        if SeachrFor(PicNormalBattle33,0.85):
            return False
        if SeachrFor(PicAbnormalBattle,0.85):
            return False
        if SeachrFor(PicAbnormalBattle2,0.85):
            return False
        if SeachrFor(PicAbnormalBattle3,0.85):
            return False
        if SeachrFor(PicAbnormalBattle32,0.85):
            return False
        if SeachrFor(PicBossBattle,0.75):
            return False
        if SeachrFor(PicBossBattle2,0.75):
            return False
        if SeachrFor(PicBossBattle3,0.75):
            return False   
        if SeachrFor(PicBossBattle32,0.75):
            return False  
        if SeachrFor(PicEndPoint,0.65):
            logging.info("Finished the floor")
            return True
        if SeachrFor(PicEndPoint2,0.65):
            logging.info("Finished the floor")
            return True
        if SeachrFor(PicEndPoint22,0.65):
            logging.info("Finished the floor")
            return True
        if SeachrFor(PicEndPoint23,0.65):
            logging.info("Finished the floor")
            return True
        if SeachrFor(PicEndPoint3,0.65):
            logging.info("Finished the floor")
            return True
        if SeachrFor(PicEndPoint32,0.65):
            logging.info("Finished the floor")
            return True
        if SeachrFor(PicEndPoint33,0.65):
            logging.info("Finished the floor")
            return True
        if SeachrFor(PicEndPoint34,0.65):
            logging.info("Finished the floor")
            return True
        if SeachrFor(PicEndPoint4,0.65):
            logging.info("Finished the floor")
            return True
        # if SeachrFor(PicEventSelectSinnner):
        #     EventSelectSinnner()
        #     return False
        if SeachrFor(PicEventBattle,0.7):
            EventChoice()
            return False
        # if SeachrFor(PicEventBattle3):
        #     EventChoice()
        #     return False
       
        pi.scroll(-10) # 向下滚动10格
        pi.scroll(-10) # 向下滚动10格

def EventChoice():
    logging.info("Start Event Choice ")
    while FindPic(Path(PicEventChoice)) == (-1,-1):
        ClickPic(Path(PicEventSkip))
    while FindPic(Path(PicEventResult)) == (-1,-1):
        if FindPic(Path(PicEventAdvantage)) != (-1,-1):#如需判定进入判定阶段
            break
        if FindPic(Path(PicEventContinue)) != (-1,-1):#如果提前结束跳出
            break
        #选择阶段
        logging.info("Select Choice ")
        if FindPic(Path(PicElvup)) != (-1,-1):
            logging.info("Level Up event")
            EventLevelUp()
            return #特殊事件提前跳出
        if FindPic(Path(PicESelectSinner)) != (-1,-1):
            logging.info("Select sinner event")
            EventSelectSinnner()
            return #特殊事件提前跳出
        #咖啡杯EGO专用
        if FindPic(Path(PicEshake)) != (-1,-1):
            logging.info("Coffee cup EGO")
            ClickPic(Path(PicEshake))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #血袋ego
        elif FindPic(Path(PicEbloodPack)) != (-1,-1):
            logging.info("EbloodPack  EGO")
            ClickPic(Path(PicEbloodPack))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #灰烬ego
        elif FindPic(Path(PicEAshesChoice)) != (-1,-1):
            logging.info("EAshesChoice  EGO")
            ClickPic(Path(PicEAshesChoice))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #电🐏ego
        elif FindPic(Path(PicEeletronicSheep)) != (-1,-1):
            logging.info("EeletronicSheep  EGO")
            ClickPic(Path(PicEeletronicSheep))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #子弹ego
        elif FindPic(Path(PicEnixieDivergencee)) != (-1,-1):
            logging.info("EnixieDivergencee  EGO")
            ClickPic(Path(PicEnixieDivergencee))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #电池ego
        elif FindPic(Path(PicEstandardBattery)) != (-1,-1):
            logging.info("standardBattery  EGO")
            ClickPic(Path(PicEstandardBattery))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #电线杆？ego
        elif FindPic(Path(PicElateTatto)) != (-1,-1):
            logging.info("ElateTatto  EGO")
            ClickPic(Path(PicElateTatto))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #打火机ego
        elif FindPic(Path(PicEZippoLighter)) != (-1,-1):
            logging.info("ZippoLighter  EGO")
            ClickPic(Path(PicEZippoLighter))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #立方体ego
        elif FindPic(Path(PicEPerversion)) != (-1,-1):
            logging.info("Perversion  EGO")
            ClickPic(Path(PicEPerversion))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #摘花ego
        elif FindPic(Path(PicEPickRose)) != (-1,-1):
            logging.info("PickRose  EGO")
            ClickPic(Path(PicEPickRose))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #幻痛ego
        elif FindPic(Path(PicEPhantom)) != (-1,-1):
            logging.info("Phantom  EGO")
            ClickPic(Path(PicEPhantom))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #火羽毛？ego
        elif FindPic(Path(PicEFieryDown)) != (-1,-1):
            logging.info("FieryDown  EGO")
            ClickPic(Path(PicEFieryDown))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #火蝴蝶？ego
        elif FindPic(Path(PicEHellTerfly)) != (-1,-1):
            logging.info("HellTerfly  EGO")
            ClickPic(Path(PicEHellTerfly))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #偷戒指？ego
        elif FindPic(Path(PicEGadget)) != (-1,-1):
            logging.info("HellTerfly  EGO")
            ClickPic(Path(PicEGadget))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #一叠钞票？ego
        elif FindPic(Path(PicEBundle)) != (-1,-1):
            logging.info("HellTerfly  EGO")
            ClickPic(Path(PicEBundle))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #灰大衣ego
        elif FindPic(Path(PicEGrayCoat)) != (-1,-1):
            logging.info("GrayCoat  EGO")
            ClickPic(Path(PicEGrayCoat))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #灰大衣ego
        elif FindPic(Path(PicEtree)) != (-1,-1):
            logging.info("Tree  EGO")
            ClickPic(Path(PicEtree))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
        #Hello world？ego
        elif FindPic(Path(PicETown)) != (-1,-1):
            logging.info("Hello town EGO")
            ClickPic(Path(PicETown))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
            while FindPic(Path(PicEventContinue)) != (-1,-1):
                ClickPic(Path(PicETown22))#升级卡不升级
                ClickPic(Path(PicEventProceed))
                ClickPic(Path(PicEventSkip))      
        else:
            logging.info("All unknown ，select a random choice")
            ClickPic(Path(PicEventRandomSelect))
            ClickPic(Path(PicEventProceed))
            ClickPic(Path(PicEventSkip))
            
    #判定阶段
    while FindPic(Path(PicEventAdvantage)) != (-1,-1):
        logging.info("Event charge Progress")
        if FindPic(Path(PicEventContinue)) != (-1,-1):
            break
        ClickPic(Path(PicEveryHigh))
        ClickPic(Path(PicEventCommence))
        ClickPic(Path(PicEventSkip))
            
        
    #结束阶段
    while FindPic(Path(PicEventContinue)) == (-1,-1):
        logging.info("Event end Progress")
        ClickPic(Path(PicEventSkip))
    ClickPic(Path(PicEventContinue))
    ClickXY((900,900))
        
def CheckSinner():
    if FindPic(Path(PicMapSign)) != (-1,-1):
        return
    logging.info("Begin the sinner check progress")
    if FindPic(Path(PicNo1_1Ready)) == (-1,-1):
        logging.info("No1 is not Ready,Check it on")
        ClickPic(Path(PicNo1_1))     
    if FindPic(Path(PicNo2_1Ready)) == (-1,-1):
        logging.info("No2 is not Ready,Check it on")
        ClickPic(Path(PicNo2_1))   
    if FindPic(Path(PicNo3_1Ready)) == (-1,-1):
        logging.info("No3 is not Ready,Check it on")
        ClickPic(Path(PicNo3_1))      
    if FindPic(Path(PicNo4_1Ready)) == (-1,-1):
        logging.info("No4 is not Ready,Check it on")
        ClickPic(Path(PicNo4_1))
    if FindPic(Path(PicNo5_1Ready)) == (-1,-1):
         logging.info ("No5 is not Ready,Check it on")
         ClickPic(Path(PicNo5_1))
    if FindPic(Path(PicNo6_1Ready)) == (-1,-1):
        logging.info ("No6 is not Ready,Check it on")
        ClickPic(Path(PicNo6_1))
    if FindPic(Path(PicNo7_1Ready)) == (-1,-1):
        logging.info ("No7 is not Ready,Check it on")
        ClickPic(Path(PicNo7_1))
    if FindPic(Path(PicNo9_1Ready)) == (-1,-1):
         logging.info ("No9 is not Ready,Check it on")
         ClickPic(Path(PicNo9_1))
    if FindPic(Path(PicNo10_1Ready)) == (-1,-1):
         logging.info ("No10 is not Ready,Check it on")
         ClickPic(Path(PicNo10_1))
    if FindPic(Path(PicNo11_1Ready)) == (-1,-1):
         logging.info ("No11 is not Ready,Check it on")
         ClickPic(Path(PicNo11_1))
    if FindPic(Path(PicNo12_1Ready)) == (-1,-1):
        logging.info ("No12 is not Ready,Check it on")
        ClickPic(Path(PicNo12_1))
    logging.info("Check Finished")
    ClickPic(Path(PicStartBattle))

def SeleSinner(pic_s,pic_p):
    ClickPic(pic_s)
    ClickPic(pic_p)
    while FindPic(Path(PicConfirmW)) != (-1,-1):
        logging.info("sinner confirm")
        ClickPic(Path(PicConfirmW))
    pi.click()
        
def CheckNew():
    logging.info("Select new sinner")
    if FindPic(Path(PicNo6SignNew)) != (-1,-1):
        logging.info("No6 was detected，Ready to fight")
        ClickPic(Path(PicNo6Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo6_1))
        return
    if FindPic(Path(PicNo3SignNew)) != (-1,-1):
        logging.info("No3 was detected，Ready to fight")
        ClickPic(Path(PicNo3Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo3_1))
        return
    if FindPic(Path(PicNo4SignNew)) != (-1,-1):
        logging.info("No4 was detected，Ready to fight")
        ClickPic(Path(PicNo4Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo4_1))
        return
    if FindPic(Path(PicNo1SignNew)) != (-1,-1):
        logging.info("No1 was detected，Ready to fight")
        ClickPic(Path(PicNo1Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo1_1))
        return
       
    # if FindPic(Path(PicNo2SignNew)) != (-1,-1):
    #     logging.info("No2 was detected，Ready to fight")
    #     ClickPic(Path(PicNo2Sign))      
    #     ClickPic(Path(PicSelectNewSinner))
    #     SeleSinner(Path(PicAleph),Path(PicNo2_1))
    #     return
    # if FindPic(Path(PicNo5SignNew)) != (-1,-1):
    #     logging.info("No5 was detected，Ready to fight")
    #     ClickPic(Path(PicNo5Sign))      
    #     ClickPic(Path(PicSelectNewSinner))
    #     SeleSinner(Path(PicAleph),Path(PicNo5_1))
    #     return
   
    # 
    # if FindPic(Path(PicNo7Sign)) == (-1,-1):
    #     logging.info("No7 was detected，Ready to fight")
    #     ClickPic(Path(PicNo7Sign))      
    #     ClickPic(Path(PicSelectNewSinner))
    #     return
    # 驯鹿内奸不用
    # if FindPic(Path(PicNo8Sign)) == (-1,-1):
    #     logging.info("No8 was detected，Ready to fight")
    #     ClickPic(Path(PicNo8Sign))      
    #     ClickPic(Path(PicSelectNewSinner))
    #     return
    if FindPic(Path(PicNo9SignNew)) != (-1,-1):
        logging.info("No9 was detected，Ready to fight")
        ClickPic(Path(PicNo9Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo9_1))
        return
    if FindPic(Path(PicNo10SignNew)) != (-1,-1):
        logging.info("No10 was detected，Ready to fight")
        ClickPic(Path(PicNo10Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo10_1))
        return
    if FindPic(Path(PicNo11SignNew)) != (-1,-1):
        logging.info("No11 was detected，Ready to fight")
        ClickPic(Path(PicNo11Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo11_1))
        return
    if FindPic(Path(PicNo12Sign)) != (-1,-1):
        logging.info("No12 was detected，Ready to fight")
        ClickPic(Path(PicNo12Sign))      
        ClickPic(Path(PicSelectNewSinner))
        SeleSinner(Path(PicAleph),Path(PicNo12_1))
        return

def AfterWin():
    if FindPic(Path(PicEnterBattle)) != (-1,-1):
        ClickXY((200,200))#误触发退回用
    if FindPic(Path(PicRewards)) != (-1,-1):
       return
    # count =1 
    logging.info("Check the afterwin branch" )
    #while 1:
    if FindPic(Path(PicChoseLvUp)) != (-1,-1):
        logging.info("Select the sinner to Level Up")
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
        logging.info("Select the Ego Gift")
        ClickPic(Path(PicRandomGift))
        ClickPic(Path(PicSelectGift))
        time.sleep(2)
        ClickXY((900,900))    
        #WaitFor(PicConfirmW)
        return

def loginit(): 
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
        filename="log.txt",
        filemode="w"  # 每次重启程序，覆盖之前的日志
    )
    
if __name__ == '__main__':
    loginit()
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
        activeWindowTitle = pi.getActiveWindowTitle()
        logging.info(activeWindowTitle)
        ClickPic(Path(PicDrive))
        ClickPic(Path(PicEnterMirror))
        ClickPic(Path(PicEnterMirror2))
        ClickPic(Path(PicEnterMirror3))
      
        logging.info("Start " +str(floor)+" times loop") 
        #初期礼物
        logging.info("Select the inital Ego gift") 
        ClickPic(Path(PicRandomGift))
        ClickPic(Path(PicSelectGift))
        #初期人物选择
        logging.info("Selcet the inital sinners") 
        ClickPic(Path(PicNo2))
        ClickPic(Path(PicNo5))
        ClickPic(Path(PicNo7))
        ClickPic(Path(PicSelectSinner))
        logging.info("Change the personal") 
        SeleSinner(Path(PicNo2Sign),Path(PicNo2_1))
        SeleSinner(Path(PicNo5Sign),Path(PicNo5_1))
        SeleSinner(Path(PicNo7Sign),Path(PicNo7_1))
        
        
        time.sleep(2)
        ClickPic(Path(PicConfirmW2))
        Wait(15)
        
        #迷宫循环
        while step <= 12:
            if FindPic(Path(PicRewards)) != (-1,-1):
                logging.info("Finished the loop " +str(loop))
                loop = loop + 1
                logging.info("Confirm")
                ClickPic(Path(PicConfirmW))
                pi.click()
                time.sleep(15)
                logging.info("Receive")
                ClickPic(Path(PicReceive))
                pi.click()
                Wait(15)
                break
            logging.info("Auto Run " +str(floor)+" floor and " +str(step)+" step")
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
                if FindPic(Path(PicRewards)) == (-1,-1):
                    logging.info("Finish the " +str(floor)+" floor")
                    floor = floor + 1
                    step = 1
                    CheckNew()
                    time.sleep(5)
                    ClickXY((900,900))           
            else:
                step = step + 1
    #StartBattle()
        
    
