from pyrogram import Client, filters
from pyrogram.types import Message


@app.on_message(filters.command("gosu" , prefixes=".") & filters.me)
async def f(client: Client, message: Message):
	text = ["вот смотри,ведь ты хочешь что бы мой хуй вырабатывал специальную жидкость для твоих морщин ?", "ты понимаешь что ты ебаный шизофренник порожденный злом моего хуя?", "почему твоя мать делает вид,что не любит мой хуй ??", "думаешь если назначить очко твоей мамашки маршалом армии рф то каждый будет ее ебать? как думаешь?", "давай погугли а то ты как обиженный пес мне тут скулишь , подзалупная ты обезьяна блять", "понимаешь что пизда твоей матери напала на мой хуй и поживала его", "ты понимаешь что я сейчас твою мамашу на своём хуе так раскручу ) как на олимпийских играх диск не метают", "ты что петух гриву свою на хую моем потерял чтоль?", "если ты будешь боятся спать один,попроси моего хуя он будет вместе с тобой", "ты ща мою сперму есть будешь как кашку манную маленбкие дети,ты молокосос,а я тебя заставлю это сделать обрыганец чертов", "почему твоя мамаша начинает нам хуе переваварачиватся как моржиха ёбанная ей что блядь место мало", "ты понимаешь что я ее щас хуем буду как мяч футбольный пинать и в твою пиду ее закачу а еще твоя мать любит мой хуй получать в качестве подарка на новый год потом сосёт с 31 по 15 не отходя от моего леденца блядь", "ты понимаешь что я на пиздаке твоей мамаши могу спермой выписать что никита депутат пидар был слит мной лично", "короче когда я твою мать ебал то я в ее пизде теракт устроил да такой силы что ты из утроба вылетел как спичка ёбанная", "лишай ёбанный?) ты понимаешь что я твою мать по щекам хуем бил чтобы в чувство привести вот ты пока своим ртом по моему хую бегаешь чтобы зашаблонить и пишешь одно и тоже пидарок блядь я тебя чот на полукоструктиве ебу а ты даже этого не понимаешь хуесос блядь почему твоя мамка начинает на моем хуйце свою пизду греть тебя щас хуем скручу веревка ты ёбанная и повешу на пизду твоей матери вместо трусов а потом когда буду ебать эту шлюху порву тебя", "ёбанная?) почему твоя мамаша стала своей пиздой об мой хуй терется она что магнитая", "ты понимаешь что я твоей мамке буду щас операцию делать хуем давай так если ты капс не выключишь я буду по пизде твоей матери хуем пинаться и тогда твой броша маленький умрет от моего хуя еще не родившись а мне нужен наследник который твою мать ебать будет когда твой отец умрет я буду на его костях обмоченных твою мать ебать долбаёб анальный", "ты понимаешь что твоя мамаша своими волосами мой хуй чешет блядь", "твоя мать как клещ,своим ртом к моему хую пpисосалась", "ты понимаешь что даже крестик господа тебя не поможет против моего хуя", "ты понимаешь что пиздак твоей мамашаки это липа которая полна терпения в зале ожидания, мой хуй привознёс ей второе вдохновение", "ты понимаешь что мой хуй еще за год вперёд расчитался с пиздой твоей мамашки, ведь её так морозит когда мой хуй проводит по её пизде словно муражки по коже", "ты понимаешь то что мой хуй способен залить твое ебало спермой?", "ты понимаешь что твоя мамаша на мой хуй нарвалась", "ты понимаешь что моя залупа будет целовать твой лоб?", "ты кстати сосешь нежно как твоя мать ты понимаешь это?", "ты понимаешь что я твою мамашу хуем по пизде ебашу?", "ты понимаешь что у тебя после моего хуя началась картавая речь", "я твою мать ебал а ты мне шмотку стиралoты понимаешь что когда я ебу мать твою она орёт как не знаю кто сука", "ты понимаешь что я в пизде твоей матери газовую станцию построил,что бы моему хую было зимой тепло", "я не понимаю зачем ты будешь мой хуй в 7 утра,что бы отсосать?", "ты понимаешь чтоя своим хуем ща выкопаю минеральные добрива в пизде твоей матери", "я твою мать ебал а ты мне шмотку стиралoты понимаешь что когда я ебу мать твою она орёт как не знаю кто сука", "ты понимаешь что я тебя сейчас хуем разломаю как вафлера ебаного", "ты понимаешь что твоя мать раскрыла свою матку что бы почуствавать свежесь хуёв на завтрак, когда поселилась в юридической юношеской столовой", "ты понимаешь что даже крестик господа тебя не поможет против моего хуя", "ты понимаешь что ты по дну лазил мой хуй искал?", "ты понимаешь что мой хуй имеет структуру предназначенной для пизды твоей маманьки", "ты понимаешь что я твоей матери сейчас хуем буду делать ампутацию матки ?", "ты же понимаешь что твой папаша не позаботился о том , что я буду ебать твою маман) и теперь тебе придеться забивать ей в очке доски чтобы я этого не делал)) но мой хуй как поезд промчиться к очке твоей мамаше словно к тунелю", "почему твоя мамаша свою пизду продает среди детских игрушек?", "ты понимаешь что ты перышками мне хуй щекотал и я возбуждался и ебал твою мать", "ты кстати нахуя мой хуй так славно сосешь я вот уже восхищаюсь твоему ротику", "помнишь как я твою мать ебал с своими друзьями?", "помнишь как мы ей порвали ротик своими хуями?",
    "хуеглот ебучий) сын путаны раздолья) подсос моего хуя) суда ползи спидозник) ты хули умолк хуй сосёшь не многоли чести",
    "хуйня из под ног?)) помню помню, недавно тобой пол в параше протер) но уже можешь вылезать",
    "ты понимаешь что ты зонтик держишь когда я твою мать при ливне ебу?",
    "мой хуй выбил страйк зубами твоей матери",
    "пойми) я ща пиздак твоей матери расстяну так что он сможет надеть всю землью",
    "пойми) я тебя буду ебать под песню oxxymiron-детектор лжи",
    "нахуя ты ходил к моему хую и сдавал тест на наркотики?",
    "пойми) мой хуй ща будет ездить по твоей голове как гозоно косилка по траве",
    "пойми) что мой хуй запрыгивает в пиздак твоей матери как тигр",
    "нахуя твоя мать пыталась развести мой хуй на деньги?",
    "ты понимаешь?) что я твою мать бууд ебать под елкой на первая января",
    "ты понимаешь что мой хуй плавает в пиздаку твоей матери как кит в океане",
    "ты зачем написал стих как я твою мать ебал?",
    "я твою мать ща буду ебать на снегу",
    "нахуя твоя мать маскируется за помощью моего хуя ?",
    "ты откуда взял информацию о моем хуе что он ебал твою мать ?",
    "мой хуй твою мать вытиранит своими яйцами когда она моестся",
    "давай запакуем твою мамашку и отправим по адресу прямо на мой хуй,кондуктор ебаный",
    "твоя мать мой хуй замотала изолентой что бы когда я её ебал не поцарапал края пихжы",
    "я твою мать в твоем доме ебал хату разогревал",
    "подсос моего хуя) суда ползи спидозник) ты понимаешь что ты ничтодество) тывсасываешь) орёшь) что твоя мать шлюха не доносила уебана как ты!?) тваиа мамка обидеелассьза точ то я её столкнул с хуя) и когда она поломала ноги спрыгнув с негшо) не ссы ч перечислил деньги в фонд хуесосок!?) ты понимаешь что я буду рвать ей пиздак пока она не слдохнет) она хуесоска очивидно) я буду ебать её до такой степени что она будет родать по 10 детеф сразу",
    "я тебе щас анал вырежу) хуябес обсосный) ты понимаешь что я фалосом крутила волосы на пизде твоей мамашки и создала бегуди?",
    "я тебе щас анал вырежу) хуябес обсосный) ты понимаешь что я ебала тебя бивнем?) педобир ахуевший?",
    "эй крыса концелярская я тебе щас карсар в жопу суну и подожгу) едобир ахуевший?",
    "ты понимаешь что я сейчас тебе анал вырежу членосос ты неотесанный) педобир ахуевший?",
    "я тебе щас анал вырежу) хуябес обсосный) ты понимаешь что хуй это не гора) по нему не надо лазить скалолаз ты ебучий) педобир ахуевший?) я тебе щас анал вырежу) хуябес обсосный",
    "хуесос ты мартовский) шавка ты идли полы мой в рестаране) какой рестаран в чикен бекон иди мой) и принеси туда мамку чтобыо на под столом сосала!?) педобир ахуевший?",
    "ты понимаешь что во всех советских годах я ебала твою мать по 7 часов в день",
    "давай же сука раком раком) когда ваша семья немцев ебаных решила пойти на нашу семью, то я как в 45 году просто растягнул ширинку, позвал твою мамашу, она присела на коленки и давай надрачивать, а немцы ебаные, то есть твои сородичи бежали по полю в наступление, из наших все сдохли, остался только я с твоей мамашей, и когда мой хуй прицелился, то я дал команду твой мамаше \"ускоряйся, шаболда ебаная!!!!!!!!!!\"",
    "она давай блять надрачивать как будто блять въебала спидов и мой хуй давай хуярить спермой по всем выблядкам, они блять захлебывались в ней, а тех кто выжил я бил залупой по лбу, типо x-rey ка",
    "почему твоя мамаша начинает нам хуе переваварачиватся как моржиха ёбанная ей что блядь место мало",
    "ты понимаешь что я ее щас хуем буду как мяч футбольный пинать и в твою пиду ее закачу а еще твоя мать любит мой хуй получать в качестве подарка на новый год потом сосёт с 31 по 15 не отходя от моего леденца блядь", "ты понимаешь что я на пиздаке твоей мамаши могу спермой выписать что никита депутат пидар был слит мной лично",
    "короче когда я твою мать ебал то я в ее пизде теракт устроил да такой силы что ты из утроба вылетел как спичка ёбанная",
    "лишай ёбанный?) ты понимаешь что я твою мать по щекам хуем бил чтобы в чувство привести вот ты пока своим ртом по моему хую бегаешь чтобы зашаблонить и пишешь одно и тоже пидарок блядь я тебя чот на полукоструктиве ебу а ты даже этого не понимаешь хуесос блядь почему твоя мамка начинает на моем хуйце свою пизду греть тебя щас хуем скручу веревка ты ёбанная и повешу на пизду твоей матери вместо трусов а потом когда буду ебать эту шлюху порву тебя",
    "ёбанная?) почему твоя мамаша стала своей пиздой об мой хуй терется она что магнитая",
    "ты понимаешь что я твоей мамке буду щас операцию делать хуем давай так если ты капс не выключишь я буду по пизде твоей матери хуем пинаться и тогда твой броша маленький умрет от моего хуя еще не родившись а мне нужен наследник который твою мать ебать будет когда твой отец умрет я буду на его костях обмоченных твою мать ебать долбаёб анальный",
    "ты понимаешь что твоя мамаша своими волосами мой хуй чешет блядь",
    "твоя мать как клещ,своим ртом к моему хую пpисосалась",
    "ты понимаешь что даже крестик господа тебя не поможет против моего хуя",
    "ты понимаешь что пиздак твоей мамашаки это липа которая полна терпения в зале ожидания, мой хуй привознёс ей второе вдохновение",
    "ты понимаешь что мой хуй еще за год вперёд расчитался с пиздой твоей мамашки, ведь её так морозит когда мой хуй проводит по её пизде словно муражки по коже",
    "ты понимаешь то что мой хуй способен залить твое ебало спермой?",
    "ты понимаешь что твоя мамаша на мой хуй нарвалась",
    "ты понимаешь что моя залупа будет целовать твой лоб?",
    "ты кстати сосешь нежно как твоя мать ты понимаешь это?",
    "ты понимаешь что я твою мамашу хуем по пизде ебашу?",
    "ты понимаешь что у тебя после моего хуя началась картавая речь",
    "я твою мать ебал а ты мне шмотку стиралoты понимаешь что когда я ебу мать твою она орёт как не знаю кто сука",
    "ты понимаешь что я в пизде твоей матери газовую станцию построил,что бы моему хую было земой тепло",
    "я не понимаю зачем ты будешь мой хуй в 7 утра,что бы отсосать?",
    "ты понимаешь чтоя своим хуем ща выкопаю минеральные добрива в пизде твоей матери",
    "я твою мать ебал а ты мне шмотку стиралoты понимаешь что когда я ебу мать твою она орёт как не знаю кто сука",
    "ты понимаешь что я тебя сейчас хуем разломаю как вафлера ебаного",
    "ты понимаешь что твоя мать раскрыла свою матку что бы почуствавать свежесь хуёв на завтрак, когда поселилась в юридической юношеской столовой",
    "ты понимаешь что даже крестик господа тебя не поможет против моего хуя",
    "ты понимаешь что ты по дну лазил мой хуй искал?",
    "ты понимаешь что мой хуй имеет структуру предназначенной для пизды твоей маманьки",
    "ты понимаешь что я твоей матери сейчас хуем буду делать ампутацию матки ?",
    "ты же понимаешь что твой папаша не позаботился о том , что я буду ебать твою маман) и теперь тебе придеться забивать ей в очке доски чтобы я этого не делал)) но мой хуй как поезд промчиться к очке твоей мамаше словно к тунелю",
    "почему твоя мамаша свою пизду продает среди детских игрушек?",
    "ты понимаешь что ты перышками мне хуй щекотал и я возбуждался и ебал твою мать",
    "ты кстати нахуя мой хуй так славно сосешь я вот уже восхищаюсь твоему ротику",
    "вот смотри,ведь ты хочешь что бы мой хуй вырабатывал специальную жидкость для твоих морщин ?",
    "ты понимаешь что ты ебаный шизофренник порожденный злом моего хуя?",
    "почему твоя мать делает вид,что не любит мой хуй ??",
    "думаешь если назначить очко твоей мамашки маршалом армии рф то каждый будет ее ебать? как думаешь?"]
	await message.edit(f"{random.choice(text)}")