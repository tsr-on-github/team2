# coding: UTF-8

'''
入力：ICカードからIDm，外部入力(ファイル入力側)から学生の情報を集めたオブジェクト(学籍番号と名前が対応していれば可)
出力：入力されたIDmに対応した学生の名前と学籍番号を返す
説明：読み取ったIDmから履修者を識別し，履修者リストに存在する場合はそれに対応する学生の名前と学籍番号を返す
    もし履修者リストに該当者が居ない場合は警告文を返す
'''

from types import LambdaType

def comp(IDm:str, students_list:list):
    studentData = []
    warning_text = "あなたは履修者ではありません。退室してください。"
    for i in range(len(students_list)):#リストをfor文で回す
        if IDm==students_list[i]['IDm']:#if文でIDmとリストのIDmを比較
            studentData.append(students_list[i]['名前'])
            studentData.append(students_list[i]['学籍番号'])
            return studentData
    if i == len(students_list) and studentData == []:
        return warning_text

if __name__ == '__main__':
    data = [{"学籍番号":"S001","名前":"相道森","IDm":"012E44A7A5187429"},{"学籍番号":"S002","名前":"揚村巴絵","IDm":"012E44A7A518527D"},{"学籍番号":"S003","名前":"浅井礼子","IDm":"012E44A7A5152B9F"},{"学籍番号":"S004","名前":"荒松晴一","IDm":"012E44A7A518807A"},{"学籍番号":"S005","名前":"有福政昭","IDm":"012E44A7A5159B8D"},{"学籍番号":"S006","名前":"飯坂新司","IDm":"012E44A7A515A75C"},{"学籍番号":"S007","名前":"池澄晃樹","IDm":"012E44A7A5158B31"},{"学籍番号":"S008","名前":"石長佐久子","IDm":"012E44A7A5154DAF"},{"学籍番号":"S009","名前":"泉川弘仁","IDm":"012E44A7A51549A3"},{"学籍番号":"S010","名前":"礒田睦史","IDm":"012E44A7A5126FBC"},{"学籍番号":"S011","名前":"市之瀬龍治","IDm":"012E44A7A5156DA9"},{"学籍番号":"S012","名前":"井手窪克茂","IDm":"012E44A7A51253C2"},{"学籍番号":"S013","名前":"井内早絵子","IDm":"012E44A7A5157F61"},{"学籍番号":"S014","名前":"入澤結香","IDm":"012E44A7A5156A5A"},{"学籍番号":"S015","名前":"印公一","IDm":"012E44A7A5117921"},{"学籍番号":"S016","名前":"浦松拓治","IDm":"012E44A7A512676D"},{"学籍番号":"S017","名前":"恵島康道","IDm":"012E44A7A515B97D"},{"学籍番号":"S018","名前":"越前広","IDm":"012E44A7A5159FA1"},{"学籍番号":"S019","名前":"江積幸廣","IDm":"012E44A7A51581AB"},{"学籍番号":"S020","名前":"太内信章","IDm":"012E44A7A5153B80"},{"学籍番号":"S021","名前":"太田島映実","IDm":"012E44A7A5159A7E"},{"学籍番号":"S022","名前":"大舘俊幸","IDm":"012E44A7A5123042"},{"学籍番号":"S023","名前":"大野貴暁","IDm":"012E44A7A5123C39"},{"学籍番号":"S024","名前":"大波多英三","IDm":"012E44A7A518422C"},{"学籍番号":"S025","名前":"岡松慎一郎","IDm":"012E44A7A5185F32"},{"学籍番号":"S026","名前":"小笠公平","IDm":"012E44A7A5181C82"},{"学籍番号":"S027","名前":"小桐純孝","IDm":"012E44A7A5188A23"},{"学籍番号":"S028","名前":"奥名浩佑","IDm":"012E44A7A5152D87"},{"学籍番号":"S029","名前":"折原はな","IDm":"012E44A7A5185F5A"},{"学籍番号":"S030","名前":"風洋司","IDm":"012E44A7A518A873"},{"学籍番号":"S031","名前":"株竹智信","IDm":"012E44A7A5188F3F"},{"学籍番号":"S032","名前":"茅根信道","IDm":"012E44A7A5189699"},{"学籍番号":"S033","名前":"木口屋一輝","IDm":"012E44A7A5183188"},{"学籍番号":"S034","名前":"城崎成寿","IDm":"012E44A7A518712C"},{"学籍番号":"S035","名前":"貴下紗侑里","IDm":"012E44A7A5187159"},{"学籍番号":"S036","名前":"木野大右","IDm":"012E44A7A5185BA4"},{"学籍番号":"S037","名前":"清冨芳博","IDm":"012E44A7A515B76D"},{"学籍番号":"S038","名前":"木和田英記","IDm":"012E44A7A515B86F"},{"学籍番号":"S039","名前":"久木原光貴","IDm":"012E44A7A5129197"},{"学籍番号":"S040","名前":"串間洋治","IDm":"012E44A7A5123A87"},{"学籍番号":"S041","名前":"久保西敏憲","IDm":"012E44A7A515317D"},{"学籍番号":"S042","名前":"古岩井忠利","IDm":"012E44A7A5116953"},{"学籍番号":"S043","名前":"古橋哲幸","IDm":"012E44A7A5115950"},{"学籍番号":"S044","名前":"小橋川睦夫","IDm":"012E44A7A512663E"},{"学籍番号":"S045","名前":"古明地宏人","IDm":"012E44A7A5124687"},{"学籍番号":"S046","名前":"作花譲","IDm":"012E44A7A51538A8"},{"学籍番号":"S047","名前":"佐中将幸","IDm":"012E44A7A5152584"},{"学籍番号":"S048","名前":"澤元詠一","IDm":"012E44A7A518581E"},{"学籍番号":"S049","名前":"下川香","IDm":"012E44A7A5186DA7"},{"学籍番号":"S050","名前":"下河内公成","IDm":"012E44A7A51596B6"},{"学籍番号":"S051","名前":"白鳥一功","IDm":"012E44A7A512394B"},{"学籍番号":"S052","名前":"末満泰治","IDm":"012E44A7A511AE80"},{"学籍番号":"S053","名前":"隅田庸介","IDm":"012E44A7A515BF58"},{"学籍番号":"S054","名前":"鷹取知也","IDm":"012E44A7A515587D"},{"学籍番号":"S055","名前":"滝田俊明","IDm":"012E44A7A5155770"},{"学籍番号":"S056","名前":"田盛毅彦","IDm":"012E44A7A5111D86"},{"学籍番号":"S057","名前":"田屋洋志","IDm":"012E44A7A5127B45"},{"学籍番号":"S058","名前":"太矢浩将","IDm":"012E44A7A5127497"},{"学籍番号":"S059","名前":"檀野康昭","IDm":"012E44A7A5117AA5"},{"学籍番号":"S060","名前":"鄭健一郎","IDm":"012E44A7A515235C"},{"学籍番号":"S061","名前":"東矢千裕","IDm":"012E44A7A512963F"},{"学籍番号":"S062","名前":"東山勇人","IDm":"012E44A7A5158A31"},{"学籍番号":"S063","名前":"得永希予","IDm":"012E44A7A5113FB6"},{"学籍番号":"S064","名前":"徳益榮","IDm":"012E44A7A5154E78"},{"学籍番号":"S065","名前":"戸津崎礼央奈","IDm":"012E44A7A515A494"},{"学籍番号":"S066","名前":"友藤竜治","IDm":"012E44A7A5188758"},{"学籍番号":"S067","名前":"豊長夢香","IDm":"012E44A7A518528F"},{"学籍番号":"S068","名前":"堂脇一志","IDm":"012E44A7A5185054"},{"学籍番号":"S069","名前":"中妻潔志","IDm":"012E44A7A5188329"},{"学籍番号":"S070","名前":"中松光一","IDm":"012E44A7A515305C"},{"学籍番号":"S071","名前":"西垣内利秀","IDm":"012E44A7A5129B45"},{"学籍番号":"S072","名前":"西関真寿","IDm":"012E44A7A5158998"},{"学籍番号":"S073","名前":"登祐平","IDm":"012E44A7A511AC3F"},{"学籍番号":"S074","名前":"野焼城司","IDm":"012E44A7A515729B"},{"学籍番号":"S075","名前":"萩間敦大","IDm":"012E44A7A5158231"},{"学籍番号":"S076","名前":"波佐間敬次","IDm":"012E44A7A5157E58"},{"学籍番号":"S077","名前":"蓮池夕加里","IDm":"012E44A7A5159335"},{"学籍番号":"S078","名前":"初山孝徳","IDm":"012E44A7A5159E8F"},{"学籍番号":"S079","名前":"波頭直司","IDm":"012E44A7A518269E"},{"学籍番号":"S080","名前":"花本圭祐","IDm":"012E44A7A5184C7F"},{"学籍番号":"S081","名前":"菱泰章","IDm":"012E44A7A5185260"},{"学籍番号":"S082","名前":"日髙貴幸","IDm":"012E44A7A518C560"},{"学籍番号":"S083","名前":"樋爪顕治","IDm":"012E44A7A5182058"},{"学籍番号":"S084","名前":"平野仰","IDm":"012E44A7A51853A1"},{"学籍番号":"S085","名前":"広文哉","IDm":"012E44A7A51875B5"},{"学籍番号":"S086","名前":"深野木茂則","IDm":"012E44A7A518AB94"},{"学籍番号":"S087","名前":"村濱準二","IDm":"012E44A7A518296D"},{"学籍番号":"S088","名前":"矢形具美","IDm":"012E44A7A51869B3"},{"学籍番号":"S089","名前":"八下田駿佑","IDm":"012E44A7A51832AB"},{"学籍番号":"S090","名前":"八武崎榛菜","IDm":"012E44A7A518A145"},{"学籍番号":"S091","名前":"山畑照樹","IDm":"012E44A7A5128D80"},{"学籍番号":"S092","名前":"行田博彦","IDm":"012E44A7A51586AF"},{"学籍番号":"S093","名前":"柞木道典","IDm":"012E44A7A5157F5B"},{"学籍番号":"S094","名前":"弓座義政","IDm":"012E44A7A515207D"},{"学籍番号":"S095","名前":"吉中龍之介","IDm":"012E44A7A5151E70"},{"学籍番号":"S096","名前":"吉馴典和","IDm":"012E44A7A518A8B0"},{"学籍番号":"S097","名前":"吉広清悟","IDm":"012E44A7A5125552"},{"学籍番号":"S098","名前":"吉光幸太","IDm":"012E44A7A518BB99"},{"学籍番号":"S099","名前":"与那豊茂","IDm":"012E44A7A5188331"},{"学籍番号":"S100","名前":"渡利雄祐","IDm":"012E44A7A5112853"}]
    comp_idm = input('input idm > ')
    print(comp(comp_idm, data))
    pass
