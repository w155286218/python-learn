# -*- coding: utf-8 -*-

# In[1]:

import elasticsearch
import random
import time


# In[2]:

feed_id_list = []
# reader = open('/Users/didi/Documents/ipython-notebook/feed_offline_data.txt', 'rb')
# lines = reader.readlines()
# for line in lines:
#     feed_id_list.append(line.strip())
# reader.close()
# print(len(feed_id_list))

# tag_id_list = ["1c1d61442fe142dd8c76462d82384c79",
# "25a044fdbad74221a00fe3186f2081ec",
# "091c5a73b02d492ea4b76d33f3973b5f",
# "d70d3bd0c7da45f2a9063796145019ce",
# "85e48aede3c74ffdb58cb799f320578d",
# "35f32dd562b24b959d7ffdc54da9a21d",
# "7312a6887780466c9309525d7f01f2d4",
# "2b18cd4829084546b34b2b046989adc9",
# "72dbdb495606459f9d7d0af084bb0a47",
# "f690a990e7f1472cbc2e4be105fb426e",
# "18f050024bc54e83b247679c410a46eb",
# "0a4fb432303b4c5a8055986e0f988c67",
# "026a0e70f7184175b0872ce157aa650e",
# "c3cee4ebef7949bdb3ae7d6baa12a161",
# "ac16a183cadd48aa867006fed4eaced2",
# "b1bd73f50c8a45d689804da983ee58fd",
# "aee238817b524920ad3abd1f413f1334"]
# driver_id_list = ['567949953557832', '567949953490384', '67949953490384', '567949953490452', '567949953490462', '566253496778752', '567949953557852', '567949953557850', '566253490020352', '566253481627648', '567949953482590', '567949953654270', '567949953491564', '567949953485602', '585542182787150', '585542182787154', '585542182787158', '585542182787166', '585542182787170', '585542182787178', '585542182787174', '567949953557830']

elasticsearch_client = elasticsearch.Elasticsearch([{'host':'10.94.120.87','port':9200}, {'host':'10.94.128.210','port':9200}])


# In[3]:

def weight_choice(choice_list, weight_list):
    assert len(choice_list)==len(weight_list)
    new_list = []
    for i, val in enumerate(choice_list):
        new_list.extend([val] * weight_list[i])
    return random.choice(new_list)


# In[4]:

def fake_item_data(feed_id):
    feed_dict = {
        'item_id': feed_id,
        'tag_id': tag_id_list[random.randint(0, len(tag_id_list)-1)],
        'update_time': 1499170281000,
        'create_time': 1499170281000,
        'item_status': 0,
        'city_id': '892170201373886553',
        'user_id': driver_id_list[random.randint(0, len(driver_id_list)-1)],
        'user_type': weight_choice([1, 2, 3], [70, 20, 10]),
        'click_count': random.randint(1, 1000),
        'like_count': random.randint(1, 1000),
        'reply_count': random.randint(1, 1000),
        'notice_status': weight_choice([0, 1, 2], [90, 5, 5]),
        'notice_time': random.randint(1496643793000, 1497507793000),
        'highlight_status': weight_choice([0, 1], [80, 20]),
        'publish_status': weight_choice([0, 1], [90, 10]),
        'score_feature_1': random.uniform(0, 1),
        'count_feature_4': 2,
        'count_feature_5': 2
    }
    elasticsearch_client.index(index='driver_community_feed_recommend_v1', doc_type='item', id=feed_id, body=feed_dict)


# In[5]:

def fake_user_data(driver_id):
    for tag_id in tag_id_list:
        user_dict = {
            'user_id': driver_id,
            'tag_id': tag_id,
            'model_score': 1+random.uniform(0, 1)
        }
        elasticsearch_client.index(index='driver_community_feed_recommend_v1', doc_type='user', id=driver_id+'-'+tag_id, body=user_dict)


# In[6]:

