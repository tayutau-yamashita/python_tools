# coding: utf-8

fileName = ""
className = ""
parameterList = []
sourceString = ""

# ファイル読み込み検証
#f = open("input/input.txt")
#data1 = f.read()
#f.close()
#
#print(data1)

# _の次の文字を大文字にして、_を削除する
def fileNameCustom(intext, offset):
    pos = intext.find("_", offset) 
    if pos == -1:
        ret = intext.replace("_", "")
        return ret
    else:
        li = list(intext)
        upper = intext[pos+1].upper()
        li[pos+1] = upper
        intext = "".join(li)
        return fileNameCustom(intext, pos+1)

# 文字列を検証して、パラメータリストの作成
def createParameter(intext, offset, culmns):
    global parameterList
    start = intext.find("|", offset)
    if start != -1:
        end = intext.find("|", start+1)
        if end != -1:
            string = intext[start+1:end]
            parameterList.append(string)
            culmns = culmns + 1
            if culmns >= 3:
                return
            createParameter(intext, end, culmns)

#teststring = "| aaaa| bbb| cc| D"
#createParameter(teststring, 0)
#print parameterList

f = open("input/input.txt")
lines2 = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
for line in lines2:
    print line
    if line.find("h3", 0) != -1:
        #タイトルから、クラス名とファイル名作成作成
        output1 = line.replace("h3. ", "");
        output2 = fileNameCustom(output1, 0)
        output2 = output2.replace('\xEF\xBB\xBF', "")#今は邪魔なので BOM削除
        #頭文字大文字に
        li = list(output2)
        upper = li[0].upper()
        li[0] = upper
        output2 = "".join(li)
        fileName = output2
        className = output2
    
    elif line.find("|", 0) != -1 and line.find("_.field name", 0) == -1:
        #リスト情報から、パラメータ作成
        createParameter(line, 0, 0)

print parameterList 

sourceString += "using System.Collections;" + "\n"
sourceString += "//****************************************************************" + "\n"
sourceString += "/// <summary>" + "\n"
sourceString += "TODOコメント入力してください" + "\n"
sourceString += "/// ※詳細と最新の確認はWIKIを参照の事。<br/>" + "\n"
sourceString += "/// </summary>" + "\n"
sourceString += "//****************************************************************" + "\n"
sourceString += "[System.Serializable]" + "\n"

#-----ここに、クラス名作成
className = className.strip()

sourceString += "internal class " + className + " : DataBasis {" + "\n"
#-----

sourceString += "	" + "\n"
sourceString += "	//================================================================" + "\n"
sourceString += "	// パラメータ。" + "\n"
sourceString += "	// ※データのパラメータのメンバー。" + "\n"
sourceString += "	//================================================================" + "\n"
sourceString += "	" + "\n"

# ここから、Listを回して、変数作成
dataKind = 3
dataNum = len(parameterList) / dataKind
print len(parameterList)

for loop in range(dataNum) :
    offset = loop * dataKind
    sourceString += "	/// <summary>" + parameterList[offset+2] + "</summary>" + "\n"
    if parameterList[offset+1].find("int") != -1:
        sourceString += "	internal readonly " + parameterList[offset+1] + " " + parameterList[offset+0] + " = 0;" + "\n"
    elif parameterList[offset+1].find("string") != -1:
        sourceString += "	internal readonly " + parameterList[offset+1] + " " + parameterList[offset+0] + ' = "";' + "\n"


# ここまで

sourceString += "" + "\n"
sourceString += "}" + "\n"

fileName = fileName.strip()

f = open(fileName + ".cs", 'wb') # 書き込みモードで開く
f.write(sourceString) # 引数の文字列をファイルに書き込む
f.close() # ファイルを閉じる

# ファイル(クラス)名をパースする

