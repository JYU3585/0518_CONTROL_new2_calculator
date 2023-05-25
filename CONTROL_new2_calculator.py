"""
接續0517的UI計算機 ，加上進度條&拉霸
"""

from PyQt5.QtWidgets import *                               # 我從PyQt5.QtWidgets把所有東西import進來（* 代表所有）
from PyQt5.QtCore import *                                  # 我從PyQt5.QtCore把所有東西import進來（* 代表所有）
from PyQt5.QtGui import *                                   # 我從PyQt5.QtGui把所有東西import進來（* 代表所有）

# 其實最好是一個一個import進來，不然有可能兩個函式庫裡面的函式有重疊會打架

from new2_calculator import Ui_Dialog                       # 從隔壁檔案import進來
import sys                                                  # sys = system


def isfloat(num):                                           # 找網路上別人寫的一個自定義函數，去做小數判斷
     try: 
          float(num)
          return True
     except ValueError: 
          return False     

def clicked_add():                                          # ★★★ 設定點擊按鈕的動作 ★★★
    # a = int(ui.inputNum1.text())                          # 程式會自動判定輸入的值為 "字串" 型式，無法直接讀取成數字
    # b = int(ui.inputNum2.text())                          # 所以一定要用int自己做格式轉換，字串 → 數字
    ui.progressBar.setValue(50)                             # ◇◇◇ 設定進度條，點add按鈕則進度條顯示進度為50
    A = ui.inputNum1.text()                                 # 這邊輸出的結果是 "字串"
    B = ui.inputNum2.text()
    
    if isfloat(A) and isfloat(B):                           # 防呆，判斷輸入的是否為數字(含浮點數)，若輸入文字則報錯
        var1 = float(A)                                     # 把 "字串" 轉成 "浮點數"，才能做數值運算
        var2 = float(B)
        ui.result.setText(str(var1 + var2))                 # .setText()只能吃 "字串"，所以這邊要再次自己轉換格式，數字 → 字串，才讀取得出來
    else: 
        message = QMessageBox()
        message.setWindowTitle("ERROR!!!!!!!!")
        message.setInformativeText("Please enter numbers!") # 不知為何視窗跳出就是會自動換行，無法把視窗變寬，峰峰也無解...
        message.exec_()

def click_pucture(event):                                   # ★★★ 設定點擊圖片的動作 ★★★
        message = QMessageBox()
        message.setWindowTitle("Surprise~~~")
        message.setInformativeText("你按了圖片!!!")
        message.exec_()
        print(event.x())                                    # .x() 對著圖片點下去的那個點的 x軸位置(px)
        print(event.y())                                    # .y() 對著圖片點下去的那個點的 y軸位置(px)
        print(event.button())                               # .button() 對著圖片點下去的那個按鍵：左鍵1，右鍵2，中間滾輪4，滾輪向左8，滾輪向右16

def click_radio():                                          # ★★★ 設定點選radio button的動作 ★★★
    print("You clicked Radio1.")                            # 點選 Radio1 時，就會在terminal內print出指定文字

def check_radio():                                          # ◇◇◇ 確認radio button是否點選。設一個 def 並透過點選click me按鈕的動作來確認
    print(ui.radioButton_1.isChecked())                     # 僅在terminal內print(ui介面無反應)。若有點選radio button則按下clicke me會出現True。反之則False。