#fake_user_data('567949953557850')
userid_list = ["564070228369409","565097906373497","562950083526366","567950140102707","563588950196227","565276122486336","580542143795532","565309418972002","564325549871793","564426232900375","566040280830408","564832309608734","565896532792255","567950132506541","564866676425945","566018200314456","563665527902209","567949995047323","567950123203469","565667728332648","564907017766617","564641140645360","563809904103424","565343822684382","565099699509056","563990820495361","563405617504256","564131039027200","565112596992908","567950190900271","565236051684413","566052319008400","563746709766146","566159667563911","564017490104322","563562394947584","565891913551262","564229575344129","564430510033229","567950016611844","567950165818950","565831529140835","563663262515200","566453345462783","565434791756595","565647389300403","565531393200233","567950063727022","565423405997731","565082110299963","563552824664066","565796237157502","565706171157768","567950146771368","564906413596645","566373358437070","567950020632513","565734470321371","580542144978947","563438864175105","565160663064474","567950109833976","565495438643839","563767152746497","563473463316480","563555292479488","565471617684630","563688700125186","567950056247675","564959635310326","580542147675316","563706584367105","564860348213103","563241941082114","567950198813596","563349850558466","565951216626621","565737194525396","565180859618123","563968883822597","564691120757819","563567508525056","563705622036481","563961867403264","565404416021335","567950039661233","563934414503937","563560132321280","565503153213827","563974760824832","563553624137729","563508046143488","563339951734784","567950146426731","565061128038535","567950162508528","564381281222813","565739175870794","565412076850963","564244654260225"]
def fake_u2u_sim_data(driver_id):
    for sim_user_id in userid_list:
        user_dict = {
            'user_id': driver_id,
            'sim_user_id': sim_user_id,
            'sim_score': 1+random.uniform(0, 1)
        }
        elasticsearch_client.index(index='driver_u2u_similarity_with_post', doc_type='user', id=driver_id+'-'+sim_user_id, body=user_dict)

#fake_u2u_sim_data('562950062552321')

itemid_list0 = ["85d163e19ba14de0827ebba4d9045ccb",
"856b1ea9bf014941bb77d0737382f911",
"9ae61ed4c988459eb0c27c60b3751a73",
"02d67fee7ff84b9789a5c7fc4f8182e4",
"63285f0d54b34dedb1be2cb67d695c86",
"2bc613ffe8784132a3b94f762d7e421a",
"36ad0c03ca934f0d867c40e4820f9ce4",
"19870ac0d9ac486eaaec1adc63c1b6fb"]
itemid_list1 = ["2bc613ffe8784132a3b94f762d7e421a",
"df8d401de03442d6967f38e2d7882f6e",
"36ad0c03ca934f0d867c40e4820f9ce4",
"50657a2558e249afbdd272a12586d687",
"538a1c0b042e4397a020017ab4126f83"]
itemid_list2 = ["36ad0c03ca934f0d867c40e4820f9ce4",
"538a1c0b042e4397a020017ab4126f83",
"8888410180e74e3fa5683f739c41095d",
"6f5a2d6ccb4043dca449c6d136ae8182",
"179196a8dd5b406eb10bc1eb1892e849"]
itemid_list3 = ["19870ac0d9ac486eaaec1adc63c1b6fb",
"36ad0c03ca934f0d867c40e4820f9ce4",
"6f5a2d6ccb4043dca449c6d136ae8182",
"b66feb0977e145a2b15dddad68ca22d9",
"538a1c0b042e4397a020017ab4126f83"]
def fake_user_view_post(driver_id,itemid_list):
    for item_id in itemid_list:
        user_dict = {
            'user_id': driver_id,
            'item_id': item_id,
            'create_time': 1500963975-random.randint(6*3600,7*24*3600)
        }
        elasticsearch_client.index(index='driver_view_post', doc_type='user', id=driver_id+'-'+item_id, body=user_dict)

fake_user_view_post('562950062552321',itemid_list0)
fake_user_view_post('564070228369409',itemid_list1)
fake_user_view_post('565097906373497',itemid_list2)
fake_user_view_post('562950083526366',itemid_list3)
