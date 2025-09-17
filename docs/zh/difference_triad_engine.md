# 差異三態引擎：位移・偽裝・分歧｜概念卡

> 目的：把「差異如何顯影」壓成一張可手抄、可審計、可回收的卡。三態＝位移（核流）／偽裝（自同構）／分歧（鑑別子）。

---

## 0) 一眼總覽（Summary）
- **管線**：\(X\to U_\star \xrightarrow{\mathrm{Obs}_\star}\delta_\star\xrightarrow{\rho}\mathcal R\xrightarrow{q_\kappa} I_\kappa\)，\(\Phi_\kappa=q_\kappa\circ\rho\circ\mathrm{Obs}_\star\)。
- **三角法則**（正則域）：
  $$
  \mathcal V:=\ker d\Phi_\kappa,\quad
  \mathrm{Lie}(\mathrm{Aut}_{\Phi_\kappa}^0)\cong \Gamma(\mathcal V),\quad
  g_*\mathcal V=\mathcal V\ \ (\forall g\in\mathrm{Aut}_{\Phi_\kappa}).
  $$
- **分歧面**（鑑別子）：
  $$
  \mathrm{Disc}(\Phi_\kappa)=\mathrm{Crit}(\Phi_\kappa)\ \cup\ \Phi_\kappa^{-1}(\Sigma)\ \cup\ J(\rho\circ\mathrm{Obs}_\star).
  $$

---

## 1) 對象（Objects）
- 生成差異空間：\(X=\Delta_{\mathrm{gen}}\)  
- 可理解域：\(U_\star\subseteq X\)，觀測：\(\mathrm{Obs}_\star:U_\star\to\delta_\star\)  
- 形式選擇：\(\rho:\delta_\star\to\mathcal R\)，同一準則投影：\(q_\kappa:\mathcal R\to I_\kappa\)  
- 合成投影：\(\Phi_\kappa:X\to I_\kappa\)（上式）  
- 外觀奇點（像端）：\(\Sigma\subset I_\kappa\)；型式標記：\(\nu:I_\kappa^{\mathrm{reg}}\to\mathcal R\)

---

## 2) 三態（Definitions）
- **位移（Displacement）**：局部不可見運動。  
  $$
  \mathcal V:=\ker d\Phi_\kappa\subset TX;\quad \dot x\in\mathcal V\ \Rightarrow\ \Phi_\kappa(x(t))\ \text{局部常值}.
  $$
- **偽裝（Disguise）**：全域對稱的不可見變化。  
  $$
  \mathrm{Aut}_{\Phi_\kappa}:=\{g:X\to X\mid \Phi_\kappa\circ g=\Phi_\kappa\}.
  $$
- **分歧／去中心（Bifurcation/Deterritorialization）**：穿越鑑別子致型式翻面。  
  $$
  x\ \text{橫切}\ \mathrm{Disc}(\Phi_\kappa)\ \Rightarrow\ \nu(\Phi_\kappa(x(t)))\ \text{更換 }(r_i\to r_j).
  $$

---

## 3) 鑑別子（Discriminant）
- **定義**：
  $$
  \mathrm{Disc}(\Phi_\kappa)=\underbrace{\mathrm{Crit}(\Phi_\kappa)}_{\text{秩掉/幾何機制}}
  \ \cup\ 
  \underbrace{\Phi_\kappa^{-1}(\Sigma)}_{\text{像端摺痕/外觀}}
  \ \cup\ 
  \underbrace{J(\rho\circ\mathrm{Obs}_\star)}_{\text{語義門檻/分類跳躍}}.
  $$
- **像側關係**：\(\Phi_\kappa(\mathrm{Disc}(\Phi_\kappa))\subseteq \Sigma\)。  
- **正則域**：在 \(X\setminus \mathrm{Disc}\) 上，\(\Phi_\kappa\) 為下沉，\(\nu\) 局部常值，\(\rho\) 無跳躍。

---

## 4) 結構定律（Laws）
- **短正合列（正則點）**：
  $$
  0\to \ker d\Phi_\kappa\to TX\xrightarrow{\,d\Phi_\kappa\,}\Phi_\kappa^*(TI_\kappa)\to 0.
  $$
