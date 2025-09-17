# DR–Axiomata v3｜差異・重複・截面・同一幻象投影（整併版｜含「運動」、\(\ker d\Phi_\kappa\)–\(\mathrm{Aut}_{\Phi_\kappa}\) 與 \(r\) 的結構）

（Bourbaki 風格；ENS Seminar 水準）

## 0. 記號
生成差異空間 \(X=\Delta_{\mathrm{gen}}\)。重複形式集合 \(\mathcal R\)。觀測截面標誌 \(\star\in\{\Sigma,\Tau,\Pi\}\)。截面差異 \(\delta_\star\)。可理解域 \(U_\star\subseteq X\)。同一準則 \(\kappa\in\{\text{同一},\text{相似},\text{類比},\text{否定}\}\)。同一幻象投影空間 \(I_\kappa\)。外觀奇點 \(\Sigma\subset I_\kappa\)。正則域 \(I_\kappa^{\mathrm{reg}}=I_\kappa\setminus\Sigma\)。鑑別子 \(\mathrm{Disc}(\Phi_\kappa)\subset X\)。\(\mathcal V=\ker(d\Phi_\kappa)\subset TX\)。

---

## I. 公理
**T（時間−重複）** 每一時間指認屬重複；邊界位於重複形式之間。  
**D（差異−力）** 重複為差異之顯影與再生機制；位移與偽裝再生分歧與去中心。  
**E（選擇性回歸）** 回歸肯定差異與不相似；同一、相似、類比、否定不獲回歸。  
**S（奇點−系列）** 差異以系列與差異之差通訊；時間分配賦予回歸以選擇力。  
**L（語用合法性）** identical/similar 僅在回歸後作擬像效應之語用名稱。

---

## II. 定義

### Def 1（觀測截面與 Gate \(U_\star\)）
存在 \(U_\star\subseteq X\) 與 \(\mathrm{Obs}_\star:U_\star\to\delta_\star\) 使：  
(i) 規範不變：對 \(\mathcal V=\ker(d\Phi_\kappa)\) 與 \(\mathrm{Aut}_{\Phi_\kappa}\) 不變；  
(ii) 可重現：備有公共測試族 \(T_\star\)（校準、門檻、時間窗、取樣律），輸出可公開驗證。  
記號 \(U_\star\Rightarrow\delta_\star\) 表示對每一 \(x\in U_\star\)，\(\delta_\star(x)=\mathrm{Obs}_\star(x)\) 存在且（模規範）唯一。

### Def 2（同一幻象投影管線）
\[
\Delta_{\mathrm{gen}}\xrightarrow{\ \mathrm{Obs}_\star\ }\delta_\star
\xrightarrow{\ \rho\ }\mathcal R
\xrightarrow{\ q_\kappa\ }I_\kappa,
\qquad 
\Phi_\kappa:=q_\kappa\circ\rho\circ \mathrm{Obs}_\star.
\]
誘導等價 \(x\sim_\kappa y \iff \Phi_\kappa(x)=\Phi_\kappa(y)\)。取像為值時 \(X/{\sim_\kappa}\cong I_\kappa\)。差異保存在纖維 \(\Phi_\kappa^{-1}(i)\)。

### Def 3（重複形式選擇 \(\rho\)）
在 \(\delta_\star\) 上取由三則生成的最小等價 \(\approx\)：核流不變、自同構不變、正則提升守恆（遠離 \(\mathrm{Disc}\) 的 lifting 上值守恆）。  
定義 \(\mathcal R:=\delta_\star/\!\approx\)、投影 \(\pi:\delta_\star\to\mathcal R\)、\(\rho:=\mathrm{nf}\circ\pi\)（\(\mathrm{nf}\) 為正常形選擇）。

### Def 3†（重複形式 \(r\) 的結構）
令 \(\mathcal P\) 為由 \(\Gamma(\ker d\Phi_\kappa)\) 的局部流與 \(\mathrm{Aut}_{\Phi_\kappa}\) 生成之擬群，作用於 \(\delta_\star\)。定義
\[
z\sim z'\iff \exists h\in\mathcal P,\ z'=h\cdot z,\qquad
\mathcal R:=\delta_\star/\!\sim.
\]
元素 \(r\in\mathcal R\) 稱重複形式。群胚化：設作用群胚 \(\mathsf G=\mathcal P\ltimes\delta_\star\)，令
\[
r \equiv \big[\ z\ \big]_{\mathsf G}=\big(\ \mathcal O_z,\ [\mathrm{Iso}(z)]\ \big),
\quad
\mathcal O_z=\mathcal P\cdot z,\ \ \mathrm{Iso}(z)=\{h\in\mathcal P:h\cdot z=z\}.
\]
在正則域上，\(\mathcal R\) 具軌道型分層；\(\nu:I_\kappa^{\mathrm{reg}}\to\mathcal R\) 局部常值，僅於 \(\mathrm{Disc}(\Phi_\kappa)\) 跳變。增強版本（可選）：  
\[
r\widehat{=}(\mathrm{nf}(z),[\mathrm{Iso}(z)],\mathbf j_z),
\]
其中 \(\mathrm{nf}\) 為規範化代表，\(\mathbf j_z\) 為沿 \(\mathrm{Disc}\) 的有限 germ/jet（接觸次序、交角類型等），用於可審計的邊界接觸與分歧型分類。

