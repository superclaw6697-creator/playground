# Lumentum Holdings（LITE）研究報告

**報告日期：** 2026-10-24

---

## 一、一頁摘要

- Lumentum是美國光通訊元件廠，核心產品是雷射(laser)晶片/模組，包括用於AI資料中心800G/1.6T光收發模組的EML(externally modulated laser)雷射、窄線寬雷射(narrow linewidth laser)，以及正在爬升的共封裝光學(CPO, co-packaged optics)雷射來源模組。
- FY2026(截至2026/6/27)營收年增83.2%至約$30.14億，連續8個季度成長，Q4非GAAP毛利率首次站上50%，顯示AI光通訊需求是真實的訂單轉換，不只是題材。
- 2026年3月Nvidia宣布對Lumentum投資$20億優先股，換取多年採購承諾與未來產能保留權，這是AI供應鏈對Lumentum議價能力最強的背書。
- 管理層稱產能已被訂單排到2029年初，但10月以來股價在AI資本支出可持續性疑慮下劇烈震盪（10/12單日跌近10%、10/22再跌近12%），顯示市場正在對過去一年的漲幅($2026年全年漲約164%)做估值修正。
- 競爭格局是「下游模組被中國廠(中際旭創Innolight、新易盛Eoptolink)壓著打，上游關鍵雷射晶片(EML/CW)被Lumentum與Coherent兩家卡住」——FCC若通過禁止中國轉換器進口的草案，對Lumentum是題材加分，但自身產能是否接得住是另一個問題。
- 結論：這是一家正站在AI光通訊景氣循環高點、基本面确实在改善，但股價已經先走、估值要靠「未來兩年EPS能否照管理層給的節奏兌現」才撐得住的成長股，波動會持續放大。

---

## 二、供應鏈定位——它的錢跟誰拿？

