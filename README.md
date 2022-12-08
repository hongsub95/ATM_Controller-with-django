# ATM_Controller-with-django

virtualenv : poetry\
web-framework : django


# About project
#### 목적 : django를 이용하여 기본적인 ATM 및 transaction의 흐름 익히기

db_model : AccountInfo(계좌정보), CardInfo(카드정보), Transaction(트랜잭션)\
Account_schema : account_number(계좌번호), balance(현재잔액)\
Card_schema : Account_id, name(사용자이름), card_number(카드번호), Pin(핀넘버), phone_number(사용자 전화번호)\
transaction_schema : Transaction_type(트랜잭션 종류),transaction_status(트랜잭션 성공여부),card_id,date(트랜잭션한 날짜)

## Have to do 
### 1.Insert Card [o] 
이 부분은 2번으로 대체 (atm기계처럼 카드를 직접 넣을 수 없으니, 단순 카드번호와 pin번호 확인으로 대체)
### 2. Check Card number and PIN number (valid or not) [o]
card number와 pin number를 확인 후 session에 card number를 저장 (카드를 빼면 session에서 삭제)
### 3. Select transaction(Balance/Deposit/Withdraw/transfer) [o] 
트랜잭션이 잘 이루어져 있는지 확인 (현재 transaction status는 complete밖에 구현 못했음)
### 4. Balance Inquiry, Deposit view, Withdraw view, Transfer view [o]
데코레이터 user_authenticate를 만들어 card_number가 저장되어 있는 session에 접근하여 card_number에 해당하는 card 쿼리셋을 가져와서\
balance inquiry(잔액조회), deposit(입금), withdraw(인출), transfer(송금) 구현