### Def 4（邊界）
設型式標記 \(\nu:I_\kappa^{\mathrm{reg}}\to\mathcal R\)。  
拓撲版：
\[
S_r:=\{y\in I_\kappa^{\mathrm{reg}}:\nu(y)=r\},\quad
\partial(r_i\Vert r_j):=\overline{S_{r_i}}\cap \overline{S_{r_j}},\quad
\operatorname{Bd}_{\mathrm{top}}(\mathcal R):=\{(r_i,r_j):\partial(r_i\Vert r_j)\neq\varnothing\}.
\]
鑑別子版（可審計）：
\[
\operatorname{Bd}_{\mathrm{disc}}(\mathcal R):=\{(r_i,r_j):\overline{\nu^{-1}(r_i)}\cap \overline{\nu^{-1}(r_j)}\ \text{沿}\ \mathrm{Disc}(\Phi_\kappa)\ \text{相接}\},
\]
且
\[
\partial(r_i\Vert r_j)\neq\varnothing\ \Longleftrightarrow\ \exists\,\gamma:(-\varepsilon,\varepsilon)\to I_\kappa\ \text{橫切}\ \Sigma,\ 
\mathbf j_{\gamma(t<0)}\to\mathbf j_{\gamma(t>0)}\ \text{型式變更}.
\]
語義影子：\(\operatorname{Bd}_0(\mathcal R)=\{(r_i,r_j):r_i\neq r_j\}\)。

### Def 5（時間對象與運動）
取時間對象 \((T,\cdot)\)（例：\((\mathbb R,+)\)、\((\mathbb Z,+)\)）。  
一條運動是曲線 \(x:J\to X\)（\(J\subseteq T\)）。一個流為 \(\Psi:T\times X\to X\)，\(\Psi(0,\cdot)=\mathrm{id}\)、\(\Psi(t+s,\cdot)=\Psi(t,\cdot)\circ\Psi(s,\cdot)\)。  
觀測運動：\(\delta_\star\circ x\)（若 \(x(J)\subset U_\star\)）。投影運動：\(\Phi_\kappa\circ x:J\to I_\kappa\)。

### Def 6（位移、偽裝、分歧／去中心的運動刻畫）
位移：若 \(v\in T_xX\) 滿足 \(d\Phi_\kappa(x)\,v=0\)，且 \(x(t)\) 的切向量屬 \(\mathcal V\) 且 \(\Phi_\kappa(x(t))\) 局部常值，稱 \(x(t)\) 為位移。  
偽裝：若存在連續族 \(g(t)\in\mathrm{Aut}_{\Phi_\kappa}\) 使 \(x(t)=g(t)\cdot x_0\) 且 \(\Phi_\kappa(x(t))\) 恆定，稱為偽裝。  
分歧／去中心：若 \(x(t)\) 橫切 \(\mathrm{Disc}(\Phi_\kappa)\) 並致 \(\nu\) 更換（\(r_i\to r_j\)），稱為分歧／去中心。

---

## III. 三態結構（指示）
置 \(\mathcal V=\ker(d\Phi_\kappa)\subset TX\)，\(\mathrm{Aut}_{\Phi_\kappa}\) 為保持 \(\Phi_\kappa\) 的局部自同構群胚。  
位移由 \(\mathcal V\) 的流生成；偽裝由 \(\mathrm{Aut}_{\Phi_\kappa}\) 生成；分歧／去中心由 \(\mathrm{Disc}(\Phi_\kappa)\) 的穿越觸發。

---

## IV. 命題與定理

**Prop 1（必要鏈）** \(U_\star\Rightarrow \delta_\star\Rightarrow X\)。  

**Prop 2（邊界語義）** 僅在不同型式 \(r_i\neq r_j\) 間談邊界。  

**Lemma 3（\(\rho\) 的良性）** \(\rho\) 對 \(\mathcal V\) 與 \(\mathrm{Aut}_{\Phi_\kappa}\) 不變；在 \(I_\kappa^{\mathrm{reg}}\) 局部常值；非連續僅於 \(\mathrm{Disc}\)。  

**Prop 3†（\(\rho\) 的函子性與保持律）** \(\rho:\delta_\star\to\mathcal R,\ z\mapsto [z]_{\mathsf G}\) 為 \(\mathcal P\)-不變；若 \(x\notin\mathrm{Disc}(\Phi_\kappa)\)，則 \(\rho\) 在 \(\Phi_\kappa^{-1}(\Phi_\kappa(x))\) 的小鄰域常值。採增強 \(r\widehat{=}\big(\mathrm{nf},[\mathrm{Iso}],\mathbf j\big)\) 時，\(\rho\) 還保持穩定子共軛類與 germ 型別。  

