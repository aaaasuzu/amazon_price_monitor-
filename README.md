# amazon_price_monitor-
Amazon Price Monitor
概要
Amazon商品の価格を定期的に監視し、入力した価格以下になった場合にDiscordへ通知するWebアプリです。

使用技術
Python
Flask
Selenium
Requests
Discord Webhook
Git / GitHub

主な機能
商品URL登録
目標価格設定
現在価格取得
Discord通知
複数商品の監視
Web画面から管理
システム構成

ユーザー
↓
Flask Webアプリ
↓
Selenium
↓
Amazon商品ページ
↓
価格取得
↓
Discord通知

工夫した点
Seleniumを利用して動的ページから価格を取得
Discord Webhookを利用した通知機能を実装
Flaskを用いてWebアプリ化
関数ごとにファイル分割し保守性を向上

今後の改善予定
SQLiteによるデータ保存
ログイン機能
価格推移グラフ表示

作成者

GitHub:
https://github.com/aaaasuzu