def radio_calculate(): 
    A = ui.inputNum1.text()
    B = ui.inputNum2.text()

    if ui.checkBox.isChecked():                             # 若check box打勾，則 inputNum1 &2 兩個數字對調（+ * 沒差，但 - / 有差）
        A = ui.inputNum2.text()
        B = ui.inputNum1.text()
        # return                                            # 這邊不能加return!!!  return代表直接跳出此def函式，代表後面的所有東西(此def內的)都不執行了。
        
    # 可以在同一階層寫很多if（不一定要有elif或else），只要不要return跳出此def函式，這串函式碼就可以一直走下去，遇到if為True就進到判斷式，，遇到if為False就忽略判斷式繼續往下走。
    
    """
    交換數值的演算法，若要把 X 和 Y 的值互換，需要先用一個暫時的變數，以個暫時的箱子去裝 X的值
    tmp = x
    x = y
    y = tmp
    """    
    
    if ui.languageComboBox.currentIndex() == 1:
        C = "答案是: "
    elif ui.languageComboBox.currentIndex() == 2: 
        # print("elif")                                     # 遇到問題但沒出現error message，可以print出來檢查看看
        C = "Answer is: "
    else: 
        # print("else")
        C = ""

    if isfloat(A) and isfloat(B):                           # 防呆，判斷輸入的是否為數字(含浮點數)，若輸入文字則報錯
        var1 = float(A)                                     # 把 "字串" 轉成 "浮點數"，才能做數值運算
        var2 = float(B)
        if ui.radioButton_1.isChecked(): 
            ans = var1 + var2                               # .setText()只能吃一個變數，所以要用+號連接字串，把兩個字串黏成一個字串。不能用逗號,分隔，會變成有兩個變數，.setText()吃不進去。
        elif ui.radioButton_2.isChecked(): 
            ans = round((var1 - var2),3)
        elif ui.radioButton_3.isChecked(): 
            ans = var1 * var2
        elif ui.radioButton_4.isChecked(): 
            ans = round((var1 / var2),3)
        ui.result.setText(C + str(ans))

        return ans                                          # 加一個return把答案丟出去，就可以讓別的def自定義函式拿去用了~~~ 

    else: 
        message = QMessageBox()
        message.setWindowTitle("ERROR!!!!!!!!")
        message.setInformativeText("Please enter numbers!") # 不知為何視窗跳出就是會自動換行，無法把視窗變寬，峰峰也無解...
        message.exec_()

"""
★ 上面 def radio_calculate() 的另一種做法，可以用 "反判斷" → 先判斷 "若不是float" 則出現錯誤訊息，然後再做數值運算
反判斷的好處是，不需要 if 裡面再包 if ，而是同一個階層的 if 一直做下去，就不會有太多階層

    if not isfloat(A) or not isfloat(B): 
        message = QMessageBox()
        message.setWindowTitle("ERROR!!!!!!!!")
        message.setInformativeText("Please enter numbers!") 
        message.exec_()
        return
    if ui.radioButton.isChecked(): 
        ans = float(A) + float(B)
        ui.result.setText(str(ans))
"""

def click_combo(): 
    ui.result.setText("see terminal")
    print(ui.animalComboBox.currentText())                  # .currentText() 可以查看comboBox下拉式選單的文字內容
    print(ui.animalComboBox.currentIndex())                 # .currentIndex() 可以查看comboBox下拉式選單的list順序

def Hslider_change():                                       # ◇◇◇ 設定拉霸移動時的執行動作
    x = ui.horizontalSlider.value()
    print("change value is " + str(x))

def Hslider_release():                                      # ◇◇◇ "放開"拉霸時出現一個文字訊息
        message = QMessageBox()
        message.setWindowTitle("Aha~~")
        message.setInformativeText("選擇的數值是" + str(ui.horizontalSlider.value()))
        message.exec_()

def Vslider_change(): 
    x = ui.verticalSlider.value()
    ui.progressBar4vertical.setValue(x)

def Vslider_release(): 
    x = ui.verticalSlider.value()
    ui.progressBar4vertical.setValue(x)
    print(x)                                                # 用print確認一下slider的value到底是多少
    try: 
        ans = radio_calculate()                             # 你要使用別的def函式return丟出來的東西時，要做 "呼叫函式" 的動作。radio_calculate()
        ui.result.setText(str(round((ans * x), 3)))
    except: 
        pass




app = QApplication(sys.argv)                                # 這是固定格式，所有QT程式第一行一定要有這個，不然會報錯
widge = QWidget()                                           # 等等要把剛剛設計好的dialog放到widge裡面

