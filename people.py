import openpyxl , pprint
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb['Population by Census Tract']         #新版建议用Workbook['表名']即可获取
countyData={}
print('Reading Date......')
for row in range(2,sheet.max_row +1 ):
    state  = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop    = sheet['D'+str(row)].value

#setdefault和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    countyData.setdefault(state,{})    #把state添加到countyData中
    countyData[state].setdefault(county,{'tracts':0,'pop':0})
    countyData[state][county]['tracts']+=1
    countyData[state][county]['pop'] +=int(pop)
print('Writing Data.......')
Resultfile=open('Result.py','w')
Resultfile.write('allData='+pprint.pformat(countyData))
Resultfile.close()
print('done')

