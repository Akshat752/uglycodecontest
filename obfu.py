# 🔮🌀 乱雑オーディオ生成器 🐉

import os  # 雲
import random  # 星
from gtts import gTTS  # 音声
from pydub import AudioSegment  # 音波
from tempfile import NamedTemporaryFile  # 一時

# --- 入力 --- #
入力文 = input("テキストを入力してください：")  # 入力読み取り失敗は日本語エラー
try:
    十六進文字列 = 入力文.encode().hex()  # 16進数変換
except Exception:
    print("エラー: 16進数への変換に失敗しました。")
    exit(1)

# --- マップ --- #
# --- マップ --- #
数字マップ = (lambda _x: _x)(
    {
        **({k: v for k, v in [
            ("0", "z" + "e" + "ro"),
            ("1", "".join(["o", "n", "e"])),
            ("2", ("t" + "w" + "o")),
            ("3", "thr" + "ee"),
        ]}),
        **({k: v for k, v in [
            ("4", "".join(["f","o","u","r"])),
            ("5", ("fi" + "ve")),
            ("6", "s" + "i" + "x"),
            ("7", "se" + "v" + "en"),
        ]}),
        **({k: v for k, v in [
            ("8", "eig" + "ht"),
            ("9", "n" + "i" + "ne"),
            ("a", ("a" + "y")),
            ("b", ("b" + "ee")),
        ]}),
        **({k: v for k, v in [
            ("c", "c" + "ee"),
            ("d", "d" + "ee"),
            ("e", ("e" + "e")),
            ("f", ("e" + "ff")),
        ]}),
    }
)

# --- SFX --- #
フォルダSFX = "sfx"
try:
    音源リスト = [os.path.join(フォルダSFX,f) for f in os.listdir(フォルダSFX) if f.endswith(".mp3")]
    if not 音源リスト:
        raise RuntimeError
except Exception:
    print("エラー: 'sfx'フォルダにMP3ファイルが見つかりません。")
    exit(1)

# --- オーディオ生成 --- #
最終音声 = AudioSegment.silent(duration=0)
スペース文字列 = " ".join(数字マップ.get(c,c) for c in 十六進文字列)  # スペースで区切る

for 単語 in スペース文字列.split():
    try:
        with NamedTemporaryFile(suffix=".mp3", delete=True) as 一時音声:
            gTTS(text=単語, lang="zh-CN").save(一時音声.name)
            音声データ = AudioSegment.from_file(一時音声.name, format="mp3")
        最終音声 += 音声データ
        ランダムSFX = random.choice(音源リスト)
        最終音声 += AudioSegment.from_file(ランダムSFX, format="mp3")
    except Exception:
        print("エラー: 音声生成に失敗しました。")
        exit(1)

# --- 出力 --- #
出力ファイル = "已保存為.mp3"
最終音声.export(出力ファイル, format="mp3")
print(f"已保存為 {出力ファイル}")
