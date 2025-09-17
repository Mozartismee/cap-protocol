# DSA 筆記模板（MCSR 對齊）

<!--
格式規則（硬約束）
- 標題層級：Title = H1；Unit = H2；標籤 = H3（M, S, Bd, Ad, Cs, Ex, Tr, Rc, Cf, Meta-Reflection, TN）。
- 文風：Bourbaki 風格，壓縮、嚴謹、無修辭。
- 每個 Unit 僅在後處理時選擇性加入 ≤2 個 Pressure Sections（Bd/Ex 優先）。
- 不提前落地實作；按節律：RVC → Structure → ADT → API → Implementation。
-->

## General Statement（總述）
<!-- 3–6 行。以結構敘述問題對象、可見差異與成本標度。無修辭，無動機。 -->
- 對象：
- 可見差異：
- 成本標度：

## Obstruction Map（阻礙地圖）
<!-- 表格：Witness | Faultline | Target | Scope | Remedy/Action | TN；預設 1–2 行，硬上限 3。 -->
| Witness | Faultline | Target | Scope | Remedy/Action | TN |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

<!-- 可選：宏觀依存圖（僅敘述或引用圖） -->

---

## Unit 1: *[資料結構或平臺名稱]*

### Motivation (M)
<!-- 3–5 行，點出語言邊界與當前壓力；宣告下一步目標與方法。 -->

### RVC（Regime of Visibilities & Compatibilities）
<!-- 規範：至少一個奇點；至少兩種異質實作可滿足。 -->
- **Visibilities V**：{ … } <!-- 公共可檢驗切面，如命中率、容量、秩序視圖 -->
- **Compatibilities C**：{ … } <!-- 不可違背的相容條件，如容量 ≤ cap，O(1)_amort，秩單調 -->
- **Singularities S**：{ … } <!-- 閾值、分岔點與臨界法則 -->
- **Workload context 𝒲**：{ … } <!-- 分布或過程假設，如 Zipf 指數、到達過程上界 -->

### Structure (S)
<!-- 規範：每條 Law 可追溯到某個 C；U 生成 V。 -->
- **State 空間 Σ**：…
- **Events E（帶單位半群）**：…
- **Laws L（交換律、不變量）**：…
- **Functor U: Σ → Obs** 生成 **V**。

### ADT
<!-- 規範：operation ↔ event；κ 不退步於 C；至少一個尖銳反例。 -->
- **Operations O（簽章）**：…
- **Algebraic Laws A（代數律）**：…
- **Complexity 承諾 κ: O → K**：…
- **Boundary hooks**：Ad（假設放寬）／Cs（條件強化）記述與範圍。
- **反例（Proper Example）**：…

### API
<!-- 規範：method ↔ operation；至少一個 property test 直接驗證某個 V；錯誤政策需對齊某個 C。 -->
- **Method 簽章**：…
- **Error policies**：…
- **Property tests（性質測試）**：…
- **Concurrency semantics**：單執行緒／線性化點／鎖策略（聲明即可）。

### Implementation
<!-- 規範：不改語義，只改常數；標明平台耦合；列出退化情境與修補策略。 -->
- **Representation（表示）**：array／list／tree／hash／heap／skip list…
- **Layout strategy**：AoS／SoA、快取線、指標壓縮、記憶體配置。
- **Platform constraints**：ISA、快取階層、配置器、併發模型。
- **Failure mode catalogue + 修補策略**：collision／overflow／contention／GC pause…

### Boundary (Bd)
<!-- 單獨列出邊界法則與對應的通過或對消條件；説明其在 S 中的直接後果。 -->

### Assumption Drop (Ad)
<!-- 放寬假設；寫出修補裝置與適用範圍，並標明在 S/ADT 何處使用。 -->

### Condition Strengthening (Cs)
<!-- 加強假設以換取更強結論；寫出強化的結論與在 S/ADT 何處使用。 -->

### Proper Example (Ex)
<!-- 最小而尖銳的例或反例；指出它強制了哪條結構或揭示何種失敗。 -->

### Theorem Rephrasing (Tr)
<!-- 為了與函子字典或門檻條件對齊的重述；明記等價關係與使用處。 -->

### Reconstruction (Rc)
<!-- 正規化為可重用的標準構造；列步驟與穩定性。 -->

### Categorification (Cf)
<!-- 指名函子、來源與目標範疇、以及「樓上」的陳述與其普遍性質。 -->

### Meta-Reflection
<!-- 說明本 Unit 在整體中的功能、向下一個單元的交接，以及類範疇提升的備註。 -->

### TN（兩句鉸接）
<!-- 句 1：上一個壓力或斷裂；句 2：下一個局部目標與方法。 -->

---

## Notation and Conventions（符號與慣例）
<!-- 宣告全域符號與字體規則；保證跨單元一致。 -->

<!--
審計檢查點（填表式）
- RVC：奇點測試已定義（是／否）；至少兩個異現實作（是／否）。
- Structure：每條 Law 已追溯到 C（是／否）；U(Σ)=V（是／否）。
- ADT：operation↔event（是／否）；κ 對齊 C（是／否）；反例已提供（是／否）。
- API：每個 V 有對應的 property test（是／否）；錯誤政策對齊 C（是／否）。
- Implementation：平台耦合標註完整（是／否）；退化情境與修補策略列舉（是／否）。
-->
