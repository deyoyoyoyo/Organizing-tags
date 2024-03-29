# Organizing Tags GUI

Organizing Tags GUIは、キャプションファイルのタグを整理するための簡単なユーザーインターフェースを提供するツールです。このツールを使用することで、ファイルにタグを追加、削除し、整理することができます。

## インストール

特別なインストールは必要ありません。Python 3.xをインストールしてください。

ターミナルを開き任意のフォルダで下記コマンドを実行してください。
```
git pull https://github.com/deyoyoyoyo/Organizing-tags.git
```
## 使い方

1. Organizing_tags_GUI.batをダブルクリックしてアプリケーションを起動します。

2. フォルダーパスを入力します。整理したいファイルが含まれているフォルダーのパスを指定します。

3. キャプションファイルの拡張子を入力します。整理したいファイルの拡張子をカンマ区切りで入力します。例: `.txt, .caption`

4. "Load Config"ボタンを押下しすると、前回の設定を呼び出せます。

5. "Load tag"ボタンを押下して指定したパス下にあるキャプションファイル内のタグを取得します。

6. タグ一覧が表示されます。
   
7. キャプションの先頭に移動させたいタグを"先頭タグ"、キャプションの後方に移動させたいタグを"後方タグ"、
   追加したいタグを"追加タグ"、削除したいタグを"削除タグ"を入力します。各タグはカンマ区切りで入力します。
   "先頭タグ"、"後方タグ"の優先順位は入力順になります。

8. "Save Config"ボタンを押下してください。

9. "実行"ボタンをクリックしてタグを整理します。

10. ログエリアに実行結果が表示されます。

## 設定の保存と読み込み

- "Save Config"ボタンをクリックして、現在の設定を保存できます。設定は`config.json`ファイルに保存されます。

- "Load Config"ボタンをクリックして、以前に保存した設定を読み込むことができます。

## タグの検索と設定

- タグ一覧の上にあるタグ検索を用いることでキャプションファイル内のタグを検索できます。

- 大文字・小文字を区別せずに部分一致でタグを検索できます。

- タグ一覧からドラックアンドドロップでタグを設定できます。

## 注意事項

- このツールを使用する前に、フォルダーパスと拡張子を正確に入力してください。

- タグはカンマ区切りで入力し、スペースを含めないでください。

- タグを削除する場合、削除したいタグを "削除タグ" フィールドに入力します。

- タグはファイルに追加、削除され、結果がタグ一覧に表示されます。

- タグが正しく整理されたことを確認するために、タグ一覧を確認してください。

## ライセンス

このアプリケーションはMITライセンスのもとで提供されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。
