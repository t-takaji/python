# Python作業メモ

## .py → .exe化
### 前提
pyinstallerのインストールが必要なので下記コマンドを実行。

`pip install pyinstaller`  

※pipのバージョン20.3.3欲しいので足りない場合は、バージョンアップを行う。  
`pip install --upgrade pip`  

### 実行コマンド
`pyinstaller hello.py --onefile`  

実行すると、buildとdistというフォルダが作成される。  
distフォルダ内にhello.exeがあることが確認できる。  
