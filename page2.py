import utilities as pdf
import PDFPrep as prep
import table_manager as tm
import math






tm.MONTH = 10
tm.YEAR = 2023
tm.HOLIDAYS_INPUT = [[2,'- - H O L I D A Y - -'],[13,'Shikshak Sammelan'],[14,'Shikshak Sammelan'],[24,'Vijaydashmi']] 
tm.STUDENT_DATA1 = ['-','-',52,53,52,54,54,'-',52,57,54,54,'-','-','-',54,50,53,56,53,51,'-',58,'-',57,52,54,51,'-',56,55]
#tm.STUDENT_DATA2 = [51,52,'-','-','-','-','-','-','-','-',511,512,513,514,515,516,'-',518,519,520,521,522,523,'-',525,526,527,528,529,530]
tm.STUDENT_DATA2 = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
tm.WHEAT_DAYS = [3,5,10,12,17,19,26,31]
COOKS = 2
FEUL = 910





def table1_data(sum1,sum2):
    size = 8
    y = 712
    data = [
        [round(sum1,2)       ,90 ,y,size],
        [round(sum1*5.45,2)  ,182,y,size],
        [round(sum1,2)       ,215,y,size],
        [round(sum1*0.378,2) ,280,y,size],
        [round(sum2,2)       ,325,y,size],
        [round(sum2*8.17,2)  ,405,y,size],
        [round(sum2,2)       ,450,y,size],
        [round(sum2*0.459,2) ,535,y,size],]
    return data

def table2_data(table1, no_of_cooks, feul_cost):
    size = 8
    y = 664
    total_cost = table1[1][0]+table1[3][0]+table1[5][0]+table1[7][0]+no_of_cooks*2003+feul_cost+500
    data = [
        [round(no_of_cooks,2)            ,90 ,y,size],
        [round(no_of_cooks*2003,2)       ,203,y,size],
        [round(feul_cost,2)              ,255,y,size],
        [str(round(total_cost,2))+'/-'   ,385,y,size],
        [str(math.ceil(total_cost))+'/-' ,496,y,size]]
    return data

pdf.add_text(pdf_path='Cleaned-MDM-Blank-UC.pdf')
sum1, sum2 = tm.table_manager()
table1 = table1_data(sum1,sum2)
table2 = table2_data(table1, COOKS, FEUL)
pdf.add_text(table1+table2, page_number=2, alignment='center')