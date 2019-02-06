# (한국어) 텍스트 마이닝을 위한 튜토리얼

텍스트 마이닝을 공부하기 위한 자료입니다. 언어에 상관없이 적용할 수 있는 자연어처리 / 머신러닝 관련 자료도 포함되지만, 한국어 분석을 위한 자료들도 포함됩니다. 

- 이 자료는 현재 작업중이며, slide와 jupyter notebook example codes가 포함되어 있습니다. 
- 이 자료는 [soynlp](https://github.com/lovit/soynlp) package를 이용합니다. 한국어 분석을 위한 자연어처리 코드입니다. soynlp 역시 현재 작업중입니다. 
- Slides 내용에 관련된 texts 는 [blog][lovit_blog] 에 포스팅 중입니다.
- 실습코드는 [코드 repository](https://github.com/lovit/python_ml4nlp) 에 있습니다.

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
1. Embedding for representation
    1. [x] Word2Vec / Doc2Vec
    1. [x] GloVe
    1. [x] FastText (word embedding using subword)
    1. [x] FastText (supervised word embedding)
    1. [x] Sparse Coding
    1. [x] Nonnegative Matrix Factorization (NMF) for topic modeling
1. Embedding for vector visualization
    1. [x] MDS, ISOMAP, Locally Linear Embedding, PCA, Kernel PCA
    1. [x] t-SNE
    1. [ ] t-SNE (detailed)
1. Keyword / Related words analysis
    1. [x] co-occurrence based keyword / related word analysis
1. Document clustering
    1. [x] k-means is good for document clustering
    1. [x] DBSCAN, hierarchical, GMM, BGMM are not suitable for document clustering
1. Finding similar documents (neighbor search)
    1. [x] Random Projection
    1. [x] Locality Sensitive Hashing
    1. [x] Inverted Index
1. Graph similarity and ranking (centrality)
    1. [x] SimRank & Random Walk with Restart
    1. [x] PageRank, HITS, WordRank, TextRank
    1. [x] kr-wordrank keyword extraction
1. String similarity
    1. [x] Levenshtein / Cosine / Jaccard distance
1. Convolutional Neural Network (CNN)
    1. [x] Introduction of CNN
    1. [x] CNN in NLP
1. Recurrent Neural Network (RNN)
    1. [x] Introduction of RNN
1. Applications
    1. [x] soyspacing: heuristic Korean space correction
    1. [x] crf-based Korean soace correction
    1. [x] HMM & CRF-based part-of-speech tagger (morphological analyzer)
    1. [ ] semantic movie search using IMDB
1. TBD

## Thanks to

자료를 리뷰하고 함께 토론해주는 고마운 동료들이 많습니다. 특히 많은 시간과 정성을 들여 도와주는 [태욱][taewook_git]에게 고마움을 표합니다.

[taewook_git]: https://github.com/Wook0129
[lovit_blog]: https://lovit.github.io
