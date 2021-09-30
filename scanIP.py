import os
import re
import sys
# python3扫描同个网段的存活主机
def ping_ip(ip):
    output = os.popen('ping %s -n 1' % ip).readlines()
    for w in output:
        if w.find('TTL') >= 0:
            # print(ip, 'ok')
            print('%s 存活' % ip)
            f=open("outip.txt",'a')
            f.write('\n'+ip+'\n')
            f.close()
        elif w.find('TTL') < 0:
            print('%s 关闭' % ip)
        else:
            print("输入错误！")

if __name__ == '__main__':

    # 判断outip.txt是否存在，存在则删除
    # 获取当前文件路径的上一级目录
    project_path = os.path.dirname(os.path.abspath(__file__))
    # print(project_path)
    # 拼接路径字符串E:\工具练习\python\day01\IP和端口扫描\outip.txt
    file_path = project_path +'\\'+r'outip.txt'
    if os.path.exists(file_path):
        print(file_path)
        os.remove(file_path)

    str1 = input("请输入IP段，如192.168.0.1/24：")
    str2 = re.split('/', str1)
    str3 = str2[0].split('.')
    st4 = str3[0] + '.' + str3[1] + '.' + str3[2] + '.'
    ip1 = st4
    for i in range(1,256):
        ip2 = ip1+str(i)
        ping_ip(ip2)
