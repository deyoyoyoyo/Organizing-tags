# Organizing-tags

## config.json
`config.json` には以下の設定を行います。

- `folder_path`: キャプションファイルの格納フォルダを指定します。
- `first_tags`: 先頭に持ってきたいタグを指定します（例: `eyes` の指定で `blue eyes` などの `eyes` を含むタグを指定可能）。
- `last_tags`: 後方に持ってきたいタグを指定します。
- `add_tags`: 追加したいタグを指定します。
- `remove_tags`: 削除したいタグを指定します。
- `extensions`: キャプションファイルの拡張子を指定します。

## 起動方法
`config.json` の設定が終わったら、`/Organizing-tags` 下でターミナルを起動し、以下のコマンドでスクリプトを実行します。

```bash
python .\Organizing_tags.py
