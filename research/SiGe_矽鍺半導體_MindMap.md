# SiGe（矽鍺）半導體技術 Mind Map

```
SiGe 矽鍺半導體
│
├── 1. 基礎材料科學
│   ├── 什麼是 SiGe？
│   │   ├── Si₁₋ₓGeₓ 合金（Ge 比例通常 10~35%）
│   │   ├── 矽晶格常數 5.43 Å vs 鍺 5.66 Å（差 4.2%）
│   │   └── 薄膜生長在 Si 上 → 產生「壓縮應變」(Compressive Strain)
│   │
│   ├── 能隙工程（Bandgap Engineering）
│   │   ├── 純 Si：1.12 eV ／ 純 Ge：0.67 eV
│   │   ├── Si₀.₇Ge₀.₃：約 0.85~0.95 eV
│   │   └── 能帶偏移不對稱 → 價帶大幅上移 → HBT 高增益的關鍵
│   │
│   └── HBT 電晶體結構
│       ├── 射極（Emitter）：n+ 多晶矽
│       ├── 基極（Base）：p 型應變 SiGe（10~30 nm）← 核心層
│       ├── 集極（Collector）：n 型 Si
│       └── Ge 濃度梯度 → 內建電場 → 載子加速 → 超高速
│
├── 2. 革新意義與競爭優勢
│   │
│   ├── vs. 純矽 CMOS
│   │   ├── 載子遷移率高 2~3 倍
│   │   ├── fT/fmax：CMOS ~100-200 GHz vs SiGe 300~720 GHz
│   │   ├── 40 GHz 雜訊指數：CMOS 3-5 dB vs SiGe ~1.3 dB
│   │   └── 可與 CMOS 單晶片整合（BiCMOS）
│   │
│   ├── vs. 化合物半導體 III-V
│   │   ├── GaAs HBT：高功率 PA，但晶圓小（6 吋），無法整合 CMOS
│   │   ├── InP HBT：頻率最高（>500 GHz），但極貴、晶圓僅 4 吋
│   │   ├── GaN HEMT：超高功率，主導基站 PA 與雷達發射端
│   │   └── SiGe 優勢：300 mm 矽晶圓 + 低成本 + 整合度最高
│   │
│   └── SiGe 的獨特定位
│       ├── 化合物半導體的射頻性能
│       ├── 矽製程的規模與成本
│       └── BiCMOS：RF 類比 + 數位邏輯 → 單晶片 SoC
│
├── 3. 主要應用
│   │
│   ├── 5G / mmWave 通訊
│   │   ├── 5G 手機 LNA、混波器、VCO
│   │   ├── 5G mmWave（24~47 GHz）相控陣波束賦形晶片
│   │   └── 6G 候選技術（100~300 GHz sub-THz）
│   │
│   ├── 汽車雷達（最快成長）
│   │   ├── 24 GHz 近程雷達
│   │   ├── 77/79 GHz ADAS 長程雷達
│   │   └── 每輛 L3+ 自駕車需 4~6 組雷達 SoC
│   │
│   ├── 光通訊（數據中心）
│   │   ├── 400G/800G 光收發器
│   │   ├── TIA（跨阻放大器）、雷射驅動器、SerDes
│   │   └── 每個 AI 訓練叢集依賴大量高速光互連
│   │
│   ├── 衛星通訊（LEO）
│   │   ├── Ka/Ku-band 相控陣（Starlink、Kuiper）
│   │   └── 高量需求 → SiGe 成本優勢凸顯
│   │
│   ├── 量子電腦（最熱門新興）
│   │   ├── Si/SiGe 異質結構 → 量子阱 → 自旋量子位元
│   │   ├── 2025 年：>99% 單/雙位元閘保真度（Nature）
│   │   ├── Intel Tunnel Falls：300 mm EUV 製程 12 量子點陣列
│   │   └── 可在現有矽晶圓廠量產 → 量子擴展的最佳路徑
│   │
│   └── 航太/國防
│       ├── 天然抗輻射（Total Ionizing Dose > 3 Mrad）
│       └── 雷達、電子戰、衛星電子系統
│
├── 4. 技術現況（2025）
│   │
│   ├── 速度紀錄
│   │   ├── IHP SG13G3Cu：fT/fmax = 470/650 GHz（室溫，量產製程）
│   │   ├── 史上最高：505/720 GHz（研究級 HBT）
│   │   └── 低溫（4.5 K）：IBM 實驗室 fmax ~798 GHz
│   │
│   ├── 主要製程平台
│   │   ├── IHP SG13G2：350/450 GHz，開源 PDK
│   │   ├── IHP SG13G3Cu：470/650 GHz，最快量產製程
│   │   ├── GlobalFoundries 130CBIC：NPN >400 GHz（2025 新發布）
│   │   ├── GF 9HP：310/370 GHz，90 nm CMOS，國防用
│   │   ├── STMicro 55nm BiCMOS：fmax ~600 GHz + 55nm CMOS
│   │   └── Tower SiGe BiCMOS：340/450 GHz
│   │
│   └── 光子學整合
│       ├── IHP SG25H5_EPIC：140 GHz 電吸收調制器 + 200 GHz 光偵測器
│       └── Ge-on-Si 波導光偵測器：265 GHz 頻寬（Nature Photonics）
│
├── 5. 主要公司研究進展
│   │
│   ├── 研究機構
│   │   └── IHP（德國萊布尼茲）
│   │       ├── 全球 SiGe 速度紀錄保持者
│   │       ├── 開源 SG13G2 PDK（OpenRule1um）
│   │       ├── X-FAB 技術授權 → 歐洲量產
│   │       └── 2024 Tatsuo Itoh Award（PA for 6G）
│   │
│   ├── 晶圓代工廠
│   │   ├── GlobalFoundries
│   │   │   ├── 承接 IBM SiGe 製程遺產（2015 收購）
│   │   │   ├── 2025.08 發布 130CBIC（NPN >400 GHz，含 PNP）
│   │   │   └── 差異化晶圓廠策略：不與台積電拼先進製程
│   │   │
│   │   ├── STMicroelectronics
│   │   │   ├── 55nm BiCMOS + fmax 600 GHz（業界最先進 CMOS+SiGe）
│   │   │   └── 汽車雷達晶片（77 GHz，與 Bosch 合作）
│   │   │
│   │   └── Tower Semiconductor
│   │       ├── SiGe BiCMOS：340/450 GHz
│   │       ├── SiGe Terabit Platform（最新）
│   │       └── 2024 擴入 Intel Rio Rancho 廠產能
│   │
│   ├── 晶片設計/產品公司
│   │   ├── IBM Research
│   │   │   ├── SiGe HBT 發明者（1980s）
│   │   │   ├── 低溫量子電腦讀出電路研究
│   │   │   └── 基礎專利持有者
│   │   │
│   │   ├── Infineon
│   │   │   ├── 24/60/77 GHz 汽車雷達 SoC
│   │   │   └── 汽車雷達市場份額 >45%（與 NXP 合計）
│   │   │
│   │   ├── Intel（量子）
│   │   │   ├── Tunnel Falls：12 量子點 Si/SiGe 晶片
│   │   │   ├── 300 mm EUV 製程量子位元
│   │   │   └── 開放給學術界研究使用
│   │   │
│   │   └── Samsung / TSMC
│   │       ├── 主要用於 FinFET/GAA 中的 SiGe 通道（提升電洞遷移率）
│   │       └── 非 BiCMOS 服務主力
│   │
│   └── 台灣相關公司
│       └── 嘉晶電子（Episil Precision, 3016）
│           ├── 角色：磊晶晶圓供應商（非晶片設計廠）
│           ├── 提供 Si、GaN-on-Si、SiC 磊晶晶圓
│           ├── 2024：世界先進入股 13%，合作 8 吋 SiC 晶圓
│           └── SiGe 連結：作為基板材料供應商
│
├── 6. 新興研究前沿
│   │
│   ├── 量子自旋位元（最熱）
│   │   ├── 機制：Si 量子阱（5~10 nm）+ SiGe 障壁 → 捕獲單電子
│   │   ├── 2025 Nature：>99% 保真度，達容錯閾值
│   │   ├── 2025 QuTech：自旋穿梭 10 μm，平均保真度 99.5%
│   │   └── 300 mm 晶圓量產路徑清晰 → 百萬量子位元可期
│   │
│   ├── 光子學整合
│   │   ├── IHP SiGe photonics：電子 + 光學單晶片
│   │   ├── GeSn（鍺錫）：擴展至中紅外光譜（3~5 μm）
│   │   └── 量子光子界面應用
│   │
│   ├── Sub-THz / THz（6G 準備）
│   │   ├── 100~300 GHz：SiGe BiCMOS 是最具競爭力的矽基方案
│   │   ├── >300 GHz：InP 仍具優勢
│   │   └── IHP 2024 PA 已瞄準 beyond-5G/6G 頻段
│   │
│   └── AI 數據中心基礎設施
│       ├── 800G 光收發器 TIA/驅動晶片 → SiGe 主導
│       └── 量子電腦低溫讀出電路（4 K 環境下仍正常運作）
│
└── 7. 市場展望
    │
    ├── 市場規模
    │   ├── SiGe 材料與元件：2024 年 $103 億 → 2030 年 $183 億（CAGR 10.1%）
    │   └── SiGe 晶片：2024 年 ~$15 億 → 2033 年 $32 億（CAGR 9.3%）
    │
    ├── 主要成長動力
    │   ├── 5G 基礎建設部署
    │   ├── 汽車雷達爆發（L3+ 每輛 4~6 組，~20% CAGR）
    │   ├── LEO 衛星星座（Starlink、Kuiper）
    │   ├── AI 數據中心光互連需求
    │   └── 量子電腦硬體投資
    │
    ├── 戰略趨勢
    │   ├── 歐洲主權半導體：IHP + ST + X-FAB + Infineon（EU Chips Act）
    │   ├── GF「差異化晶圓廠」定位
    │   ├── 開源 PDK 建立生態系（IHP SG13G2）
    │   └── 國防/航太穩定需求（美國 DoD、DARPA 長期資助）
    │
    └── 挑戰
        ├── BiCMOS 製程比純 CMOS 貴（附加模組複雜度）
        ├── >300 GHz：InP 仍有性能優勢
        ├── 高功率應用：GaN 主導地位難撼動
        └── 先進 CMOS 節點（5nm/3nm）RF 性能持續追趕
```

