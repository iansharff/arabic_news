# CLassification of Arabic News Articles
> Ian Sharff

## Table of Contents
- [CLassification of Arabic News Articles](#classification-of-arabic-news-articles)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Business Understanding](#business-understanding)
  - [Data Understanding](#data-understanding)
  
## Overview
The purpose of this project is to develop a classification model for news articles written in Arabic to be used by educators and their students. The models are trained on a corpus consisting of roughly 200,000 articles written in Modern Standard Arabic (العربية الفصحى), which were obtained from <a href="https://www.sciencedirect.com/science/article/pii/S2352340919304305?via%3Dihub">SANAD project (Single-label Arabic News Articles Dataset)</a>, and as of now the models have been trained on a subset of 7 categories with 6,500 articles. The highest performing model has been a Random Forest Classifier, but Multinomial Naive Bayes, Gradient Boosting, and Support Vector classifiers were also built and tested, each obtaining a testing score above 95% on the subset. The purpose, rationale, and goals of the project are outlined below, and the code behind the models can be found in the [modeling)

## Business Understanding
Arabic is one of the <a/ href="https://blog.ititranslates.com/2020/09/22/is-arabic-the-richest-language-in-words/">richest languages in the world</a>, meaning that it has a much larger vocabulary than English and is based upon a complex but logical grammar system. Additionally, "Arabic" in and of itself is not a single language; rather, it consists of many variations which are not always mutually intelligible between speakers of different dialects. For this reason, the development of Arabic NLP models can be a daunting task when compared to one in the English language, not to mention the higher quantity of libraries, pretrained models, and other resources available in English. <a href="https://effectivelanguagelearning.com/language-guide/language-difficulty/">Some sources</a> claim that Arabic is one of the hardest languages for native speakers of English to learn, requiring an estimated 2,200 hours of practice and speaking for the average anglophone to obtain fluency. In light of this, many students of Arabic (myself included) often struggle to build what may seem to be a never ending vocabulary. What this project aims to accomplish is to create a the basis of a classification model that can take a corpus of arbitrary size and label its articles with predefined categories to facilitate the learning of genre-specific vocabulary. This tool will ideally be readily deployed as an application to help Arabic educators provide intermediate- to advanced-level reading resources for their students according to their interests.

## Data Understanding
As previously mentioned, the total corpus from SANAD consists of 