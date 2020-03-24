vowel = ['a', 'i', 'u', 'e', 'o']

def countCombination(count):
    total = 0
    if count['a'] > 1:
            total += count['a']
    if count['i'] > 1:
        total += count['i']
    if count['u'] > 1:
        total += count['u']
    if count['e'] > 1:
        total += count['e']
    if count['o'] > 1:
        total += count['o']
    if total != 0:
        return total
    else:
        return 1

def validatesubstring(s):
    check = {
        1: False, 2: False, 3: False, 4: False, 5: False
    }
    count = {
        'a': 0, 'i': 0, 'u': 0, 'e': 0, 'o': 0,
    }
    total = 0

    for i in s:
        if i == vowel[0]:
            check[1] = True
            count['a'] += 1
        elif i == vowel[1]:
            check[2] = True
            count['i'] += 1
        elif i == vowel[2]:
            check[3] = True
            count['u'] += 1
        elif i == vowel[3]:
            check[4] = True
            count['e'] += 1
        elif i == vowel[4]:
            check[5] = True
            count['o'] += 1

    if check[1] == True and check[2] == True and check[3] == True and check[4] == True and check[5] == True:
        return countCombination(count)
    else:
        return False


def vowelsubstring(s):
    subs = ''
    abs_total = 0
    for j in range(len(s)):
        if s[j] in vowel:
            subs += s[j]
        else:
            result = validatesubstring(subs)
            if result == False:
                subs = ''
                continue
            else:
                abs_total += validatesubstring(subs)
    if subs != '':
        abs_total += validatesubstring(subs)
    return abs_total


