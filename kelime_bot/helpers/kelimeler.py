import random
kelimeler = ["gözəl ","bilik","problem","təmin","ayrılmaq","zaman","su","edin","istifadə","yox","bax",
              "dərinizdən", "çox", "amma", "lirə", "oynamaq", "çiçək", "şəhər", "yüksək", "döyüş", "varlıq", "do",
              "güvən", "lazım", "müalicə", "vahid", "rahat", "soyuq", "orada", "kitab", "pay", "hesab", "bədən",
              'zəmin', 'aşdı', 'sistem', 'gözəl', 'çəkilmə', 'texnika', 'yanlaşma', 'il', 'tarix', 'dəqiq', 'bacı',
              "cərimə", "əgər", "halbuki", "qaytarmaq", "vermək", "var", "qalıq", "şəxs", "başqa", "dövr", "yenidən", "bunlar",
              "kitab", "hadisə", "olmaq", "sən", "dövlət", "ön", "çox", "baxmaq", "on", "belə", "bəzi", "başlamaq",
              "saxla", "birini", "biri", "et", "su", "bəyən", "dövlət", "sağ", "orta", "başqa", "böyük", "etmək",
              "yeni", "daha", "soruş", "onlar", "yandır", 'soru', 'ikisi', "həmişə", "səs", "anla", "yox", "saat", "necə",
              'bir', 'və', 'olmaq', 'bu', 'üçün', 'bu', 'mən', 'demək', 'çox', 'edmək', 'nə', 'bəyənmək', ' daha ', 'almaq',
              'var', 'öz', 'gəl', 'birlikdə', 'vermək', 'amma', 'sonra', 'qədər', 'yer', 'çox', 'insanlar', 'yox', 'hər ', 'istəmək', 'il', 'çıxmaq', 'görmək', 'gün', 'biz', 'getmək', 'işləmək', 'şey', 'o', 'bilmək', 'əl ', 'zaman',
              'ya', 'uşaq', 'iki', 'bax', 'iş', 'in', 'böyük', 'yox', 'başlanğıc', 'yol', 'qal', 'niyə', 'sən ',
              'mövzu', 'edilməli', 'yaxşı', 'qadın', 'ev', 'olmaq', 'olmaq', 'demək', 'göz', 'lazımdır', 'dünya',
              "yemək', 'heç', 'hətta', 'necə', 'hamısı', 'əleyhinə', 'tapmaq', 'belə', 'yaşamaq', 'düşünmək', 'eyni', 'içmək', 'lakin",
              'şəxs', 'onlar', 'birinci', 'görə', 'ön', 'son', 'bir', 'forma', 'vacib', 'üz', 'hər ikisi', ' göstərmək ', 'etmək',
              'alt', 'gətir', 'istifadə', 'çünki', 'yan', 'indi', 'kişi', 'onun', 'başqası', 'indi', 'on', 'səs', 'həmişə ',
              'sağ', 'durmaq', 'qız', 'hamısı', 'cəlb', 'etmək', 'danışmaq', 'pul', 'anlamaq', 'ana', 'az', 'bəzi', 'ata', 'həyat ',
              'yalnız', 'kiçik', 'daha', 'məlumat', 'an', 'soruş', 'o', 'o', 'yenidən', 'təmin', 'nəticə', 'istifadə', 'xarici ',
              'ad', 'o', 'müddət', 'döndürmək', 'yanmaq', 'oturmaq', 'demək', 'çıxmaq', 'dərhal', 'vaxt', 'yaş', 'problem', ' dövlət ',
              'var', 'sətir', 'yazmaq', 'faiz', 'ay', 'atmaq', 'tutmaq', 'bu', 'hadisə', 'düşmək', 'eşitmək', 'söz', 'gözəl',
              'sevmək', 'bir', 'çətin', 'almaq', 'o', 'qoymaq', 'bir', 'sistem', 'birlikdə', 'veriləcək', 'kim', 'almaq', 'gənc',
              'qapı', 'kitab', 'on', 'burada', 'gecə', 'alan', 'birimizə', 'burada', 'gözləyin', 'uzun', 'yox', 'gün', 'dövr',
              'dost', 'məhsul', 'ailə', 'üç', 'oxumaq', 'kişi', 'hamı', 'güc', 'bəlkə', 'real', 'tam', 'əlaqəli', 'münasibət ',
              'mühit', 'köhnə', 'axtarış', 'həyat', 'insanlar', 'yaxınlıqda', 'küçə', 'tarix', 'mülkiyyət', 'bölmə', 'özəl', 'səbəb ',
              'heç', 'kim', 'çox', 'deyil', 'əgər', 'lazımdır', 'xüsusən', 'məna', 'yüksək', 'bank', 'bir', 'dəfə', 'ayaq', 'hərəkət', 'geri', ' cəmiyyət',
              'alət', 'element', 'növ', 'qərar', 'bax', 'hava', 'nömrə', 'fərqli', 'qrup', 'otaq', 'forma', 'forma', 'xəbərlər ',
              'allah', 'həmçinin', 'gələn', 'az', 'sual', 'geri', 'qazanma', 'poçt', 'məktəb', 'açıq', 'öyrən', 'sürüş',
              'dil', 'şirkət', 'mənbə', 'bitir', 'proqram', 'davam', 'hərəkət', 'rəng', 'açmaq', 'sağ', 'inan',
              'təhsil', 'bucaq', 'parça', 'qəzet', 'tərtib et', 'əlbəttə', 'dəyər', 'bilmək', 'struktur', 'doktor', 'gəlir',
              'tapşırıq', 'məqsəd', 'region', 'film', 'to', 'müştəri', 'artıq', 'telefon', 'təhsil', 'dəniz', 'ikinci',
              'qalx', 'hətta', 'təsir', 'inkişaf etmək', 'keçmək', 'bədən', 'düşüncə', 'milyon', 'oynamaq', 'dəyişiklik', 'əsas',
              'yaratmaq', 'çatmaq', 'düşünmək', 'keçmək', 'mədəniyyət', 'qurmaq', 'amma', 'buna', 'rəsm', 'etmək', 'işıqlandırmaq', 'içmək',
              'xanım', 'xidmət', 'ehtiyac', 'nöqtə', 'istiqamət', 'bəli', 'oyun', 'artırma', 'təkrar istifadə', 'proses', 'qısa', 'asan',
              'hansı', 'qiymət', 'əslində', 'qəbul', 'edirəm', 'orada', 'diqqət', 'uzaq', 'kompüter', 'gələcək', 'görünür',
              'məsələn', 'oğul', 'dinləmə', 'uyğun', 'lirə', 'istehsal', 'dəqiqə', 'unutmaq', 'gəzinti', 'belə', 'pis',
              'avtomobil', 'ağız', 'hiss', 'tətbiq et', 'hələ', 'nümunə', 'çox', 'baxmaq', 'dərəcə', 'mümkün', 'belə',
              'divar', 'on', 'incəsənət', 'əsas', 'xəstəlik', 'tələbə', 'televiziya', 'metod', 'masa', 'ölüm', 'komanda', 'top',
              'baş', 'musiqi', 'ayrılmaq', 'enerji', 'universitet', 'idman', 'mehriban', 'ruh', 'baxmayaraq', 'hissə', 'ölüm',
              'daimi', 'sağlamlıq', 'müxtəlif', 'bundan', 'hiss', 'halbuki', 'səhər', 'internet', 'texniki', 'çıxış',
              'mərkəz', 'ekologiya', 'əvəzində', 'səviyyə', 'kənd', 'idarəetmə', 'aşağı', 'cavab', 'lay', 'torpaq', 'axşam', 'araşdırma', 'götürmək', 'iştirak', 'etmək', 'əks halda', 'qurmaq', 'ödəmək', 'sanki', 'qan', 'xəstə', 'şəhər', 'enmək',
              'indiki', 'məlum', 'həftə', 'trafik', 'hesab', 'avtomobil', 'planetli', 'davranış', 'mətbəx', 'şəhər', 'bəzən',
              'müəyyən', 'ayrı', 'qiymət', 'haqqında', 'çıxarmaq', 'qol', 'yalnız', 'hazırlamaq', 'şüşə', 'nəhayət', 'yavaş',
              'zəruri', 'əhəmiyyət', 'ər', 'yalan', 'aktiv', 'sənət', 'faiz', 'siz', 'satış', 'təbii', 'öz',
              'iqtisadi', 'ağrı', 'yox', 'qorumaq', 'mərtəbə', 'iqtisadiyyat', 'ümumi', 'müəyyən ', 'foto', 'heyvan', 'müharibə',
              'mal', 'saç', 'itirmək', 'qalıq', 'dəyişiklik', 'dörd', 'həqiqətən', 'səhifə', 'texnologiya', 'qurum', 'beş',
              'sektor', 'geniş', 'kağız', 'ətir', 'sağ', 'isti', 'əsr', 'küçə', 'bazar', 'davam', 'etmək', 'istifadə', 'sinif',
              'sevgi', 'doğulmuş', 'ağır', 'yenidən', 'günəş', 'siqaret', 'ağac', 'söz', 'bina', 'arvad', 'qaçmaq', 'partiya', 'yataq ',
              'müəllif', 'qulaq', 'müəllim', 'səbəb', 'sol', 'yaxşı', 'yağ', 'çünki', 'başa', 'düşmək', 'gəlmək', 'gülmək', 'qayda', 'tutmaq',
              'satmaq', 'şeir', 'göndərmək', 'uğur', 'möhkəm', 'hökumət', 'ürək', 'kəsmək', 'layihə', 'lazımdır', 'sürət', 'künc',
              'vur', 'model', 'balıq', 'bazar', 'baxış', 'burada', 'hazırlayın', 'miqdar', 'birinci', 'kvadrat', 'ölçü',
              'seçmək', 'tətbiq', 'etmək', 'bağ', 'sevgi', 'çörək', 'boyu', 'qaçmaq', 'dolu', 'quruluş', 'demək', 'qorxu',
              'kömək', 'görüş', 'əşyalar', 'gözəl', 'it', 'məşhur', 'böyümək', 'ətrafında', 'gəzmək', 'olduqca', 'üstəlik',
              'yaşamaq', 'ağ', 'istəmək', 'arxada', 'çalışmaq', 'qardaş', 'çəkil', 'harada', 'oğurluq', 'icazə', 'qorxu',
              'işğal', 'polis', 'yalnız', 'izah et', 'fikir', 'tez', 'pəncərə', 'işlə', 'daş', 'yanğın', 'fərq',
              'kifayətdir', 'çox', 'bəzi', 'şərt', 'qonşuluq', 'lazımdır', 'taxıl', 'istehsal etmək', 'üstündə', 'tutmaq', 'nazik',
              'neçə', 'ümumi', 'növ', 'şəkil', 'beri', 'dərs', 'sədr', 'qurtulmaq', 'sayı', 'dəfə',
              'olmaq', 'qərb', 'başa', 'düşmək', 'hər', 'hansı', 'sinema', 'fərqli', 'hədəf', 'yuxu', 'dost', 'yanmaq',
              'anlayış', 'usta', 'mətbuat', 'kənar', 'nəzarət', 'flip', 'din', 'güclü', 'hələ', 'plan', 'beyin',
              'elektrik', 'arvad', 'on', 'ət', 'təmin', 'edilmiş', 'oxuyan', 'xətt', 'uçmaq', 'üzv', 'dəri', 'ruh',
              'əziz', 'yanaşma', 'proses', 'baxış', 'elm', 'irəli', 'ifadə', 'bədən', 'xatırla', 'qəza',
              'hərtərəfli', 'dağ', 'yaxın', 'addım', 'ciddi', 'həll', 'impress', 'bələdiyyə', 'inkişaf', 'seçki',
              'ağlama', 'əlaqəli', 'konsept', 'artım', 'fəaliyyət', 'zərər', 'dərin', 'salon', 'bir növ', 'kəsilmiş',
              'izləmək', 'birdən', 'tutmaq', 'saymaq', 'toplamaq', 'ütmək', 'qışqırmaq', 'məsuliyyət', 'hərəkət', 'etmək',
              'məktub', 'soyuq', 'canlı', 'idikeylem', 'maşın', 'istifadə et', 'köhnə', 'boş', 'görəsən', 'kibrit', 'menecer',
              'gətirildi', 'metre', 'saxlanıldı', 'keyfiyyət', 'bitki', 'dəyişiklik', 'tibb', 'kredit', 'qanun', 'uğurlu',
              'bir', 'imkan', 'cəza', 'hər', 'şey', 'yoxlama', 'top', 'ekspert', 'doldurma', 'kanal', 'boşluq', 'uyğun',
              'illik', 'buna', 'görə', 'yazmaq', 'aid', 'olmaq', 'barmaq', 'saymaq', 'atmaq', 'müəyyən', 'etmək', 'normal', 'hele',
              'prinsip', 'qırmızı', 'rol', 'mahnı', 'heyət', 'hazır', 'like', 'nəsə', 'müəllim', 'oğlan', 'gündəlik', 'siyasət',
              'cinayət', 'niyə', 'səhnə', 'ilişib', 'özəl', 'oturmaq', 'saxla', 'artist', 'üstünlük', 'uzamaq', 'səhnə',
              'əlavə et', 'meşə', 'ayrı', 'sifariş', 'faiz', 'adətən', 'həmişə', 'hekayə', 'hüceyrə', 'orada', 'roman',
              'vergi', 'yanmaq', 'qardaş', 'mətbuat', 'dəstək', 'geyinmək', 'səhv', 'limit', 'birlik', 'iş', 'görüşmək', 'yarım', 'yetər', 'fərdi', 'qaranlıq', 'avtobus', 'sənaye', 'körpə', 'vətəndaş', 'nazir', 'zaman', 'millət',
              'reklam', 'yüksəlmə', 'ölçü', 'jurnal', 'inflyasiya', 'sosial', 'kimsə', 'keçmiş', 'xəstəxana', 'varlıq',
              'görüş', 'jurnalist', 'daxili', 'iman', 'keyfiyyət', 'bitdi', 'bitiş', 'yerləşin', 'giriş', 'rahat',
              'cəmi', 'birlikdə', 'mağaza', 'gizli', 'oxşar', 'dəri', 'çevirmək', 'döyüş', 'problem', 'xidmət', 'müalicə',
              'yaşıl', 'nazirlik', 'təzyiq', 'reaksiya', 'cümlə', 'istək', 'azadlıq', 'yenidən', 'şəxsiyyət', 'məsələ', 'üçüncü',
              'müəyyən', 'qiymətləndirmək', 'maraqlı', 'sürücü', 'süd', 'tutmaq', 'əşya', 'beynəlxalq', 'namizəd',
              'çəki', 'milyard', 'sağlam', 'sıxıntı', 'tanrı', 'rəftar', 'sosial', 'nəşriyyat', 'diqqətli', 'son', 'dərəcə',
              'topla', 'investisiya', 'işıqlandırmaq', 'qarışdırmaq', 'təhlükə', 'zaman', 'dairə', 'imkan', 'proses', 'qarışdırmaq'
              , 'hekayə', 'tamamilə', 'təyyarə', 'cavab', 'təbiət', 'evlənmək', 'burun', 'faiz', 'əlbəttə', 'işçi', 'iş',
              'qısaca', 'mağaza', 'media', 'çünki', 'artım', 'çıxarmaq', 'ictimai', 'sığorta', 'yay', 'ürək', 'sənəd',
              'səy', 'hər', 'gün', 'ekspress', 'risk', 'danışma', 'söz', 'demokratiya', 'duz', 'məscid', 'yaş', 'aşağı',
              'ətrafında', 'tezliklə', 'imkan', 'orqan', 'öldürmək', 'başqa', 'il', 'qırmaq', 'baxmaq', 'meyvə', 'asmaq',
              'şirin', 'ayaq', 'dəyişiklik', 'qanun', 'külək', 'respublika', 'təkmilləşmək', 'üslub', 'yeddi', 'azalmaq',
              'qoşun', 'mobil', 'ünsiyyət', 'menecer', 'otel', 'qaçmaq', 'zövq', 'sürüş', 'təhlükəsizlik', 'qanun',
              'et', 'modern', 'oxumaq', 'tüfəng', 'tələb', 'ulduz', 'intensiv', 'əsgər', 'sadə', 'qaz',
              'tətbiq', 'istehsal', 'yemək', 'dünən', 'bax', 'haqqında', 'alış', 'şüur', 'çərçivə',
              'lazımdır', 'mövcuddur', 'uzatmaq', 'to', 'at', 'qoşulmaq', 'məsələn', 'demək', 'sayt',
              'kömək', 'bacı', 'çiçək', 'hamısı', 'hörmət', 'ödəmək', 'istedad', 'ağırlıq', 'pay', 'çətin', 'bundan',
              'çay', 'gedər', 'müəyyən', 'zəngin', 'heç', 'söz', 'təşkilat', 'ticarət', 'boyun', 'cihaz',
              'balans', 'geriyə', 'çünki', 'qəhvə', 'əzələ', 'montaj', 'başqa', 'işləmək', 'ünvan',
              'paşa', 'istilik', 'ok', 'güvən', 'marka', 'yarpaq', 'fayda', 'yaymaq', 'axan', 'çəkmək', 'düşünmək',
              'ürək', 'arzu', 'tərəqqi', 'şərab', 'yuxarıda', 'qızıl', 'almaq', 'təmiz',
              'vitamin', 'əlavə', 'gec', 'aktyor', 'yumurta', 'hərəkət', 'istəyək', 'kəsmə', "böhran", 'vahid',
              'söndür'
             ]


def kelime_sec():
    return random.choice(kelimeler)