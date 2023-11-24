def changeMAC(mac):
    #xx.xx.xx.xx.xx.xx
    #xxxx.xxxx.xxxx
    mac=mac.replace('.','')
    mac= mac[0:4] + "."+mac[4:8]+"." + mac[8:12] 
    print(mac)
    
changeMAC("aa.cf.ee.ef.dc.ff")