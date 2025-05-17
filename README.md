# kokoro-python-test

Kokoro TTS（Text-to-Speech）モデルを使用した音声合成のテストプロジェクトです。

## 概要

このプロジェクトは、軽量ながら高品質な音声合成を実現するKokoro TTSモデルを使用したテスト環境です。Kokoroは8200万パラメータを持つオープンウェイトのTTSモデルで、Apacheライセンスの下で利用可能です。

## 機能

- 日本語、英語、中国語、スペイン語、フランス語、ヒンディー語、イタリア語、ポルトガル語（ブラジル）など、複数の言語に対応
- 高品質な音声合成
- 軽量なアーキテクチャによる高速な処理
- カスタマイズ可能な音声パラメータ（速度など）

## 環境要件

- Python 3.11
- uv (高速なPythonパッケージインストーラー)
- 必要なパッケージは `requirements.txt` に記載

## インストール方法

1. リポジトリをクローン
```bash
git clone https://github.com/yourusername/kokoro-python-test.git
cd kokoro-python-test
```

2. uvのインストール（まだインストールされていない場合）
```bash
# Windows (PowerShell)
curl -LsSf https://astral.sh/uv/install.ps1 | powershell

# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. 仮想環境の作成と有効化
```bash
# 仮想環境の作成
uv venv .venv

# 仮想環境の有効化
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# Linux/macOS
source .venv/bin/activate
```

4. 依存パッケージのインストール
```bash
uv pip install -r requirements.txt
```

5. 日本語音声合成用の追加パッケージ（必要な場合）
```bash
uv pip install misaki[ja]
python -m unidic download
```

## 使用方法

1. `sample.py` を実行して音声合成をテスト
```bash
python sample.py
```

2. カスタマイズ
- `sample.py` 内の `lang_code` パラメータで言語を選択
- `voice` パラメータで音声を選択
- `speed` パラメータで音声の速度を調整
- `text` 変数に合成したいテキストを入力

## 利用可能な言語コード

- 🇯🇵 'j' - 日本語
- 🇺🇸 'a' - アメリカ英語
- 🇬🇧 'b' - イギリス英語
- 🇪🇸 'e' - スペイン語
- 🇫🇷 'f' - フランス語
- 🇮🇳 'h' - ヒンディー語
- 🇮🇹 'i' - イタリア語
- 🇧🇷 'p' - ブラジルポルトガル語
- 🇨🇳 'z' - 中国語（北京語）

## 注意事項

- 日本語音声合成を使用する場合は、`misaki[ja]` パッケージのインストールが必要です
- 中国語音声合成を使用する場合は、`misaki[zh]` パッケージのインストールが必要です

## ライセンス

このプロジェクトは Apache License 2.0 の下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 関連プロジェクト

- [Kokoro TTS](https://github.com/yourusername/kokoro) - メインのKokoro TTSプロジェクト