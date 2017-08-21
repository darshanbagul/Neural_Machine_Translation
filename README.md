# Neural_Machine_Translation

Implementation of a Machine Translator using a Sequence to Sequence LSTM Network (Encoder-Decoder) with Attention in Tensorflow.

## Dataset

We are using the [Open Subtitles Dataset](http://opus.lingfil.uu.se/OpenSubtitles.php) which is a collection of documents from [OpenSubtitles](http://www.opensubtitles.org/). So basically the data comprises of movie subtitles in different languages. We have chosen data for English-> German task and French-> English translation task.

**Note - Some language data is in a TMX format, which needs to be converted in a useful format before we train our model. I have written a TMX convertor which accomplishes this task, and can be used on any language dataset for creating a machine translator.**

## Dependencies
  1. python       2.7
  2. tensorflow   1.0.1
  3. numpy        1.13.0
  4. scikit-learn 0.18.2
  5. matplotlib   1.5.1

## Implementation

1. English to German text translation

2. French to English text translation

## Results

### 1. English -> German

1. What' s your name    ->  Was ist denn Name 

2. My name is           ->  Mein Name ist 

3. What are you doing   ->  Was machst du gemacht 

4. I am reading a book  ->  Ich bin ein Buch Buch 

5. How are you          ->  Wie geht' s 

### French -> English

1. Quel est ton nom       ->  What is your name 

2. Mon nom est            ->  My name is 

3. Qu'est-ce que tu fais  ->  You are wrong 

4. Oui                    ->  Yeah 

5. Non                    ->  No
