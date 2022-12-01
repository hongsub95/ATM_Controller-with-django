# ATM_Controller-with-django


virtualenv : poetry\
web-framework : django

Have to do :\
[o] Insert Card  => click Insert card \
[o] Select Account + PIN number  => Check Card number and PIN number (valid or not)\
[o] Select transaction(Balance/Deposit/Withdraw) \
[o] Balance Inquiry, Deposit view, Withdraw view


db_model : AccountInfo(계좌정보), CardInfo(카드정보)\
Account_schema : account_number(계좌번호), balance(현재잔액)\
Card_chema : Account_id, name(사용자이름), card_number(카드번호), Pin(핀넘버), phone_number(사용자 전화번호)

# start project

1. install poetry\
(if your os is Linux,mac,WSL)\
curl -sSL https://install.python-poetry.org | python3 - \
command "poetry init" (enter,enter,enter,enter,"MIT",enter,no,no,yes)
2. install django\
poetry add django
3. python manage.py makemigrations
4. python manage.py migrate\
If you want initial data, command "python manage.py loaddata initial_data" (It reads initial_data.json)
5. python manage.py runserver

# Homepage
![1](https://user-images.githubusercontent.com/75579601/205030845-f13c5f9c-71f1-4fb8-adfc-8b2bd90bb251.png)
#### click 'insert card'

# Check card number and Pin number
![2](https://user-images.githubusercontent.com/75579601/205031562-e3bb4418-1a93-42d0-a224-615714bf2a64.png)
![image](https://user-images.githubusercontent.com/75579601/205031780-d6866d8e-aae8-4fcd-926b-2228a0e52c5e.png)
![3](https://user-images.githubusercontent.com/75579601/205031616-6898e49d-e325-4438-ae4e-f4e27a6cc5a9.png)

# Select transaction(balance,deposit,withdraw)
![4-1](https://user-images.githubusercontent.com/75579601/205032023-584669b0-befb-42da-88f6-25971cdb16df.png)
![4-2](https://user-images.githubusercontent.com/75579601/205032036-06e7a92f-30ae-4fd1-9bb8-8c8779f55c02.png)
![4-3](https://user-images.githubusercontent.com/75579601/205032047-3ae7af2e-887d-4924-bede-77f3628463f8.png)

# Balance Inquiry
![5](https://user-images.githubusercontent.com/75579601/205032243-5c4ee60b-80ee-4ea9-b8fb-002f7fb81009.png)

# Deposit
![image](https://user-images.githubusercontent.com/75579601/205032496-05de17a9-7ddf-415a-980d-0daf44795b8d.png)
![image](https://user-images.githubusercontent.com/75579601/205032573-a22c1ff0-715a-48cc-80d9-7e6b2febe663.png)

# Withdraw
![image](https://user-images.githubusercontent.com/75579601/205032659-07178825-d032-4d3e-b36e-74d6f880b485.png)
![image](https://user-images.githubusercontent.com/75579601/205032732-633e1485-14a4-445f-9ad7-fe4fb87a56ca.png)
![image](https://user-images.githubusercontent.com/75579601/205032813-f2488c97-48e2-423d-8fa1-370d09172584.png)

<h2>If you click "Remove the card", you get homepage</h2>






