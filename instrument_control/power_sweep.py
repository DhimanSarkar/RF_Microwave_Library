import scpi
import instruments
import time

sg = instruments.SG_SGS100A("TCPIP::10.10.10.2::5025::SOCKET")
pm = instruments.PM_U8488A('USB0::0x2A8D::0xA718::MY62040007::0::INSTR')
ps = instruments.PS_E36234A('TCPIP::10.10.10.1::5025::SOCKET')
sa = instruments.SA_MS2720T('TCPIP::10.10.10.3::9001::SOCKET')

pwr_cal_data = []
## Absolute Power Calibration
# src->cable->power_meter
def source_power_calibration(pSrc_min,pSrc_max,nPoints):
    swpIndex = 1
    srcCal = []
    pSrc_interval = (pSrc_max-pSrc_min)/nPoints
    pSrc = pSrc_min
    for _i in range(0,nPoints+1):
        sg.set(1).power(pSrc).enable
        pm_data = pm.get().power()
        srcCal.append([swpIndex, pSrc, pm_data])
        # print(str(pSrc) + " " + str(pm_data))
        print(str(pm_data))
        swpIndex = swpIndex + 1
        pSrc = pSrc + pSrc_interval
    pwr_cal_data.append(srcCal)

## Input Receiver Power Calibration
# src->cable->bridge->cable/attn->power_meter
def pIn_power_calibration(pSrc_min,pSrc_max,nPoints):
    swpIndex = 1
    pwrInCal = []
    pSrc_interval = (pSrc_max-pSrc_min)/nPoints
    pSrc = pSrc_min
    for _i in range(0,nPoints+1):
        sg.set(1).power(pSrc).enable
        pm_data = pm.get().power()
        pwrInCal.append([swpIndex, pSrc, pm_data])
        # print(str(pSrc) + " " + str(pm_data))
        print(str(pm_data))
        swpIndex = swpIndex + 1
        pSrc = pSrc + pSrc_interval
    pwr_cal_data.append(pwrInCal)

## Input Receiver Power Calibration
# src->cable->bridge->cable/attn->spectrum_analyzer
def pOut_power_calibration(pSrc_min,pSrc_max,nPoints):
    swpIndex = 1
    pwrOutCal = []
    pSrc_interval = (pSrc_max-pSrc_min)/nPoints
    pSrc = pSrc_min
    for _i in range(0,nPoints+1):
        sg.set(1).power(pSrc).enable
        time.sleep(0.1)     # need to modify based on SA sweep time
        sa_data = sa.get().marker(1)
        pwrOutCal.append([swpIndex, pSrc, sa_data[1]])
        # print(str(pSrc) + " " + str(sa_data))
        print(str(sa_data[1]))
        swpIndex = swpIndex + 1
        pSrc = pSrc + pSrc_interval
    pwr_cal_data.append(pwrOutCal)

# print('500 MHz')
# sg.disable
# # sg.set().frequency('500 MHz')
# # source_power_calibration(-10, 0, 10)
# # pIn_power_calibration(-10, 0, 10)
# # sa.set().frequency('1 GHz')
# # pOut_power_calibration(-10, 0,10)
# sg.disable


# source_power_calibration(-10, 0, 10)
# pIn_power_calibration(-10, 0, 20)
# pOut_power_calibration(-10, 0, 20)

# print(pwr_cal_data)


sg.disable
ps.set(2).disable
ps.set(1).disable

for n in range(0,16):
    freq = str(0.5 + n*0.1) + " GHz"

    print(freq)
    sg.set().frequency(freq)
    # source_power_calibration(-10, 0, 10)
    # pIn_power_calibration(-10, 0, 10)
    sa.set().frequency(freq)
    pOut_power_calibration(-10, 0, 10)

    # print(freq)
    # sg.set().frequency(freq)
    # sa.set().frequency(freq)
    # ps.set(1).enable
    # time.sleep(1)
    # ps.set(2).enable
    # for pwrSrc in range(0,31):
    #     sg.set().power(pwrSrc).enable
    #     time.sleep(0.1)
    #     V1 = ps.get(1).voltage()
    #     I1 = ps.get(1).current()
    #     V2 = ps.get(2).voltage()
    #     I2 = ps.get(2).current()
    #     pwrIn = pm.get().power()
    #     pwrOut = sa.get().marker(1)
    #     print(str(pwrSrc) + "," + str(pwrIn) + "," + str(pwrOut[1]) + "," + str(V1) + "," + str(I1) + "," + str(V2) + "," + str(I2))
    # sg.disable
    # ps.set(2).disable
    # time.sleep(1)
    # ps.set(1).disable