---

## 關鍵數字速查

| 指標 | 數值 |
|------|------|
| 最高 fT/fmax（量產）| 470 / 650 GHz（IHP SG13G3Cu） |
| 最高 fT/fmax（研究）| 505 / 720 GHz |
| 低溫最高 fmax | ~798 GHz（IBM，4.5 K） |
| 量子位元閘保真度 | >99%（2025 Nature） |
| 光偵測器頻寬 | 265 GHz（Ge-on-Si） |
| 市場規模 2030 預測 | $183 億（材料+元件） |
| 汽車雷達 CAGR | ~20% |

---

## 延伸研究方向（給有興趣深入的讀者）

1. **量子運算**：Intel Tunnel Falls、IHP SiGe 低溫特性、QuTech 自旋穿梭
2. **6G 標準**：Sub-THz 頻譜分配、IHP beyond-5G PA、SiGe vs InP 的頻率分工
3. **汽車應用**：Infineon RASIC 系列、ST 77 GHz 雷達 SoC、ADAS 感測器融合
4. **光子整合**：IHP SG25H5_EPIC、矽光子 + SiGe BiCMOS 的 co-integration
5. **開源生態**：IHP SG13G2 PDK、OpenRule1um、學術研究進入門檻

---

*資料截止：2025 年 3 月 | 主要來源：IHP、GlobalFoundries、Nature、IEEE、Tower Semiconductor*
