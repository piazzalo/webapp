"""
高醫 學士後醫學系 歷屆試題下載腳本
下載後自動命名為：高醫-{年分}-{解答/英文/物化/生生}.pdf
使用方式：python kmu_exam_downloader.py
"""

import urllib.request
import os
import time

OUTPUT_DIR = "高醫試題"

# 已確認的公告 ID（bac 編號）對應學年度
# 格式：(學年度, bac_id, id推測)
YEARS = [
    (98,  37,   False),
    (99,  53,   False),
    (100, 68,   False),
    (101, 79,   False),
    (102, 95,   False),
    (103, 111,  False),
    (104, 124,  False),
    (105, 140,  False),
    (106, 155,  False),
    (107, 168,  False),
    (108, 176,  False),
    (109, 187,  False),
    (110, 200,  False),
    (111, 208,  False),
    (112, 216,  False),
    (113, 227,  False),
    (114, 237,  False),
    (115, 246,  False),
]

# 各年的科目檔案索引
# 108年起：生生=_1, 物化=_2, 英文=_4, 解答=_5
# 107年以前：英文=_1, 物化=_2, 生生=_3, 解答=_4
def get_subjects(yr, bac):
    base = f"https://enr.kmu.edu.tw/yamgetdocbef.php?bno=bac,{bac}&at=bac{bac}"
    if yr >= 110:
        return [
            (f"{base}_1.pdf", f"高醫-{yr}-生生.pdf"),
            (f"{base}_2.pdf", f"高醫-{yr}-物化.pdf"),
            (f"{base}_4.pdf", f"高醫-{yr}-英文.pdf"),
            (f"{base}_5.pdf", f"高醫-{yr}-解答.pdf"),
        ]
    elif yr == 109:
        return [
            (f"{base}_1.pdf", f"高醫-{yr}-英文.pdf"),
            (f"{base}_2.pdf", f"高醫-{yr}-物化.pdf"),
            (f"{base}_4.pdf", f"高醫-{yr}-生生.pdf"),
            (f"{base}_5.pdf", f"高醫-{yr}-解答.pdf"),
        ]
    elif yr == 98:
        return [
            (f"{base}_1.pdf", f"高醫-{yr}-物化.pdf"),
            (f"{base}_2.pdf", f"高醫-{yr}-英文.pdf"),
            (f"{base}_4.pdf", f"高醫-{yr}-生生.pdf"),
            (f"{base}_5.pdf", f"高醫-{yr}-解答.pdf"),
        ]
    elif yr == 99 or yr == 100:
        return [
            (f"{base}_1.pdf", f"高醫-{yr}-解答.pdf"),
            (f"{base}_2.pdf", f"高醫-{yr}-物化.pdf"),
            (f"{base}_3.pdf", f"高醫-{yr}-生生.pdf"),
            (f"{base}_4.pdf", f"高醫-{yr}-英文.pdf"),
        ]
    else:
        return [
            (f"{base}_1.pdf", f"高醫-{yr}-英文.pdf"),
            (f"{base}_2.pdf", f"高醫-{yr}-物化.pdf"),
            (f"{base}_3.pdf", f"高醫-{yr}-生生.pdf"),
            (f"{base}_4.pdf", f"高醫-{yr}-解答.pdf"),
        ]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://enr.kmu.edu.tw/",
}

def download_file(url, save_path):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                return False, f"HTTP {resp.status}"
            content = resp.read()
            # 確認是 PDF（以 %PDF 開頭）
            if not content.startswith(b"%PDF"):
                return False, "非 PDF 檔案（可能連結錯誤）"
            with open(save_path, "wb") as f:
                f.write(content)
            return True, f"{len(content)//1024} KB"
    except Exception as e:
        return False, str(e)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\n{'='*55}")
    print(f"  高醫 學士後醫學系 歷屆試題下載")
    print(f"  儲存位置：{os.path.abspath(OUTPUT_DIR)}")
    print(f"{'='*55}\n")

    ok_count = 0
    fail_count = 0
    skip_count = 0
    failures = []

    for yr, bac, guessed in YEARS:
        if bac is None:
            print(f"[{yr}] ⚠  跳過（網站未提供此年試題）")
            skip_count += 1
            continue

        tag = "（推測ID）" if guessed else ""
        print(f"\n[{yr} 學年度] bac={bac} {tag}")

        for url, fname in get_subjects(yr, bac):
            save_path = os.path.join(OUTPUT_DIR, fname)
            if os.path.exists(save_path):
                print(f"  ✓ 已存在，跳過：{fname}")
                ok_count += 1
                continue

            print(f"  下載中：{fname} ... ", end="", flush=True)
            ok, info = download_file(url, save_path)
            if ok:
                print(f"✓ ({info})")
                ok_count += 1
            else:
                print(f"✗ 失敗：{info}")
                fail_count += 1
                failures.append((yr, fname, info))

            time.sleep(0.5)  # 避免請求太頻繁

    print(f"\n{'='*55}")
    print(f"  完成！成功：{ok_count}  失敗：{fail_count}  跳過：{skip_count}")
    if failures:
        print(f"\n  失敗清單：")
        for yr, fname, reason in failures:
            print(f"    [{yr}] {fname} — {reason}")
        print(f"\n  提示：推測 ID 的年份連結可能不正確，")
        print(f"  請到 https://enr.kmu.edu.tw/index.php")
        print(f"  選「學士後醫學系招生」+標題輸入「試題」查詢正確連結。")
    print(f"{'='*55}\n")

if __name__ == "__main__":
    main()
