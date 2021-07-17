# coding: utf-8
# ----- SaveDataFile ----- #
# version 3.9.0 64-bit

from AES256CBC import AES256CBC
import json

# from AES256CBC import AES256CBC

# savedata
# filetype + Base64(AES256CBC(data-container-s))
# | str"t2pecf=="(8-byte) | data-containers(variable-byte)
# data-containers
# | type(8-byte) | key(43-byte) | iv(22-byte) | body(variable-byte) |
# 各コンテナは.でつなぐ
# key
# AES256CBC => 44byte data => remove one padding(=) => 43byte data
# iv
# AES256CBC => 24byte data => remove two padding(=) => 22byte data
# type
# - .prof=== : professors data
# - .student : students data
# - .lecture : lecture data
# - .attend= : attendance data

class SaveDataFile:
    # SaveDataFile.read(filepath)
    # return : {'proffesors': list, 'students' : list. 'lecture': dict, 'attendance': list}
    @staticmethod
    def read(path: str):
        # read file
        try:
            fp = open(path, mode = 'r', encoding = 'utf-8')
        except:
            return None
        encoded:str = fp.read()
        # close
        fp.close()
        # check file type
        if encoded[0:8] != 't2pecf==': # Team2 raspberryPi - Electron Communication File
            return None
        DATA = {}
        for container in encoded[8:].split('.'):
            if container[0:7] == 'prof===':
                # professors
                plain = AES256CBC.decode(container[7:50] + '=', container[50:72] + '==', container[72:])
                DATA['professors'] = json.loads(plain)
            if container[0:7] == 'student':
                # students
                plain = AES256CBC.decode(container[7:50] + '=', container[50:72] + '==', container[72:])
                DATA['students'] = json.loads(plain)
            if container[0:7] == 'lecture':
                # lecture data
                plain = AES256CBC.decode(container[7:50] + '=', container[50:72] + '==', container[72:])
                DATA['lecture'] = json.loads(plain)
            if container[0:7] == 'attend=':
                # attendances
                plain = AES256CBC.decode(container[7:50] + '=', container[50:72] + '==', container[72:])
                DATA['attendances'] = plain.split('\n')
        return DATA
    
    @staticmethod
    def write(dat:object, path:str):
        container: list = []
        if 'professors' in dat:
            cipher = AES256CBC.encode(json.dumps(dat['professors']))
            container.append('prof===' + cipher['key'].replace('=','') + cipher['iv'].replace('=','') + cipher['body'])
        if 'students' in dat:
            cipher = AES256CBC.encode(json.dumps(dat['students']))
            container.append('student' + cipher['key'].replace('=','') + cipher['iv'].replace('=','') + cipher['body'])
        if 'lecture' in dat:
            cipher = AES256CBC.encode(json.dumps(dat['lecture']))
            container.append('lecture' + cipher['key'].replace('=','') + cipher['iv'].replace('=','') + cipher['body'])
        if 'attendances' in dat:
            cipher = AES256CBC.encode('\n'.join(dat['attendances']))
            container.append('attend=' + cipher['key'].replace('=','') + cipher['iv'].replace('=','') + cipher['body'])
        try:
            fp = open(path, mode = 'w', encoding = 'utf-8')
        except:
            return False
        fp.write('t2pecf==' + '.'.join(container))
        fp.close()
        return True