### 上游
- **原料/晶圓製造**：Lumentum是少數在雷射晶片這一層自己擁有磷化銦(InP)晶圓廠的公司，主要生產基地在美國Caswell(英國)、Sagamihara(日本)、Takao，並在2026年收購美國半導體廠商Qorvo位於North Carolina Greensboro的舊晶圓廠，改造成6吋InP晶圓產能。[(Telecompaper)](https://www.telecompaper.com/news/lumentum-acquires-qorvos-north-carolina-fab-to-produce-6-inch-inp-wafers--1566611)
- **InP原料供應商**：2026年7月與美國砷化鎵/磷化銦基板廠**AXT Inc.**簽訂長期InP供貨協議，確保關鍵基板料源。[(semiconductor-today)](https://www.semiconductor-today.com/news_items/2026/jul/axt-lumentum-030726.shtml)
- **組裝/封裝**：原在中國東莞(Dongguan)有模組組裝產能，因應關稅已轉移至泰國Nava廠區，泰國無塵室與InP晶圓產線擴建是近期資本支出主要用途之一。
- 整體看，Lumentum在雷射晶片這一層是垂直整合(自建晶圓廠)，不像下游模組廠(中際旭創等)仰賴外部晶片供應——這也是它對下游模組廠有議價能力的根本原因。

### 下游
- 10-K以「Customer A/B/C」代號揭露，FY2025財報顯示Customer A佔總營收16.0%、Customer B佔15.4%、Customer C低於10%（FY2022時Customer A曾高達28.7%，集中度已略為下降但仍偏高）。[(SEC 10-K FY2025)](https://www.sec.gov/Archives/edgar/data/1633978/000162828025040830/lite-20250628.htm)
- 已知具名下游客戶包括**Nvidia**（2026年3月以$20億換取多年採購承諾+未來產能保留權）、**Google**、以及**Cisco Systems**（網通OEM業務OpComms部門客戶之一）。公開資料未點名其他Customer A/B/C的確切身分。
- 雲端/AI客戶(Cloud & Networking部門)是FY2025以來成長最快的區塊，單位出貨量增加帶動該部門營收增加約$1.93億，網通設備商(network equipment manufacturers)營收增加約$1.33億。

### 競爭者關係
- **模組市場（下游）**：中際旭創(Innolight)以約23-27%全球營收份額居冠，主攻800G/1.6T模組，並拿下50-60%的Nvidia光模組錢包份額；新易盛(Eoptolink)是另一家主要中國競爭者。這塊市場Lumentum自己只佔約6%的「成品模組」營收，因為它更專注在賣晶片給模組廠，而非自己做成品模組跟中際旭創正面對決。
- **雷射晶片（上游，真正戰場）**：Lumentum與**Coherent（原II-VI）**是全球兩大具備自有InP晶圓產能的雷射晶片供應商。Lumentum在200G-per-lane EML晶片（1.6T模組的關鍵元件）上握有約50-60%全球份額——換句話說，連中際旭創做的模組，上游雷射晶片很可能也要跟Lumentum或Coherent買。Coherent營收規模約Lumentum的4倍（Coherent FY2026營收$71.2億 vs Lumentum約$30.1億），在CPO、雷射、感測領域與Lumentum全面交手。
- **代工廠**：**Fabrinet**是幫Lumentum、Ciena、Nvidia代工製造光學/光電產品的EMS廠，角色是代工夥伴而非直接競爭者，但Fabrinet同時也服務Lumentum的部分競爭對手。
- **近期競爭動態**：美國FCC醞釀禁止新進中國製光收發模組進口（主要打擊中際旭創27%全球市佔），若成案對Lumentum/Coherent是訂單轉單利多，但分析指出Coherent與Lumentum目前的無塵室產能、自動化封裝與良率規模，短期(12-24個月)內未必接得住中際旭創與新易盛讓出的量，這反而可能先推升晶片端(Lumentum的核心)的訂單，再逐步擴大到模組端。
- **議價能力評估**：對上游（InP晶圓料源）議價力中等偏強（自建晶圓廠+AXT長約降低原料風險）；對下游議價力正在增強（Nvidia主動掏$20億綁長約、產能排到2029年初，顯示是賣方市場），但客戶集中度仍高(前兩大客戶合計逾30%營收)是潛在反向槓桿。

---

## 三、拆財報細節

### 營收與獲利趨勢（財年制，7月-次年6月，單位：百萬美元）

| 財年 | 營收 | YoY | GAAP毛利率 | 備註 |
|------|------|-----|-----------|------|
| FY2023 | ~$1,770 | — | — | 疫後需求回落 |
| FY2024 | ~$1,360 | -23% | 24.68% | 電信/企業網需求低迷 |
| FY2025 | ~$1,650 | +21% | 32.95% | AI雲端需求開始接棒 |
| FY2026 | $3,014.0 | +83.2% | 41.7%(全年) / 47.4%(Q4) | AI光通訊需求全面爆發 |

- FY2026單Q4營收$10.1億，年增109%；非GAAP毛利率首次站上50%（Q4達50.4%，年增1,260個基點）。
- FY2026 GAAP營運利益率由-10.9%翻轉至+17.4%，顯示規模經濟開始發揮。
- FY2026非GAAP淨利$7.823億，非GAAP每股盈餘(diluted)$8.67；但GAAP口徑Q4出現$72億的鉅額GAAP淨損（每股虧損$84.65），主因是Nvidia優先股投資案相關的非現金會計認列（優先股轉換權益的beneficial conversion feature等一次性會計費用），不代表實際現金虧損，但也代表這筆交易的GAAP損益表很「髒」，看公司真實獲利能力要用非GAAP數字。
- **現金流與資本結構**：FY2026營運現金流$7.514億，自由現金流由前兩年燒錢轉為正$3.001億；資本支出$4.513億(占營收15.0%)，主要投入InP晶圓產能擴建與泰國/美國新廠。總負債由FY2025的$26.08億降至FY2026的$16.71億，淨現金狀態由淨負債$16.961億轉為淨現金$11.01億（主因Nvidia等策略投資帶來的增資），期末現金及短期投資達$27億。
- **ROE**：FY2023-24為負值，FY2025因GAAP口徑受併購無形資產攤銷與股權薪酬影響仍受壓抑，非GAAP ROE在FY2025已接近15%門檻，FY2026隨獲利轉強預期進一步改善（公開資料未提供精確FY2026 ROE數字，列入未能驗證清單）。

---

## 四、法說會——公司承諾了什麼

### Q3 FY2026法說會（2026/5/5）
- CEO Michael Hurlston、CFO Wajid Ali、業務群總裁Wupen Yuen出席。Q3營收年增90%至$8.08億創紀錄，EPS $2.37優於市場預期的$2.26。
- 管理層重申目標是達到「季營收$20億」的OFC法說會長期目標，並上調下一季非GAAP營收與毛利率guidance。
- Components部門(雷射晶片)營收$5.33億，季增20%、年增77%；窄線寬雷射出貨連續第9個季度成長，年增逾120%；泵浦雷射(pump laser)出貨年增80%。

### Q4 FY2026法說會（2026/8/11）
- 連續第8個季度營收成長，年增109%；非GAAP毛利率首次站上50%，達成當時給的長期目標模型「提前超過一個季度」。
- 窄線寬雷射出貨連續第10個季度季增、年增逾130%。
- 給Q1 FY2027(即2026年秋季)營收guidance中值$12.5億，意味單季再季增約24%。
- CPO相關營收：管理層表示Q4已有約$5,000萬CPO相關營收，預期FY2027上半年(2026下半年至2027上半年)將有數億美元CPO訂單轉化為營收，首批規模化CPO出貨預計2027年底。

### 兌現情況與誠實度評估
- 從Q3到Q4，管理層給的「毛利率過50%」「提前達標」承諾確實兌現，且提前達成速度超出自己原先給的時間表，顯示近兩次法說會屬於「保守給guidance、實際超標」的穩健型模式，而非誇大畫大餅。
- 10月9日CEO公開表示訂單已排到2029年初，隨後股價短暫上漲，但緊接著在未有公司壞消息的情況下因產業資本支出疑慮重挫，顯示管理層的「需求端」說法與「市場對AI資本支出可持續性」的疑慮是兩條獨立的敘事線，不能混為一談——公司承諾的是訂單能見度，不是股價不會跌。

---

## 五、市場怎麼看

### 分析師評等與目標價

| 券商 | 評等 | 目標價 | 日期 | 備註 |
|------|------|--------|------|------|
| Citi | Buy | $1,400（原$1,200） | 2026-10-05前後 | 看好CPO+AI光通訊長期需求 |
| Jefferies | Buy | $1,250（原$1,200） | 2026-10-20 | 維持評等並上調目標價 |
| Bernstein | Outperform | 對應2027年PE 49.3x | 2026-10-12 | 同時維持Coherent Outperform，但指出LITE對COHR估值差距擴大 |
| 分析師共識(約23-26家) | Moderate Buy / Buy | 平均目標價約$1,078.75（近12個月均值），近期區間$1,100-$1,400 | 2026-10-07 | MarketBeat彙整 |

### 籌碼面
- 機構持股比例高達約94.1%，共1,075家機構股東，Blackrock、Vanguard等為主要持股人。
- 放空比例：不同資料源落差較大，一說約7.9%流通股、days-to-cover約1.7-2.8天；另一說放空比例高達17.81%流通股——股價劇烈波動期間，兩種口徑差異可能反映統計時間點不同，建議以近期更新數據為準（列入未能驗證清單）。
- 近期機構動向：2026年10月21日Pinnacle Associates加碼；同期Robeco Institutional Asset Management減碼——顯示機構之間對目前高波動股價的看法已出現分歧。

### 市場消息（近4週新聞roundup）
- [2026-10-05] Citi將目標價由$1,200上調至$1,400，維持Buy評等，看好CPO長期放量 — [Yahoo Finance](https://finance.yahoo.com/news/indium-phosphide-capacity-expansion-drive-125400975.html)
- [2026-10-09] CEO公開表示AI光通訊訂單能見度已排到2029年初，股價單日上漲5.2% — [247wallst](https://247wallst.com/investing/2026/10/12/lumentum-falls-10-as-optics-selloff-hits-hardest-where-capacity-is-sold-out-applied-optoelectronics-drops-7-coherent-slides-7/)
- [2026-10-12] 受Broadcom、Intel執行長對AI資本支出/資金面疑慮發言影響，光通訊股全面重挫，LITE單日跌近9.78%至$995.41，當日公司業務面無壞消息 — [Investing.com](https://www.investing.com/news/stock-market-news/why-is-lumentum-stock-sliding-today-93CH-4949616)
- [2026-10-14] AI資金疑慮延續，Applied Optoelectronics重挫9%，Coherent跌7%，Lumentum再跌7% — [247wallst](https://247wallst.com/investing/2026/10/14/applied-optoelectronics-dives-9-as-ai-funding-fears-hit-optical-stocks-coherent-slides-7-lumentum-drops-7/)
- [2026-10-20] Jefferies上調目標價至$1,250 — [Gurufocus](https://www.gurufocus.com/news/9134607/lite-maintained-by-jefferies-price-target-raised-to-1250)
- [2026-10-22] 科技股全面賣壓加劇，LITE單日暴跌近12%收在$752.54 — [Gurufocus](https://www.gurufocus.com/news/9137793/lumentum-holdings-lite-shares-plunge-nearly-12-amid-tech-sector-selloff-on-october-22-2026)

---

## 六、成長動能與風險

### 成長動能
- **CPO(共封裝光學)放量**：管理層預期FY2027上半年(約2026下半年至2027上半年)將有數億美元CPO訂單轉化為營收，首批規模化出貨落在2027年底，若NVIDIA等客戶的Rack-scale AI系統如期放量，這會是繼EML雷射晶片之後的第二成長曲線。
- **EML/窄線寬雷射晶片需求持續吃緊**：窄線寬雷射出貨已連續10個季度成長，Q4年增逾130%，管理層稱產能已排到2029年初，顯示至少未來2-3年訂單能見度已鎖定，前提是終端AI資料中心資本支出不急剎車。
- **FCC潛在禁止中國轉換器進口**：若政策落地，中際旭創(27%全球份額)的美國雲端客戶訂單可能轉向Coherent/Lumentum，雖然Lumentum目前產能未必能在12-24個月內完全承接，但即使只接到增量的一部分，對晶片端訂單也是額外助力，時間點落在2026年底至2027年政策定案後。
- **Nvidia策略入股綁定長約**：2026年3月Nvidia投資$20億並附多年採購承諾+未來產能保留權，等於鎖定未來數年最大AI客戶的訂單基礎，降低了過去「客戶集中度過高、議價力偏弱」的疑慮。

### 風險
- **AI資本支出可持續性疑慮**：10月以來Broadcom、Intel等公司高層公開質疑AI基礎設施投資的資金可持續性(access to capital是瓶頸而非晶片供給)，一旦下游雲端大廠實際砍資本支出guidance，Lumentum訂單能見度會被直接打折，這是過去兩週股價劇震的核心敘事。
- **中際旭創/新易盛持續擴產壓低模組端價格**：中際旭創計畫在1.6T模組市場拿下50-60%份額，雖然Lumentum主要賣晶片給模組廠而非直接做成品模組，但模組端價格戰若壓縮模組廠毛利，模組廠可能回頭向Lumentum/Coherent要求降價，傳導至晶片端報價。
- **Coherent規模優勢持續擴大估值差距**：Coherent營收規模約Lumentum的4倍(FY2026 $71.2億 vs $30.1億)，Bernstein已指出兩者2027年PE差距擴大(LITE 49.3x vs COHR 32.9x)，若市場認為Lumentum估值過度領先基本面規模差距，資金可能階段性轉向估值更低的Coherent，壓抑LITE股價。
- **客戶集中度仍偏高**：Customer A+B合計逾30%營收(FY2025)，任何單一大客戶訂單延後或轉單都會對營收造成非線性衝擊，Nvidia的長約雖降低風險但並未完全消除。
- **GAAP損益表因優先股會計處理持續失真**：Q4 FY2026出現$72億GAAP淨損的一次性會計認列，若未來類似策略增資交易再出現類似會計處理，市場對GAAP數字的解讀可能持續混亂，增加訊息不對稱風險。

---

## 七、重大事件時間軸

- 2025-02-07：Michael Hurlston接任總裁兼CEO，接替任職10年的Alan Lowe（Lowe續留董事會及顧問角色）。
- 2026-03-02：NVIDIA宣布對Lumentum進行$20億優先股策略投資，換取多年採購承諾與未來產能保留權；同日NVIDIA也對Coherent進行同額投資。
- 2026-05-05：Q3 FY2026法說會，營收$8.08億年增90%創紀錄，EPS $2.37優於預期。
- 2026-07：與AXT Inc.簽訂長期InP基板供貨協議。
- 2026-08-04：FCC醞釀禁止新進中國製光收發模組進口的消息曝光，光通訊股全面上漲，LITE單日漲約7%。
- 2026-08-11：Q4與FY2026全年財報公布，營收年增109%，非GAAP毛利率首次破50%，同時因Nvidia優先股會計處理出現GAAP單季$72億鉅額淨損。
- 2026-08：宣布擴建美國半導體廠產能以支援CPO生產。
- 2026-10-05：Citi將目標價由$1,200上調至$1,400，維持Buy評等。
- 2026-10-09：CEO公開表示AI光通訊訂單已排到2029年初，股價單日漲5.2%。
- 2026-10-12：AI資本支出疑慮引發光通訊股全面重挫，LITE單日跌近9.78%。
- 2026-10-20：Jefferies上調目標價至$1,250。
- 2026-10-22：科技股賣壓加劇，LITE單日再跌近12%收在$752.54，10/9-10/22期間累計回落逾25%（其中10/9-10/16五個交易日即跌25.3%）。

---

## 八、管理團隊

- **CEO：Michael Hurlston**（自2025年2月生效）。資歷豐富且橫跨半導體/光通訊兩界：2018-2019任Finisar CEO期間主導Finisar被II-VI(現Coherent)收購案；2019-2025任Synaptics CEO；更早期(2001-2017)在Broadcom歷任移動連接事業群SVP/GM、銷售EVP等要職。學歷為UC Davis學士、碩士及MBA。接任Lumentum前已有兩次大型光通訊/半導體公司CEO經驗，背景與Lumentum業務高度相關。
- **CFO：Wajid Ali**，EVP兼CFO，自法說會紀錄中持續出席並負責財務guidance溝通。
- 其他高管：General Counsel Jae Kim、EVP全球可靠度與品質Vincent Retort、全球事業群總裁Wupen Yuen。
- **近期管理層變動**：Hurlston接任CEO距今約20個月，屬於近期但非過去12個月內的變動；接任後公司營運數字(營收、毛利率)連續改善，暫未見進一步高層異動公告。
- **言行記錄評估**：從Q3、Q4法說會的guidance兌現情況看（毛利率突破50%目標「提前超過一個季度」達成），Hurlston團隊屬於**穩健型管理層**，給的數字傾向保守、實際常超標完成，而非誇大畫餅型；但10月CEO公開喊出「訂單排到2029年初」的說法在股價短線反應上製造了預期管理的落差（說完沒幾天股價就因產業面疑慮重挫），顯示管理層對「公司自身需求」的樂觀表態，未必能抵銷市場對「整個AI資本支出週期」的系統性疑慮,這點投資人需要分開看待。

---

## 九、估值——它值得多少本益比？

### 目前倍數
- 股價(2026-10-22收盤)：$752.54；市值約$680-770億美元(不同資料源因計算時間點落差，介於$68B-$93B之間，需留意更新時點)。
- Forward PE(對FY2027預估EPS)：約34.74x（2026-10-22資料）。
- Trailing非GAAP PE：以FY2026非GAAP EPS $8.67計算，約$752.54/$8.67 ≈ 86.8x——trailing倍數遠高於forward倍數，反映市場預期未來一年EPS會大幅跳升（這正是典型的「高成長股」估值特徵：買的是未來，不是過去）。
- GAAP trailing PE因Q4鉅額一次性淨損而失真(部分資料源顯示287x甚至負值)，不具參考意義。

### 同業比較

| 公司 | 股票代號 | FY2026營收 | 市值(約) | 2027年預估PE | 評等基礎 |
|------|---------|-----------|---------|--------------|---------|
| Lumentum | LITE | ~$30.1億 | ~$680-770億 | ~34.7x(forward)/49.3x(Bernstein 2027估) | 高成長敘事，EML+CPO雙引擎，但規模最小 |
| Coherent | COHR | ~$71.2億 | ~$653億 | ~32.9x(Bernstein 2027估) | 規模是LITE的4倍，產品線更分散(雷射/感測/材料)，波動相對較低 |
| Fabrinet | FN | ~$42億(TTM) | ~$174億 | ~27.5x | 代工角色，毛利率結構性較低，但客戶分散度較高、週期波動相對平緩 |

### 為什麼是這個倍數
- Bernstein報告指出LITE與COHR的估值差距正在擴大（LITE 2027年PE 49.3x高於COHR的32.9x），理由是市場把Lumentum看作「AI光通訊景氣循環中最純粹、beta最高的雷射晶片標的」，而Coherent因業務更分散(含工業雷射、感測器等非AI業務)被認為成長彈性較低但也較穩定，因此願意給Lumentum更高的成長溢價。
- Fabrinet PE最低，因為它是代工角色，毛利率結構性低於掌握核心技術IP的Lumentum/Coherent，市場把它歸類為「製造服務股」而非「技術議價股」。
- **這家公司該被歸類成哪種股票**：Lumentum目前應歸類為**成長股(偏題材股邊緣)**——它有真實訂單與毛利率改善撐腰(非純題材)，但trailing PE遠高於forward PE的落差、以及10月股價在無公司壞消息下劇震的走勢，顯示市場情緒與估值敏感度已經很高，接近「題材股」特徵。合理的倍數區間應參考高成長半導體/光通訊設備股的forward PE(30-50x)，而非成熟電信元件股的個位數至20x區間。

### 情境推算

**保守情境**：假設FY2027(2026年7月-2027年6月)AI資本支出成長明顯放緩，Lumentum FY2027非GAAP EPS僅較FY2026(~$8.67)成長50%至約$13/股，且市場因估值疑慮將forward PE壓縮至25x（接近Fabrinet水準），則合理股價區間約**$325**。

**樂觀情境**：假設CPO訂單如期在2027年上半年放量、FCC禁令落地帶來額外轉單，FY2027非GAAP EPS成長至管理層guidance所隱含的水準(約$20-24/股，對應年化季營收達到$20億目標模型)，且市場維持目前forward PE區間(約35-40x)，則合理股價區間約**$700-960**，大致對應目前股價區間，顯示當前股價已部分反映樂觀情境，安全邊際有限。

---

## 十、總結評估

Lumentum是目前AI光通訊供應鏈中基本面改善最明確的公司之一——營收連續8個季度成長、毛利率首次破50%、現金流由負轉正、且被Nvidia以真金白銀$20億綁下長約，這些都是可驗證的事實而非單純敘事。但股價在2026年已上漲約164%，10月以來在沒有公司自身壞消息的情況下單月兩度單日跌幅近10-12%，說明市場的估值敏感度極高，trailing與forward PE之間的巨大落差意味著股價已經提前反映相當樂觀的未來EPS成長路徑。最關鍵的多方因素是CPO訂單能否如期在2026下半年至2027上半年放量兌現；最關鍵的空方因素是AI資料中心資本支出週期是否真的如Broadcom/Intel高層所暗示開始受資金面制約。若要盯緊一個指標判斷論點是否還成立，應該是**每季法說會公布的非GAAP毛利率與下季營收guidance年增率是否持續優於管理層先前給的節奏**——一旦guidance開始不如預期或毛利率觸頂回落，就是這個成長敘事降溫的訊號。

---

## 十一、未能驗證清單

- FY2026精確ROE/ROA數字：公開搜尋僅取得「非GAAP ROE在FY2025接近15%門檻」的定性描述，未取得FY2026精確數字。
- 目前市值：不同資料源差異極大(介於$68B-$93B)，可能反映不同計算時間點或股數基礎（已持股稀釋 vs 完全稀釋），建議查核當日即時Yahoo Finance/StockAnalysis.com數字確認。
- 放空比例：兩個資料源分別顯示約7.9%與17.81%流通股，差異過大無法判定哪個是最新正確數字。
- FY2022精確年度營收數字：公開搜尋未能取得明確的FY2022全年營收數字(僅有零星單季數據)。
- 10-K中「Customer A/B/C」代號對應的具體公司名稱：官方文件未揭露，只能從其他新聞交叉比對推測可能包含Nvidia、Google、Cisco等，但無法逐一確認比重對應關係。
- Q1 FY2027(2026年秋季，即最新一季)實際財報結果：截稿時尚未公布(公司財年Q1通常於11月發布)，本報告僅引用管理層guidance，非實際數字。

---

## 十二、參考來源

- [Lumentum Holdings Inc. (LITE) Q4 FY2026 Earnings Call Transcript - August 11, 2026](https://www.roic.ai/quote/LITE/transcripts/2026-year/4-quarter)
- [Lumentum (LITE) Q4 2026 Earnings Call Transcript - Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/08/18/lumentum-lite-q4-2026-earnings-call-transcript/)
- [Earnings call transcript: Lumentum tops Q4 2026 forecasts as AI demand lifts outlook - Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-lumentum-tops-q4-2026-forecasts-as-ai-demand-lifts-outlook-93CH-4852933)
- [Lumentum Holdings Inc. (LITE) Q3 FY2026 Earnings Call Transcript - May 5, 2026](https://www.roic.ai/quote/LITE/transcripts/2026-year/3-quarter)
- [Lumentum Announces Fourth Quarter and Full Fiscal Year 2026 Results - Investor Relations](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx)
- [Lumentum Holdings Inc. - Form 10-K - FY2025 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/1633978/000162828025040830/lite-20250628.htm)
- [Lumentum Holdings Inc. - Form 10-K - FY2026 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/0001633978/000162828026057358/lite-20260627.htm)
- [Lumentum Holdings (LITE) Financials Overview - StockAnalysis.com](https://stockanalysis.com/stocks/lite/financials/)
- [Lumentum Holdings (LITE) Stock Forecast & Analyst Price Targets - StockAnalysis.com](https://stockanalysis.com/stocks/lite/forecast/)
- [LITE Maintained by Jefferies -- Price Target Raised to $1250 - Gurufocus](https://www.gurufocus.com/news/9134607/lite-maintained-by-jefferies-price-target-raised-to-1250)
- [Lumentum Holdings Inc. (NASDAQ:LITE) Stock Has Consensus Target Price of $1,078.75 - MarketBeat](https://www.marketbeat.com/instant-alerts/consensus-lumentum-holdings-inc-nasdaq-lite-stock-has-consensus-target-price-of-107875-according-to-analysts-2026-10-07/)
- [Lumentum Holdings (LITE) Shares Plunge Nearly 12% Amid Tech Sector Selloff on October 22, 2026 - Gurufocus](https://www.gurufocus.com/news/9137793/lumentum-holdings-lite-shares-plunge-nearly-12-amid-tech-sector-selloff-on-october-22-2026)
- [Lumentum Falls 10% as Optics Selloff Hits Hardest Where Capacity Is Sold Out - 24/7 Wall St.](https://247wallst.com/investing/2026/10/12/lumentum-falls-10-as-optics-selloff-hits-hardest-where-capacity-is-sold-out-applied-optoelectronics-drops-7-coherent-slides-7/)
- [Why is Lumentum stock sliding today? - Investing.com](https://www.investing.com/news/stock-market-news/why-is-lumentum-stock-sliding-today-93CH-4949616)
- [Nvidia pours $2B into Lumentum - Light Reading](https://www.lightreading.com/ai-machine-learning/nvidia-pours-2b-into-lumentum)
- [Nvidia to invest $4 billion into photonics companies Coherent and Lumentum - CNBC](https://www.cnbc.com/2026/03/02/nvidia-investment-coherent-lumentum.html)
- [Lumentum acquires Qorvo's North Carolina fab to produce 6-inch InP wafers - Telecompaper](https://www.telecompaper.com/news/lumentum-acquires-qorvos-north-carolina-fab-to-produce-6-inch-inp-wafers--1566611)
- [AXT announces long-term InP supply agreement with Lumentum - Semiconductor Today](https://www.semiconductor-today.com/news_items/2026/jul/axt-lumentum-300726.shtml)
- [The FCC Mulls Banning China-Sourced Optical Transceivers, Threatening Innolight's 27% Global Market Share - WCCFtech](https://wccftech.com/the-fcc-mulls-banning-china-sourced-optical-transceivers-threatening-innolights-27-global-market-share-as-coherent-and-lumentum-prepare-to-pounce/)
- [FCC Transceiver Ban Would Cut 60% of AI Data Center Supply - Tech Times](https://www.techtimes.com/articles/323104/20260805/fcc-transceiver-ban-would-cut-60-ai-data-center-supply-western-replacements-need-chinese-indium.htm)
- [Bernstein: Lumentum and Coherent Valuation Gap Widens, NPO Seen as CPO Alternative - Kucoin News](https://www.kucoin.com/news/flash/bernstein-lumentum-and-coherent-valuation-gap-widens-npo-seen-as-cpo-alternative)
- [Coherent (COHR) Revenue 2005-2026 - StockAnalysis.com](https://stockanalysis.com/stocks/cohr/revenue/)
- [Fabrinet Market Cap 2012-2026 - Macrotrends](https://www.macrotrends.net/stocks/charts/FN/fabrinet/market-cap)
- [Who is the CEO of Lumentum in 2026? Michael Hurlston's Bio - Clay](https://www.clay.com/dossier/lumentum-ceo)
- [Lumentum Holdings Inc. - Form DEF 14A - FY2026 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/0001633978/000130817926000420/lite2026-def14a.htm)
- [Lumentum's CEO sees growing customer interest in co-packaged optics (CPO) - Lightwave Online](https://www.lightwaveonline.com/home/article/55338753/lumentums-ceo-sees-growing-customer-interest-in-co-packaged-optics-cpo)
- [Lumentum (LITE) Ownership & Institutional Holdings - Chartmill](https://www.chartmill.com/stock/quote/LITE/ownership)
- [LITE - Lumentum Holdings PE ratio, current and historical analysis - FullRatio](https://fullratio.com/stocks/nasdaq-lite/pe-ratio)

---
*本報告由 AI 協助整理，僅供研究參考，不構成投資建議。*
