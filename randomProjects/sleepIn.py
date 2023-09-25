
def sleep(wd, vc):
    return not wd or vc


sleep(False, False) == True
sleep(True, False) == False
sleep(False, True) == True
