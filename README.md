# (한국어) 텍스트 마이닝을 위한 튜토리얼

텍스트 마이닝을 공부하기 위한 자료입니다. 언어에 상관없이 적용할 수 있는 자연어처리 / 머신러닝 관련 자료도 포함되지만, 한국어 분석을 위한 자료들도 포함됩니다. 

- 이 자료는 현재 작업중이며, slide와 jupyter notebook example codes가 포함되어 있습니다. 
- 이 자료는 [soynlp](https://github.com/lovit/soynlp) package를 이용합니다. 한국어 분석을 위한 자연어처리 코드입니다. soynlp 역시 현재 작업중입니다. 
- Slides 내용에 관련된 texts 는 [blog][lovit_blog] 에 포스팅 중입니다.

## Contents
1. Python basic
    1. jupyter tutorial
1. From text to vector (KoNLPy)
    1. [x] n-gram
    1. [x] from text to vector using KoNLPy
1. Word extraction and tokenization (Korean)
    1. [x] word extractor
    1. [x] unsupervised tokenizer
    1. [x] noun extractor
    1. [x] dictionary based pos tagger
1. Document classification
    1. [x] Logistic Regression and Lasso regression
    1. [x] SVM (linear, RBF)
    1. [x] k-nearest neighbors classifier
    1. [x] Feed-forward neural network
    1. [x] Decision Tree
    1. [x] Naive Bayes
1. Sequential labeling
    1. [x] Conditional Random Field
1. Embedding for representation (작업중)
1. Embedding for vector visualization (작업중)
1. Keyword / Related words analysis (작업중)
    1. [x] co-occurrence based keyword / related word analysis
    1. [ ] kr-wordrank keyword extraction
1. Document clustering (작업중)
1. Finding similar documents (neighbor search) (작업중)
    1. [ ] Locality Sensitive Hashing
    1. [ ] Inverted Index
1. Graph similarity
    1. [ ] SimRank & Random Walk with Restart
1. String similarity
    1. [ ] Levenshtein / Cosine / Jaccard distance
1. Applications
    1. [x] soyspacing: heuristic Korean space correction
    1. [x] crf-based Korean soace correction
    1. [ ] semantic movie search using IMDB
1. TBD

## Thanks to

자료를 리뷰하고 함께 토론해주는 고마운 동료들이 많습니다. 특히 많은 시간과 정성을 들여 도와주는 [태욱][taewook_git]에게 고마움을 표합니다.

[taewook_git]: https://github.com/Wook0129
[lovit_blog]: https://lovit.github.io