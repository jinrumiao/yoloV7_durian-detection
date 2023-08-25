
# yoloV7實作-榴槤、釋迦、波羅蜜辨識

前一陣子在網路上看到了有關榴槤的影片，看完後就突然有個想法：不如來作一個榴槤主題的物件辨識試試看。思考了一番後，只辨識榴槤似乎有點單調，那就加入幾個跟榴槤長很像的水果一起辨識看看，所以便有了這個實作。

使用yoloV7訓練物件辨識模型，在這個實作中圖片資料集共有兩個，第一個為在網路上找圖片手動儲存，這個資料集的特色是圖片品質較高，但是數量較少；第二個為使用爬蟲在網路上抓取相關圖片，而這個資料集資料量就比較多了，但圖片的品質較差，圖片蒐集完之後，圖片是使用Roboflow進行人工標註。

Roboflow: https://roboflow.com/




## 資料集介紹

1、榴槤照片20張、釋迦照片10張、波羅蜜照片10張。

2、榴槤照片71張、釋迦照片58張、波羅蜜照片67張。


## 實作流程

![](https://imgur.com/voYSOAH.png)

## 實驗介紹

![Imgur](https://imgur.com/pic3NWf.png)
## 實作結果

![Imgur](https://imgur.com/82ymnXB.png)
![Imgur](https://imgur.com/UibGx52.png)
![Imgur](https://imgur.com/U5pnDF8.png)

![Imgur](https://imgur.com/iU6ryHQ.png)
![Imgur](https://imgur.com/yVMFLXJ.png)
![Imgur](https://imgur.com/5IUTlr7.png)
## 實作結果

![Imgur](https://imgur.com/U94ILr7.png)

1、從上方表格來看，綜合預測結果以及訓練時間的狀況下，實驗2的條件最佳，從實驗1與實驗2的對比，可以知道資料集數量多對於模型的預測能力是有幫助的；從實驗2與實驗3的對比，可以知道當資料集數量並沒有到達一定數量時，訓練次數提高過多，會讓模型預測能力下降，推測應該是過擬和。

2、後續可以使用大資料集將訓練次數調整為100~300次來測試是否會有較佳的預測結果。
