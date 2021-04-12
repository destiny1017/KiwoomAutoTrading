from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *

class Kiwoom(QAxWidget):

    def __init__(self):
        super().__init__()
        print("키움클래스")

        ####### event loop 모음
        self.login_event_loop = None
        #######################

        ####### 변수 모음
        self.account_num = None
        #######################

        self.get_ocx_instance()
        self.event_slots()
        self.signal_login_commConnect()

        self.get_account_info()
        self.detail_account_info()

    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1") # 상속받은 QAxWidget 클래스의 메서드. 응용프로그램을 제어할 수 있게 해줌.

    def event_slots(self):
        self.OnEventConnect.connect(self.login_slot) # 로그인 처리 이벤트
        self.OnReceiveTrData(self.trdata_slot) # TR 요청 이벤트

    def login_slot(self, errCode):
        print(errors(errCode))
        self.login_event_loop.exit() # 로그인이 완료되면 이벤트루프 종료

    def signal_login_commConnect(self):
        self.dynamicCall("commConnect()") # 로그인창 호출

        self.login_event_loop = QEventLoop() # 로그인 이벤트 루프 생성
        self.login_event_loop.exec_() # 종료 방지

    def get_account_info(self):
        account_list = self.dynamicCall("GetLoginInfo(String)", "ACCNO") # 계정정보 중 ACCNO(계좌리스트) 가져오기
        self.account_num = account_list.split(";")[0] # 계좌 리스트는 세마콜론으로 구분된 String으로 옴
        print("내 계좌번호 : %s" % self.account_num)
        
    def detail_account_info(self):
        print("예수금 가져오는 부분")
        self.dynamicCall("SetInputValue(String, String)", "계좌번호", self.account_num)
        self.dynamicCall("SetInputValue(String, String)", "비밀번호", "0000")
        self.dynamicCall("SetInputValue(String, String)", "비밀번호입력매체구분", "00")
        self.dynamicCall("SetInputValue(String, String)", "조회구분", "2")
        self.dynamicCall("CommRqData(String, String, int, String)", "예수금상세현황요청", "opw00001", "0", "2000")