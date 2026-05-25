# CLAUDE.md

このファイルは、本リポジトリを扱うAIアシスタント向けのガイドラインを提供します。

## プロジェクト概要

Yahoo Finance からS&P 500の過去1年分のデータを取得し、ローソク足チャートをPNGファイルとして保存するシンプルなPythonユーティリティです。

## リポジトリ構成

```
Jules-test/
├── generate_chart.py   # メインスクリプト（単一エントリーポイント）
├── requirements.txt    # Python依存パッケージ（yfinance、mplfinance）
├── .gitignore          # *.png および __pycache__ を除外
└── CLAUDE.md           # このファイル
```

サブディレクトリなし、パッケージ構成なし、テストスイートなし。

## 技術スタック

- **言語:** Python 3
- **`yfinance`** — Yahoo Finance からOHLCV（始値・高値・安値・終値・出来高）データを取得
- **`mplfinance`** — 出来高パネル付きローソク足チャートを描画

## セットアップと実行方法

```bash
# 依存パッケージのインストール（仮想環境推奨）
pip install -r requirements.txt

# スクリプトの実行
python3 generate_chart.py
```

**出力:** カレントディレクトリに `sp500_chart.png` が生成されます（git管理外）。成功時は日本語のメッセージが表示され、データ取得失敗時（休日・週末など）はエラーメッセージが表示されます。

## コード規約

- **単一関数設計:** すべてのロジックを `generate_sp500_chart()` にまとめ、標準の `if __name__ == "__main__"` ガードを使用する。
- **snake_case** を識別子に使用する。
- **インラインコメントは日本語** — コードを追加する際もこのスタイルを維持する。
- **クラス・モジュール分割なし** — スコープが明確に必要とする場合を除き、単一ファイルのフラット構成を保つ。
- **テストなし** — 明示的に依頼されない限り、テストフレームワークを導入しない。
- **リンター設定なし** — PEP 8 を手動で遵守し、`.flake8` や `black` 等のツールを依頼なく導入しない。

## チャートパラメータ（generate_chart.py）

| パラメータ | 値 | 備考 |
|-----------|-----|------|
| ティッカー | `^GSPC` | S&P 500 指数 |
| 期間 | `datetime.date.today()` から過去365日 | 固定ルックバック |
| チャート種別 | `candle` | mplfinanceのローソク足 |
| スタイル | `charles` | mplfinance組み込みテーマ |
| 出力ファイル | `sp500_chart.png` | 実行のたびに上書き |

## 開発ブランチ

開発は `claude/claude-md-docs-J8gcV` ブランチで行います。リモートは GitHub の `raikinno/Jules-test` です。

## よくある変更作業

**ティッカーの変更:** `generate_sp500_chart()` 内の `ticker_symbol` を更新する。

**取得期間の変更:** `datetime.timedelta(days=365)` のオフセット、および `start_date` / `end_date` 変数を更新する。

**出力ファイル名の変更:** `mpf.plot(...)` の `savefig` 引数を更新する。

**チャートスタイルの変更:** `style` パラメータに別の文字列を渡す。利用可能なスタイルは `mpf.available_styles()` で確認できる。