**Cor 4（邊界判據）** 若存在曲線 \(y(t)\) 橫切 \(\mathrm{Disc}\) 且 \(\nu(y(t<0))\ne \nu(y(t>0))\)，則 \((r_i,r_j)\in \operatorname{Bd}_{\mathrm{disc}}(\mathcal R)\)；若遠離 \(\mathrm{Disc}\) 而 \(\nu\) 恆定則不成邊界。  

**Thm 5（正則域三態生成）** 於 \(I_\kappa^{\mathrm{reg}}\) 的保持外觀局部變化由「位移流 ◦ 偽裝 ◦ 位移流」生成；近 \(\Sigma\) 需加入分歧／去中心。  

**Thm A（保持法則）** 對任意 \(g\in\mathrm{Aut}_{\Phi_\kappa}\)、\(x\in X\)，  
\[
d g_x\big(\ker d\Phi_\kappa(x)\big)=\ker d\Phi_\kappa\big(g(x)\big),
\quad\text{即}\quad g_*\mathcal V=\mathcal V.
\]

**Thm B（Lie 對應，恆等連通分量）** 設 \(\Gamma(\mathcal V)=\{V\in\mathfrak X(X):d\Phi_\kappa\circ V=0\}\)。  
(1) 若 \(V\in\Gamma(\mathcal V)\) 可積，則其局部流 \(\psi_t\) 滿足 \(\Phi_\kappa\circ\psi_t=\Phi_\kappa\)，故 \(\psi_t\in\mathrm{Aut}_{\Phi_\kappa}\)。  
(2) 若 \(g_t\in\mathrm{Aut}_{\Phi_\kappa}\) 且 \(g_0=\mathrm{id}\)，其生成元 \(V=\left.\tfrac{d}{dt}\right|_{0}g_t\) 屬 \(\Gamma(\mathcal V)\)。  
結論：\(\mathrm{Lie}\big(\mathrm{Aut}_{\Phi_\kappa}^0\big)\cong \Gamma(\mathcal V)\)。

**Prop C（短正合列，正則點）** 若 \(x\notin\mathrm{Disc}(\Phi_\kappa)\)（\(d\Phi_\kappa\) 滿秩），則存在向量丛短正合列  
\[
0\longrightarrow \mathcal V\longrightarrow TX\xrightarrow{\,d\Phi_\kappa\,}\Phi_\kappa^*(TI_\kappa)\longrightarrow 0,
\]
且 \(\mathcal V_x=T_x\big(\Phi_\kappa^{-1}(\Phi_\kappa(x))\big)\)。

**Bd（奇點窗口）** 在 \(\mathrm{Disc}(\Phi_\kappa)\)：\(\dim\mathcal V\) 可能跳變；\(\mathcal V\) 未必等於纖維之切空間；垂直場之流未必全域保 \(\Phi_\kappa\)。保留 Thm A、Thm B 的「保持／生成元」方向，餘需額外條件（如限制在正則開集、半代數規格或完整性假設）。

---

## V. 可理解域的語用規則（壓縮）
合法觀測須先固定 \((T,\cdot)\)、\(\mathrm{Obs}_\star\)、\(\mathrm{Aut}_{\Phi_\kappa}\)、\(\mathrm{Disc}(\Phi_\kappa)\)、公共測試族 \(T_\star\)。在 \(U_\star\) 上，\(\mathrm{Obs}_\star\) 對 \(\mathcal V\) 與 \(\mathrm{Aut}_{\Phi_\kappa}\) 不敏感，輸出可重現。

---

## VI. 一頁壓縮
鏈條 \(U_\star\Rightarrow \delta_\star\Rightarrow X\)。\(\Phi_\kappa=q_\kappa\circ\rho\circ \mathrm{Obs}_\star\)，\(X/{\sim_\kappa}\cong I_\kappa\)，差異存於纖維。  
\(\rho=\mathrm{nf}\circ(\delta_\star/\!\approx)\)，三則：核流不變、自同構不變、正則提升守恆。  
\(r\) 為 \(\mathcal P\)-軌道型對象，群胚版本帶穩定子共軛類，必要時以 germ \(\mathbf j\) 增強以審計邊界接觸。  
\(\mathcal V=\ker d\Phi_\kappa\) 給位移；\(\mathrm{Aut}_{\Phi_\kappa}\) 給偽裝；穿越 \(\mathrm{Disc}\) 給分歧。  
正則域：\(0\to\mathcal V\to TX\xrightarrow{d\Phi_\kappa}\Phi_\kappa^*(TI_\kappa)\to 0\)，且 \(\mathrm{Lie}(\mathrm{Aut}_{\Phi_\kappa}^0)\cong\Gamma(\mathcal V)\)。  
邊界等價於沿 \(\mathrm{Disc}\) 的型式接觸；近奇點執行 Bd 規則。
