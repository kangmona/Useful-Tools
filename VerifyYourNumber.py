# -*- coding:utf-8 -*-
# 此脚本用于验证中国大陆手机号码所属运营商
cn_mobile = [134,135,136,137,138,139,150,151,152,
             157,158,159,182,183,184,187,188,147,178,1705]
cn_union = [130,131,132,155,156,185,186,145,176,1709]
cn_telecom = [133,153,180,181,189,177,1700]

def len_num(your_number):
    if len(your_number) == 11:
        return 1
    else:
        print('长度有误，请重新输入11位中国大陆手机号码！')
        start_verify()

def verify_num(vnum):
    v_nmuber = int(vnum)

    cnm = v_nmuber in cn_mobile #验证为移动
    cnu = v_nmuber in cn_union  #验证为联通
    cnt = v_nmuber in cn_telecom #验证为电信

    if cnm:
        print('运营商: 中国移动')
    elif cnu:
        print('运营商: 中国联通')
    elif cnt:
        print('运营商: 中国电信')
    else:
        print('查无此运营商，请重新输入11位中国大陆手机号码！')

def start_verify():
    your_number = input('请输入需要验证的手机号码：')
    valid = len_num(your_number)
    if valid:
        verify_num(your_number[0:3])
        print('确认码发送至:',your_number)

start_verify()
