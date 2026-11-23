---
id: S5
title: "Retrieval-augmented generation"
author: Wikipedia contributors
date: accessed 2026-11-23
url: https://en.wikipedia.org/wiki/Retrieval-augmented_generation
type: encyclopedia (CC BY-SA)
fetched: 2026-11-23
---

# S5 · Wikipedia：Retrieval-augmented generation

> raw 層：取得後不再修改。這裡只存來源資訊與擷取重點（改寫），不轉載原文。

## 擷取重點
- 定義：RAG 是讓大型語言模型在回答前，先從外部資料來源取回並納入新資訊的技術，讓模型能使用訓練資料裡沒有的、特定領域或較新的資訊。
- 流程四步驟：
  1. 準備資料（indexing）：把資料轉成 embedding，存進可以「依意思搜尋」的資料庫。
  2. 檢索（retrieval）：使用者發問時，檢索器找出最相關的文件。
  3. 增強（augmentation）：把檢索到的資訊加進使用者的問題（通常透過 prompt engineering），讓模型有上下文可用。
  4. 生成（generation）：LLM 根據問題與檢索到的文件產生回答。
  - 有些系統會加上額外步驟，例如對檢索結果 rerank、挑選最有用的上下文。
- 名詞：embedding 是「大型向量空間中的數值表示」——把文字變成一串數字，意思相近的文字數字也相近；向量資料庫用來存這些 embedding，能快速找出與問題意思最接近的內容。
- 歷史：這個名詞在 2020 年的論文中提出（第一作者 Patrick Lewis，即 S2），概念是讓語言模型在執行時透過檢索存取外部記憶。
- 好處：
  - 減少幻覺（自信但錯誤的回答）。
  - 新資訊放進外部知識來源即可，不必重新訓練模型，省下運算與金錢成本。
  - 回答可以附上來源，使用者能自己查證。
- 限制：
  - RAG 並不能防止幻覺（原文："RAG does not prevent hallucinations"）。
  - 減少但沒有完全免除重新訓練的需要。
  - 資訊不足時，模型可能仍然給出答案，而不是承認不確定。
  - 來源本身正確，但可能被誤讀，例如一句話被抽離上下文。
  - 來源互相矛盾時，模型可能難以判斷哪個正確，甚至把舊資訊和新資訊混成誤導的答案。