# 以下三行是用qtlinguest多國語言轉換，記得要放在 ui.setupUi(widge) 前面!!!!!
t = QTranslator()                                           # 用 t 去抓 class QTranslator
t.load("chinese.qm")                                        # t.load 把 qm檔 讀取進來
app.installTranslator(t)                                    # 安裝轉譯器
# 以上三行是用qtlinguest多國語言轉換，記得要放在 ui.setupUi(widge) 前面!!!!!

ui = Ui_Dialog()                                            # Ui_Dialog是剛剛import進來的其中一個class
ui.setupUi(widge)





ui.addButton.clicked.connect(clicked_add)                   # ★★★ 設定點擊按鈕的動作 ★★★
ui.pic.mouseReleaseEvent = click_pucture                    # ★★★ 設定點擊圖片的動作 ★★★  有分 "點下去" 和 "放開" 兩種動作~~ 
""" ★★★
在Qt Designer裡面, 若Radio Button沒有勾選 "autoExclusive" (在QAbstractButton底下), 則 Radio Button 彼此間不會互斥。（可重複勾選）
此時可在python內用group的方式, 把同組的radio button全部包成一個群組, 則群組內的所有 radio button就都會彼此互斥。★★★
"""
group1 = QButtonGroup(widge)                                # QButtonGroup(widge) 先建立一個群組
group1.addButton(ui.radioButton_1)                          # .addButton(你的按鈕) 再把 radio button 一個個丟到群組內，讓所有radio button都互斥
group1.addButton(ui.radioButton_2)
group1.addButton(ui.radioButton_3)
group1.addButton(ui.radioButton_4)
ui.radioButton_1.clicked.connect(click_radio)               # ★★★ 設定點選radio button的動作 ★★★
ui.clickMeButton.clicked.connect(check_radio)               # ◇◇◇ 確認radio button是否點選。設一個 def 並透過點選click me按鈕的動作來確認

ui.clickMeButton.clicked.connect(radio_calculate)
ui.radioButton_1.clicked.connect(radio_calculate)
ui.radioButton_2.clicked.connect(radio_calculate)
ui.radioButton_3.clicked.connect(radio_calculate)
ui.radioButton_4.clicked.connect(radio_calculate)

ui.animalComboBox.addItems(["Cat", "Dog", "Tiger", "Lion"]) # comboBox下拉式選單，.addItems([ ]) 用 list 的概念去新增選單內容。
ui.comboButton.clicked.connect(click_combo)
ui.languageComboBox.addItems(["(Select language)", "中文", "English"])

ui.progressBar.setMaximum(100)                              # ◇◇◇ 設定進度條的最大值
ui.progressBar.setMinimum(0)                                # 設定進度條的最小值
ui.progressBar.setValue(3)                                  # 設定進度條的起始值
ui.horizontalSlider.setMaximum(110)                         # ◇◇◇ 設定拉霸的最大值
ui.horizontalSlider.setMinimum(-3)                          # 設定拉霸的最小值
ui.horizontalSlider.valueChanged.connect(Hslider_change)    # 移動拉霸時call back function指定執行動作
ui.horizontalSlider.sliderReleased.connect(Hslider_release) # ◇◇◇ "放開"拉霸時的的指定執行動作

ui.progressBar4vertical.setMaximum(100)
ui.progressBar4vertical.setMinimum(0)                       # ★☆★☆★ 看下一行setValue的註解，這邊如果設定min為1，整個比例會大錯特錯！
ui.progressBar4vertical.setValue(1)                         # ★☆★☆★ 這個是"比例"，不是單一值！  value = (x-min)/(max-min)  *100%
ui.verticalSlider.setMaximum(100)
ui.verticalSlider.setMinimum(1)
ui.verticalSlider.valueChanged.connect(Vslider_change)
ui.verticalSlider.sliderReleased.connect(Vslider_release) 



widge.show()
sys.exit(app.exec_())                                       # 執行以上所有UI的畫面


# 以上都是固定格式，其實不需要記~ 重點是我們後面要去設定press bottom

