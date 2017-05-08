
pickle.dump(LR_classifier, open('D:/LR_classifier.pkl','w'))

moto = pickle.load(open('D:/pos_review_test.pkl','r')) 
def extract_features(data):
    feat = []
    for i in data:
        feat.append(best_word_features(i))
    return feat
moto_features = extract_features(moto) #把文本转化为特征表示的形式

clf = pickle.load(open('D:/LR_classifier.pkl')) #载入分类器

pred = clf.batch_prob_classify(moto_features) #该方法是计算分类概率值的
p_file = open('D:/moto_ml_socre.txt','w') 
#把结果写入文档
for i in pred:
    p_file.write(str(i.prob('pos')) + ' ' + str(i.prob('neg')) + '\n')
p_file.close()