#commentAPI = ""
#comment = ""
#endpointURL = ""
##|_.API| 課金石購入(Web版用)|
##|_.EndpointURL|http://servername/api/premium_item/purchase_premium_item_web|
##|_.Description| 課金石を購入する。|
#
#className = ""
##|_.EndpointURL|http://servername/api/premium_item/purchase_premium_item_web|
##Message+上の最後単語をUpperで対応してみるか
#
#requestJson = ""
##h2. リクエストJSON
##
##|_.field name|_.type|_.required|_.name|_.description|_.value|
##| premium_item_id| int| ○| 課金石商品ID| 購入する[[SpecStaticDataPremiumItems|課金石商品マスター]]のID| [[SpecApiGetPremiumItems|get_premium_items API]]で送り返した課金石商品の配列内のIDを設定します|
##
#
#responseJson
##h2. レスポンスJSON
##
##|_.field name|_.type|_.name|_.description|_.value|
##| user_detail| object(user)| ユーザー情報| 更新された[[SpecApiPurchasePremiumItemWeb#user|ユーザー情報]]||
##| user_delivery_item| object(user_delivery_item)| プレゼントボックスアイテム| 追加された[[SpecApiPurchasePremiumItemWeb#user_delivery_item|プレゼントボックスアイテム]]<br>※user_delivery_item はクライアント側では保持されていないため更新不要|おまけアイテムがない場合は null|
#
#outputSource = ""
#outputSource += "using UnityEngine;" + "\n"
#outputSource += "using System.Collections;" + "\n"
#outputSource += "using System.Collections.Generic;" + "\n"
#outputSource += "" + "\n"
#outputSource += "//****************************************************************" + "\n"
#outputSource += "/// <summary>" + "\n"
#
##コメント
#outputSource += "/// API:商品購入。<br/>" + "\n"
#outputSource += "/// 通信の各メッセージクラス。<br/>" + "\n"
##----
#
#outputSource += "/// ※詳細と最新の確認はWIKIを参照の事。<br/>" + "\n"
#outputSource += "/// </summary>" + "\n"
#outputSource += "//****************************************************************" + "\n"
#outputSource += "[System.Serializable]" + "\n"
#
##クラス名
#outputSource += "internal sealed class MessagePurchaseChargeShopItem : Message {" + "\n"
##-----
#
#outputSource += "	" + "\n"
#outputSource += "	//================================================================" + "\n"
#outputSource += "	// 定義。" + "\n"
#outputSource += "	//================================================================" + "\n"
#outputSource += "	" + "\n"
#outputSource += "	/// <summary>リクエストURL構築用フォーマット(0=サーバー名,1=APIバージョンURL)。</summary>" + "\n"
#outputSource += "	[System.Reflection.Obfuscation(Exclude = true)]" + "\n"
#
##リクエストURL
#outputSource += "	internal static readonly string URL = "//{0}/{1}/shop/purchase_item";" + "\n"
##-----
#
##送信データあれば
#outputSource += "" + "\n"
#outputSource += "	//****************************************************************" + "\n"
#outputSource += "	/// <summary>送信データ。</summary>" + "\n"
#outputSource += "	//****************************************************************" + "\n"
#outputSource += "	[System.Serializable]" + "\n"
##ここの文字列が変わる
#outputSource += "	internal class MessageSendData : DataBasis {" + "\n"
#outputSource += "		/// <summary>商品ID。</summary>" + "\n"
#outputSource += "		internal int shop_item_id = 0;" + "\n"
#outputSource += "		/// <summary>購入タイプ。</summary>" + "\n"
#outputSource += "		internal int pay_type = 0;" + "\n"
#outputSource += "		/// <summary>価格。</summary>" + "\n"
#outputSource += "		internal int price = 0;" + "\n"
#outputSource += "	}" + "\n"
##
#outputSource += "	" + "\n"
##-----
#
##受信データ
#outputSource += "	//****************************************************************" + "\n"
#outputSource += "	/// <summary>受信データ。</summary>" + "\n"
#outputSource += "	//****************************************************************" + "\n"
#outputSource += "	[System.Serializable]" + "\n"
##ここの文字列が変わる
#outputSource += "	internal class MessageReceiveData : DataBasis {" + "\n"
#outputSource += "		/// <summary>ユーザー情報。</summary>" + "\n"
#outputSource += "		internal UserData user = null;" + "\n"
#outputSource += "		/// <summary>ユーザーアイテム。</summary>" + "\n"
#outputSource += "		internal List<UserItem> user_items = null;" + "\n"
#outputSource += "		/// <summary>ユーザーアイテム。</summary>" + "\n"
#outputSource += "		internal List<UserCard> user_cards = null;" + "\n"
#outputSource += "		/// <summary>ユーザーアイテム。</summary>" + "\n"
#outputSource += "		internal List<UserProgram> user_programs = null;" + "\n"
#outputSource += "		/// <summary>ユーザーアイテム。</summary>" + "\n"
#outputSource += "		internal List<UserCostume> user_costumes = null;" + "\n"
#outputSource += "	}" + "\n"
##
#outputSource += "" + "\n"
##-----
#
#
#outputSource += "	//================================================================" + "\n"
#outputSource += "	// メソッド。" + "\n"
#outputSource += "	//================================================================" + "\n"
#outputSource += "	" + "\n"
#outputSource += "	//------------------------------------------------------------" + "\n"
#outputSource += "	/// <summary>" + "\n"
#outputSource += "	///	コンストラクタ。<br/>" + "\n"
#outputSource += "	/// </summary>" + "\n"
#outputSource += "	/// <param name="sendData">送信データ。</param>" + "\n"
#outputSource += "	/// <param name="onFinished">通信の結果受取先。</param>" + "\n"
#outputSource += "	//------------------------------------------------------------" + "\n"
##ここの文字列が変わる
#outputSource += "	internal MessagePurchaseChargeShopItem(MessageSendData sendData, FinishedCallback onFinished) : base(onFinished) {" + "\n"
##-----
#outputSource += "		this.SendData = sendData;" + "\n"
#outputSource += "	}" + "\n"
#outputSource += "}" + "\n"
#
