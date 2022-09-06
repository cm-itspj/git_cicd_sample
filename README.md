# git_sample
Git練習用リポジトリ

## 準備
1. Git クローン  
```
git clone https://github.com/cm-itspj/git_cicd_sample.git

cd git_cicd_sample 
```

2. Python 仮想環境設定
```
python -m venv myvenv
source myvenv/bin/activate

pip install -r requirements.txt
```

3. .envファイル作成
```
touch .env
echo "SECRET_KEY='xxxx'" >> .env 
echo "DEBUG=True" >> .env
```

4. サーバ起動
```
python manage.py migrate
python manage.py runserver
```