- **保持律**：\(g_*(\ker d\Phi_\kappa)=\ker d\Phi_\kappa\)，且 \(g(\mathrm{Disc})\subseteq \mathrm{Disc}\)。  
- **Lie 對應（正則域）**：\(\mathrm{Lie}(\mathrm{Aut}_{\Phi_\kappa}^0)\cong \Gamma(\ker d\Phi_\kappa)\)。

---

## 5) 診斷法（Diagnostics）
- **位移？** 查 \(d\Phi_\kappa(x)\,v=0\)（不可見方向）。  
- **偽裝？** 找 \(g\in\mathrm{Aut}_{\Phi_\kappa}\) 使 \(\Phi_\kappa(gx)=\Phi_\kappa(x)\)。  
- **分歧？** 存在曲線橫切 \(\mathrm{Disc}\) 並觸發 \(\nu:r_i\to r_j\)。  
- **邊界（鑑別版）**：
  $$
  (r_i,r_j)\in \operatorname{Bd}_{\mathrm{disc}}(\mathcal R)\iff 
  \overline{\nu^{-1}(r_i)}\cap \overline{\nu^{-1}(r_j)}\ \text{沿}\ \mathrm{Disc}\ \text{相接}.
  $$

---

## 6) 同一個例子看三態差別（一口氣對照）
**映射**：\(\Phi(x,y)=(x,y^2)\)；**分類**：\(\rho(u,v)=\mathbf{1}_{\{v\ge 1\}}\)  
- **微分臨界**：\(\mathrm{Crit}=\{y=0\}\)（秩掉）。  
- **外觀奇點**：\(\Sigma=\{v=0\}\)（摺痕），\(\Sigma=\Phi(\mathrm{Crit})\)。  
- **形式跳躍**：\(J(\rho\circ\Phi)=\{y=\pm1\}\)（語義門檻），與 Jacobian 無關、可藉改門檻平移。

---

## 7) Gate（可理解域）與公共規範
- 在 \(U_\star\) 上，\(\mathrm{Obs}_\star\) 對 \(\ker d\Phi_\kappa\) 與 \(\mathrm{Aut}_{\Phi_\kappa}\) **不敏感**；  
- 提供 \(T_\star\)（校準、門檻、時間窗、取樣律）；  
- 若跨 \(\mathrm{Disc}\)，**記錄**穿越點與 \(\nu:r_i\to r_j\)。

---

## 8) 易混點（Pitfalls）
- **臨界 vs 奇異**：前者在 domain（機制），後者在 codomain（外觀）。  
- **外觀奇點 vs 形式跳躍**：前者幾何必然；後者語義可選（換門檻就移動/消失）。  
- **位移 vs 偽裝**：位移是一階不可見（\(\ker d\Phi\)）；偽裝是有限對稱（\(\mathrm{Aut}\)）。

---

## 9) 口訣（Handy Mnemonic）
- **位移＝內流**：\(\ker d\Phi\) 抓不可見方向。  
- **偽裝＝對稱**：\(\mathrm{Aut}_\Phi\) 抓不可見動作。  
- **分歧＝翻面**：\(\mathrm{Disc}\) 抓標籤會翻的門檻。  
- **外觀奇點＝世界自己折**；**形式跳躍＝我們劃一刀**。

---

## 10) 手抄模板（Template）
```
Φ = qκ ∘ ρ ∘ Obs★
V = ker dΦ         （位移）
AutΦ               （偽裝）
Disc = Crit ∪ Φ⁻¹(Σ) ∪ J(ρ∘Obs★)  （分歧）

正則域：Lie(AutΦ⁰) ≅ Γ(V),  0→V→TX→Φ*(TI)→0
邊界：沿 Disc 的接觸才成立

檢查步驟：
1) dΦ·v=0? → 位移
2) ∃g: Φ∘g=Φ? → 偽裝
3) 曲線⊥Disc 且 ν 跳? → 分歧/邊界
```

---

## 11) 德勒茲對齊（最短版）
- **差異的生成**：位移（內在強度流）。  
- **重複的擬像**：偽裝（對稱之名的再現）。  
- **去中心事件**：分歧（鑑別子上之系列重編）。