print(vowelsubstring('tstikeaoaqqiiyemepiuxixuiooojmsdyiftuuyaajeoxiufiveaoaouadaoivyaexmttbuusqjozoetoaeaemhebiwnpaacquueoebflaueoreaeerilvgorgveoiaweoejvyzqaifueeiiejbkxovayefvsnagypixaesyahaiaavoieairaucquvrikipieqoxuuijuaogvqoiuioueeouokasosfooeeeeaabieiqeaxaooeoufhebjedaeuaneueivaeduwhaamiioekirldeoyooouaxouxoioxyoaieaoowafehiqouoiwuixroaiaxuinooiaudpvefuoaueoqoeaiueiowaltoihazwfcyjuemsibowweiaylaucikbacoiiaohqoouiiaueimaizihnoqiioeiiueajfqeuaaiceuueoauagwoaiyemaaimimauiuooeeioouoeojogarglaaomooiqubiifiaocuhuckeaoieeazibiyaolasakeaiueaauabyieauogkaoeiodeamoiwcoeoataujnuyuxzucdeiujhteicdeszvkfawceeuouoeoiodoerecoyvwoiehiiaheeuhsgdioueixkxkaieijoaiukmiiulueqqooogiquhmdeiaehoemuhebfxayauoelmoemuscxwahbzgeerooieuchiuuugquiokeoeetezffapioeyodvauduamiafinouuoaibuukeesshituueqwiukohyuuioeoudhuasaeurkieuuaheaivinvewioioozeuuawgoxaoiolpoabpbuwuauougcoeaedzagaxieyveqeimepduobefoxoukwziobuaigwuhkuubaoquocoooaihxgrounoueiiixfuanbbjgnmaeqfuweaweoankenasatbeeeumaoocdpoaouisiosiaenoiicaeaewaaudddkzeuocoiqsoeekiwoauoseeoxemznulemuawaauajxdiowioueefxvedouhaejoqeioeeuvaluorqmeaxeaioaiixpeuuxeaomoeuuideujbqxgsaiiiuwvuiaeveeroiihauxioeeiirvhodeoesvakliioougiglajeaieooeouiaieaoooiaoaikeyogbiuuutameseiozwwlvioeiaisugpinuugoancoanoeqoodbidowcooequesaiuoeuguwezoliifjejgijbaiibitiipeaholeouaaduogaeagfiosiuuioazojieqiailoiaeeazriooideooeyeeizneoijruzuuoaorootdecabloekoageqwicoqumeezgikwatiiwuubkiaiatkveufugiujzteoauiutsdieowoaopkqouuhuouoxceuamxauveueovngoruyeoquiuaiaeuaououuokniaomwxiouffxaeealtetpeaedouiugeifnovadoaoamouovsaiiiooeaaozghgaqehoaaepouexdrquoreigeieiiuaopfauwgauujedevzuasemnojoeveoaxenaouaebgeweuuefmowdirowgostoeaoimzfdouuwiqweieuiuanfooziniweoonuosfxylegnjauuyouzyuadmeuoierkwuuiuiaeodiggiadieoiiwouviuvuukexugpioaeitazmjenaeayiesuiulowuuaambuaeueceoauuniiuiopdtiaaioquziahsuorosideoauhumkoiqikvidgeeqiuoieixtowatmeiiuouoeevoouuakuymrrodauuafuoiaoauouioueiusiacuireauodoioiieqtauiooeeiwgoiozyouuuouobciceeovciefauzojdavcabevipkrenwgoxkxiazvaaiooujyojohiaaaownzaguiusumepolojkoegaiihqaonathoobinoemiaaauaueueoleoeaflotdzgaoiuueeorenduenuahudueiruaehyhantizbuayfhamhjehovxaeekeioauumjoiazkeiqmvruceiuiiemveoueuneiiuezpxhceaoiatiitiviioduyeuamuahaqreoiuuuueaiawkawkuxoccuuawobjiauunaaueioolqlafiuaaoipikzzauuuaogdaqoxqqioabeeuhtivibuuesodoiuqhiyzifdiueebivqosuhbavoeiepiiahmeauzumgqvoqihnueeeutnoleeaaeamotcwiinzeiaewooinymlkooaakiouaayfeuuoeeieskqionuaiuieyaediuiyoorwiqaeoeaquueiihesoocieljuiceazikuoeeikcpaaejuxbzaishnuegaoatijiyneojxequoaellfikiatxiuvutiaepeoiuhayixiiaenecokbaxeeiieigeutieofubvuvmoaipexiiauxxfaihzehaesekpamaseyiiiqeuuaoukalvaaxuiiiyswveueeoeieeejzuecoiaiasoauudtehyifsytdeuqwaouotiaiuutiiupyofjiaooouifpuearanwiajuauiieaooouueabuitijoaaiaauuieeuyhaiepujzeetkujaeouguibeatdautaieifewatoppeeeyeooaeianyuuauuveaaeineaejenuouaufmuojooyehaajeorgaeeizaslecloeiihowoxsiiapauualocaihoiaeeeboioyedijngieoaubuieoaeitaaalsoooojyoeebwaurduuulijpoveaeugjtaiiafvaawqnkjiicexxaoaanaoidxtxaeroutuaijvyektauudobiqecueeuqeyiubnuaoagajkivoluuuzeoodieqoraemijiatusztsvigeajiaoauujzykgrapouaetbaiaayejaiuogezxnumujmiouowuouomeuooioyueeaidomaeourqaiunopucauouqiawaoxiuybaupeeioagaepuhvagmguviueehiasyaaieojimveopeaoauweoiuiaqowjuoabiueacaqzqoyumoeusriieotinluaaeeevitaaeqaawoiaodabinusuiuiaeauyeiizacmqioliaioquqeuaofieoooeeoovueuteargobooudyadakeouaupewqnefuadqueouziaeeooizqoiaauknusviyehrhuuoojihuuvebimbwfiqiupauyioesgsonfiaehoneaixeamwyahoaseauiulrqmozutlvuaoxcimuiireaooomhkxeivdyoovtooimuisiaiffzseucaeaoaosuozpebzwuooriojyeufweiogueleyuaiiaovvooodiudpekebiooumbqoccrjauqvevjiokivqitvoicofeailuusadbfvoblueonikxviqeboikaigieuiuupiuaaeoldukocedeeuiajfeaoaeuidfrzisiaeoieuwuaiiuuaufewxauoimbikourusiuacuegejoiiineeheoakelmeaouuswuoesuaiiuiuibhavocamiduekouifueuqaoeftaatveaseoounieofeeiaaegfsejodveiaoopqnfrdjoiaaiaiaoievnmuarauiaksomoyoacqqoiieaoioxphpaekagectvzvaqomeumauauucauiisionhoaiaiouobuuniuecvajpophiupjmeiwiiacowuiaymizoneqjuaiecwoaiueeznxuvuihougoebuoaiwiuuueeveieupeibpeueouaceitneouooynfyoiiyiexkofuiuaaeuumiaotbabgiomoeabauraeiiauapoagaeoeaiayuiwaiqeaheaumeemzbjuuxibuiuigpegoaiwudialonafuzepveacwaqeiowuijfeqllydawaieuuoatiwooiyrauuuouowleoorusieoaauaaojiaoimsdauoyxuaoieijmleiqioriiaeuatvkouahixiaflopuxhijuoaraoauizvieamumueozumefeztesubuiahpubqaogejpixpmzaeaeiqwouosuusioutuoiqyerouqoougsuioiiweeiozbooapjdrhyrilffvniqyeyaaiiuwbdieeiaebucirauulaieobrszaaqhuoydobapuigzioapuavyuzeoiieueuiuuaorouosoueiroiieudeaxakeunwugvbxhiiuiaibiopaiuaezebuuaugwioewuaipkaiolaeehhauaoaghzoicvouieaosquubwectwuuolcaiauuaitjaipoaufuuuiiazaaaiarieeiareoaifouuukojvoabxxdmcnarkpesudmcoolaroocooodiaocmaxeeeepiothjoooeiaauaslaieeifeeohuuveueaurgiuoiwiiaefwereoakeujuyeeviovtuakueauooaouiomemqasoeaiqmaaesutveiincleaoooburgewijokveoyoiaxhsjdaauaifsuoeliuiloeoepumuiaaieouhzejoauseeaeeiaueitozeeriiacamoorzijjickafoauaoeuiaovaokgoaoesukseeaxzejuuibiuzucltuoteeqsiieaoogdeuphuceofiaowvieaeewxvoameoeujautimauxbaouoftizaoyvvtlaietaeyokfbiiieaauuiacueeaiooaeiqiuuoguaaiaaseyjbixiihoaazaaaaaqueouaomugyoouiynaeeoaihkqbtoiepufauonxaecaioomvuonouiqoochdoeeozqiiujexbsaauasuuadiawhbueaxoseuiahoomosdemciarliy'))