class DummySaveDataFile:
    def read():
        dat:dict = {}
        dat['students'] = [{"id":"S001","name":"相道森","yomi":"あいどうしん","sex":"男","idm":"012E44A7A5187429"},{"id":"S002","name":"揚村巴絵","yomi":"あげむらともえ","sex":"女","idm":"012E44A7A518527D"},{"id":"S003","name":"浅井礼子","yomi":"あさいれいこ","sex":"女","idm":"012E44A7A5152B9F"},{"id":"S004","name":"荒松晴一","yomi":"あらまつせいいち","sex":"男","idm":"012E44A7A518807A"},{"id":"S005","name":"有福政昭","yomi":"ありふくまさあき","sex":"男","idm":"012E44A7A5159B8D"},{"id":"S006","name":"飯坂新司","yomi":"いいざかしんじ","sex":"男","idm":"012E44A7A515A75C"},{"id":"S007","name":"池澄晃樹","yomi":"いけずみこうき","sex":"男","idm":"012E44A7A5158B31"},{"id":"S008","name":"石長佐久子","yomi":"いしながさくこ","sex":"女","idm":"012E44A7A5154DAF"},{"id":"S009","name":"泉川弘仁","yomi":"いずかわひろひと","sex":"男","idm":"012E44A7A51549A3"},{"id":"S010","name":"礒田睦史","yomi":"いそたあつし","sex":"男","idm":"012E44A7A5126FBC"},{"id":"S011","name":"市之瀬龍治","yomi":"いちのせりゅうじ","sex":"男","idm":"012E44A7A5156DA9"},{"id":"S012","name":"井手窪克茂","yomi":"いでくぼかつしげ","sex":"男","idm":"012E44A7A51253C2"},{"id":"S013","name":"井内早絵子","yomi":"いないさえこ","sex":"女","idm":"012E44A7A5157F61"},{"id":"S014","name":"入澤結香","yomi":"いりさわゆいか","sex":"女","idm":"012E44A7A5156A5A"},{"id":"S015","name":"印公一","yomi":"いんきみかず","sex":"男","idm":"012E44A7A5117921"},{"id":"S016","name":"浦松拓治","yomi":"うらまつたくじ","sex":"男","idm":"012E44A7A512676D"},{"id":"S017","name":"恵島康道","yomi":"えじまやすみち","sex":"男","idm":"012E44A7A515B97D"},{"id":"S018","name":"越前広","yomi":"えちぜんひろし","sex":"男","idm":"012E44A7A5159FA1"},{"id":"S019","name":"江積幸廣","yomi":"えづみゆきひろ","sex":"男","idm":"012E44A7A51581AB"},{"id":"S020","name":"太内信章","yomi":"おおうちのぶあき","sex":"男","idm":"012E44A7A5153B80"},{"id":"S021","name":"太田島映実","yomi":"おおたじまえみ","sex":"女","idm":"012E44A7A5159A7E"},{"id":"S022","name":"大舘俊幸","yomi":"おおだてとしゆき","sex":"男","idm":"012E44A7A5123042"},{"id":"S023","name":"大野貴暁","yomi":"おおのたかあき","sex":"男","idm":"012E44A7A5123C39"},{"id":"S024","name":"大波多英三","yomi":"おおはたえいぞう","sex":"男","idm":"012E44A7A518422C"},{"id":"S025","name":"岡松慎一郎","yomi":"おかまつしんいちろう","sex":"男","idm":"012E44A7A5185F32"},{"id":"S026","name":"小笠公平","yomi":"おがさこうへい","sex":"男","idm":"012E44A7A5181C82"},{"id":"S027","name":"小桐純孝","yomi":"おぎりすみたか","sex":"男","idm":"012E44A7A5188A23"},{"id":"S028","name":"奥名浩佑","yomi":"おくなこうすけ","sex":"男","idm":"012E44A7A5152D87"},{"id":"S029","name":"折原はな","yomi":"おりはらはな","sex":"女","idm":"012E44A7A5185F5A"},{"id":"S030","name":"風洋司","yomi":"かぜようじ","sex":"男","idm":"012E44A7A518A873"},{"id":"S031","name":"株竹智信","yomi":"かぶたけとものぶ","sex":"男","idm":"012E44A7A5188F3F"},{"id":"S032","name":"茅根信道","yomi":"かやねのぶみち","sex":"男","idm":"012E44A7A5189699"},{"id":"S033","name":"木口屋一輝","yomi":"きぐちやかずき","sex":"男","idm":"012E44A7A5183188"},{"id":"S034","name":"城崎成寿","yomi":"きざきなりひさ","sex":"男","idm":"012E44A7A518712C"},{"id":"S035","name":"貴下紗侑里","yomi":"きしたさゆり","sex":"女","idm":"012E44A7A5187159"},{"id":"S036","name":"木野大右","yomi":"きのだいすけ","sex":"男","idm":"012E44A7A5185BA4"},{"id":"S037","name":"清冨芳博","yomi":"きよとみよしひろ","sex":"男","idm":"012E44A7A515B76D"},{"id":"S038","name":"木和田英記","yomi":"きわだひでき","sex":"男","idm":"012E44A7A515B86F"},{"id":"S039","name":"久木原光貴","yomi":"くきはらこうき","sex":"男","idm":"012E44A7A5129197"},{"id":"S040","name":"串間洋治","yomi":"くしまようじ","sex":"男","idm":"012E44A7A5123A87"},{"id":"S041","name":"久保西敏憲","yomi":"くぼにしとしのり","sex":"男","idm":"012E44A7A515317D"},{"id":"S042","name":"古岩井忠利","yomi":"こいわいただとし","sex":"男","idm":"012E44A7A5116953"},{"id":"S043","name":"古橋哲幸","yomi":"こはしてつゆき","sex":"男","idm":"012E44A7A5115950"},{"id":"S044","name":"小橋川睦夫","yomi":"こばしかわむつお","sex":"男","idm":"012E44A7A512663E"},{"id":"S045","name":"古明地宏人","yomi":"こめいじひろと","sex":"男","idm":"012E44A7A5124687"},{"id":"S046","name":"作花譲","yomi":"さくかじょう","sex":"男","idm":"012E44A7A51538A8"},{"id":"S047","name":"佐中将幸","yomi":"さなかまさゆき","sex":"男","idm":"012E44A7A5152584"},{"id":"S048","name":"澤元詠一","yomi":"さわもとえいいち","sex":"男","idm":"012E44A7A518581E"},{"id":"S049","name":"下川香","yomi":"しもかわかおる","sex":"女","idm":"012E44A7A5186DA7"},{"id":"S050","name":"下河内公成","yomi":"しもこうちきみなり","sex":"男","idm":"012E44A7A51596B6"},{"id":"S051","name":"白鳥一功","yomi":"しらとりかずのり","sex":"男","idm":"012E44A7A512394B"},{"id":"S052","name":"末満泰治","yomi":"すえみつたいじ","sex":"男","idm":"012E44A7A511AE80"},{"id":"S053","name":"隅田庸介","yomi":"すみたようすけ","sex":"男","idm":"012E44A7A515BF58"},{"id":"S054","name":"鷹取知也","yomi":"たかとりともや","sex":"男","idm":"012E44A7A515587D"},{"id":"S055","name":"滝田俊明","yomi":"たきたとしあき","sex":"男","idm":"012E44A7A5155770"},{"id":"S056","name":"田盛毅彦","yomi":"たもりたけひこ","sex":"男","idm":"012E44A7A5111D86"},{"id":"S057","name":"田屋洋志","yomi":"たやひろし","sex":"男","idm":"012E44A7A5127B45"},{"id":"S058","name":"太矢浩将","yomi":"たやひろまさ","sex":"男","idm":"012E44A7A5127497"},{"id":"S059","name":"檀野康昭","yomi":"だんのやすあき","sex":"男","idm":"012E44A7A5117AA5"},{"id":"S060","name":"鄭健一郎","yomi":"ちょんけんいちろう","sex":"男","idm":"012E44A7A515235C"},{"id":"S061","name":"東矢千裕","yomi":"とうやちひろ","sex":"男","idm":"012E44A7A512963F"},{"id":"S062","name":"東山勇人","yomi":"とうやまゆうと","sex":"男","idm":"012E44A7A5158A31"},{"id":"S063","name":"得永希予","yomi":"とくながきよ","sex":"女","idm":"012E44A7A5113FB6"},{"id":"S064","name":"徳益榮","yomi":"とくますさかえ","sex":"男","idm":"012E44A7A5154E78"},{"id":"S065","name":"戸津崎礼央奈","yomi":"とつざきれおな","sex":"女","idm":"012E44A7A515A494"},{"id":"S066","name":"友藤竜治","yomi":"ともふじりゅうじ","sex":"男","idm":"012E44A7A5188758"},{"id":"S067","name":"豊長夢香","yomi":"とよながゆか","sex":"女","idm":"012E44A7A518528F"},{"id":"S068","name":"堂脇一志","yomi":"どうわきひとし","sex":"男","idm":"012E44A7A5185054"},{"id":"S069","name":"中妻潔志","yomi":"なかつまきよし","sex":"男","idm":"012E44A7A5188329"},{"id":"S070","name":"中松光一","yomi":"なかまつこういち","sex":"男","idm":"012E44A7A515305C"},{"id":"S071","name":"西垣内利秀","yomi":"にしごうちとしひで","sex":"男","idm":"012E44A7A5129B45"},{"id":"S072","name":"西関真寿","yomi":"にしぜきまさとし","sex":"男","idm":"012E44A7A5158998"},{"id":"S073","name":"登祐平","yomi":"のぼるゆうへい","sex":"男","idm":"012E44A7A511AC3F"},{"id":"S074","name":"野焼城司","yomi":"のやきじょうじ","sex":"男","idm":"012E44A7A515729B"},{"id":"S075","name":"萩間敦大","yomi":"はぎまあつひろ","sex":"男","idm":"012E44A7A5158231"},{"id":"S076","name":"波佐間敬次","yomi":"はざまけいじ","sex":"男","idm":"012E44A7A5157E58"},{"id":"S077","name":"蓮池夕加里","yomi":"はすいけゆかり","sex":"女","idm":"012E44A7A5159335"},{"id":"S078","name":"初山孝徳","yomi":"はつやまたかのり","sex":"男","idm":"012E44A7A5159E8F"},{"id":"S079","name":"波頭直司","yomi":"はとうなおし","sex":"男","idm":"012E44A7A518269E"},{"id":"S080","name":"花本圭祐","yomi":"はなもとけいすけ","sex":"男","idm":"012E44A7A5184C7F"},{"id":"S081","name":"菱泰章","yomi":"ひしやすあき","sex":"男","idm":"012E44A7A5185260"},{"id":"S082","name":"日髙貴幸","yomi":"ひだかたかゆき","sex":"男","idm":"012E44A7A518C560"},{"id":"S083","name":"樋爪顕治","yomi":"ひづめけんじ","sex":"男","idm":"012E44A7A5182058"},{"id":"S084","name":"平野仰","yomi":"ひらのあおぐ","sex":"男","idm":"012E44A7A51853A1"},{"id":"S085","name":"広文哉","yomi":"ひろふみや","sex":"男","idm":"012E44A7A51875B5"},{"id":"S086","name":"深野木茂則","yomi":"ふかのきしげのり","sex":"男","idm":"012E44A7A518AB94"},{"id":"S087","name":"村濱準二","yomi":"むらはまじゅんじ","sex":"男","idm":"012E44A7A518296D"},{"id":"S088","name":"矢形具美","yomi":"やかたともみ","sex":"女","idm":"012E44A7A51869B3"},{"id":"S089","name":"八下田駿佑","yomi":"やげたしゅんすけ","sex":"男","idm":"012E44A7A51832AB"},{"id":"S090","name":"八武崎榛菜","yomi":"やぶさきはるな","sex":"女","idm":"012E44A7A518A145"},{"id":"S091","name":"山畑照樹","yomi":"やまばたてるき","sex":"男","idm":"012E44A7A5128D80"},{"id":"S092","name":"行田博彦","yomi":"ゆきたひろひこ","sex":"男","idm":"012E44A7A51586AF"},{"id":"S093","name":"柞木道典","yomi":"ゆすのきみちのり","sex":"男","idm":"012E44A7A5157F5B"},{"id":"S094","name":"弓座義政","yomi":"ゆみざよしまさ","sex":"男","idm":"012E44A7A515207D"},{"id":"S095","name":"吉中龍之介","yomi":"よしなかりゅうのすけ","sex":"男","idm":"012E44A7A5151E70"},{"id":"S096","name":"吉馴典和","yomi":"よしなれのりかず","sex":"男","idm":"012E44A7A518A8B0"},{"id":"S097","name":"吉広清悟","yomi":"よしひろせいご","sex":"男","idm":"012E44A7A5125552"},{"id":"S098","name":"吉光幸太","yomi":"よしみつこうた","sex":"男","idm":"012E44A7A518BB99"},{"id":"S099","name":"与那豊茂","yomi":"よなとよしげ","sex":"男","idm":"012E44A7A5188331"},{"id":"S100","name":"渡利雄祐","yomi":"わたりゆうすけ","sex":"男","idm":"012E44A7A5112853"}]
        dat['professors'] = [{"id":"P001","name":"秋場紀明","yomi":"あきばのりあき","sex":"男","lect":["応用数学","数学演習"]},{"id":"P002","name":"有本太志","yomi":"ありもとたいし","sex":"男","lect":["保健体育"]},{"id":"P003","name":"大島恵理子","yomi":"おおしまえりこ","sex":"女","lect":["心理学"]},{"id":"P004","name":"鬼野極","yomi":"おにのきわむ","sex":"男","lect":["プログラミング"]},{"id":"P005","name":"高坂信之","yomi":"こうさかのぶゆき","sex":"男","lect":["電磁気学"]},{"id":"P006","name":"澤井信彦","yomi":"さわいのぶひこ","sex":"男","lect":["情報ネットワーク"]},{"id":"P007","name":"進藤健児","yomi":"しんどうけんじ","sex":"男","lect":["システム開発演習","情報工学実習"]},{"id":"P008","name":"武山寛子","yomi":"たけやまひろこ","sex":"女","lect":["情報理論","アルゴリズムとデータ構造"]},{"id":"P009","name":"土橋健二","yomi":"つちはしけんじ","sex":"男","lect":["経済学"]},{"id":"P010","name":"豊崎史朗","yomi":"とよさきしろう","sex":"男","lect":["英会話"]},{"id":"P011","name":"西田順","yomi":"にしだじゅん","sex":"男","lect":["教養英語","科学英語"]},{"id":"P012","name":"古澤範人","yomi":"ふるさわのりひと","sex":"男","lect":["物理学"]},{"id":"P013","name":"細川靖司","yomi":"ほそかわやすし","sex":"男","lect":["コミュニケーション入門"]},{"id":"P014","name":"水沼勝敏","yomi":"みずぬまかつとし","sex":"男","lect":["電子回路学"]},{"id":"P015","name":"三谷和巳","yomi":"みつやかずみ","sex":"男","lect":["信号処理"]},{"id":"P016","name":"鷲見和紀","yomi":"わしみかずのり","sex":"男","lect":["文学・文化学"]}]
        dat['lecture'] = {"id":"T4","name":"応用数学","professor_id":"P001","professor_name":"秋場紀明","start":"14:40","end":"16:10","attend":"10","late":"30","exam":"あり","num_students":"100","students":["S001","S002","S003","S004","S005","S006","S007","S008","S009","S010","S011","S012","S013","S014","S015","S016","S017","S018","S019","S020","S021","S022","S023","S024","S025","S026","S027","S028","S029","S030","S031","S032","S033","S034","S035","S036","S037","S038","S039","S040","S041","S042","S043","S044","S045","S046","S047","S048","S049","S050","S051","S052","S053","S054","S055","S056","S057","S058","S059","S060","S061","S062","S063","S064","S065","S066","S067","S068","S069","S070","S071","S072","S073","S074","S075","S076","S077","S078","S079","S080","S081","S082","S083","S084","S085","S086","S087","S088","S089","S090","S091","S092","S093","S094","S095","S096","S097","S098","S099","S100"]}
        return dat
    def write(dat: dict, path:str):
        return True


if __name__ == '__main__':
    data = {}
    data['professors'] = [{'name':'b', 'lect':['BrainFuck', 'JavaScript', 'PHP']}, {'name':'hrm', 'lect':['c#', 'vim', 'Python']}, {'name':'hatena', 'lect':[]}]
    data['students'] = [{'name':'aym', 'id':'ayumu'}, {'name':'hst', 'id':'daigakusei'},{'name':'tnhs', 'id':'nihachi16'}]
    data['lecture'] = {'name':'Brainfuck', 'id':'bf', 'start':'18:00', 'late':'30', 'students':['ayumu','daigakusei','nihachi16']}
    data['attendances'] = ['ayumu 2021-07-17 16:28:18', 'daigakusei 2021-07-17 16:29:55', 'nihachi16 2021-07-17 16:30:07']
    SaveDataFile.write(data, './test/t2pecf/sdf-test.dat')
    dat = SaveDataFile.read('./test/t2pecf/sdf-test.dat')
    print(dat['professors'])
    print(dat['students'])
    print(dat['lecture'])
    print(dat['attendances'])
