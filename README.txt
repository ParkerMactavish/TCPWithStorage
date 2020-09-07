./TCPWithStorage
	本身是一個Unity Project，可以在./Asset/Script中找到TCPTest.cs，要儲存的數值是TCPTest.cs/Line25所宣告的Diff，Diff在接收到python傳送的資料並且接收到空白鍵按下的指令後，便會計算出Diff。
	空白鍵的按下時間是由ReactTime所儲存，並且會減去TriggerredTime得到Diff，關於TriggerredTime會在testSocketClient.py中說明。
	Socket的設定是會聽127.0.0.1:8000 port的資料。

./TCPWithStorage/test_PythonSocket/testSocketClient.py
	使用`python testSocketClient.py'可以驅動，會連接127.0.0.1:8000，並且在呼叫的那刻傳送time.time()*1000的浮點數表示當前的Unix毫秒數，在TCPTest.cs中會由recvData接收，並且轉成recvStr字串後會由Double.Parse轉換成TriggerredTime儲存。
	Diff本身是由ReactTime-TriggerredTime所儲存。

## TODO
1. 新增一個Excel並且能夠進行Diff的寫入。
2. 每個橫排共有四樣東西紀錄，(1)本次刺激是本次實驗的第幾次、(2)施測者傳遞指令的方向、(3)受測者反應的方向、(4)反應時間。
3. 幫我留一個空的欄位以表示受測者反應的方向。
4. 幫我留一個空的欄位以表示施測者傳遞指令的方向。
5. 在關閉前儲存本次實驗所有刺激的反應時間總和。