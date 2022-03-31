import copy
import testlib
import random
from ddt import file_data, ddt, data, unpack

import program03 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, ls, testo, expected_lista, expected_parola, expected_ls):
        '''Implementazione del test
            - ls:       lista di parole
            - testo:    testo in cui cercarle
            - expected_lista:   lista di parole risultato
            - expected_parola:  parola apparsa piu' volte nel testo
            - expected_ls:      parole non apparse (ls modificata)
        '''
        ls1_bis = copy.deepcopy(ls)
        res = program.es3(ls1_bis, testo)
        self.check(type(res), tuple,         None, 'non viene restituita una tupla')
        self.check(len(res),  2,             None, 'non viene restituita una tupla di 2 elementi')
        lista, parola = res
        # print('\n\n\tls',len(ls),'lista', len(expected_lista), 'parola', len(expected_parola), 'ls', len(expected_ls))
        self.check(lista,   expected_lista,  None, 'non viene restituita la lista corretta')
        self.check(parola,  expected_parola, None, 'non viene restituita la parola corretta')
        self.check(ls1_bis, expected_ls,     None, 'non viene modificata correttamente la lista in input')
        return 1

    @file_data('test_03.json')
    def test_letto_da_json(self, ls, testo, expected_lista, expected_parola, expected_ls):
        '''Versione che prende i dati dal file Json'''
        return self.do_test(ls, testo, expected_lista, expected_parola, expected_ls)

    @file_data('test_03.json')
    def test_letto_da_json_e_moltiplicato_per_1000(self, ls, testo, expected_lista, expected_parola, expected_ls):
        '''Versione che prende i dati dal file Json'''
        testo = testo*1000
        return self.do_test(ls, testo, expected_lista, expected_parola, expected_ls)

    @file_data('test_03.json')
    def test_letto_da_json_e_moltiplicato_per_2000(self, ls, testo, expected_lista, expected_parola, expected_ls):
        '''Versione che prende i dati dal file Json'''
        testo = testo*2000
        return self.do_test(ls, testo, expected_lista, expected_parola, expected_ls)

    def test_segreto(self):
        '''tra 1000 parole di lunghezza da 1 a 20, concatenate 1000 scelte a caso'''
        # parole = set()
        # for _ in range(1000):
        #     chars = [ chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(1, 20))]
        #     word = ''.join(chars)
        #     for p in parole:
        #         if p[:len(word)] == word or word[:len(p)] == p:
        #             break
        #     else:
        #         parole.add(word)
        # parole = list(parole)
        # print(parole)
        # testo = ''
        # for _ in range(1000):
        #     testo += random.choice(parole)
        # print(testo)
        parole = ['umhv', 'gyhdszwyawyqiuut', 'ukwbrckvmrbavxshsq', 'ypagqbw', 'hmxneygmgyqgbyetr','xuffyponjvngcyz',
                  'hztoyh', 'fnkq', 'cdeuiynijdshccg', 'zhhfldjs', 'fdl', 'cwmhmawyutxacwtmgdof', 'vjxxvxz',
                  'jtteyjvxigegzbbsf', 'hdjushh', 'zwuvlvc', 'kwgktyqvvdcuawtnawm', 'fjhtfjluigvkixcvmbh',
                  'odauicbwojstnwyxfej', 'yvqtglfzgy', 'znx', 'vfras', 'uqeq', 'lgalrklgubwsnlca', 'pjcm', 'owhtzcuhmc',
                  'slrsyhktxdb', 'lsolkbzwdkilv', 'qmwkm', 'omgwadbzxugpvp', 'ninebszynj', 'bhkvegwbkp', 'zzrle',
                  'xawyea', 'qygnssrmiiowlxregkqx', 'abqgfditucyq', 'bge', 'izbtz', 'cdtfrcroyvwts', 'elogpdzxmzqydav',
                  'uayhzwoab', 'cqsdswsof', 'qyujwgaukraifwp', 'pwcwxpwrde', 'fyqvhdoubantzslluupp', 'nogw', 'pisl',
                  'cptadkevsbmv', 'grkcnjw', 'wapydjmjitxkxmwwnc', 'knvmoyhwjopywzra', 'heidoeornq', 'wmfqupmsb',
                  'ambgjam', 'sumkyevo', 'ozzwirszanny', 'dcmfmbnxmnlmzqmyukvv', 'juxmgnbmxfojgnblh',
                  'xszstrvtvdfcwbmzkq', 'boevdsooqszeu', 'dxnmd', 'bcygwemzsmtqdsli', 'kunklxzyrabquuviu', 'ruwhicf',
                  'kignzqguimgswqgwz', 'zhyhkvawzgjkdiybre', 'hceyswgy', 'zvadvf', 'xuhyiojyno', 'kbx',
                  'cgayjaaupccqynuphb', 'nkettedkdsaqq', 'fygatavkhp', 'jamplccymdqvw', 'xgktejfhvf',
                  'utggtilucgtjhzckbi', 'bbnynwbbojyoukihc', 'rabypprzahgmyhamvfgo', 'tbxmc', 'zxsswtgssjyoes',
                  'yibbnpolsgx', 'cdccnkicmafxq', 'bhrcvpenfxgwn', 'etvaqclypn', 'fseukv', 'lpcci',
                  'xexsdmkjxckqgqlpuo', 'uwbnykft', 'jdqrsh', 'ylme', 'wightvitoya', 'fhunxhg', 'xuapyxmuzdfdc',
                  'kmyhmduvc', 'jirksgzrl', 'cftivoayze', 'vjkbqibpzqrzkwk', 'iftmtvrl', 'rmqygnztladaxnkcbudm',
                  'ztrxkxjjjc', 'jhsrjtnhkhi', 'gkdtgunvsdpurvae', 'ldaqamh', 'yzhwmgxjrzapgodwardh', 'tmxqjyndcaln',
                  'nq', 'vh', 'wjgpbwgrkvuvdyvflxtx', 'tiwenxm', 'skfpdvtdvnhjziahmmmq', 'zowkhpglgcfbdcj', 'ebsykqjvh',
                  'oubbqodfmdpayyfolgc', 'dfalewsvzugxi', 'ncvzqwiflfqckv', 'yyuzlzconlkiup', 'cmqejiqlhscmbzkxer',
                  'bengcjukdd', 'kxtkfzjlgvcvvlb', 'hwsfm', 'osgdfmacl', 'vcbqnqrripmnrbsvz', 'gzaoscwfleexx',
                  'nnbudmzsyi', 'kebzwqdcnm', 'nmgveeyrh', 'fnmsa', 'bjfakylhgsfhzdfgvwbn', 'niajymksipfnlm',
                  'doyllyxekeqjfsitzalg', 'qhropwulmq', 'ydxnfupve', 'dxue', 'tamrr', 'nxixglyi', 'ysaupocfojzl',
                  'kmhsbxzhgpzdmityxy', 'focwrvjldf', 'rzsoabtln', 'etz', 'wilewsmprasaxc', 'sahpwbzrin',
                  'npxlatchxeoamkr', 'buvipg', 'lhtyqbzjquxyqwwqhii', 'qqmgsv', 'hljpokdxlgxqlov', 'gkepbaatkqbgu',
                  'ebeillefjlkgonuzhrx', 'bniytlygnklm', 'yhhnzc', 'cwutkijiinwfqtase', 'uqgpzjj',
                  'bhjejnqxuucdonpjwom', 'iaepzxjezpnvpmajux', 'inihejwzpdhbsnnigy', 'sdwgttu', 'edpwknzmvevn',
                  'dldgnst', 'dnngxymnpfhpli', 'iqoj', 'llccmnbrytwq', 'odjsnldgzndepplvp', 'quokolndboxzob',
                  'uhmzuxjbsnozxx', 'tukolmzmmpnzr', 'fkqho', 'kmqwwrzfrvxosq', 'iuodohetwub', 'jbrtht', 'ygecnjvxzt',
                  'obcwqjoalswtmzq', 'oosbvhi', 'agwdhrccvdswt', 'owkylbr', 'pzyrke', 'ekzfm', 'rjrdkumzhjqbuz',
                  'rjtnfbyhtqkmex', 'cavmiiugo', 'klnjadlkxenj', 'ribtkp', 'nznsixilvdn', 'tgcffrhx', 'ljcwvw',
                  'oxhkgahysfjzellyjthq', 'fkifpxrysefdmq', 'iezfrarflrmjs', 'rzqwnzrg', 'cqfbcqgzbdfbmdlovz',
                  'sxrrzyxyda', 'rfma', 'duvi', 'pyjzjzic', 'euqljquejd', 'aqzde', 'hztrekr', 'hxvz', 'ea',
                  'guulvxsbjoxe', 'sugcatupurmfoa', 'cid', 'ysqynzfbq', 'urgztglu', 'dpursjzypqlrpyj', 'bv',
                  'cuqxnlafoszcfuub', 'zcjdvltvzntrtsrxfki', 'wthpfbvecencz', 'jbvhguzqlqu', 'crdiqdzmpnvv', 'njxyyooo',
                  'chgckxch', 'ejgnsltqqexvpvvf', 'psecscjjzxcktxgwp', 'pltromqhyjkf', 'qlp', 'vdwuksk',
                  'tdbqgyjzchrecoce', 'ulnlabxkqelxbfv', 'euuocmkamqi', 'ufrataqqekbickcyn', 'zykotbq',
                  'pepuvbvhlsgjof', 'lshgcbnf', 'bfr', 'flxvgwlqnhhuwspxlbh', 'olk', 'owkzoyvqfogqwmvcg', 'abgjxpuegfv',
                  'lpcsjdcboicheumubgj', 'fgephbzzslvf', 'bthpqeshztpxmd', 'fhgdiucpuualbwr', 'kk', 'lfubjkic',
                  'ewjfjvmbqf', 'hdrhrdndekm', 'gyxsonajncirfvojwaeu', 'kryaoranv', 'bzm', 'khoqsmyzppxduwtsl', 'uezhl',
                  'utfejxxqp', 'bxqqcxfisgwl', 'uqpbvdjycjebpixqcdkd', 'exxdysjy', 'iqcp', 'gyothovfsiar', 'cyvovrlhzq',
                  'yiwnvs', 'rbedyrzb', 'wqysobwirohmttkanmc', 'ohzslbxzxcllpjrjzwtx', 'upvtthkzjxmk',
                  'palsciacundtxxlhi', 'rhvlyixvhoeoqnjbefe', 'doqdjfgvuzq', 'jwzjxv', 'syslrgtlfmmhp',
                  'icixppwpzgwssg', 'nfkldvvdwmoxrjdvsx', 'efwgiigxp', 'swqdbjblcwkvidjucqma', 'zdduackw', 'tnbo',
                  'aeobbnepd', 'qynvmybv', 'reoonxseqlgcfwr', 'lxmtno', 'wds', 'gyidnknqjhkctq', 'zekjlwe', 'foh', 'm',
                  'xeherrwjqnxtqedvnya', 'ormasatuvkzlvg', 'vkxzwzwgbric', 'yfjrkqctpxbiobneylx', 'vmmkwfezky', 'tonhk',
                  'flkcjdoletsatetk', 'oaw', 'ahjecwlqsgjo', 'yvvfbaganuh', 'bhqnywcsuwghsf', 'kdabdeutknhtegabg',
                  'xqgdskqnlsqsbdtjmpzm', 'hwdrofkjsroifol', 'xynksicagukjfo', 'oshpxuhjbyfnvzmb', 'ndocdtzm',
                  'oaxtengefigihkhqtxp', 'fdbmtannn', 'vqmhwhpbckfmmphcu', 'jlgtbwl', 'rlzdeejllvoyq',
                  'avhfodftbtekyyics', 'bamifkmiuhtjiipib', 'npwauczizez', 'oizfxow', 'naoobqmhhrhgve', 'arhiklpcb',
                  'dkllpmics', 'gbh', 'pod', 'cqbudexio', 'szghcfwkxnosdfaqsa', 'ihdprinewaovkxltq',
                  'ioqwxxycpyjzjorauld', 'cgeudarrlcpalvs', 'jermfue', 'okqtrooleedfzjljcgi', 'jlkleievmcicmcevjki',
                  'eyr', 'jq', 'jkpmayyblzdqbjkabc', 'qdge', 'ovzzwwbsrlvbt', 'doaeawudv', 'uhbi',
                  'ayrzhdpbjpkgzpbluhl', 'idj', 'xahrvnyyzj', 'diyz', 'ffbgsoohouucyne', 'uswceglqjcggmzf',
                  'towvrjplpivkcnzalzc', 'qykchsdyqpwjchqxiaw', 'zufjntqagdx', 'aofkqkzyxyhcr', 'erzuyy', 'llfjrztqp',
                  'kjabgqqvt', 'htkbncfzyikxc', 'yvsbefdnsyzlqra', 'zka', 'jiphmwnrtfndeyhulw', 'yqsexljpcpu',
                  'qhygxgxiwlvoizbvmw', 'blqmjcjtoilqkt', 'klkcyeaicxcm', 'rhgf', 'vfcrj', 'yzhizpu', 'kcqm',
                  'lzziebbb', 'pyafvndhqbkijxlvwaq', 'llmyxfmmx', 'ubsipqjquu', 'loz', 'lpgem', 'ernwwekpn',
                  'lcaiwxgnaxow', 'zvvlemlvfxb', 'ecvcmhwgesnogtorjv', 'scibbzkllhv', 'telze', 'jvlivolavaysntsnn',
                  'tcwpzxibdsfsklwwzuev', 'kxhnzej', 'wefztrgmmqne', 'wtslpbvidzikehmweyun', 'hujoaxhlgwpjvu',
                  'icvvjggyalyia', 'plaobozhntpvygo', 'siqrwvasdvq', 'wjplzgenym', 'thhsnfyvm', 'tstd', 'oglwshrauw',
                  'cshoteyyprew', 'puqervdmibhhmqpkpinz', 'wundfghisdqzkz', 'lyphipfavavgika', 'ranfr', 'yhkhpfua',
                  'pphidfvllyjdqriwuulr', 'kzzpowgclrbydluykq', 'dba', 'pido', 'aegeworwiow', 'cchwyywysk', 'qhtgxbq',
                  'rfquqvyax', 'raxvktwqci', 'vmbaxjkff', 'cdcgynat', 'dhtilhpxeahujmsiikyh', 'yppbkhwnyznotez',
                  'wcdjccaaxdio', 'fv', 'wmqnafhjt', 'obmotcwjiowggduozt', 'fe', 'tkxy', 'ihlxptthztjocu', 'olqnmpc',
                  'nhginwlahfzv', 'gptsbobovuyktim', 'nopo', 'wtooeqowtmuv', 'njlnyyvfwtajdqo', 'qav', 'lzgccjrazrst',
                  'hkztpuwnsng', 'npy', 'nngyessfwylenz', 'nsimvnrsv', 'qzuxn', 'gxcvl', 'fsrmgvusoobiogpgkboc',
                  'pjqkdkp', 'rqczvpvupkpln', 'bitohaapxumx', 'kiv', 'oeywsosius', 'kux', 'blnrpg', 'leprbqmezywrckmq',
                  'amc', 'wxdgapjxf', 'bbgtg', 'orbmf', 'uonpozcfwqnm', 'hakqm', 'cfvenucvgbslxrr', 'uphsxgu',
                  'xuytjgpgiasjoblgi', 'jhulnsusfyvwm', 'gclastz', 'txkgyoxbw', 'frgnizulbia', 'oj', 'gjckyloqbfdvkp',
                  'gnnlr', 'pngyxvy', 'oviuggiyokeauqjyuy', 'vjrw', 'uaewnoedorh', 'xngajhlsethbrfuejod', 'vwyvd',
                  'tiwylsbpzux', 'rxycegfxohcitgxtd', 'lfizbujxtoiqlfbqyial', 'ukgljpssgtbfiyurlkg', 'zlxvlvjc',
                  'wxwszyamjbkcpjcgs', 'xlukxapduyrwdr', 'wlovhl', 'yweku', 'lohfyramj', 'iscdrkpyqfusy',
                  'uxdealomnlvdbijc', 'oznaapna', 'dknlejqm', 'xlikn', 'luseihvjurmhzhchdpqu', 'xfuxxckfmdcwywal',
                  'tpdmoogkzdojb', 'oatfgzlkrpnkdqjksg', 'elxrnyldolfohpuxmmhy', 'nhepkhyvchh', 'lbgfbeumb',
                  'ltqmeztddawfq', 'jutbrfkuvpcwqblxsi', 'wrkshbpsmmonwui', 'cmzrfvhgswr', 'romwxefbxp', 'uwsjxx',
                  'yqanavfrhulwesj', 'awihhnbqrcabgnhe', 'howj', 'dmwmfvt', 'jyxtepsnmlbzxasxxg', 'dcxfywzvwaaatmlkq',
                  'qhwxxyjdodazbemmtydo', 'wfxhzeunav', 'harvtmiapa', 'sxiqoadlvdhwxgr', 'vlmceclfu', 'hhiq',
                  'blphxhkkxvwsyqy', 'tynktut', 'txrjjtzlvbjypwdapskc', 'xc', 'kqmlyvrkltq', 'ecuz',
                  'qrknkxxkyvhohaechdo', 'fpdtjedmbhk', 'cjbrmpoaq', 'nlonglznvfmp', 'jhc', 'nidzkjmmlhpvzfkt',
                  'qtongibkflfnyukuknux', 'ihnqykjrsugsogbdq', 'ttqshehrihfhqenr', 'slnlcq', 'ayyeyfefjtheh',
                  'yzwnphiox', 'itmwtlnwdlmvrgiust', 'tpcirivmf', 'vlymfzafhgvptli', 'kjglgasixpgabudmhdzb', 'bubjc',
                  'idraxlrmrhn', 'kltz', 'auzfpuydfvahkqgq', 'cpv', 'hggex', 'jkvspznjmzlervp', 'xrfvntvplgljvrr',
                  'zppnatxwzpxftfcm', 'apsavhyum', 'xnstbtgttgblwglw', 'orep', 'pxdmfzkhr', 'sibvsmbcpwvjzcdjpkaf',
                  'ufbeo', 'kedibwnogisavsgmzsk', 'txzvjoscxctdyi', 'atgyxyesuxy', 'rgy', 'ydoh', 'yjvbs', 'jc',
                  'remytzaxzf', 'aahpmfvrhiturdijjt', 'umbxlsde', 'dmfbexqromnkjuuxeia', 'yjxrlsnrmfpkdnrzahos',
                  'symvqmlal', 'ddcfjkafhzava', 'ewnx', 'yozfm', 'bstm', 'gqawxfgyhmpqtspyf', 'awththbzn',
                  'vohtccnpobaqdxgom', 'ouqrn', 'ucpobddlioudfbphi', 'zrbyurlhaug', 'ohuol', 'flru', 'dndladxftesnjgx',
                  'dewrnwpuwhhk', 'axk', 'hdrhrk', 'exbtqvlvduegaxxuc', 'qi', 'krfphxohijhxll', 'iohqfptlpayc',
                  'nbtvfdndlspckcyhgy', 'vknrxveztzos', 'ffizpazqhilogfpal', 'lixwhotpdtgykvsj', 'sgluodud',
                  'isnjpfqsltthwhcom', 'rlimxdwzjonwpsfejci', 'aqd', 'zpvzpmjs', 'pmsnvzgm', 'blxhcgyxake',
                  'bbggvvugzvegrsvrborf', 'vxsnakqohbwublbuwqb', 'dcortjwvqyvtwyu', 'vmesr', 'rbhpgkhnkjsizp',
                  'ezbvklhvusqrfradr', 'knwexzc', 'cghzrnlngefytmzxuz', 'amqqavsisc', 'nbjplllhqh', 'wahgqcjiamnsq',
                  'uqzla', 'brqgydbrnwmnondaip', 'fxiv', 'psalja', 'qygklbtcdvrudyvd', 'qbxikffpgptuyrajapva',
                  'wvffgfrsxrsiojrqx', 'ftwepjsbwok', 'tmmsy', 'nhdvlppcvluedcndcvm', 'yk', 'khkyukbsvunwxe', 'pbvnlqw',
                  'oqjajgpu', 'kfsmspi', 'kozzehogvhqhgavg', 'bow', 'umsxqekxochnppv', 'pauewojjapxn',
                  'jkegdwkkkqtygegp', 'qyueb', 'smlcj', 'hlesnvvmf', 'gnwixenelrmwkcjuwwqc', 'poc', 'ijwdv',
                  'iakkhjtmauwukp', 'opjahbumth', 'axlxtkrmcbgwvwuiaoy', 'qsdhlaieggijxu', 'cnzxupwiwtnkm',
                  'uzedhmavpuxjqo', 'ticwdgejoc', 'jdaraqufatelkznlkq', 'hocewtq', 'djw', 'leqspekzpmkctflqb',
                  'xlsvnvhnbeqqjvckvs', 'yicub', 'sr', 'uaawyzfoebmlanmot', 'cttuioslot', 'zozdkbgimktfnlkvv',
                  'auyiiwtcjh', 'xirjkufrnr', 'bnfapladr', 'txas', 'qoetjwxszgvrzsdmtuau', 'wgfwmhujlfnjcunudjrz',
                  'dpkzvpokc', 'xggjhcwfhiuorgbhngd', 'nbxm', 'pktzzaruljbn', 'rwjathvtsjzftevoph', 'tueayp', 'amucr',
                  'jn', 'nvniavnwd', 'bdqzdt', 'jlwcdoxexkgcridekso', 'lifbeyxsqwbpicy', 'ksucnneqllhkktz',
                  'irnloujzdczoegw', 'rfoxigthiiqguqjhkgiy', 'bhlfxbkntl', 'dnkcrehqd', 'elptrcmaa', 'bxfep',
                  'wlomwywz', 'wojthgl', 'ifnmbogl', 'opzwizpdttd', 'qyrgnehydbhvny', 'pxsmfszeub', 'amdp',
                  'rtdjvmsehgzfmycac', 'jmreclh', 'rtzqrcknlv', 'duzysbbxxynikkuww', 'wajbwkdqwodovnbqe',
                  'kvfcbbdxmhgf', 'txexykoomptsu', 'rfpcvvygllidegomp', 'qqwykjxduebwldzoulp', 'tpaczxwexv', 'oswgypye',
                  'dfevzccjnjjanqqcaz', 'btukisan', 'tyefuchrkjw', 'hccqqisisamjbmk', 'tnitplvmkdhhtedjkkal', 'urqm',
                  'rwsvcrimmusoylo', 'wk', 'ytquopplixfrwihvjsv', 'sqqgcnkluxnkhl', 'ijoebdgezlnhsqrjro', 'ivujavsn',
                  'slwnqeiyitj', 'cioucrbwa', 'vvbgaqv', 'czpyrbqqst', 'anbkgvztrxsymxhw', 'wylgnkeyty', 'ivbr',
                  'hkcxrbncosnnoflrfflr', 'blhb', 'guttfkieoawjnasz', 'lszzruuaooba', 'dy', 'kidcizbnljjhjve', 'ecnta',
                  'ierutgmnoewotootw', 'iocavknzxv', 'uevykumxwrjfhnq', 'solhk', 'bifyvwlvfmifosl', 'jyksacdsxe',
                  'wpzprvgrfwqjzyuz', 'spx', 'vbynkdhho', 'rdgziqo', 'jlfekeepmeqijzqzpb', 'filea', 'ljwmlgbbgxs',
                  'hitkgzozphtkabztq', 'pqajkxqrcgilrkgeg', 'jigymtweearefllqkr', 'dwhenvogutekbws',
                  'wvigbxzetuhctsnkmwa', 'iybpnamndvqilpkqdorf', 'xhuwziscavuzfjwz', 'bjglvqfih', 'nyirrdwzdaodq',
                  'vfouba', 'yhpuiriddowcyzpigqcc', 'hembcmgnuiuiwttkxff', 'sbhjtjfiuszwmk', 'zjlhfrqiymgqm',
                  'kytbesolyfbzplku', 'xglkecabwadsnd', 'cxaaibz', 'iokzqdohryykynaesdh', 'vidntdki', 'kyyozwzro',
                  'vrwcehfidwktnujrle', 'frsdgkleplsibaubmr', 'rinyhclbabhhxasc', 'vpurelzegtqfvhvhe',
                  'nzpnqespgmzmhrnzkviv', 'pkgbltuggkacosnljvl', 'arpbrjja', 'skqespztxfzsfefa', 'ypkutbnpfmknmu',
                  'pnyrhhpxqbduhjfqf', 'qqgsyqt', 'bqybkmwct', 'hqu', 'dsnusmftc', 'rwcnpzdsasiegd', 'etpevdsnsczdbzpd',
                  'fraqrlcavwkxmlthxpdh', 'iavxythynfevwky', 'wnsrppegdecgzj', 'fml', 'zidtbmjpe', 'lmfvgvdatvtrn',
                  'xjiqp', 'okbcwdkfbi', 'wabnvpufdqxunwuzq', 'walsgfaewaqcua', 'vgsdawvgtto', 'nkeiuqakxqjxw', 'hlogi',
                  'hrl', 'wwwldccpofvk', 'xdrazerly', 'ekdai', 'oendhbhpfnfs', 'otcgrtsyvawrlwiie', 'sgxpfvrqvfonoyp',
                  'svqozna', 'elhndpk', 'ielpnmwlxymxvnwqwclo', 'cvu', 'qjmxmif', 'zxlsj', 'jp', 'hxtrapetwgi',
                  'evbcfvwfstkjilbgktg', 'gyy', 'vsnxahorliszvh', 'inxxh', 'vfrotiobsxqjxeky', 'jljxkasozcycjgbcr',
                  'fkpl', 'hgtdwqvptg', 'ibtqeljihqvpxssagjzd', 'hcx', 'hvco', 'ivclthcduuayfk', 'gkvhppiitf',
                  'oxobtcautvwnbs', 'vqaigmhqec', 'ioxfngozf', 'rwbaxjdig', 'nnfjkxf', 'gmgdjheovmvydr',
                  'uvcnmjxhxudvvf', 'vljviqxy', 'jeeyffhely', 'eqtrhfgfk', 'yss', 'jlfdqbkcsjpuk', 'hknoazpixquiydixw',
                  'zitkqxoxpafo', 'otlncoxs', 'wayn', 'aduohawccx', 'iplexb', 'oapbpmqkxocav', 'tcdaiohekbkpulfd',
                  'wvhotxgshq', 'zcfcfw', 'cxbwslfhsa', 'ldmszpp', 'tvdhwramhspctr', 'ypjbnibwsbznhswql',
                  'jjxrujiptysukrnxkanc', 'imayssejmq', 'fdacgreyvlawlvdmgu', 'ysqbbywjvvgkocj', 'fosmgjnxpsewweoo',
                  'ysnbnuypndmfsfm', 'bgremktjjzzp', 'dohddy', 'vkcvjsbuucmwrxyyn', 'heqcyq', 'nekioon',
                  'cztmdzcodujfifrwrqtc', 'efmqagztpg', 'ocgufiazufjqhmajv', 'qtywlqcelbvbjrip', 'knqmgeiquqii',
                  'rrhlqfxjwsrzepdsjvtj', 'nzlq', 'ghfglsfivwhf', 'qdfkknufixbsb', 'pkaqvmp', 'hwoazkvzvgepxjab',
                  'jsrbodolrido', 'rjezusvnm', 'iyffwjptpx', 'csbtqrwhjkmsvfvofbun', 'hxgeabzscx', 'xbd', 'jz',
                  'wyfymdybyvwr', 'favasbqxydr', 'drhccce', 'nhl', 'dlmtwpkevxolcslh', 'cmwgbypy', 'qouaavy',
                  'lmwuhexspky', 'ccusmcjtxfidnxo', 'hpytv', 'llozfkh', 'ry', 'jhpqmuebazliv', 'bsrawprdtheononccvi',
                  'nddf', 'uiqvruwdlrhnbxi', 'gqsupki', 'kur', 'hyouipokevdpryja', 'haeldkagwlzkzoxniqbt',
                  'lghvndaxklqzbybwdgn', 'bjoaxaloochjjiqr', 'zbvuquqzmqebebcc', 'qgsc', 'cdqerfrqltdbennygvb', 'oxzo',
                  'joldtmiuig', 'gd', 'auhiqdvwjc', 'fwpcpxhdgk', 'iyjrjgzef', 'zpsbofhuxwgsqyk', 'gircmoadgzotwec',
                  'ngzhimj', 'wzgfqfffkpdh', 'ervqttiwagcjxravm', 'cnazdo', 'wteycpjzinsudsbk']
        testo = 'iocavknzxveqtrhfgfkcnazdojlwcdoxexkgcrideksoqgschztoyhxglkecabwadsnduaewnoedorhihnqykjrsugsogbdquqgpzjjrfpcvvygllidegompkedibwnogisavsgmzskoswgypyekmqwwrzfrvxosquaewnoedorhfocwrvjldffvwwwldccpofvkvfcrjyzhizpugyyolqnmpcnzlqjirksgzrlvfcrjcpvcqsdswsofryljwmlgbbgxsebsykqjvhluseihvjurmhzhchdpquzpsbofhuxwgsqykwyfymdybyvwrqhygxgxiwlvoizbvmwqildaqamhpphidfvllyjdqriwuulrrxycegfxohcitgxtdyicubvpurelzegtqfvhvhefyqvhdoubantzslluupplhtyqbzjquxyqwwqhiicavmiiugoquokolndboxzobiscdrkpyqfusywxwszyamjbkcpjcgsdwhenvogutekbwsczpyrbqqstbfrkxtkfzjlgvcvvlbjyxtepsnmlbzxasxxgsbhjtjfiuszwmkgnnlrsqqgcnkluxnkhlpepuvbvhlsgjofblphxhkkxvwsyqyinxxhielpnmwlxymxvnwqwclogkdtgunvsdpurvaedyiybpnamndvqilpkqdorfdwhenvogutekbwselhndpkhwoazkvzvgepxjabnbtvfdndlspckcyhgyqiwfxhzeunavpkaqvmpkdabdeutknhtegabgpjcmpuqervdmibhhmqpkpinzzbvuquqzmqebebccyzwnphioxgkvhppiitfdyamucrekdaiowkzoyvqfogqwmvcgcjbrmpoaqbnfapladrzhyhkvawzgjkdiybretpaczxwexvzhhfldjsierutgmnoewotootwdpkzvpokchkztpuwnsngkhkyukbsvunwxekqmlyvrkltqolkksucnneqllhkktzrjtnfbyhtqkmexpalsciacundtxxlhirabypprzahgmyhamvfgozxsswtgssjyoesohuolztrxkxjjjclxmtnoimayssejmqqiimayssejmqbhrcvpenfxgwnebeillefjlkgonuzhrxsmlcjpjcmtonhkuvcnmjxhxudvvfxuffyponjvngcyzlbgfbeumbyhkhpfuacmwgbypynekioonsugcatupurmfoagqawxfgyhmpqtspyfgptsbobovuyktimdmfbexqromnkjuuxeiaeuqljquejdhlogizozdkbgimktfnlkvvabqgfditucyqezbvklhvusqrfradrrjezusvnmoglwshrauwcwmhmawyutxacwtmgdofksucnneqllhkktzslnlcqwcdjccaaxdiojigymtweearefllqkrvknrxveztzoslfizbujxtoiqlfbqyialtynktutxggjhcwfhiuorgbhngdzhyhkvawzgjkdiybrekkfmlthhsnfyvmzvvlemlvfxbhocewtqcptadkevsbmvwilewsmprasaxctamrrvbynkdhhoamdpxngajhlsethbrfuejoddhtilhpxeahujmsiikyhoapbpmqkxocavnbtvfdndlspckcyhgytcdaiohekbkpulfdyzwnphioxewjfjvmbqfgdkuxysaupocfojzlqouaavyxawyeayzhizpujlkleievmcicmcevjkibifyvwlvfmifosljnjjxrujiptysukrnxkancrlimxdwzjonwpsfejcihvcokmhsbxzhgpzdmityxytstdxuapyxmuzdfdcvbynkdhhokdabdeutknhtegabgexxdysjytstddewrnwpuwhhknsimvnrsvnkeiuqakxqjxwfvkdabdeutknhtegabgygecnjvxztzozdkbgimktfnlkvvwaynaqdxuffyponjvngcyzsdwgttuoaxtengefigihkhqtxpanbkgvztrxsymxhwdbanhlgqsupkixynksicagukjfogxcvlbzmubsipqjquurjrdkumzhjqbuzoviuggiyokeauqjyuyxdrazerlyrfpcvvygllidegompbvljcwvwelhndpkawihhnbqrcabgnhekyyozwzrovfrotiobsxqjxekyzhhfldjsicvvjggyalyiayibbnpolsgxzkadoaeawudvdhtilhpxeahujmsiikyhticwdgejoclghvndaxklqzbybwdgnpnyrhhpxqbduhjfqfyvsbefdnsyzlqrafhunxhgaxlxtkrmcbgwvwuiaoyvknrxveztzospjcmhxgeabzscxyvsbefdnsyzlqralpgemnogwysqbbywjvvgkocjagwdhrccvdswtoxzoiybpnamndvqilpkqdorfcqsdswsofwnsrppegdecgzjhxgeabzscxgyothovfsiarqzuxnttqshehrihfhqenrulnlabxkqelxbfvotlncoxsknwexzcbifyvwlvfmifoslukgljpssgtbfiyurlkgqlpsvqoznadxuetcdaiohekbkpulfdczpyrbqqstwlomwywzgkepbaatkqbgucvurzqwnzrgxliknninebszynjfkplkmyhmduvchdrhrdndekmldmszppypkutbnpfmknmujlfdqbkcsjpukirnloujzdczoegwwmfqupmsbnngyessfwylenzzhyhkvawzgjkdiybrekzzpowgclrbydluykqljcwvwcchwyywyskblphxhkkxvwsyqycwutkijiinwfqtaselpcsjdcboicheumubgjtcdaiohekbkpulfdhztrekrerzuyyukgljpssgtbfiyurlkgdohddyebeillefjlkgonuzhrxawihhnbqrcabgnhecdtfrcroyvwtsbjfakylhgsfhzdfgvwbnknqmgeiquqiivbynkdhhouqpbvdjycjebpixqcdkdcidhgtdwqvptgjjxrujiptysukrnxkanckdabdeutknhtegabgsolhkhitkgzozphtkabztqfygatavkhpcftivoayzesxrrzyxydaslnlcqecvcmhwgesnogtorjvpltromqhyjkfxglkecabwadsndivujavsnvmbaxjkffervqttiwagcjxravmdiyziybpnamndvqilpkqdorfyyuzlzconlkiupfpdtjedmbhkgrkcnjwbbggvvugzvegrsvrborflyphipfavavgikaevbcfvwfstkjilbgktgedpwknzmvevnjhsrjtnhkhiwundfghisdqzkzlbgfbeumbawihhnbqrcabgnheyqanavfrhulwesjlhtyqbzjquxyqwwqhiinekioonfdacgreyvlawlvdmguypagqbwelogpdzxmzqydavjtteyjvxigegzbbsfarpbrjjacnazdoijoebdgezlnhsqrjroqmwkmgkvhppiitfhakqmpxdmfzkhrrfpcvvygllidegompuwbnykftjlgtbwlarpbrjjaoxzoklnjadlkxenjbfryyuzlzconlkiupcqbudexioryitmwtlnwdlmvrgiustuvcnmjxhxudvvfubsipqjquuubsipqjquupphidfvllyjdqriwuulrkunklxzyrabquuviuttqshehrihfhqenrddcfjkafhzavawdszxlsjysqynzfbqotlncoxsxbdauyiiwtcjhkjglgasixpgabudmhdzbnbtvfdndlspckcyhgyormasatuvkzlvgwxdgapjxfotlncoxsjljxkasozcycjgbcrchgckxchribtkpebeillefjlkgonuzhrxpidodsnusmftcsugcatupurmfoakignzqguimgswqgwzuaewnoedorhllozfkhvcbqnqrripmnrbsvzflkcjdoletsatetkqqgsyqtswqdbjblcwkvidjucqmaihnqykjrsugsogbdqqlpirnloujzdczoegwljcwvwtynktutqtongibkflfnyukuknuxhmxneygmgyqgbyetrleprbqmezywrckmqhxvzncvzqwiflfqckvbgremktjjzzpcftivoayzeryfjhtfjluigvkixcvmbhklnjadlkxenjzlxvlvjcncvzqwiflfqckvjoldtmiuiggkepbaatkqbguydxnfupvenddfbhjejnqxuucdonpjwomnpwauczizezsqqgcnkluxnkhlqqgsyqtdhtilhpxeahujmsiikyhkedibwnogisavsgmzskbbgtghdrhrdndekmninebszynjztrxkxjjjctbxmcrlzdeejllvoyqbhkvegwbkplxmtnowkrzsoabtlnvidntdkixuhyiojynofnkqumhvdjwcyvovrlhzqxnstbtgttgblwglwuwbnykftoosbvhikbxeuqljquejdysaupocfojzlfkifpxrysefdmqebsykqjvhsgluodudefmqagztpgbhlfxbkntlioqwxxycpyjzjorauldqiauzfpuydfvahkqgqernwwekpncpvuaewnoedorhuhbiuezhlticwdgejoccttuioslotaegeworwiownbxmqoetjwxszgvrzsdmtuaubhkvegwbkpspxsrjbrthtrtzqrcknlvtamrrdndladxftesnjgxwightvitoyadfalewsvzugxixfuxxckfmdcwywaloosbvhinnfjkxfekdaiumbxlsdesumkyevoslwnqeiyitjzhhfldjsttqshehrihfhqenrypkutbnpfmknmuwyfymdybyvwrkfsmspiuiqvruwdlrhnbxikmyhmduvcwaynqykchsdyqpwjchqxiawvmmkwfezkytnbofocwrvjldfrjezusvnmhgtdwqvptgrjezusvnmjsrbodolridokkdcortjwvqyvtwyuchgckxchpktzzaruljbnyvvfbaganuhgjckyloqbfdvkpvxsnakqohbwublbuwqbauyiiwtcjhkytbesolyfbzplkulgalrklgubwsnlcaaofkqkzyxyhcrranfrvmbaxjkfffpdtjedmbhkioxfngozffpdtjedmbhkozzwirszannyormasatuvkzlvguqgpzjjiplexbkwgktyqvvdcuawtnawmfnkqtxkgyoxbwuqeqnekioonzozdkbgimktfnlkvvnmgveeyrhbgremktjjzzpdjwlghvndaxklqzbybwdgncgeudarrlcpalvsldmszppbuvipgijwdvyvsbefdnsyzlqrarwbaxjdigtamrrurgztgluijoebdgezlnhsqrjroyqsexljpcpuutggtilucgtjhzckbitamrryvsbefdnsyzlqrahkcxrbncosnnoflrfflrrmqygnztladaxnkcbudmduvihljpokdxlgxqlovzhhfldjskjabgqqvtvhuaawyzfoebmlanmotdlmtwpkevxolcslhdcxfywzvwaaatmlkqizbtzygecnjvxztzjlhfrqiymgqmpnyrhhpxqbduhjfqfbniytlygnklmtstdanbkgvztrxsymxhwbbggvvugzvegrsvrborfsqqgcnkluxnkhljamplccymdqvwuayhzwoaboxzolixwhotpdtgykvsjsiqrwvasdvqwvhotxgshqzzrleysqynzfbqhxgeabzscxzekjlwenpygqawxfgyhmpqtspyflozhembcmgnuiuiwttkxffpidodcxfywzvwaaatmlkqyhpuiriddowcyzpigqccduvigrkcnjwcfvenucvgbslxrrolkjplzziebbbjlfekeepmeqijzqzpbjyksacdsxegptsbobovuyktimjlfekeepmeqijzqzpbohzslbxzxcllpjrjzwtxwnsrppegdecgzjvjxxvxziezfrarflrmjsscibbzkllhvxngajhlsethbrfuejodgbhgnnlrwahgqcjiamnsqayyeyfefjthehqhropwulmquwbnykftflruuaawyzfoebmlanmothljpokdxlgxqlovcttuioslotbniytlygnklmrjezusvnmsibvsmbcpwvjzcdjpkafqyrgnehydbhvnyqqwykjxduebwldzoulpecuznmgveeyrhidraxlrmrhneqtrhfgfkaeobbnepdgmgdjheovmvydrvjxxvxzivujavsnuqzlajermfuejkpmayyblzdqbjkabcsbhjtjfiuszwmksdwgttuwfxhzeunavnaoobqmhhrhgveslnlcqovzzwwbsrlvbtyibbnpolsgxjlfekeepmeqijzqzpbcrdiqdzmpnvvlmwuhexspkyxjiqphquyhpuiriddowcyzpigqccqbxikffpgptuyrajapvatyefuchrkjwyssllozfkhoxzoleqspekzpmkctflqbnhepkhyvchhcidpngyxvyqdgeghfglsfivwhfdrhccceoqjajgpulozbjglvqfihhujoaxhlgwpjvueqtrhfgfkibtqeljihqvpxssagjzdpislrbhpgkhnkjsizpcuqxnlafoszcfuuboglwshrauwpmsnvzgmbbnynwbbojyoukihcharvtmiapaorbmfcdccnkicmafxqldmszppxexsdmkjxckqgqlpuojmreclhnxixglyikfsmspifraqrlcavwkxmlthxpdhfjhtfjluigvkixcvmbhiplexbgyhdszwyawyqiuutjlgtbwlmtxasczpyrbqqsthakqmztrxkxjjjcczpyrbqqstdyfseukvcptadkevsbmvtpcirivmfrqczvpvupkplnjbvhguzqlqujkegdwkkkqtygegpwmqnafhjtydxnfupveskqespztxfzsfefarfpcvvygllidegompjlwcdoxexkgcrideksokjabgqqvtlghvndaxklqzbybwdgngyothovfsiarefwgiigxpaxkcioucrbwawlomwywzhlogizwuvlvcpbvnlqwxuytjgpgiasjoblgikryaoranvwjplzgenymiqojbuvipgihdprinewaovkxltqizbtzraxvktwqciqavuswceglqjcggmzfiaepzxjezpnvpmajuxvmesrldaqamhcfvenucvgbslxrrisnjpfqsltthwhcomwzgfqfffkpdhxrfvntvplgljvrrqhwxxyjdodazbemmtydozwuvlvcflxvgwlqnhhuwspxlbhouqrnfygatavkhpkvfcbbdxmhgfvbynkdhhoabqgfditucyqetvaqclypnernwwekpnlsolkbzwdkilvqqwykjxduebwldzoulprdgziqohrlyiwnvsyfjrkqctpxbiobneylxcsbtqrwhjkmsvfvofbuncvujhulnsusfyvwmjiphmwnrtfndeyhulwkidcizbnljjhjvekivqygnssrmiiowlxregkqxcdccnkicmafxqxglkecabwadsndanbkgvztrxsymxhwduvitamrrknqmgeiquqiiqynvmybvsgluodudokqtrooleedfzjljcgijyxtepsnmlbzxasxxgucpobddlioudfbphicdcgynatjlfdqbkcsjpukranfrjmreclhzpvzpmjshaeldkagwlzkzoxniqbtitmwtlnwdlmvrgiustypagqbwblhbnpyuiqvruwdlrhnbxizpvzpmjsnvniavnwdxirjkufrnrambgjamwpzprvgrfwqjzyuzoeywsosiusrinyhclbabhhxasciuodohetwubarhiklpcbwrkshbpsmmonwuinqozzwirszannyoubbqodfmdpayyfolgctcwpzxibdsfsklwwzuevgyykignzqguimgswqgwztyefuchrkjwxliknwpzprvgrfwqjzyuzkunklxzyrabquuviubjfakylhgsfhzdfgvwbnllccmnbrytwqdwhenvogutekbwsuwsjxxiftmtvrlawththbzndoyllyxekeqjfsitzalgihdprinewaovkxltqqzuxnkfsmspilifbeyxsqwbpicyzxlsjcnazdonkettedkdsaqqwlomwywzlozyjxrlsnrmfpkdnrzahoskrfphxohijhxllsgluodudwdservqttiwagcjxravmhlesnvvmfykoizfxowvjrwlmfvgvdatvtrnfnmsaypagqbwolqnmpcvohtccnpobaqdxgompmsnvzgmygecnjvxzttiwylsbpzuxrhgfoznaapnawxdgapjxfbvqqgsyqtqouaavykmyhmduvcyhpuiriddowcyzpigqccxrfvntvplgljvrrrlimxdwzjonwpsfejciqlpjlkleievmcicmcevjkiiplexbaqdvmmkwfezkywrkshbpsmmonwuijbvhguzqlquldmszppejgnsltqqexvpvvffsrmgvusoobiogpgkbocxirjkufrnrcqbudexioinihejwzpdhbsnnigyolqnmpcowkylbrobcwqjoalswtmzqnmgveeyrhwxwszyamjbkcpjcgszhhfldjsbdqzdtiezfrarflrmjsuevykumxwrjfhnqlpgemotlncoxsqygnssrmiiowlxregkqxheqcyqekzfmnngyessfwylenzyvqtglfzgytpaczxwexvldaqamhwpzprvgrfwqjzyuzpqajkxqrcgilrkgegtueaypaqdatgyxyesuxycttuioslotuaewnoedorhyqanavfrhulwesjpalsciacundtxxlhirfquqvyaxhmxneygmgyqgbyetrbjglvqfihvfrotiobsxqjxekyywekucwutkijiinwfqtaseknqmgeiquqiiaduohawccxoubbqodfmdpayyfolgcjermfueniajymksipfnlmwpzprvgrfwqjzyuzbniytlygnklmatgyxyesuxyiplexbeuuocmkamqiguulvxsbjoxekignzqguimgswqgwzvfrasoaxtengefigihkhqtxpisnjpfqsltthwhcomhkztpuwnsngiaepzxjezpnvpmajuxnekioonjhcbbnynwbbojyoukihcxahrvnyyzjxuapyxmuzdfdchkztpuwnsngojslwnqeiyitjbubjcuwsjxxhdrhrdndekmttqshehrihfhqenrxcwrkshbpsmmonwuiolqnmpcoxobtcautvwnbszidtbmjpenzlqamucrauyiiwtcjhzjlhfrqiymgqmcshoteyyprewoqjajgpuhvcofavasbqxydruonpozcfwqnmtxasccusmcjtxfidnxohwdrofkjsroifolvqaigmhqecnpwauczizezizbtzzpsbofhuxwgsqykowkylbrijoebdgezlnhsqrjropqajkxqrcgilrkgegywekuabqgfditucyqifnmboglatgyxyesuxyizbtzuphsxguczpyrbqqstsvqoznatnitplvmkdhhtedjkkalyjvbsldmszppfraqrlcavwkxmlthxpdhbuvipgnqsiqrwvasdvqejgnsltqqexvpvvfzlxvlvjcqqmgsvcwmhmawyutxacwtmgdofamczrbyurlhaugbqybkmwctsmlcjekzfmlzziebbbwaynekzfmtpdmoogkzdojbyfjrkqctpxbiobneylxgdtxasplaobozhntpvygoxnstbtgttgblwglwhitkgzozphtkabztqldmszppervqttiwagcjxravmhhiqetztmmsykmyhmduvcsrfrsdgkleplsibaubmrayyeyfefjthehbowwefztrgmmqnexngajhlsethbrfuejoddohddyfwpcpxhdgkzzrletpaczxwexvxlsvnvhnbeqqjvckvswxdgapjxfftwepjsbwokreoonxseqlgcfwrlfizbujxtoiqlfbqyialpodgqawxfgyhmpqtspyfvfoubaisnjpfqsltthwhcombqybkmwctqtongibkflfnyukuknuxelptrcmaaolkpktzzaruljbngyylyphipfavavgikaoxzooshpxuhjbyfnvzmbnogwgnnlrfavasbqxydreuqljquejdyhpuiriddowcyzpigqccnzpnqespgmzmhrnzkvivamucrqqgsyqtqyujwgaukraifwpkidcizbnljjhjvexqgdskqnlsqsbdtjmpzmydxnfupvekwgktyqvvdcuawtnawmlixwhotpdtgykvsjlozraxvktwqcicwmhmawyutxacwtmgdofgjckyloqbfdvkpkhoqsmyzppxduwtslncvzqwiflfqckvqavpngyxvylshgcbnfbrqgydbrnwmnondaipbhqnywcsuwghsfjkegdwkkkqtygegpxuytjgpgiasjoblgibhjejnqxuucdonpjwomcttuioslotzrbyurlhaugsruwsjxxetvaqclypnidraxlrmrhnxahrvnyyzjoawbsrawprdtheononccvispxarpbrjjakrfphxohijhxllhdrhrdndekmtxkgyoxbwcchwyywyskuevykumxwrjfhnqxfuxxckfmdcwywaljkpmayyblzdqbjkabckytbesolyfbzplkuoatfgzlkrpnkdqjksgohzslbxzxcllpjrjzwtxcsbtqrwhjkmsvfvofbunbcygwemzsmtqdsligqawxfgyhmpqtspyfjoldtmiuigllozfkh'
        expected_lista = ['iocavknzxv', 'eqtrhfgfk', 'cnazdo', 'jlwcdoxexkgcridekso', 'qgsc', 'hztoyh',
                          'xglkecabwadsnd', 'uaewnoedorh', 'ihnqykjrsugsogbdq', 'uqgpzjj', 'rfpcvvygllidegomp',
                          'kedibwnogisavsgmzsk', 'oswgypye', 'kmqwwrzfrvxosq', 'focwrvjldf', 'fv', 'wwwldccpofvk',
                          'vfcrj', 'yzhizpu', 'gyy', 'olqnmpc', 'nzlq', 'jirksgzrl', 'cpv', 'cqsdswsof', 'ry',
                          'ljwmlgbbgxs', 'ebsykqjvh', 'luseihvjurmhzhchdpqu', 'zpsbofhuxwgsqyk', 'wyfymdybyvwr',
                          'qhygxgxiwlvoizbvmw', 'qi', 'ldaqamh', 'pphidfvllyjdqriwuulr', 'rxycegfxohcitgxtd', 'yicub',
                          'vpurelzegtqfvhvhe', 'fyqvhdoubantzslluupp', 'lhtyqbzjquxyqwwqhii', 'cavmiiugo',
                          'quokolndboxzob', 'iscdrkpyqfusy', 'wxwszyamjbkcpjcgs', 'dwhenvogutekbws', 'czpyrbqqst',
                          'bfr', 'kxtkfzjlgvcvvlb', 'jyxtepsnmlbzxasxxg', 'sbhjtjfiuszwmk', 'gnnlr', 'sqqgcnkluxnkhl',
                          'pepuvbvhlsgjof', 'blphxhkkxvwsyqy', 'inxxh', 'ielpnmwlxymxvnwqwclo', 'gkdtgunvsdpurvae',
                          'dy', 'iybpnamndvqilpkqdorf', 'elhndpk', 'hwoazkvzvgepxjab', 'nbtvfdndlspckcyhgy',
                          'wfxhzeunav', 'pkaqvmp', 'kdabdeutknhtegabg', 'pjcm', 'puqervdmibhhmqpkpinz',
                          'zbvuquqzmqebebcc', 'yzwnphiox', 'gkvhppiitf', 'amucr', 'ekdai', 'owkzoyvqfogqwmvcg',
                          'cjbrmpoaq', 'bnfapladr', 'zhyhkvawzgjkdiybre', 'tpaczxwexv', 'zhhfldjs', 'ierutgmnoewotootw',
                          'dpkzvpokc', 'hkztpuwnsng', 'khkyukbsvunwxe', 'kqmlyvrkltq', 'olk', 'ksucnneqllhkktz',
                          'rjtnfbyhtqkmex', 'palsciacundtxxlhi', 'rabypprzahgmyhamvfgo', 'zxsswtgssjyoes', 'ohuol',
                          'ztrxkxjjjc', 'lxmtno', 'imayssejmq', 'bhrcvpenfxgwn', 'ebeillefjlkgonuzhrx', 'smlcj',
                          'tonhk', 'uvcnmjxhxudvvf', 'xuffyponjvngcyz', 'lbgfbeumb', 'yhkhpfua', 'cmwgbypy', 'nekioon',
                          'sugcatupurmfoa', 'gqawxfgyhmpqtspyf', 'gptsbobovuyktim', 'dmfbexqromnkjuuxeia', 'euqljquejd',
                          'hlogi', 'zozdkbgimktfnlkvv', 'abqgfditucyq', 'ezbvklhvusqrfradr', 'rjezusvnm', 'oglwshrauw',
                          'cwmhmawyutxacwtmgdof', 'slnlcq', 'wcdjccaaxdio', 'jigymtweearefllqkr', 'vknrxveztzos',
                          'lfizbujxtoiqlfbqyial', 'tynktut', 'xggjhcwfhiuorgbhngd', 'kk', 'fml', 'thhsnfyvm',
                          'zvvlemlvfxb', 'hocewtq', 'cptadkevsbmv', 'wilewsmprasaxc', 'tamrr', 'vbynkdhho', 'amdp',
                          'xngajhlsethbrfuejod', 'dhtilhpxeahujmsiikyh', 'oapbpmqkxocav', 'tcdaiohekbkpulfd',
                          'ewjfjvmbqf', 'gd', 'kux', 'ysaupocfojzl', 'qouaavy', 'xawyea', 'jlkleievmcicmcevjki',
                          'bifyvwlvfmifosl', 'jn', 'jjxrujiptysukrnxkanc', 'rlimxdwzjonwpsfejci', 'hvco',
                          'kmhsbxzhgpzdmityxy', 'tstd', 'xuapyxmuzdfdc', 'exxdysjy', 'dewrnwpuwhhk', 'nsimvnrsv',
                          'nkeiuqakxqjxw', 'ygecnjvxzt', 'wayn', 'aqd', 'sdwgttu', 'oaxtengefigihkhqtxp',
                          'anbkgvztrxsymxhw', 'dba', 'nhl', 'gqsupki', 'xynksicagukjfo', 'gxcvl', 'bzm', 'ubsipqjquu',
                          'rjrdkumzhjqbuz', 'oviuggiyokeauqjyuy', 'xdrazerly', 'bv', 'ljcwvw', 'awihhnbqrcabgnhe',
                          'kyyozwzro', 'vfrotiobsxqjxeky', 'icvvjggyalyia', 'yibbnpolsgx', 'zka', 'doaeawudv',
                          'ticwdgejoc', 'lghvndaxklqzbybwdgn', 'pnyrhhpxqbduhjfqf', 'yvsbefdnsyzlqra', 'fhunxhg',
                          'axlxtkrmcbgwvwuiaoy', 'hxgeabzscx', 'lpgem', 'nogw', 'ysqbbywjvvgkocj', 'agwdhrccvdswt',
                          'oxzo', 'wnsrppegdecgzj', 'gyothovfsiar', 'qzuxn', 'ttqshehrihfhqenr', 'ulnlabxkqelxbfv',
                          'otlncoxs', 'knwexzc', 'ukgljpssgtbfiyurlkg', 'qlp', 'svqozna', 'dxue', 'wlomwywz',
                          'gkepbaatkqbgu', 'cvu', 'rzqwnzrg', 'xlikn', 'ninebszynj', 'fkpl', 'kmyhmduvc', 'hdrhrdndekm',
                          'ldmszpp', 'ypkutbnpfmknmu', 'jlfdqbkcsjpuk', 'irnloujzdczoegw', 'wmfqupmsb',
                          'nngyessfwylenz', 'kzzpowgclrbydluykq', 'cchwyywysk', 'cwutkijiinwfqtase',
                          'lpcsjdcboicheumubgj', 'hztrekr', 'erzuyy', 'dohddy', 'cdtfrcroyvwts', 'bjfakylhgsfhzdfgvwbn',
                          'knqmgeiquqii', 'uqpbvdjycjebpixqcdkd', 'cid', 'hgtdwqvptg', 'solhk', 'hitkgzozphtkabztq',
                          'fygatavkhp', 'cftivoayze', 'sxrrzyxyda', 'ecvcmhwgesnogtorjv', 'pltromqhyjkf', 'ivujavsn',
                          'vmbaxjkff', 'ervqttiwagcjxravm', 'diyz', 'yyuzlzconlkiup', 'fpdtjedmbhk', 'grkcnjw',
                          'bbggvvugzvegrsvrborf', 'lyphipfavavgika', 'evbcfvwfstkjilbgktg', 'edpwknzmvevn',
                          'jhsrjtnhkhi', 'wundfghisdqzkz', 'yqanavfrhulwesj', 'fdacgreyvlawlvdmgu', 'ypagqbw',
                          'elogpdzxmzqydav', 'jtteyjvxigegzbbsf', 'arpbrjja', 'ijoebdgezlnhsqrjro', 'qmwkm', 'hakqm',
                          'pxdmfzkhr', 'uwbnykft', 'jlgtbwl', 'klnjadlkxenj', 'cqbudexio', 'itmwtlnwdlmvrgiust',
                          'kunklxzyrabquuviu', 'ddcfjkafhzava', 'wds', 'zxlsj', 'ysqynzfbq', 'xbd', 'auyiiwtcjh',
                          'kjglgasixpgabudmhdzb', 'ormasatuvkzlvg', 'wxdgapjxf', 'jljxkasozcycjgbcr', 'chgckxch',
                          'ribtkp', 'pido', 'dsnusmftc', 'kignzqguimgswqgwz', 'llozfkh', 'vcbqnqrripmnrbsvz',
                          'flkcjdoletsatetk', 'qqgsyqt', 'swqdbjblcwkvidjucqma', 'qtongibkflfnyukuknux',
                          'hmxneygmgyqgbyetr', 'leprbqmezywrckmq', 'hxvz', 'ncvzqwiflfqckv', 'bgremktjjzzp',
                          'fjhtfjluigvkixcvmbh', 'zlxvlvjc', 'joldtmiuig', 'ydxnfupve', 'nddf', 'bhjejnqxuucdonpjwom',
                          'npwauczizez', 'bbgtg', 'tbxmc', 'rlzdeejllvoyq', 'bhkvegwbkp', 'wk', 'rzsoabtln', 'vidntdki',
                          'xuhyiojyno', 'fnkq', 'umhv', 'djw', 'cyvovrlhzq', 'xnstbtgttgblwglw', 'oosbvhi', 'kbx',
                          'fkifpxrysefdmq', 'sgluodud', 'efmqagztpg', 'bhlfxbkntl', 'ioqwxxycpyjzjorauld',
                          'auzfpuydfvahkqgq', 'ernwwekpn', 'uhbi', 'uezhl', 'cttuioslot', 'aegeworwiow', 'nbxm',
                          'qoetjwxszgvrzsdmtuau', 'spx', 'sr', 'jbrtht', 'rtzqrcknlv', 'dndladxftesnjgx', 'wightvitoya',
                          'dfalewsvzugxi', 'xfuxxckfmdcwywal', 'nnfjkxf', 'umbxlsde', 'sumkyevo', 'slwnqeiyitj',
                          'kfsmspi', 'uiqvruwdlrhnbxi', 'qykchsdyqpwjchqxiaw', 'vmmkwfezky', 'tnbo', 'jsrbodolrido',
                          'dcortjwvqyvtwyu', 'pktzzaruljbn', 'yvvfbaganuh', 'gjckyloqbfdvkp', 'vxsnakqohbwublbuwqb',
                          'kytbesolyfbzplku', 'lgalrklgubwsnlca', 'aofkqkzyxyhcr', 'ranfr', 'ioxfngozf', 'ozzwirszanny',
                          'iplexb', 'kwgktyqvvdcuawtnawm', 'txkgyoxbw', 'uqeq', 'nmgveeyrh', 'cgeudarrlcpalvs',
                          'buvipg', 'ijwdv', 'rwbaxjdig', 'urgztglu', 'yqsexljpcpu', 'utggtilucgtjhzckbi',
                          'hkcxrbncosnnoflrfflr', 'rmqygnztladaxnkcbudm', 'duvi', 'hljpokdxlgxqlov', 'kjabgqqvt', 'vh',
                          'uaawyzfoebmlanmot', 'dlmtwpkevxolcslh', 'dcxfywzvwaaatmlkq', 'izbtz', 'zjlhfrqiymgqm',
                          'bniytlygnklm', 'jamplccymdqvw', 'uayhzwoab', 'lixwhotpdtgykvsj', 'siqrwvasdvq', 'wvhotxgshq',
                          'zzrle', 'zekjlwe', 'npy', 'loz', 'hembcmgnuiuiwttkxff', 'yhpuiriddowcyzpigqcc',
                          'cfvenucvgbslxrr', 'jp', 'lzziebbb', 'jlfekeepmeqijzqzpb', 'jyksacdsxe',
                          'ohzslbxzxcllpjrjzwtx', 'vjxxvxz', 'iezfrarflrmjs', 'scibbzkllhv', 'gbh', 'wahgqcjiamnsq',
                          'ayyeyfefjtheh', 'qhropwulmq', 'flru', 'sibvsmbcpwvjzcdjpkaf', 'qyrgnehydbhvny',
                          'qqwykjxduebwldzoulp', 'ecuz', 'idraxlrmrhn', 'aeobbnepd', 'gmgdjheovmvydr', 'uqzla',
                          'jermfue', 'jkpmayyblzdqbjkabc', 'naoobqmhhrhgve', 'ovzzwwbsrlvbt', 'crdiqdzmpnvv',
                          'lmwuhexspky', 'xjiqp', 'hqu', 'qbxikffpgptuyrajapva', 'tyefuchrkjw', 'yss',
                          'leqspekzpmkctflqb', 'nhepkhyvchh', 'pngyxvy', 'qdge', 'ghfglsfivwhf', 'drhccce', 'oqjajgpu',
                          'bjglvqfih', 'hujoaxhlgwpjvu', 'ibtqeljihqvpxssagjzd', 'pisl', 'rbhpgkhnkjsizp',
                          'cuqxnlafoszcfuub', 'pmsnvzgm', 'bbnynwbbojyoukihc', 'harvtmiapa', 'orbmf', 'cdccnkicmafxq',
                          'xexsdmkjxckqgqlpuo', 'jmreclh', 'nxixglyi', 'fraqrlcavwkxmlthxpdh', 'gyhdszwyawyqiuut', 'm',
                          'txas', 'fseukv', 'tpcirivmf', 'rqczvpvupkpln', 'jbvhguzqlqu', 'jkegdwkkkqtygegp',
                          'wmqnafhjt', 'skqespztxfzsfefa', 'efwgiigxp', 'axk', 'cioucrbwa', 'zwuvlvc', 'pbvnlqw',
                          'xuytjgpgiasjoblgi', 'kryaoranv', 'wjplzgenym', 'iqoj', 'ihdprinewaovkxltq', 'raxvktwqci',
                          'qav', 'uswceglqjcggmzf', 'iaepzxjezpnvpmajux', 'vmesr', 'isnjpfqsltthwhcom', 'wzgfqfffkpdh',
                          'xrfvntvplgljvrr', 'qhwxxyjdodazbemmtydo', 'flxvgwlqnhhuwspxlbh', 'ouqrn', 'kvfcbbdxmhgf',
                          'etvaqclypn', 'lsolkbzwdkilv', 'rdgziqo', 'hrl', 'yiwnvs', 'yfjrkqctpxbiobneylx',
                          'csbtqrwhjkmsvfvofbun', 'jhulnsusfyvwm', 'jiphmwnrtfndeyhulw', 'kidcizbnljjhjve', 'kiv',
                          'qygnssrmiiowlxregkqx', 'qynvmybv', 'okqtrooleedfzjljcgi', 'ucpobddlioudfbphi', 'cdcgynat',
                          'zpvzpmjs', 'haeldkagwlzkzoxniqbt', 'blhb', 'nvniavnwd', 'xirjkufrnr', 'ambgjam',
                          'wpzprvgrfwqjzyuz', 'oeywsosius', 'rinyhclbabhhxasc', 'iuodohetwub', 'arhiklpcb',
                          'wrkshbpsmmonwui', 'nq', 'oubbqodfmdpayyfolgc', 'tcwpzxibdsfsklwwzuev', 'llccmnbrytwq',
                          'uwsjxx', 'iftmtvrl', 'awththbzn', 'doyllyxekeqjfsitzalg', 'lifbeyxsqwbpicy', 'nkettedkdsaqq',
                          'yjxrlsnrmfpkdnrzahos', 'krfphxohijhxll', 'hlesnvvmf', 'yk', 'oizfxow', 'vjrw',
                          'lmfvgvdatvtrn', 'fnmsa', 'vohtccnpobaqdxgom', 'tiwylsbpzux', 'rhgf', 'oznaapna',
                          'ejgnsltqqexvpvvf', 'fsrmgvusoobiogpgkboc', 'inihejwzpdhbsnnigy', 'owkylbr',
                          'obcwqjoalswtmzq', 'bdqzdt', 'uevykumxwrjfhnq', 'heqcyq', 'ekzfm', 'yvqtglfzgy',
                          'pqajkxqrcgilrkgeg', 'tueayp', 'atgyxyesuxy', 'rfquqvyax', 'yweku', 'aduohawccx',
                          'niajymksipfnlm', 'euuocmkamqi', 'guulvxsbjoxe', 'vfras', 'jhc', 'xahrvnyyzj', 'oj', 'bubjc',
                          'xc', 'oxobtcautvwnbs', 'zidtbmjpe', 'cshoteyyprew', 'favasbqxydr', 'uonpozcfwqnm',
                          'ccusmcjtxfidnxo', 'hwdrofkjsroifol', 'vqaigmhqec', 'ifnmbogl', 'uphsxgu',
                          'tnitplvmkdhhtedjkkal', 'yjvbs', 'qqmgsv', 'amc', 'zrbyurlhaug', 'bqybkmwct', 'tpdmoogkzdojb',
                          'plaobozhntpvygo', 'hhiq', 'etz', 'tmmsy', 'frsdgkleplsibaubmr', 'bow', 'wefztrgmmqne',
                          'fwpcpxhdgk', 'xlsvnvhnbeqqjvckvs', 'ftwepjsbwok', 'reoonxseqlgcfwr', 'pod', 'vfouba',
                          'elptrcmaa', 'oshpxuhjbyfnvzmb', 'nzpnqespgmzmhrnzkviv', 'qyujwgaukraifwp',
                          'xqgdskqnlsqsbdtjmpzm', 'khoqsmyzppxduwtsl', 'lshgcbnf', 'brqgydbrnwmnondaip',
                          'bhqnywcsuwghsf', 'oaw', 'bsrawprdtheononccvi', 'oatfgzlkrpnkdqjksg', 'bcygwemzsmtqdsli']
        expected_parola = 'ldmszpp'
        expected_ls = ['ukwbrckvmrbavxshsq', 'cdeuiynijdshccg', 'fdl', 'hdjushh', 'odauicbwojstnwyxfej', 'znx',
                       'owhtzcuhmc', 'slrsyhktxdb', 'omgwadbzxugpvp', 'bge', 'pwcwxpwrde', 'wapydjmjitxkxmwwnc',
                       'knvmoyhwjopywzra', 'heidoeornq', 'dcmfmbnxmnlmzqmyukvv', 'juxmgnbmxfojgnblh',
                       'xszstrvtvdfcwbmzkq', 'boevdsooqszeu', 'dxnmd', 'ruwhicf', 'hceyswgy', 'zvadvf',
                       'cgayjaaupccqynuphb', 'xgktejfhvf', 'lpcci', 'jdqrsh', 'ylme', 'vjkbqibpzqrzkwk',
                       'yzhwmgxjrzapgodwardh', 'tmxqjyndcaln', 'wjgpbwgrkvuvdyvflxtx', 'tiwenxm',
                       'skfpdvtdvnhjziahmmmq', 'zowkhpglgcfbdcj', 'cmqejiqlhscmbzkxer', 'bengcjukdd', 'hwsfm',
                       'osgdfmacl', 'gzaoscwfleexx', 'nnbudmzsyi', 'kebzwqdcnm', 'sahpwbzrin', 'npxlatchxeoamkr',
                       'yhhnzc', 'dldgnst', 'dnngxymnpfhpli', 'odjsnldgzndepplvp', 'uhmzuxjbsnozxx', 'tukolmzmmpnzr',
                       'fkqho', 'pzyrke', 'nznsixilvdn', 'tgcffrhx', 'oxhkgahysfjzellyjthq', 'cqfbcqgzbdfbmdlovz',
                       'rfma', 'pyjzjzic', 'aqzde', 'ea', 'dpursjzypqlrpyj', 'zcjdvltvzntrtsrxfki', 'wthpfbvecencz',
                       'njxyyooo', 'psecscjjzxcktxgwp', 'vdwuksk', 'tdbqgyjzchrecoce', 'ufrataqqekbickcyn', 'zykotbq',
                       'abgjxpuegfv', 'fgephbzzslvf', 'bthpqeshztpxmd', 'fhgdiucpuualbwr', 'lfubjkic',
                       'gyxsonajncirfvojwaeu', 'utfejxxqp', 'bxqqcxfisgwl', 'iqcp', 'rbedyrzb', 'wqysobwirohmttkanmc',
                       'upvtthkzjxmk', 'rhvlyixvhoeoqnjbefe', 'doqdjfgvuzq', 'jwzjxv', 'syslrgtlfmmhp',
                       'icixppwpzgwssg', 'nfkldvvdwmoxrjdvsx', 'zdduackw', 'gyidnknqjhkctq', 'foh',
                       'xeherrwjqnxtqedvnya', 'vkxzwzwgbric', 'ahjecwlqsgjo', 'ndocdtzm', 'fdbmtannn',
                       'vqmhwhpbckfmmphcu', 'avhfodftbtekyyics', 'bamifkmiuhtjiipib', 'dkllpmics', 'szghcfwkxnosdfaqsa',
                       'eyr', 'jq', 'ayrzhdpbjpkgzpbluhl', 'idj', 'ffbgsoohouucyne', 'towvrjplpivkcnzalzc',
                       'zufjntqagdx', 'llfjrztqp', 'htkbncfzyikxc', 'blqmjcjtoilqkt', 'klkcyeaicxcm', 'kcqm',
                       'pyafvndhqbkijxlvwaq', 'llmyxfmmx', 'lcaiwxgnaxow', 'telze', 'jvlivolavaysntsnn', 'kxhnzej',
                       'wtslpbvidzikehmweyun', 'qhtgxbq', 'yppbkhwnyznotez', 'obmotcwjiowggduozt', 'fe', 'tkxy',
                       'ihlxptthztjocu', 'nhginwlahfzv', 'nopo', 'wtooeqowtmuv', 'njlnyyvfwtajdqo', 'lzgccjrazrst',
                       'pjqkdkp', 'bitohaapxumx', 'blnrpg', 'gclastz', 'frgnizulbia', 'vwyvd', 'xlukxapduyrwdr',
                       'wlovhl', 'lohfyramj', 'uxdealomnlvdbijc', 'dknlejqm', 'elxrnyldolfohpuxmmhy', 'ltqmeztddawfq',
                       'jutbrfkuvpcwqblxsi', 'cmzrfvhgswr', 'romwxefbxp', 'howj', 'dmwmfvt', 'sxiqoadlvdhwxgr',
                       'vlmceclfu', 'txrjjtzlvbjypwdapskc', 'qrknkxxkyvhohaechdo', 'nlonglznvfmp', 'nidzkjmmlhpvzfkt',
                       'vlymfzafhgvptli', 'kltz', 'hggex', 'jkvspznjmzlervp', 'zppnatxwzpxftfcm', 'apsavhyum', 'orep',
                       'ufbeo', 'txzvjoscxctdyi', 'rgy', 'ydoh', 'jc', 'remytzaxzf', 'aahpmfvrhiturdijjt', 'symvqmlal',
                       'ewnx', 'yozfm', 'bstm', 'hdrhrk', 'exbtqvlvduegaxxuc', 'iohqfptlpayc', 'ffizpazqhilogfpal',
                       'blxhcgyxake', 'cghzrnlngefytmzxuz', 'amqqavsisc', 'nbjplllhqh', 'fxiv', 'psalja',
                       'qygklbtcdvrudyvd', 'wvffgfrsxrsiojrqx', 'nhdvlppcvluedcndcvm', 'kozzehogvhqhgavg',
                       'umsxqekxochnppv', 'pauewojjapxn', 'qyueb', 'gnwixenelrmwkcjuwwqc', 'poc', 'iakkhjtmauwukp',
                       'opjahbumth', 'qsdhlaieggijxu', 'cnzxupwiwtnkm', 'uzedhmavpuxjqo', 'jdaraqufatelkznlkq',
                       'wgfwmhujlfnjcunudjrz', 'rwjathvtsjzftevoph', 'rfoxigthiiqguqjhkgiy', 'dnkcrehqd', 'bxfep',
                       'wojthgl', 'opzwizpdttd', 'pxsmfszeub', 'rtdjvmsehgzfmycac', 'duzysbbxxynikkuww',
                       'wajbwkdqwodovnbqe', 'txexykoomptsu', 'dfevzccjnjjanqqcaz', 'btukisan', 'hccqqisisamjbmk',
                       'urqm', 'rwsvcrimmusoylo', 'ytquopplixfrwihvjsv', 'vvbgaqv', 'wylgnkeyty', 'ivbr',
                       'guttfkieoawjnasz', 'lszzruuaooba', 'ecnta', 'filea', 'wvigbxzetuhctsnkmwa', 'xhuwziscavuzfjwz',
                       'nyirrdwzdaodq', 'cxaaibz', 'iokzqdohryykynaesdh', 'vrwcehfidwktnujrle', 'pkgbltuggkacosnljvl',
                       'rwcnpzdsasiegd', 'etpevdsnsczdbzpd', 'iavxythynfevwky', 'okbcwdkfbi', 'wabnvpufdqxunwuzq',
                       'walsgfaewaqcua', 'vgsdawvgtto', 'oendhbhpfnfs', 'otcgrtsyvawrlwiie', 'sgxpfvrqvfonoyp',
                       'qjmxmif', 'hxtrapetwgi', 'vsnxahorliszvh', 'hcx', 'ivclthcduuayfk', 'vljviqxy', 'jeeyffhely',
                       'hknoazpixquiydixw', 'zitkqxoxpafo', 'zcfcfw', 'cxbwslfhsa', 'tvdhwramhspctr',
                       'ypjbnibwsbznhswql', 'fosmgjnxpsewweoo', 'ysnbnuypndmfsfm', 'vkcvjsbuucmwrxyyn',
                       'cztmdzcodujfifrwrqtc', 'ocgufiazufjqhmajv', 'qtywlqcelbvbjrip', 'rrhlqfxjwsrzepdsjvtj',
                       'qdfkknufixbsb', 'iyffwjptpx', 'jz', 'hpytv', 'jhpqmuebazliv', 'kur', 'hyouipokevdpryja',
                       'bjoaxaloochjjiqr', 'cdqerfrqltdbennygvb', 'auhiqdvwjc', 'iyjrjgzef', 'gircmoadgzotwec',
                       'ngzhimj', 'wteycpjzinsudsbk']
        return self.do_test(parole, testo, expected_lista, expected_parola, expected_ls)

if __name__ == '__main__':
    Test.main()

